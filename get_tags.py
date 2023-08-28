import nltk
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# nltk.download('averaged_perceptron_tagger')


def extract_tags(text):
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    tags = [f"#{word}" for word, pos in pos_tags if pos.startswith('N')]
    tags_string = ' '.join(tags)
    return tags_string


# tags = extract_tags("The last time Hollywood's actors and writers went on strike at the same time, the biggest stars were fighting for residual pay cheques. Decades later, streaming giants and artificial intelligence are at the heart of the debate")
# print(tags)
