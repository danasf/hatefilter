Hate Filter
=====
A simple experiment using a Naïve Bayes classifier to detect homophobia, other types of hate in comments, text and tweets. At the moment the corpus of training data is really small.

Contributions and ideas for improvement are welcome. 


How To Run
-----
At the command line

`python python hate_classifier.py`

Via the browser

`http://localhost:5000/classify?message=this%20isn't%20hateful` 

Returns JSON
```
{
  "classification": "not", 
  "message": "this isn't hateful", 
  "prob_hate": 0.23, 
  "prob_not": 0.77
}
```

Futher Reading
-----

* Python's [NLTK](http://www.nltk.org/) and [TextBlob](http://textblob.readthedocs.org/en/latest/index.html#)
* Tutorial on building a [text classification system](http://textblob.readthedocs.org/en/latest/classifiers.html)
* Read about Naïve Bayes classifier as a tool for [spam filtering](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)

