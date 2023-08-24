from faker import Faker


def random_word_generator(num_words):
    if num_words > 10000:
        raise ValueError("Number of words cannot exceed 10,000")

    fake = Faker()
    words_generated = set()

    while len(words_generated) < num_words:
        random_word = fake.word()

        if random_word not in words_generated:
            words_generated.add(random_word)
            yield random_word


int_words = 100
word_generator = random_word_generator(int_words)

for word in word_generator:
    print(word)
