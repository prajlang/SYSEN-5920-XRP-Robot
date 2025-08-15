# XRP PI Line Follower Algorithm (Proportional-Integral)
# Using two sensors and arcade drive for robust control.

from XRPLib.defaults import *
import time

# --- Configuration ---
# Use these values to tune the robot's behavior.
FWD_POWER = 0.4   # Constant forward power (0.0 to 1.0). Start around 0.3-0.4.
TURN_CLAMP = 0.5  # Maximum turning effort (limits how sharp the robot can turn).

# --- GAIN TUNING ---
# These are starting points.
KP = 0.9  # Proportional gain: The primary steering correction.
KI = 0.03 # Integral gain: Corrects for long-term drift.

def clamp(value, min_val, max_val):
    """Helper function to limit a value to a specific range."""
    return max(min_val, min(value, max_val))

def pi_line_follower(duration=60):
    """
    Follows a line using a two-sensor PI algorithm and arcade drive.
    """
    print("Starting PI line follower... Press the user button to stop.")
    integral = 0
    
    # Wait for the user to be ready.
    time.sleep(1)

    try:
        # The loop will run until the duration is over or the user button is pressed.
        start_time = time.ticks_ms()
        while not board.is_button_pressed() and time.ticks_diff(time.ticks_ms(), start_time) < duration * 1000:
            # 1. Calculate Differential Error
            left_val = reflectance.get_left()
            right_val = reflectance.get_right()
            error = left_val - right_val

            # 2. Calculate Integral Error
            integral = integral + error
            
            # --- Anti-Windup for Integral ---
            if error == 0 or (error > 0) != (integral > 0):
                integral = 0
            integral = clamp(integral, -100, 100) # Clamp the integral

            # 3. Calculate the Turn Command
            turn_cmd = (KP * error) + (KI * integral)
            
            # Clamp the turn command to prevent excessive turning
            turn_cmd = clamp(turn_cmd, -TURN_CLAMP, TURN_CLAMP)

            # 4. Drive the robot using arcade drive
            drivetrain.arcade(FWD_POWER, turn_cmd)

            # 5. Print Debug Telemetry
            print(f"L:{left_val:.2f} R:{right_val:.2f} | err:{error:.2f} | turn:{turn_cmd:.2f}")

            time.sleep(0.02) # Loop delay

    except KeyboardInterrupt:
        print("\nProgram stopped.")
    finally:
        drivetrain.stop()
        print("Robot stopped.")

# --- Main execution ---
if __name__ == "__main__":
    pi_line_follower(duration=60)
