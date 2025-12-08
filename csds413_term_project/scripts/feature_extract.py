'''
Feature extraction script for the permutation test.

:author: Jacob Anderson
:version: 0.1.0
'''

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

def download_nltk_resources():
    '''
    Downloads NLTK resources.
    '''
    try: nltk.data.find('tokenizers/punkt')
    except LookupError: nltk.download('punkt', quiet=True)
    
    try: nltk.data.find('corpora/stopwords')
    except LookupError: nltk.download('stopwords', quiet=True)

def is_abnormal_capitalization(word: str, is_sentence_start: bool) -> bool:
    '''
    Determines if a word has abnormal capitalization patterns; this is determined
    by a couple of rules that I figured would apply well to most cases in the cleaned
    data. It includes formal rules for capitalizing sentences, use of acronyms, and
    mixed case criteria.
    
    :param word: Word to check
    :type word: str
    :param is_sentence_start: Whether word starts a sentence
    :type is_sentence_start: bool
    :returns: True if abnormal, False otherwise
    :rtype: bool
    '''
    
    if len(word) <= 1:
        if word == 'i': 
            return True
        return False
    
    if word.isupper() and len(word) >= 5: return True
    
    capital_positions = [i for i, c in enumerate(word) if c.isupper()]
    if len(capital_positions) > 1: return True
    
    if is_sentence_start and word[0].islower(): return True
    
    return False

def extract_features(text: str, stopwords_set: set) -> dict:
    '''
    Extracts the five statistical features for a single tweet.
    
    :param text: Cleaned tweet text
    :type text: str
    :param stopwords_set: Set of functional words
    :type stopwords_set: set
    :returns: Dictionary containing the five features
    :rtype: dict
    '''
    # Tokenizes text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenizes into words and filters to alphabetic only
    all_tokens = word_tokenize(text)
    words = [token for token in all_tokens if token.isalpha()]
    
    # Handles empty tweet edge case. The cleaning does handle empty tweets,
    # but after tokenizing, some tweets filled with just smybols or something
    # else weird may come up empty and give div by zero errors
    if len(words) == 0 or len(sentences) == 0:
        return {'V': 0.0, 'S': 0.0, 'W': 0.0, 'F': 0.0, 'C': 0.0}
    
    # Vocab richness
    unique_words = len(set(words))
    total_words = len(words)
    V = unique_words / total_words
    
    # Sentence length
    total_sentences = len(sentences)
    S = total_words / total_sentences
    
    # Word length
    total_chars = sum(len(word) for word in words)
    W = total_chars / total_words
    
    # Function word freq
    function_words = [word for word in words if word.lower() in stopwords_set]
    F = len(function_words) / total_words
    
    # Capitalization abnormality
    abnormal_count = 0
    for sentence in sentences:
        sentence_tokens = word_tokenize(sentence)
        sentence_words = [token for token in sentence_tokens if token.isalpha()]
        
        for i, word in enumerate(sentence_words):
            is_sentence_start = (i == 0)
            if is_abnormal_capitalization(word, is_sentence_start):
                abnormal_count += 1
    C = abnormal_count / total_words
    
    return {'V': V, 'S': S, 'W': W, 'F': F, 'C': C}

def main():
    # Loads NLTK resources
    download_nltk_resources()
    stopwords_set = set(stopwords.words('english'))
    
    output_path = '../data/tweepfake_features.csv'
    df = pd.read_csv('../data/tweepfake.csv', sep=';')
    
    # Performs feature extraction
    features_list = []
    for _, row in df.iterrows():
        features = extract_features(row['text'], stopwords_set)
        features['text'] = row['text']
        features['label'] = row['label']
        features_list.append(features)

    # Frames and orders cols    
    features_df = pd.DataFrame(features_list)
    features_df = features_df[['text', 'label', 'V', 'S', 'W', 'F', 'C']]

    features_df.to_csv(output_path, sep=';', index=False)
    
if __name__ == "__main__": main()
