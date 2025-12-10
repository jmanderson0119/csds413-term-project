'''
Data cleaning script for TweepFake dataset.

Removes URLs, mentions, hashtags, emojis, escape 
sequences, filters corrupted content, etc.

:author: Jacob Anderson
:version: 0.1.0
'''

import pandas as pd
import re

def clean_tweet(text: str) -> str:
    '''
    Cleans a single tweet by removing URLs, mentions, hashtags, emojis,
    and literal escape sequences.
    
    :param text: Raw tweet text
    :type text: str
    :returns: Cleaned tweet text with normalized whitespace
    :rtype: str
    '''
    text = re.sub(r'http\S+|https\S+|www\.\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'\\n', ' ', text)
    text = re.sub(r'\\t', ' ', text)
    text = re.sub(r'\\r', ' ', text)
    text = re.sub(r'\\\\', '', text)
    text = re.sub(r'<U\+[0-9A-Fa-f]+>', '', text)
    
    # Removes unicode ranges for emojis; occurrences are represented as raw text in hte dataset
    emoji_pt = re.compile(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )
    text = emoji_pt.sub('', text)
    
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    text = text.strip('"""')
    text = text.strip('""')
    
    return text

def contains_html_markup(text: str) -> bool:
    '''
    Checks if text contains HTML/XML markup or escaped characters.
    
    :param text: Clean tweet text
    :type text: str
    :returns: True if detected, False otherwise
    :rtype: bool
    '''
    if pd.isna(text):
        return False
    
    html_pt = [r'<[^>]+>', r'&[a-z]+;', r'class=', r'src=', r'id=', 
               r'alt=', r'\\r\\n', r'\\"']
    
    for pattern in html_pt:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

def contains_mojibake(text: str) -> bool:
    '''
    Checks if text contains corrupted char encodings.
    
    :param text: Cleaned text
    :type text: str
    :returns: True if detected, False otherwise
    :rtype: bool
    '''
    moj_pt = [r'Ã[\x80-\xBF]', r'Â[\x80-\xBF]', r'Ã¯Â¿Â½', r'[ÃÂ¯¿½]{3,}']
    
    for pattern in moj_pt:
        if re.search(pattern, text):
            return True
    return False

def contains_file_paths(text: str) -> bool:
    '''
    Checks if text contains file paths.
    
    :param text: Cleaned text
    :type text: str
    :returns: True if detected, False otherwise
    :rtype: bool
    '''
    if pd.isna(text):
        return False
    
    path_patterns = [r'dev', r'/usr/', r'/etc/', r'/var/', 
                     r'/vars/', r'/home/', r'/opt/', r'[A-Z]:\\', 
                     r'/[\w.-]+/[\w.-]+/', r'\d{10,}']
    
    for pattern in path_patterns:
        if re.search(pattern, text):
            return True
    return False

def main():
    df = pd.read_csv('../../data/tweepfake_raw.csv', sep=';')
    df['text'] = df['text'].apply(clean_tweet)

    # Removes any tweets rendered completely blank    
    df = df[df['text'].str.len() > 0]

    # Filters out tweets with html/xml markup    
    df = df[~df['text'].apply(contains_html_markup)]
    
    # Filters out tweets with corrupted encodings
    df = df[~df['text'].apply(contains_mojibake)]
    
    # Filters out tweets with file paths and system artifacts
    df = df[~df['text'].apply(contains_file_paths)]
    
    df = df[['text', 'account.type']]
    df = df.rename(columns={'account.type': 'label'})

    df.to_csv('../../data/tweepfake.csv', sep=';', index=False)

if __name__ == "__main__": main()
