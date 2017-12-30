import unittest
from pymongo import MongoClient
from datetime import datetime
from MongoDBPractice import DateQueries


class MongoDBPracticeTests(unittest.TestCase):

    @classmethod
    def setUp(cls):
        client = MongoClient()
        db = client.test

        db.words.remove()

        dates = [datetime(2017, 12, 12, 0, 0), datetime(2017, 12, 13, 5, 0), datetime(2017, 12, 27, 0, 0),
                 datetime(2017, 12, 19, 0, 10), datetime(2017, 12, 28, 0, 59)]
        words = [["this", "is", "a"], ["test", "word", "for", "testing"], ["test", "this", "words"],
                 ["test", "testy", "tester"], ["test", "testy", "testy"]]

        for i in range(len(dates)):
            entry = {"date": dates[i], "words": words[i]}
            db.words.insert(entry)

        cls.collection = db.words

    def test_most_frequent_word_all(self):
        result = DateQueries.most_frequent_word(self.collection)
        self.assertEqual(result, "test")

    def test_most_frequent_word_1_day(self):
        result = DateQueries.most_frequent_word(self.collection, 1)
        self.assertEqual(result, "testy")

    def test_most_trending_word(self):
        result = DateQueries.most_trending_word(self.collection)
        self.assertEqual(result, "testy")



if __name__ == '__main__':
    unittest.main()
