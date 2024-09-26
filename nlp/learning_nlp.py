import nltk

#Lowercasing
og_text1 = "DATA Science and MACHINE Learning are closely related."

lowercase = og_text1.lower()

print(f"Lowercased text: {lowercase}")


#Removing dupilcated words
og_text2 = "Amazing, amazing, amazing product!"

new_text2 = [i.lower() for i in og_text2.replace('!', '').replace(',', '').split()]

processed_text2 = ' '.join(sorted(set(new_text2))).capitalize()

print(processed_text2)
