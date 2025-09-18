payment_method = input("Payment method? (card/cash): ").lower()
if payment_method == "card":
   print("Processing...")
else:
   print("Cash accepted")