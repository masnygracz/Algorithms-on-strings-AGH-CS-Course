def text_counter():
    # Pobieranie danych od użytkownika
    text = input("Wprowadź tekst do analizy: ")
    
    # Obliczenia
    # TODO: Oblicz liczbę wszystkich znaków w tekście
    char_count = ___
    
    # TODO: Oblicz liczbę znaków bez spacji
    char_count_no_spaces = ___
    
    # TODO: Podziel tekst na słowa i oblicz ich liczbę
    words = ___
    word_count = ___
    
    # Liczenie samogłosek i spółgłosek
    vowels = "aeiouAEIOUąęióóyĄĘIÓÓY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZćłńśźżĆŁŃŚŹŻ"
    
    # TODO: Zlicz samogłoski w tekście
    vowel_count = ___
    
    # TODO: Zlicz spółgłoski w tekście
    consonant_count = ___
    
    # Wyświetlanie wyników
    print(f"\nAnaliza tekstu: \"{text}\"")
    print(f"Liczba słów: {word_count}")
    print(f"Liczba znaków (ze spacjami): {char_count}")
    print(f"Liczba znaków (bez spacji): {char_count_no_spaces}")
    print(f"Liczba samogłosek: {vowel_count}")
    print(f"Liczba spółgłosek: {consonant_count}")


# Wywołanie funkcji
if __name__ == "__main__":
    text_counter()