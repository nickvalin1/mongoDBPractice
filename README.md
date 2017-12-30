MongoDBPractice.py includes a class called DateQueries that includes two static classes:

 1. ****most_frequent_word**** finds the most commonly used word in a collection with documents containing a date value and an array of words. There is an optional ****days**** parameter that specifies the number of days to consider when returning the most common word. If ****days**** is left blank, the function will consider all data regardless of date.

 2. ****most_trending_word**** finds the word that's usage has increased the most in the past 24 hours relative to the 24 hours before that in a collection with documents containing a date value and an array of words.

MongoDBPracticeTests.py includes unit tests for these two methods.
