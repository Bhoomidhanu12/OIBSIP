import datetime

def respond_to_hello():
    return "Hello! How can I help you?"

def get_current_time():
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%H:%M')}."

def get_current_date():
    now = datetime.datetime.now()
    return f"Today is {now.strftime('%Y-%m-%d')}."

def search_web(query):
    return f"I'm sorry, I cannot perform web searches in this basic version. You asked about: {query}"

def main():
    print("Voice Assistant Activated. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            print(respond_to_hello())
        elif "time" in user_input:
            print(get_current_time())
        elif "date" in user_input:
            print(get_current_date())
        elif "search" in user_input:
            query = user_input.replace("search", "").strip()
            print(search_web(query))
        elif user_input == "exit":
            print("Voice Assistant Deactivated.")
            break
        else:
            print("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
