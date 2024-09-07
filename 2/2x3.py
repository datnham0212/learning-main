
def vowels_count(text):
    vowels = 'aeiou'
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

if __name__ == '__main__':
    string = input('Enter text: ') 
    print("Number of vowels: ", vowels_count(string))
    print("Number of consonants: ", len(string) - vowels_count(string))

