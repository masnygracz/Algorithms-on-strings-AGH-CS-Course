def zad3():
    text = input("Wprowadź ciąg znaków: ")
    
    frequency = {}
    for letter in text:
        frequency[letter] = frequency.get(letter, 0) + 1
    
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    print("\nCzęstotliwość znaków (od najczęstszych)")
    for char, count in sorted_frequency:
        print(f"{char} : {count}")
    
    text2 = input("Wprowadź drugie słowo: ")
    frequency2 = {}
    for letter in text2:
        frequency2[letter] = frequency2.get(letter, 0) + 1
    
    for char in frequency2:
        if char not in frequency or frequency2[char] > frequency[char]:
            print("False")
            return None
    print("True")


if __name__ == "__main__":
    zad3()