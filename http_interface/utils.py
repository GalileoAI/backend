import datetime
import os

MESSAGES_FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/logs/messages.txt"


def save_message(message, initialized=False):
    with open(MESSAGES_FILE_PATH, "r", encoding="utf-8") as file:
        lines = file.readlines()
        file.close()

    if initialized:
        lines.append(f"\nClient Initialization {datetime.datetime.now()}")

    lines.append(f"\n{datetime.datetime.now()}: {message}")

    with open(MESSAGES_FILE_PATH, "w", encoding="utf-8") as file:
        file.writelines(lines)
        file.close()
