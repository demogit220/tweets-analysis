import pandas as pd
import numpy as np
import re
import os


class RacialSlurClassifier:
    def __init__(self, tweets_file_path, slurs_file_path) -> None:
        self.df = pd.read_csv(tweets_file_path)
        with open(slurs_file_path, 'r', encoding='utf-8') as f:
            self.racial_slurs = f.read().splitlines()

    # The function returns the same input string but without the given pattern
    def _remove_pattern(self, input_txt, pattern):
        r = re.findall(pattern, input_txt)
        for i in r:
            input_txt = re.sub(i, '', input_txt)

        return input_txt

    # Combining all the words from slurs.txt with separater as `|`
    def _get_regex_pattern(self):
        pattern = re.compile('|'.join(self.racial_slurs), re.IGNORECASE)
        return pattern

    def get_profanity_degree(self, tweet):
        degree_of_profanity = 0

        # count number of racial slurs in tweet
        num_slurs = len(re.findall(self._get_regex_pattern(), tweet))

        # calculate degree of profanity as a percentage of total words in tweet
        if len(tweet.split()) > 0:  # checking for divide by zero error
            degree_of_profanity = num_slurs / len(tweet.split()) * 100
        return degree_of_profanity

    def clean_data(self):
        # Removes all types of twitter handles (@user)
        self.df['tidy_tweet'] = np.vectorize(
            self._remove_pattern)(self.df['tweet'], "@[\w]*")

        # Removes special characters, numbers and punctuations
        self.df['tidy_tweet'] = self.df['tidy_tweet'].str.replace(
            "[^a-zA-Z]", " ")

        # Removing all the words with less than 3 characters
        self.df['tidy_tweet'] = self.df['tidy_tweet'].apply(
            lambda x: ' '.join([w for w in x.split() if len(w) >= 3]))

    def print_profanity_degree(self):
        # iterate over tweets and check for racial slurs
        for tweet in self.df['tidy_tweet']:
            degree_of_profanity = self.get_profanity_degree(tweet)
            # print degree of profanity for tweet
            print(
                f"Tweet: {tweet.strip()} \nDegree of Profanity: {degree_of_profanity:.2f}%\n")


# Add environment variables if required
TWEETS_FILE_PATH = os.path.join('resources', "tweets.csv")
SLURS_FILE_PATH = os.path.join('resources', "slurs.txt")


if __name__ == "__main__":
    classifier_object = RacialSlurClassifier(TWEETS_FILE_PATH, SLURS_FILE_PATH)
    classifier_object.clean_data()
    classifier_object.print_profanity_degree()
