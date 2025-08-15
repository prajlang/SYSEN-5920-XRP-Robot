# ---------------------------------------------------------------
# Maze Right-Hug PD
# ---------------------------------------------------------------
STOP_DIST_CM     = 18.0
FWD_POWER_MAZE   = 0.4
RIGHT_BIAS_TURN  = 0.03
KP_MAZE          = 0.25
KD_MAZE          = 0.4
TURN_CLAMP_MAZE  = 3
LOOP_DT_S_MAZE   = 0.02
HISTORY_LEN      = 20
SAME_TOL_CM      = 1
BACKUP_TIME_S    = 0.35
BACKUP_POWER     = -0.415
NUDGE_TURN       = -0.28
NUDGE_TIME_S     = 0.2

def is_stuck(history):
    return len(history) >= HISTORY_LEN and (max(history) - min(history)) <= SAME_TOL_CM

def unstick():
    drivetrain.arcade(BACKUP_POWER, 0.0)
    if wait_with_stop_check(BACKUP_TIME_S): return True
    drivetrain.arcade(0.0, NUDGE_TURN)
    if wait_with_stop_check(NUDGE_TIME_S): return True
    stop()
    return False

def maze_right_hug_pd():
    print("Maze Right-Hug PD started")
    stop()
    history, prev_e, prev_ms = [], 0.0, time.ticks_ms()

    while not should_stop():
        d = safe_distance_cm()
        history.append(d)
        if len(history) > HISTORY_LEN: history.pop(0)

        if is_stuck(history):
            if unstick(): break
            history.clear()
            prev_ms, prev_e = time.ticks_ms(), STOP_DIST_CM - d
            continue

        turn_cmd = -RIGHT_BIAS_TURN
        e = STOP_DIST_CM - d
        now_ms = time.ticks_ms()
        dt = max(1e-3, time.ticks_diff(now_ms, prev_ms) / 1000.0)
        de_dt = (e - prev_e) / dt
        if e > 0:
            turn_cmd += KP_MAZE * e + KD_MAZE * de_dt

        turn_cmd = clamp(turn_cmd, -TURN_CLAMP_MAZE, TURN_CLAMP_MAZE)
        drivetrain.arcade(FWD_POWER_MAZE, turn_cmd)
        prev_e, prev_ms = e, now_ms
        time.sleep(LOOP_DT_S_MAZE)
    stop()
    print("Maze stopped")