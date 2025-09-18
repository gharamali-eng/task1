user_name = input("Name? ").strip()
mood = input("Payment method? (card/cash): ").lower()
if mood == "card":
    print("Processing...")
else :
    message = "Cash accepted"
    print(message)


