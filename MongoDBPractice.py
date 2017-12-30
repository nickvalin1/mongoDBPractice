from collections import Counter
from datetime import datetime, timedelta


class DateQueries:
    @staticmethod
    def most_frequent_word(collection, days=None):
        # The default behavior is to use all data
        if days is None:
            results = collection.find()
        # If the days parameter is included, filter the data based on a cutoff of days many days ago
        else:
            today = datetime.today()
            cutoff = today - timedelta(days=days)
            results = collection.find({"date": {"$gt": cutoff}})
        words = []
        # Add all words for each document into a list
        for item in results:
            words.extend(item["words"])
        # Counter is a subclass of dictionary that returns counts of unique words in the words list
        counts = Counter(words)
        # Return the word with the highest count
        if len(counts) > 0:
            return max(counts, key=counts.get)
        # Return None if there are no words in the date range
        else:
            return None

    @staticmethod
    def most_trending_word(collection):
        upper_bound = datetime.today() - timedelta(days=1)
        lower_bound = datetime.today() - timedelta(days=2)
        # Return all results from 24-48 hours ago
        older_results = collection.find({"date": {"$gte": lower_bound}, "date": {"$lt": upper_bound}})
        # Return all results from 0-24 hours ago
        newer_results = collection.find({"date": {"$gte": upper_bound}})
        older_words = []
        newer_words = []
        # Create lists of the words from all documents from each query
        for item in older_results:
            older_words.extend(item["words"])
        for item in newer_results:
            newer_words.extend(item["words"])
        # Create counter objects from each list to get word counts
        older_counts = Counter(older_words)
        newer_counts = Counter(newer_words)
        # Counter objects can be subtracted
        # This does not work for negative results,
        # but a negative result can be ignored because we are only looking for positive increases
        increase = newer_counts - older_counts
        if len(older_counts) > 0 and len(newer_counts) > 0:
            return max(increase, key=increase.get)
        # If there are no documents in either date range, return None
        else:
            return None
