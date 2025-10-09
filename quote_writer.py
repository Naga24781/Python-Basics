
try:
    with open("quote.txt", "w") as f:
        quote = input("Enter your favorite quote: ")
        f.write(quote)
    print(" Quote saved successfully!")

    with open("quote.txt", "r") as f:
        print("\n Your saved quote:")
        print(f.read())

except Exception as e:
    print(" Error:", e)
