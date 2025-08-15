# XRP Proportional Line Following Algorithm - Optimized for a WHITE line

from XRPLib.defaults import *
import time

# --- Configuration ---
# 1. RUN calibrate_threshold() FIRST to find this value!
THRESHOLD = 0.2659302   # << UPDATE THIS VALUE AFTER CALIBRATING

# 2. Set your speeds
DRIVE_SPEED = 1   # 10% of a base speed of 60
KP = 0.05         # Proportional gain (turn sensitivity). Fine-tune this.
                  # If the robot zig-zags too much, lower KP.
                  # If it turns too slowly, increase KP.

# --- Main Program ---
def proportional_line_follower(duration=30):
    """
    Follows a white line for a set duration using a proportional algorithm.
    """
    print(f"Starting white line following for {duration} seconds...")
    start_time = time.ticks_ms()

    try:
        while time.ticks_diff(time.ticks_ms(), start_time) < duration * 1000:
            # Read the sensor and calculate the error from the threshold
            current_position = reflectance.get_left()
            error = current_position - THRESHOLD

            # Calculate the turning adjustment based on the error
            turn_adjustment = error * KP

            # Adjust motor speeds to correct the robot's course
            left_speed = DRIVE_SPEED + turn_adjustment
            right_speed = DRIVE_SPEED - turn_adjustment

            drivetrain.set_speed(left_speed, right_speed)

            time.sleep(0.01) # A small delay improves stability

    except KeyboardInterrupt:
        print("Program stopped.")
    finally:
        drivetrain.stop()
        print("Line following complete.")

# --- Calibration Function ---
def calibrate_threshold():
    """
    Helps you find the perfect threshold value for your environment.
    """
    print("--- Sensor Calibration Routine ---")
    print("For 10 seconds, move the sensor back and forth between the")
    print("white tape and the bare floor to find min and max readings.")
    input("Press Enter to begin...")

    readings = []
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < 10000:
        val = reflectance.get_left()
        readings.append(val)
        print(f"Current Reading: {val}")
        time.sleep(0.1)

    if readings:
        max_reading = max(readings)
        min_reading = min(readings)
        suggested_threshold = (min_reading + max_reading) // 2
        
        print("\n--- Calibration Complete! ---")
        print(f"Max Value (on white tape): {max_reading}")
        print(f"Min Value (on floor):      {min_reading}")
        print(f"==> Suggested THRESHOLD value: {suggested_threshold}")
        print("Update the THRESHOLD variable in the code with this value.")
    else:
        print("No readings were captured. Please try again.")


# --- Main execution ---
if __name__ == "__main__":
    
    # STEP 1: Run calibration first by itself.
    # To do this, comment out the line follower call below,
    # and uncomment the calibrate_threshold() call.
    
    # calibrate_threshold()
    
    # STEP 2: After calibrating and updating the THRESHOLD variable,
    # comment out the calibration call above and run the line follower.
    
    # input("Set THRESHOLD, then press Enter to start the line follower...")
    proportional_line_follower(60) # Run for 60 seconds