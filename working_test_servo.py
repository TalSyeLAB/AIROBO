from cvzone.SerialModule import SerialObject
from time import sleep

# ------------------- Initializations -------------------

arduino = SerialObject("COM8", digits=3)  # Replace COM3 with your actual port

sleep(2)

# Initial positions: [LServo, RServo, HServo]
last_positions = [90, 90, 90]  # Use mid-range values to avoid stalling

# ------------------- Functions -------------------

def move_servo(target_positions, delay=0.01):
    """
    Moves the servos smoothly to the target positions.

    :param target_positions: List of target angles [LServo, RServo, HServo]
    :param delay: Time delay (in seconds) between each incremental step
    """
    global last_positions

    # Clamp values to 0–180
    target_positions = [max(0, min(180, val)) for val in target_positions]

    max_steps = max(abs(target_positions[i] - last_positions[i]) for i in range(3))

    for step in range(max_steps):
        current_positions = [
            last_positions[i] + (step + 1) * (target_positions[i] - last_positions[i]) // max_steps
            if abs(target_positions[i] - last_positions[i]) > step else target_positions[i]
            for i in range(3)
        ]
        arduino.sendData(current_positions)
        sleep(delay)

    last_positions = target_positions[:]

# ------------------- Main Usage -------------------

target_positions = [10, 30, 40]  # Set target positions for LServo, RServo, and HServo
move_servo(target_positions)
