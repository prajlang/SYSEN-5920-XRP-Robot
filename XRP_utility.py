# robot_multitask_full.py
from XRPLib.defaults import *
from pestolink import PestoLinkAgent
import time

# ===== Manual drive sensitivity/stability tunables =====
AXIS_TURN     = 0  # left stick X
AXIS_THROTTLE = 1  # left stick Y

DEADZONE      = 0.10   # ignore +/-10% stick noise
TURN_SCALE    = 0.6    # lower = gentler steering
THROTTLE_SCALE= 0.8    # lower = gentler throttle
EXPO          = 0.3    # 0 = linear, up to ~0.5 for softer near center
SLEW_PER_SEC  = 3.0    # max change in turn per second; 0 to disable

_last_turn = 0.0
_last_ms   = time.ticks_ms()

def _dz(x, dz=DEADZONE):
    """Deadzone filter."""
    return 0.0 if abs(x) < dz else x

def _expo(x, k=EXPO):
    """Expo curve."""
    return (1 - k) * x + k * (x ** 3)

def teleop_step():
    """Improved manual drive: deadzone, expo, scaling, slew-limit."""
    global _last_turn, _last_ms

    # Raw inputs
    raw_th = -pestolink.get_axis(AXIS_THROTTLE)  # invert so forward stick = positive throttle
    raw_tx = -pestolink.get_axis(AXIS_TURN)

    # Deadzone & expo
    th_in = _expo(_dz(raw_th)) * THROTTLE_SCALE
    tx_in = _expo(_dz(raw_tx)) * TURN_SCALE

    # Slew-limit on turn
    now = time.ticks_ms()
    dt = max(1e-3, time.ticks_diff(now, _last_ms) / 1000.0)
    if SLEW_PER_SEC > 0:
        max_step = SLEW_PER_SEC * dt
        if tx_in > _last_turn + max_step:
            tx_in = _last_turn + max_step
        elif tx_in < _last_turn - max_step:
            tx_in = _last_turn - max_step

    drivetrain.arcade(th_in, tx_in)
    _last_turn, _last_ms = tx_in, now
        self.DETECT_RANGE_CM = 80.0
        self.NUM_PASSES = 3  # or whatever value you want

    def run(self):
        print("Tower Smash started")
        time.sleep(0.2)
        for i in range(self.NUM_PASSES):
            if should_stop(): break
            print(f"Pass #{i+1}")
   
            # Charge for a fixed time or until stop
            end_time = time.ticks_ms() + 2000  # 2 seconds
            while time.ticks_ms() < end_time and not should_stop():
                drivetrain.arcade(0.6, 0.0)
                time.sleep(0.02)
            stop()
   
            if i < self.NUM_PASSES - 1:
                # Reverse
                end_time = time.ticks_ms() + 600
                while time.ticks_ms() < end_time and not should_stop():
                    drivetrain.arcade(-0.6, 0.0)
                    time.sleep(0.02)
                stop()
                teleop_step()

            # Task triggers
            if pestolink.get_button(0): maze_right_hug_pd()
            elif pestolink.get_button(1): line_follower_pi()
            elif pestolink.get_button(2): SumoPushOut().run()
            elif pestolink.get_button(3): TowerSmash().run()
            elif pestolink.get_button(12): GolfSwing()
            elif pestolink.get_button(13): Hanoi()

        else:
            stop()
        time.sleep(0.05)

if __name__ == "__main__":
    main()