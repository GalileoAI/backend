import datetime
MESSAGES_FILE_PATH = "logs/messages.txt"


def save_message(message, initialized=False):
    with open(MESSAGES_FILE_PATH, "r") as file:
        lines = file.readlines()
        file.close()

    if initialized:
        lines.append(f"\nClient Initialization {datetime.datetime.now()}")

    lines.append(f"\n{datetime.datetime.now()}: {message}")

    with open(MESSAGES_FILE_PATH, "w") as file:
        file.writelines(lines)
        file.close()
