def text_counter():
    # Pobieranie danych od użytkownika
    text = input("Wprowadź tekst do analizy: ")
    
    char_count = len(text)
    
    spaces_amnt = sum(1 for char in text if char == " ")
    char_count_no_spaces = len(text) - spaces_amnt
    
    words = text.split()
    word_count = len(words)
    
    # Liczenie samogłosek i spółgłosek
    vowels = "aeiouAEIOUąęióóyĄĘIÓÓY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZćłńśźżĆŁŃŚŹŻ"
    
    vowel_count = sum(1 for char in text if char in vowels)
    
    consonant_count = sum(1 for char in text if char in consonants)
    
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