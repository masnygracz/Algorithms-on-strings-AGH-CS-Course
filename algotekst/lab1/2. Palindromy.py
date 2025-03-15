def is_palindrome(text):
    
    return text == text[::-1]


def make_palindrome(text):
    # Usuwamy spacje i konwertujemy do małych liter
    text = text.replace(" ", "")
    
    # Sprawdzamy, czy już jest palindromem
    if is_palindrome(text):
        return text
    
    option1 = text + text[::-1]
    
    option2 = text[:0:-1] + text
    
    return option1 if len(option1) < len(option2) else option2


def palindrome_checker():
    # Pobieranie danych od użytkownika
    text = input("Wprowadź słowo lub frazę: ")
    
    clean_text = "".join(char.lower() for char in text if char.isalnum())
    
    # Sprawdzanie, czy to palindrom
    if is_palindrome(clean_text):
        print(f"\"{text}\" jest palindromem!")
    else:
        print(f"\"{text}\" nie jest palindromem.")
        suggested = make_palindrome(clean_text)
        print(f"Sugerowany palindrom: {suggested}")


# Wywołanie funkcji
if __name__ == "__main__":
    palindrome_checker()