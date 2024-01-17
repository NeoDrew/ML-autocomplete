# ML-autocomplete

Machine Learning autocompletion


# Plan

### Goal

Create a machine learning algorithm that will autocomplete input words given a corpous of text.

### Components

* Corpus - local copy of large text sample
* Tokenizer - storing tokens
* App.py - main functions for autocompletion
* Tests.py - Used to test accuracy (Precision, Recall, F1, etc)

### Corpus

Plan to use compilation of books. Books provide a good source as they often contain a large variety in vocabulary. The weakpoint of this model will be the variety of text it is trained on.

### Tokenizer

The tokenizer can be seen as an abstract model which is provided with a number of preprocessed words (tokens.) The words will be stored in working memory. This will speed up look-up times for the autocompletion.

Words can be stored using their values but can be looked up using their prefix. For example, 'museum' can be stored and returned as part of a vector of matches for the prefix 'mus.' This implementation will have to be well thought out; some data structures will not be appropriate: hashmap, queue, etc.

A possible implementation could be a simple ordered vector, utilising a divide and conquor search algorithm, then returning the next n-number of words with the same starting prefix.

### App.py

App.py will handle the front-end implementation of the autocorrection model. Given a specific prefix, app.py will return a number of potential endings, with the following constraints: it will only return the 'best' 3 words and the words will be ordered by their probabilites.

The next step for App.py will be to dynamic autocorretion, e.g autocorrect suggestions while typing. This would allow a user to type the start of the word and enter more characters to retrieve more precise suggestions.

### Tests.py

Like with any good ML model, tests are an essential part of the evaluation process. A typical split, which I will be using, is 20:80. Meaning 20% of my corpous will be for testing the model which will be trained on the other 80%.

A good model should be able to correctly predict the ending of a word given a number of characters. The number of characters can vary by test, a single character would not be enough information to make an accurate guess.

**My goal for this model to have an accuracy of over 80% given a softmax on its predicted endings.**
