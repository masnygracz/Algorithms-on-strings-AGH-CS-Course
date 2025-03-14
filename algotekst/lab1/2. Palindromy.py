def is_palindrome(text):
    # TODO: Usuń spacje i przekształć tekst na małe litery
    text = ___
    
    # TODO: Sprawdź, czy tekst czytany od przodu jest taki sam jak od tyłu
    # WSKAZÓWKA: Użyj notacji text[::-1] aby odwrócić tekst
    return ___


def make_palindrome(text):
    # Usuwamy spacje i konwertujemy do małych liter
    text = text.lower().replace(" ", "")
    
    # Sprawdzamy, czy już jest palindromem
    if is_palindrome(text):
        return text
    
    # TODO: Utwórz palindrom dodając odwrócone znaki na końcu
    # (bez ostatniego znaku, który już jest na początku odwróconego tekstu)
    option1 = ___
    
    # TODO: Utwórz palindrom dodając odwrócone znaki na początku
    # (bez pierwszego znaku, który już jest na końcu oryginalnego tekstu)
    option2 = ___
    
    # TODO: Zwróć krótszą opcję jako wynik
    return ___


def palindrome_checker():
    # Pobieranie danych od użytkownika
    text = input("Wprowadź słowo lub frazę: ")
    
    # TODO: Usuń znaki, które nie są literami ani cyframi, i zamień na małe litery
    # WSKAZÓWKA: Wykorzystaj funkcję isalnum() i list comprehension lub wyrażenie generujące
    clean_text = ___
    
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