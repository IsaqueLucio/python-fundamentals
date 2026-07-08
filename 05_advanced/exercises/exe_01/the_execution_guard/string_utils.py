def reverse_string(text: str) -> str:
    return text[::-1]

def count_vowels(text: str) -> int:
    text_low = text.lower()
    cont = 0
    vowels = ['a','e','i','o','u']
    for letter in text_low:
        if letter in vowels:
            cont +=1
    return cont

if __name__ == "__main__":
    python = "Python"
    developer = "Developer"
    print(count_vowels(developer))
    print(reverse_string(python))