import json
import nltk
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


def update_config(key, value):
    config = json.loads(open("app_data/app_config.json", "r").read())

    config[key] = value

    open("app_data/app_config.json", "w").write(json.dumps(config, indent=4))
  




def get_config(key):
    return json.loads(open("app_data/app_config.json", "r").read())[key]




# def extract_tags(text):
#     # Tokenize the text into individual words
#     words = nltk.word_tokenize(text)

#     # Remove stopwords (common words like 'is', 'this', etc.)
#     stopwords = nltk.corpus.stopwords.words('english')
#     filtered_words = [word for word in words if word.lower() not in stopwords]

#     # Perform part-of-speech tagging to identify nouns and adjectives
#     pos_tags = nltk.pos_tag(filtered_words)

#     # Select only nouns and adjectives as tags
#     tags = [word for word, pos in pos_tags if pos.startswith('N') or pos.startswith('J')]

#     return tags

# # Example usage
# text = "Hello world! This is simple text"
# tags = extract_tags(text)
# print(tags)




# nltk.download('punkt')

