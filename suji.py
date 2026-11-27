import requests
import json
import time
import os
from datetime import datetime
from urllib.parse import urlencode

# =====================================
# NG SUJEET AUTO GUILD JOINER
# Developer: SUJEET SAHNI
# =====================================

API_URL = ""  # Disabled: do not send account passwords to an unverified third party.

ACCOUNTS_FILE = "accounts.json"
DELAY = 2


def banner():
    os.system("clear")

    print("""
╔══════════════════════════════════════╗
║                                      ║
║       NG SUJEET GUILD JOINER         ║
║                                      ║
║          AUTO JOIN SYSTEM            ║
║                                      ║
║          Developer: SUJEET           ║
║                                      ║
╚══════════════════════════════════════╝
""")


def log(message, status="INFO"):
    now = datetime.now().strftime("%H:%M:%S")

    colors = {
        "SUCCESS": "\033[92m",
        "ERROR": "\033[91m",
        "INFO": "\033[96m",
        "WARNING": "\033[93m"
    }

    reset = "\033[0m"
    color = colors.get(status, "")

    print(f"{color}[{now}] [{status}] {message}{reset}")


def load_accounts():

    if not os.path.exists(ACCOUNTS_FILE):
        log("accounts.json not found!", "ERROR")
        return []

    try:
        with open(ACCOUNTS_FILE, "r") as file:
            accounts = json.load(file)

        if not isinstance(accounts, list):
            log("Invalid accounts.json format!", "ERROR")
            return []

        valid = []

        for account in accounts:
            if (
                isinstance(account, dict)
                and account.get("uid")
                and account.get("password")
            ):
                valid.append(account)

        return valid

    except Exception as error:
        log(f"File Error: {error}", "ERROR")
        return []


def join_guild(guild_uid, account):
    log("External guild-join API is disabled because it previously transmitted account passwords to a third party.", "ERROR")
    return False


def main():

    banner()

    accounts = load_accounts()

    if not accounts:
        log("No valid accounts found!", "ERROR")
        return

    print(f"\n[+] Loaded Accounts: {len(accounts)}")

    print("\n" + "=" * 40)

    guild_uid = input("\n[?] Enter Guild ID: ").strip()

    if not guild_uid.isdigit():
        log("Invalid Guild ID!", "ERROR")
        return

    print("\n" + "=" * 40)

    print(f"Guild ID : {guild_uid}")
    print(f"Accounts : {len(accounts)}")

    print("=" * 40)

    confirm = input("\nStart Guild Join? (y/n): ").lower()

    if confirm != "y":
        log("Operation Cancelled!", "WARNING")
        return

    print("\n")

    successful = 0
    failed = 0

    for index, account in enumerate(accounts, 1):

        print(f"\n[{index}/{len(accounts)}] Processing Account")

        before = time.time()

        join_guild(guild_uid, account)

        # Wait between requests
        if index < len(accounts):
            time.sleep(DELAY)

    print("\n")
    print("=" * 40)
    print("       GUILD JOIN PROCESS FINISHED")
    print("=" * 40)

    log("All accounts processed.", "SUCCESS")


if __name__ == "__main__":
    main()