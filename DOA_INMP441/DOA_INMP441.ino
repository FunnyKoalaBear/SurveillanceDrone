#include <Arduino.h>
#include "driver/i2s.h"
#include "esp_dsp.h"
#include <math.h>

// ===== Pins =====
#define I2S_WS     6
#define I2S_SCK    5
#define I2S0_SD    4   // Left + Right
#define I2S1_SD    7   // Front + Back

// ===== Config =====
#define SAMPLE_RATE    16000
#define FRAME_SAMPLES  256
#define MIC_DISTANCE   0.08f //this is 8cm
#define SPEED_SOUND    343.0f

// ===== Buffers =====
int32_t bufLR[FRAME_SAMPLES * 2];
int32_t bufFB[FRAME_SAMPLES * 2];

float micL[FRAME_SAMPLES], micR[FRAME_SAMPLES];
float micF[FRAME_SAMPLES], micB[FRAME_SAMPLES];

float A[2 * FRAME_SAMPLES];
float B[2 * FRAME_SAMPLES];
float C[2 * FRAME_SAMPLES];

// ===== I2S Setup =====
void setupI2S(i2s_port_t port, int data_pin) {
  i2s_config_t cfg = {};
  cfg.mode = (i2s_mode_t)(I2S_MODE_MASTER | I2S_MODE_RX);
  cfg.sample_rate = SAMPLE_RATE;
  cfg.bits_per_sample = I2S_BITS_PER_SAMPLE_32BIT;
  cfg.channel_format = I2S_CHANNEL_FMT_RIGHT_LEFT;
  cfg.communication_format = I2S_COMM_FORMAT_I2S;
  cfg.dma_buf_count = 4;
  cfg.dma_buf_len = FRAME_SAMPLES;

  i2s_pin_config_t pin_cfg = {};
  pin_cfg.bck_io_num = I2S_SCK;
  pin_cfg.ws_io_num  = I2S_WS;
  pin_cfg.data_in_num = data_pin;
  pin_cfg.data_out_num = -1;

  i2s_driver_install(port, &cfg, 0, NULL);
  i2s_set_pin(port, &pin_cfg);
}

// ===== GCC-PHAT =====
int gcc_phat(float *x, float *y) {
  for (int i = 0; i < FRAME_SAMPLES; i++) {
    A[2*i] = x[i]; A[2*i+1] = 0;
    B[2*i] = y[i]; B[2*i+1] = 0;
  }

  dsps_fft2r_fc32(A, FRAME_SAMPLES);
  dsps_fft2r_fc32(B, FRAME_SAMPLES);
  dsps_bit_rev_fc32(A, FRAME_SAMPLES);
  dsps_bit_rev_fc32(B, FRAME_SAMPLES);

  for (int i = 0; i < FRAME_SAMPLES; i++) {
    float re = A[2*i]*B[2*i] + A[2*i+1]*B[2*i+1];
    float im = A[2*i+1]*B[2*i] - A[2*i]*B[2*i+1];
    float mag = sqrtf(re*re + im*im) + 1e-9f;
    C[2*i]   = re / mag;
    C[2*i+1] = im / mag;
  }

  dsps_fft2r_fc32(C, FRAME_SAMPLES);
  dsps_bit_rev_fc32(C, FRAME_SAMPLES);

  int peak = 0;
  float maxVal = -1e9;
  for (int i = 0; i < FRAME_SAMPLES; i++) {
    float v = C[2*i];
    if (v > maxVal) { maxVal = v; peak = i; }
  }

  return (peak > FRAME_SAMPLES/2) ? peak - FRAME_SAMPLES : peak;
}
void removeDC(float *x, int N) {
  float mean = 0;
  for (int i = 0; i < N; i++) mean += x[i];
  mean /= N;
  for (int i = 0; i < N; i++) x[i] -= mean;
}

// ===== Setup =====
void setup() {
  Serial.begin(115200);
  delay(1000);

  setupI2S(I2S_NUM_0, I2S0_SD);
  setupI2S(I2S_NUM_1, I2S1_SD);

  dsps_fft2r_init_fc32(NULL, FRAME_SAMPLES);

  Serial.println("4-Mic GCC-PHAT AoA ready");
}

// ===== Loop =====
void loop() {
  size_t br0, br1;

  i2s_read(I2S_NUM_0, bufLR, sizeof(bufLR), &br0, portMAX_DELAY);
  i2s_read(I2S_NUM_1, bufFB, sizeof(bufFB), &br1, portMAX_DELAY);

  for (int i = 0; i < FRAME_SAMPLES; i++) {
    micL[i] = (float)bufLR[2*i];
    micR[i] = (float)bufLR[2*i + 1];
    micF[i] = (float)bufFB[2*i];
    micB[i] = (float)bufFB[2*i + 1];
  }

  removeDC(micL, FRAME_SAMPLES);
  removeDC(micR, FRAME_SAMPLES);
  removeDC(micF, FRAME_SAMPLES);
  removeDC(micB, FRAME_SAMPLES);

  int lag_x = gcc_phat(micL, micR);
  int lag_y = gcc_phat(micF, micB);

  float dx = (float)lag_x / SAMPLE_RATE;
  float dy = (float)lag_y / SAMPLE_RATE;

  float angle = atan2(dx, dy) * 180.0f / PI;

  Serial.print("Lag X: "); Serial.print(lag_x);
  Serial.print(" | Lag Y: "); Serial.print(lag_y);

  Serial.print("Angle: ");
  Serial.println(angle);

  delay(20);
}
