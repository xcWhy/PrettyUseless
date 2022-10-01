from tika import parser # pip install tika
import string
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from heapq import nlargest
punctuations = string.punctuation
nlp = English()
nlp.add_pipe('sentencizer') # updated
language = English()

paragraphs = []
par = ''

def pre_process(document):
    clean_tokens = [token.lemma_.lower().strip() for token in document]
    clean_tokens = [token for token in clean_tokens if token not in STOP_WORDS and token not in punctuations]
    tokens = [token.text for token in document]
    lower_case_tokens = list(map(str.lower, tokens))

    return lower_case_tokens

def generate_numbers_vector(tokens):
    frequency = [tokens.count(token) for token in tokens]
    token_dict = dict(list(zip(tokens,frequency)))
    maximum_frequency=sorted(token_dict.values())[-1]
    normalised_dict = {token_key:token_dict[token_key]/maximum_frequency for token_key in token_dict.keys()}
    return normalised_dict

def sentences_importance(text, normalised_dict):
    importance ={}
    for sentence in nlp(text).sents:
        for token in sentence:
            target_token = token.text.lower()
            if target_token in normalised_dict.keys():
                if sentence in importance.keys():
                    importance[sentence]+=normalised_dict[target_token]
                else:
                    importance[sentence]=normalised_dict[target_token]
    return importance

def generate_summary(rank, text):
    target_document = language(text)
    importance = sentences_importance(text, generate_numbers_vector(pre_process(target_document)))
    summary = nlargest(rank, importance, key=importance.get)
    return summary

def create_txt(location_for_new_file, location_of_pdf):

    with open(str(f'D:\Downloads\{location_for_new_file}.txt'), "w", encoding="utf-8") as f:
        global par
        raw = parser.from_file(f'{location_of_pdf}')
        print(raw['content'])
        text = raw['content']

        print(len(text))

        for i in text:
            par += i
            if len(par) == 2000:
                paragraphs.append(par)
                par = ''

        print(paragraphs)
        print(len(paragraphs))

        num_sentences_to_generate = 1
        for i in range(len(paragraphs)):

            summary = generate_summary(num_sentences_to_generate, paragraphs[i])
            f.write(str(summary))
            f.write('\n\n~~~~~~~~~~~~~~~~~~~~~~~\n\n')
            print(summary)

    print('the file is done')

#create_txt(1, 2)

print('done')

# with open('D:\Downloads\emi_pdf.txt', "w", encoding="utf-8") as f:
#     raw = parser.from_file('D:\Downloads\\19660001593.pdf')