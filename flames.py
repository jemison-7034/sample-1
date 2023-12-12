def flames(First_persons_Name, Second_persons_name):
    combined_name = (First_persons_Name + Second_persons_name).lower()
    flames = "flames"
    count = {}
    for letter in flames:
        count[letter] = combined_name.count(letter.lower())

   
    remaining = sum(count.values())
    while len(flames) > 1:
        index = remaining % len(flames)
        if index == 0:
            index = len(flames)
        flames = flames[:index - 1] + flames[index:]
    
    return flames


First_persons_name = input("Enter the  First_persons_name: ")
Second_persons_name = input("Enter the  Second_persons_name: ")
flames_result = flames(First_persons_name, Second_persons_name)


Result = {
    'f': "Friend",
    'l': "Love",
    'a': "Affection",
    'm': "Marriage",
    'e': "Enemy",
    's': "Sibling"}


print(f"Flames Result: {flames_result}")
print(f"Meaning: {Result[flames_result]}")
