import random
import requests
import os

# Fallback quotes if API doesn't work
def get_local_quotes():
    with open("quotes.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

# Try fetching a quote from an online API
def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}" — {data["author"]}'
    except:
        pass

    # Fallback to local quotes safely
    fallback_quotes = get_local_quotes()
    if fallback_quotes:
        return random.choice(fallback_quotes)
    else:
        return "No quotes available. Please check your quotes.txt file."

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}" — {data["author"]}'
    except:
        pass

    # Fallback to local quotes safely
    fallback_quotes = get_local_quotes()
    if fallback_quotes:
        return random.choice(fallback_quotes)
    else:
        return "No quotes available. Please check your quotes.txt file."

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}" — {data["author"]}'
    except:
        pass

    # Fallback to local quotes safely
    fallback_quotes = get_local_quotes()
    if fallback_quotes:
        return random.choice(fallback_quotes)
    else:
        return "No quotes available. Please check your quotes.txt file."

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}" — {data["author"]}'
    except:
        pass

    # Fallback to local quotes safely
    fallback_quotes = get_local_quotes()
    if fallback_quotes:
        return random.choice(fallback_quotes)
    else:
        return "No quotes available. Please check your quotes.txt file."

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}" — {data["author"]}'
    except:
        pass

    # Fallback to local quotes safely
    fallback_quotes = get_local_quotes()
    if fallback_quotes:
        return random.choice(fallback_quotes)
    else:
        return "No quotes available. Please check your quotes.txt file."

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}" — {data["author"]}'
    except:
        pass

    # Fallback to local quotes safely
    fallback_quotes = get_local_quotes()
    if fallback_quotes:
        return random.choice(fallback_quotes)
    else:
        return "No quotes available. Please check your quotes.txt file."

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}" — {data["author"]}'
    except:
        pass

    # Fallback to local quotes safely
    fallback_quotes = get_local_quotes()
    if fallback_quotes:
        return random.choice(fallback_quotes)
    else:
        return "No quotes available. Please check your quotes.txt file."

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}" — {data["author"]}'
    except:
        pass

    # Fallback to local quotes safely
    fallback_quotes = get_local_quotes()
    if fallback_quotes:
        return random.choice(fallback_quotes)
    else:
        return "No quotes available. Please check your quotes.txt file."

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}" — {data["author"]}'
    except:
        pass

    # Fallback to local quotes safely
    fallback_quotes = get_local_quotes()
    if fallback_quotes:
        return random.choice(fallback_quotes)
    else:
        return "No quotes available. Please check your quotes.txt file."


# Save a quote to a file
def save_quote(quote):
    with open("saved_quotes.txt", "a", encoding="utf-8") as file:
        file.write(quote + "\n")

def main():
    print("\n🎉 Welcome to the Quote Generator 🎉")
    while True:
        quote = get_quote()
        print("\n👉 " + quote)
        print("\nOptions:\n[1] New quote\n[2] Save this quote\n[3] Exit")
        choice = input("Choose: ")
        if choice == "1":
            continue
        elif choice == "2":
            save_quote(quote)
            print("✅ Quote saved!")
        elif choice == "3":
            print("👋 Bye! Stay inspired.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
