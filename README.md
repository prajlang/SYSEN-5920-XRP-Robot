# Cornell XRP System Proving Ground Competition

## Overview

This repository contains our team's solutions for the Cornell XRP System Proving Ground Competition - a robotics challenge featuring XRP robots with Technic Legos. The competition takes place in a 3m x 4m proving ground arena with 11 distinct challenges designed to test autonomous and semi-autonomous robotic capabilities.

## Robot Requirements

### Physical Constraints
- **Starting Dimensions**: Maximum 1' length × 9" width × 1' height
- **Platform**: XRP (Experimental Robotics Platform) with Lego Technic compatibility
- **No part damage**: XRP components and Legos cannot be altered or damaged
- **Detachment allowed**: No penalty if parts become detached during challenges

### Allowed Materials
- ✅ **XRP components** (provided)
- ✅ **Lego Technic pieces** (provided kit)
- ✅ **Cardboard, string, tape** (tape cannot be attached to XRP or Legos)
- ❌ **No external components** from lab or other teams
- ❌ **No spare XRP/Lego parts** beyond provided kit

### XRP Component List
- XRP Controller Board (Raspberry Pi Pico W)
- Two motors with encoders and wheels
- Servo motor with Lego-compatible hub
- Ultrasonic distance sensor
- IR reflectance sensor board (2 sensors)
- Color sensor (TCS-34725)
- Touch sensor/button
- 6-axis IMU (built into controller)
- 4AA battery holder

## Competition Challenges

### 1. **The Maze** 🌀
**Objective**: Transport a ball from start to end of maze
- Semi-autonomous scoring for "hard coded" solutions
- Points awarded for distance traveled
- Bonus points for maze completion

### 2. **The Transporter** 📦
**Objective**: Deliver items to specified color-coded locations
- **Delivery Schedule**:
  - Blue Marble → Green 1
  - Yellow Marble → Blue 2  
  - Green Marble → Red 1
  - Red Marble → Blue 2
  - Blue Marble → Red 1
  - Red Marble → Blue 1
- Scoring based on correct deliveries made

### 3. **Pattern Match** 🧩
**Objective**: Recreate a given 4-cell grid pattern using matching blocks
- Must use blocks same size and color as original pattern
- Precision and accuracy scoring

### 4. **Stacker** 📚
**Objective**: Build a pyramid with specific color arrangement
- **Structure**: Blue blocks (bottom) → Green blocks (middle) → Red block (top)
- Scoring based on height and correctness

### 5. **Mini-Golf** ⛳
**Objective**: Get ball into hole from starting distance with minimum strokes
- Fewer strokes = higher score
- Use plastic golf ball or large foam ball

### 6. **Sumo** 🥊
**Objective**: Push castle blocks out of center ring
- Start in center with random orientation
- Push blocks outside ring (but not outside proving grounds)
- Penalty for blocks pushed inward

### 7. **Tower of Hanoi** 🗼
**Objective**: Complete the classic Tower of Hanoi puzzle
- Traditional rules apply
- Autonomous manipulation required

### 8. **Basket Gallery** 🏀
**Objective**: Shoot balls into baskets in specified order (Red → Blue → White)
- Different baskets worth different points
- Bonus for matching ball color to backboard color

### 9. **Tower Smash** 💥
**Objective**: Knock down castle towers to single brick level
- Bonus points for indirect knockdowns (not directly touched)
- Extra bonus for ending with marble on treasure space

### 10. **Line Follower** 🛤️
**Objective**: Follow line path from end to end while straddling the line
- Wheels/locomotion cannot cross the line
- Points for distance traveled along path

### 11. **Additional Challenges**
- May be added throughout the week
- May or may not involve the XRP Proving Ground directly

## Competition Format

### Setup Phase (10 minutes)
- Position robot in proving grounds
- **Only time** motors/sensors from other teams may be added
- Prepare for challenge attempts

### Competition Phase (12 minutes)
- Each challenge attempted **only once**
- Must declare challenge start to judge
- Challenge ends when: objective reached, terminating condition, or team decides to end

### Cleanup Phase (5 minutes)
- Clear and reset proving grounds
- **Penalty** if not completed in time

## Scoring System

### Autonomy Levels
- **Fully Autonomous**: Highest points - start program via button, no human intervention
- **Semi-Autonomous**: Medium points - program directed with some human intervention  
- **Manual**: Lower points - completely human controlled

### Additional Scoring Factors
- **Resource Usage**: Lighter entries score more points
  - Weight = Final entry minus (motors + sensors + XRP board + batteries)
  - **"All Bricks Challenge"**: Use all Legos in useful fashion for zero weight score
- **Style Points**: Cool looks, moves, music, design aesthetics
- **Attempt Points**: Awarded for "reasonable attempts" as determined by judge

## Team Roles (Competition Day)

### Station Manager
- **Cannot touch** robot during competition
- May use: pencil/pen, paper, ruler, calculator, laptop
- **Only person** who can officially declare challenge start/end
- **Only person** who talks with judge
- Coordinates team communications

### Programmer  
- **Only person** who can download files to XRP during competition
- No other robot interaction allowed

### Maintenance Bay
- May adjust robot configuration **only in Base Station area**

### Operators (Human Sensors & Actuators)
- May start programs and operate robot
- Direct robot control responsibilities

**Note**: Roles must be declared before competition and cannot be switched during event.

## Repository Structure

├── challenges/
│   ├── maze/
│   ├── transporter/
│   ├── pattern_match/
│   ├── stacker/
│   ├── mini_golf/
│   ├── sumo/
│   ├── tower_hanoi/
│   ├── basket_gallery/
│   ├── tower_smash/
│   └── line_follower/
├── utils/
│   ├── sensor_calibration/
│   ├── motor_control/
│   └── base_functions/
├── docs/
│   ├── competition_rules.md
│   └── setup_guide.md
└── README.md

## Getting Started

1. **Hardware Setup**: Assemble XRP robot according to provided guide
2. **Software Setup**: Connect to [XRP Code Editor](https://xrpcode.wpi.edu/staging/)
3. **Sensor Calibration**: Run calibration scripts for your environment
4. **Challenge Testing**: Test individual challenge solutions
5. **Integration**: Combine solutions for competition day

## Safety Requirements

⚠️ **Critical Safety Notes**:
- Any unsafe equipment use results in severe penalties
- Safety concerns may cause complete design rejection
- Contact instructor immediately for safety questions
- No food/drink in lab area

## Competition Day Logistics

- **Time**: 8:00 AM start
- **Location**: Duffield Hall Atrium  
- **Setup**: Teams transport proving grounds from lab (recommended 7:00 AM)
- **Cleanup**: Lab must be cleaned **before** 8:00 AM competition start
- **Post-Competition**: Breakdown and return proving grounds to lab

## Team Information

**Team #**: [Your Team Number]  
**Team Name**: [Your Team Name]  
**Members**: [List team members]

## Additional Resources

- [XRP User Guide](https://xrpusersguide.readthedocs.io/en/latest/)
- [XRP Code Editor](https://xrpcode.wpi.edu/staging/)
- [Competition RFP Document](link-to-document)

---

*"Break the Rules!"* - Cornell Engineering Motto
