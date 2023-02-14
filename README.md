## AffinityAnswers Assignment

This is my solution for assignment by **AffinityAnswers** for role **Data Engineering internship**


### Assignment

> Do read the following [blog](https://medium.com/affinityanswers-tech/recruitment-how-not-to-answer-our-take-home-questions-57153d143447) post before answering the questions

Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. Write a program that can indicate the degree of profanity for each sentence in the file. Write in any programming language (preferably in Python) - make any assumptions, but remember to state them. 


### Solution

NOTE: A dataset is included in `resources` directory

I will break my solution into multiple steps which are following:

1. Load Tweets and Slurs from respective files. Make dataframe from tweets.
2. Clean the data(tweets) by removing:
    - `@user`
    - Punctuations
    - Special Characters
    - Numbers
    - Words which contain less than 3 words(except slurs)
3. Create regex pattern for matching racial slurs.
4. Loop through the data and calculate degree of profanity and print it.


### Setup Instructions

- Navigate into *project's home directory*
- Install required modules by using:

    ```bash
    pip install -r requirements.txt
    ```
- Run the program using:
    ```bash
    python main.py
    ```