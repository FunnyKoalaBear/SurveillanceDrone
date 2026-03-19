import asyncio
from mavsdk import System

async def main():
    drone = System()
    
    # 1. Connect using the string we confirmed works
    print("Connecting to drone on serial:///dev/serial0:921600 ...")
    await drone.connect(system_address="serial:///dev/serial0:921600")

    print("Waiting for drone connection...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Connected!")
            break

    # 2. Check if we are ready to arm
    # Note: On a bench, this might fail due to "Compass/GPS" errors.
    # If it fails, see the troubleshooting section below.
    print("Checking health...")
    async for health in drone.telemetry.health():
        if health.is_gyrometer_calibration_ok and health.is_accelerometer_calibration_ok:
            print("  - Gyro/Accel calibration OK")
            break
            
    print("-- ARMING MOTORS (At Idle Speed) --")
    try:
        await drone.action.arm()
        print("Armed! Motors should be spinning at idle.")
    except Exception as e:
        print(f"Arming failed: {e}")
        return

    # 3. Keep them spinning for 5 seconds
    # We don't need to send a throttle command; 'Armed' state maintains idle throttle.
    print("Spinning for 5 seconds...")
    await asyncio.sleep(2)

    print("-- DISARMING --")
    await drone.action.disarm()
    print("Disarmed. Test complete.")

if __name__ == "__main__":
    asyncio.run(main())