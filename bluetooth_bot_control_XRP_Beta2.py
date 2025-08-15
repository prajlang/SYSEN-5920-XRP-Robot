# ---------------------------------------------------------------
# Bluetooth Control with Idle Teleop + Btn7 Stop
# ---------------------------------------------------------------
robot_name = "BetaBot"
pestolink = PestoLinkAgent(robot_name)

def main():
    print("Ready: Btn0=Maze, Btn1=Line, Btn2=Sumo, Btn3=Tower, Btn7=Stop.")
    while True:
        if pestolink.is_connected():
            # Btn7 always stops immediately
            if pestolink.get_button(7):
                stop()
                print("[Stop] Button 7 pressed.")
                while pestolink.get_button(7):
                    time.sleep(0.05)  # Wait until release

            # Idle joystick control
            if not any(pestolink.get_button(i) for i in range(4)):
                rotation = -1 * pestolink.get_axis(0)
                throttle = -1 * pestolink.get_axis(1)
                drivetrain.arcade(throttle, rotation)

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