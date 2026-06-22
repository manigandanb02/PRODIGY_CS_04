from datetime import datetime

LOG_FILE = "key_logs.txt"

def show_banner():
    print("=" * 50)
    print("KeyScribe - Terminal Key Logger")
    print("=" * 50)
    print("This program records only the text typed inside this terminal.")
    print("It does NOT run in background.")
    print("It does NOT capture system-wide keystrokes.")
    print("Type 'exit' to stop logging.")
    print("=" * 50)

def write_log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {text}\n")

def main():
    show_banner()

    permission = input("Do you give permission to start logging? (yes/no): ").lower()

    if permission != "yes":
        print("Permission denied. Program stopped.")
        return

    print("\nLogging started...")
    print("Type something and press Enter.")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("Input: ")

        if user_input.lower() == "exit":
            print("Logging stopped.")
            break

        write_log(user_input)
        print("Saved to log file.")

if __name__ == "__main__":
    main()
