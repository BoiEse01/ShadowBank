import os
import json

USERS_DIR = "users"

def create_account():
    name = input("Enter your full name: ")
    pin = input("Set a 4-digit PIN: ")
    balance = 0.0
    account = {
        "name": name,
        "pin": pin,
        "balance": balance
    }

    filename = os.path.join(USERS_DIR, name.lower().replace(" ", "_") + ".json")
    with open(filename, "w") as f:
        json.dump(account, f)
    print(f"✅ Account created for {name}!\n")

def login():
    name = input("Enter your name: ")
    pin = input("Enter your PIN: ")
    filename = os.path.join(USERS_DIR, name.lower().replace(" ", "_") + ".json")

    if not os.path.exists(filename):
        print("❌ Account not found.\n")
        return

    with open(filename, "r") as f:
        account = json.load(f)

    if account["pin"] != pin:
        print("❌ Wrong PIN.\n")
        return

    print(f"✅ Welcome {account['name']}!")
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"💳 Balance: ₦{account['balance']}")
        elif choice == "2":
            amt = float(input("Enter amount to deposit: ₦"))
            account["balance"] += amt
            print(f"✅ New Balance: ₦{account['balance']}")
        elif choice == "3":
            amt = float(input("Enter amount to withdraw: ₦"))
            if amt > account["balance"]:
                print("❌ Insufficient funds.")
            else:
                account["balance"] -= amt
                print(f"✅ New Balance: ₦{account['balance']}")
        elif choice == "4":
            break

        # Save after every change
        with open(filename, "w") as f:
            json.dump(account, f)

def main():
    if not os.path.exists(USERS_DIR):
        os.makedirs(USERS_DIR)

    while True:
        print("\n🏦 Welcome to ShadowBank")
        print("1. Create Account\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

  
