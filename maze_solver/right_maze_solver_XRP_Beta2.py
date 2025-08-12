from XRPLib.defaults import *
import time

# ----------- Tunables -----------
STOP_DIST_CM     = 15.0    # desired minimum clearance ahead
FWD_POWER        = 0.4    # forward throttle
RIGHT_BIAS_TURN  = 0.03    # constant right bias (negative turn)
KP               = 0.2   # proportional gain on distance error
KD               = 0.15    # derivative gain (set to 0.0 to start P-only)
TURN_CLAMP       = 3    # max magnitude of turn command
LOOP_DT_S        = 0.02    # control loop period
# --------------------------------

def safe_distance_cm():
    d = rangefinder.distance()
    if d is None or d <= 0:
        return 999.0
    return float(d)

def clamp(x, lo, hi):
    return lo if x < lo else (hi if x > hi else x)

def stop():
    drivetrain.arcade(0.0, 0.0)

def maze_right_hug_pd():
    print("Right-hug with P/PD front clearance. Press user button to stop.")
    stop()
    time.sleep(0.2)

    prev_e = 0.0
    prev_ms = time.ticks_ms()

    while not board.is_button_pressed():
        d = safe_distance_cm()
        print("Distance: %.2f cm" % d)

        # Base: forward with a small right bias
        turn_cmd = -RIGHT_BIAS_TURN

        # If too close, add left correction proportional to how close you are
        e = STOP_DIST_CM - d  # positive when too close
        now_ms = time.ticks_ms()
        dt = max(1e-3, time.ticks_diff(now_ms, prev_ms) / 1000.0)
        de_dt = (e - prev_e) / dt

        if e > 0:
            turn_cmd += KP * e + KD * de_dt

        # Limit turn authority
        turn_cmd = clamp(turn_cmd, -TURN_CLAMP, TURN_CLAMP)

        # Drive
        drivetrain.arcade(FWD_POWER, turn_cmd)

        # Update history and pace
        prev_e = e
        prev_ms = now_ms
        time.sleep(LOOP_DT_S)

    stop()
    print("Controller stopped.")

# Run it
maze_right_hug_pd()
