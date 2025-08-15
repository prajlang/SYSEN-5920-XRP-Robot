# ---------------------------------------------------------------
# Tower Smash
# ---------------------------------------------------------------
class TowerSmash:
    def __init__(self):
        self.DRIVE_EFFORT = 2
        self.CHARGE_DISTANCE_CM = 100
        self.REVERSE_DISTANCE_CM = 30
        self.NUM_PASSES = 3

    def run(self):
        print("Tower Smash started")
        time.sleep(2)
        for i in range(self.NUM_PASSES):
            if should_stop(): break
            print(f"Pass #{i+1}")
            drivetrain.straight(self.CHARGE_DISTANCE_CM, max_effort=self.DRIVE_EFFORT)
            if i < self.NUM_PASSES - 1:
                drivetrain.straight(-self.REVERSE_DISTANCE_CM, max_effort=self.DRIVE_EFFORT)
        stop()
        print("Tower Smash stopped")