# XRP Line Following Algorithm - MicroPython
# Simple two-sensor line following for curved lines

from XRPLib.defaults import *
import time

# Configuration parameters
LINE_THRESHOLD = 500    # Adjust based on your line/surface contrast
STRAIGHT_SPEED = 50     # Speed when going straight (0-100)
TURN_SPEED_FAST = 50    # Speed of faster wheel when turning
TURN_SPEED_SLOW = 20    # Speed of slower wheel when turning
LOOP_DELAY = 0.05       # Small delay between readings (seconds)

def line_follow():
    """
    Main line following function using two IR sensors
    """
    print("Starting line following...")
    print("Press User button to stop")
    
    try:
        while True:
            # Check if user button is pressed to stop
            if board.user_button.is_pressed():
                print("User button pressed - stopping")
                break
            
            # Read both IR sensors
            left_sensor = reflectance.get_left()
            right_sensor = reflectance.get_right()
            
            # Debug: Print sensor values (comment out for competition)
            # print(f"Left: {left_sensor}, Right: {right_sensor}")
            
            # Line following logic
            if left_sensor < LINE_THRESHOLD and right_sensor < LINE_THRESHOLD:
                # Both sensors see the line - go straight
                drivetrain.set_speed(STRAIGHT_SPEED, STRAIGHT_SPEED)
                
            elif left_sensor < LINE_THRESHOLD and right_sensor >= LINE_THRESHOLD:
                # Left sensor sees line, right doesn't - turn left
                # Slow down left wheel, keep right wheel fast
                drivetrain.set_speed(TURN_SPEED_SLOW, TURN_SPEED_FAST)
                
            elif left_sensor >= LINE_THRESHOLD and right_sensor < LINE_THRESHOLD:
                # Right sensor sees line, left doesn't - turn right  
                # Slow down right wheel, keep left wheel fast
                drivetrain.set_speed(TURN_SPEED_FAST, TURN_SPEED_SLOW)
                
            else:
                # Neither sensor sees the line - stop and search
                drivetrain.stop()
                print("Line lost! Stopping...")
                # Optional: Add search pattern here
                time.sleep(0.5)  # Brief pause before continuing
            
            # Small delay to prevent overwhelming the system
            time.sleep(LOOP_DELAY)
            
    except KeyboardInterrupt:
        print("Program interrupted")
    
    finally:
        # Always stop the robot when exiting
        drivetrain.stop()
        print("Line following stopped")

def calibrate_sensors():
    """
    Helper function to calibrate sensors and find good threshold
    Run this first to understand your sensor readings
    """
    print("Sensor Calibration Mode")
    print("Place robot over line and off line to see values")
    print("Press User button to exit calibration")
    
    while not board.user_button.is_pressed():
        left = reflectance.get_left()
        right = reflectance.get_right()
        print(f"Left: {left:4d}, Right: {right:4d}")
        time.sleep(0.2)
    
    print("Calibration complete")

def enhanced_line_follow():
    """
    Enhanced version with lost line recovery
    """
    print("Starting enhanced line following...")
    
    # Variables for lost line recovery
    last_direction = "straight"  # Track last known direction
    search_count = 0
    
    try:
        while True:
            if board.user_button.is_pressed():
                break
            
            left_sensor = reflectance.get_left()
            right_sensor = reflectance.get_right()
            
            if left_sensor < LINE_THRESHOLD and right_sensor < LINE_THRESHOLD:
                # Both sensors see line - go straight
                drivetrain.set_speed(STRAIGHT_SPEED, STRAIGHT_SPEED)
                last_direction = "straight"
                search_count = 0
                
            elif left_sensor < LINE_THRESHOLD and right_sensor >= LINE_THRESHOLD:
                # Turn left
                drivetrain.set_speed(TURN_SPEED_SLOW, TURN_SPEED_FAST)
                last_direction = "left"
                search_count = 0
                
            elif left_sensor >= LINE_THRESHOLD and right_sensor < LINE_THRESHOLD:
                # Turn right
                drivetrain.set_speed(TURN_SPEED_FAST, TURN_SPEED_SLOW)
                last_direction = "right"
                search_count = 0
                
            else:
                # Line lost - implement search pattern
                search_count += 1
                
                if search_count < 10:  # Try continuing last direction briefly
                    if last_direction == "left":
                        drivetrain.set_speed(TURN_SPEED_SLOW, TURN_SPEED_FAST)
                    elif last_direction == "right":
                        drivetrain.set_speed(TURN_SPEED_FAST, TURN_SPEED_SLOW)
                    else:
                        drivetrain.set_speed(STRAIGHT_SPEED, STRAIGHT_SPEED)
                else:
                    # If still lost, stop
                    drivetrain.stop()
                    print("Line lost for too long - stopping")
                    break
            
            time.sleep(LOOP_DELAY)
            
    except KeyboardInterrupt:
        print("Program interrupted")
    
    finally:
        drivetrain.stop()
        print("Enhanced line following stopped")

# Main program
if __name__ == "__main__":
    print("XRP Line Following Program")
    print("1. Run calibrate_sensors() first to find good threshold")
    print("2. Then run line_follow() for basic algorithm")
    print("3. Or run enhanced_line_follow() for recovery features")
    
    # Uncomment one of these to run:
    
    # Step 1: Calibrate sensors first
    # calibrate_sensors()
    
    # Step 2: Run basic line following
    line_follow()
    
    # Alternative: Run enhanced version
    # enhanced_line_follow()
