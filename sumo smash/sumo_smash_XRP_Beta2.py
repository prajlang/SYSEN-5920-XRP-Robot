# ---------------------------------------------------------------
# Sumo Push-Out
# ---------------------------------------------------------------
class SumoPushOut:
    def __init__(self):
        self.DETECT_RANGE_CM = 150.0
        self.CONTACT_DIST_CM = 2.0
        self.LINE_THRESHOLD = 0.93
        self.SCAN_STEP_DEG = 10.0
        self.TURN_TIME_S = 0.05
        self.FWD_POWER = 0.60
        self.PUSH_POWER = 0.80
        self.REV_POWER = -0.60
        self.APPROACH_TIMEOUT_S = 10.0
        self.EXTRA_PUSH_TIME_S = 0.2

    def distance_cm(self):
        return safe_distance_cm()

    def on_white_tape(self):
        l, r = reflectance.get_left(), reflectance.get_right()
        return (l <= self.LINE_THRESHOLD) or (r <= self.LINE_THRESHOLD)

    def turn_step(self):
        drivetrain.arcade(0.0, 0.4)
        if wait_with_stop_check(self.TURN_TIME_S): return True
        stop()
        time.sleep(0.1)
        return False

    def scan_for_object(self):
        for _ in range(int(360 / self.SCAN_STEP_DEG)):
            if should_stop(): return False
            if self.distance_cm() <= self.DETECT_RANGE_CM:
                return True
            if self.turn_step(): return False
        return False

    def approach_and_push(self):
        start, prev_d = time.ticks_ms(), self.distance_cm()
        while not should_stop():
            if (time.ticks_diff(time.ticks_ms(), start) / 1000.0) > self.APPROACH_TIMEOUT_S:
                stop(); return False
            if self.on_white_tape():
                t0 = time.ticks_ms()
                while (time.ticks_diff(time.ticks_ms(), t0) / 1000.0) < self.EXTRA_PUSH_TIME_S:
                    if should_stop(): return False
                    drivetrain.arcade(self.PUSH_POWER, 0.0)
                    time.sleep(0.02)
                stop()
                return True
            d = self.distance_cm()
            touching = (d <= self.CONTACT_DIST_CM) or (abs(d - prev_d) < 0.5)
            drivetrain.arcade(self.PUSH_POWER if touching else self.FWD_POWER, 0.0)
            prev_d = d
            time.sleep(0.02)
        return False

    def retreat(self):
        while self.on_white_tape() and not should_stop():
            drivetrain.arcade(self.REV_POWER, 0.0)
            time.sleep(0.02)
        t0 = time.ticks_ms()
        while (time.ticks_diff(time.ticks_ms(), t0) / 1000.0) < 0.9 and not should_stop():
            drivetrain.arcade(self.REV_POWER, 0.0)
            time.sleep(0.02)
        stop()

    def run(self):
        print("Sumo Push-Out started")
        stop()
        time.sleep(0.2)
        while not should_stop():
            if self.scan_for_object():
                if self.approach_and_push():
                    self.retreat()
            if self.turn_step(): break
        stop()
        print("Sumo stopped")
