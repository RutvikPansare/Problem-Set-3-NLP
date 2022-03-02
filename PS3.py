import nltk
from textblob import TextBlob
from allennlp.predictors.predictor import Predictor
import spacy

"""
NLP 681 PS3
Author: Rutvik pansare rp2832
"""

def textblob_sentiment(sentences):
    for sentence in sentences:
        testimonial = TextBlob(sentence)
        print(testimonial.sentiment)




sentence1 = "He hath eaten me out of house and "
sentence2 = "tis not long after but i will wear my heart upon my sleeve ."
sentence3 =  "You know that smoodle pinkered and that I want to get him"
sentence4 = "My door sat through the lamp in the "
sentence5 = "A self-driving small-sized car stopped at the light"

sentences = [sentence1,sentence2,sentence3,sentence4,sentence5]
textblob_sentiment(sentences)



