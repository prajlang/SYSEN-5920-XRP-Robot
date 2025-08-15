# ---------------------------------------------------------------
# Tower of Hanoi
# ---------------------------------------------------------------
# ===== Full-speed until white line, then stop =====

# Tunables
LINE_THRESHOLD = 0.93   # Adjust based on your sensors/floor
CONFIRM_COUNT  = 3      # Require this many consecutive "white" reads
LOOP_DT        = 0.02   # Control loop period (s)
FWD_FULL       = 0.8    # Full-speed forward

def Hanoi():
    """
    Drive forward at full speed until a white line is detected, then stop.
    """
    print("Run: full speed until white line")
    consecutive = 0

    # Ensure we start from a stop
    stop()
    time.sleep(0.1)

    while True:
        # Read sensors
        l = reflectance.get_left()
        r = reflectance.get_right()
        white = (l <= LINE_THRESHOLD) or (r <= LINE_THRESHOLD)

        # Debounce against noise
        consecutive = consecutive + 1 if white else 0

        # Drive straight until confirmed white
        drivetrain.arcade(FWD_FULL, 0.0)

        if consecutive >= CONFIRM_COUNT:
            print("White line detected; stopping.")
            break

        time.sleep(LOOP_DT)

    # Stop the robot
    stop()
    print("Tower of Hanoi stopped")