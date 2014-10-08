# -*- coding: utf-8 -*-
# An experiment using Naive Bayes classifier to detect homophobia, other types of hate in comments, text and tweets.
from textblob.classifiers import NaiveBayesClassifier
from flask import Flask,request
import pickle,os
from termcolor import colored, cprint

app = Flask(__name__)

tests = [
("I will beat a dyke ass over mine",'hate'),
("Dick riding faggot, you love the attention",'hate'),
("Twilight marathon tonight ? (No homo)",'hate'),
("this so he knows how much of a faggot he is",'hate'),
("you look like such a faggot  You prolly hate your parents soooooo much I bet you think the only good cop is a dead one","hate"),
("and the trannies are already pissed lol ","hate"),
("*Sees a hedgehog on tumblr* babe I want a hedgehog go get me a hedgehog - every stupid bitch ever","hate"),
('fucking pathetic pathetic human being, cunt','hate'),
("people who have faggot or other unnecessary slurs in their usernames on social media :/ it is 2014 stop being gross","not"),
("sunshine and puppies and rainbows",'not'),
("i want to eat cabbage",'not'),
("straight guys in my art class saying \"faggot\" made me feel so much anger agree!!!",'not'),
("Just googled, 'Can cats have panic attacks?', after Zula ran in from the garden, hissed at me and now is weezing/panting :/",'not'),
("I don't think people should use the word faggot",'not'),
("there should be no reason that i see the word faggot, cunt, tranny, etc on my TL unless ur dragging someone for using those terms",'not'),
("Demi gets called a dyke or a lesbian for things that people with any sexual orientation do or wear. I don't get it.",'not'),
("Hearing the word \"faggot\" come out of anybody's mouth makes me cringe. When you're a PARENT and saying it...makes me extra disgusted.",'not'),
("I hate the word faggot.",'not'),
("I feel amazing!", 'not'),
('Gary is a friend of mine.', 'not'),
("I can't believe I'm doing this.", 'not'),
]

def save_classifier(classifier):
	f = open('hate_classifier.pickle', 'wb')
	pickle.dump(classifier, f, -1)
	f.close()

def load_classifier():
	f = open('hate_classifier.pickle', 'rb')
	classifier = pickle.load(f)
	f.close()
	return classifier

def setup_classifier():
	if os.path.isfile('hate_classifier.pickle'):
		cl = load_classifier()
	else:
		with open('train.json', 'r') as fp:
			cl = NaiveBayesClassifier(fp, format="json")
			save_classifier(cl)
	return cl


def run_tests(cl):
	print "=================="
	print "accuracy vs test set:",cl.accuracy(tests)
	print "=================="

	for item in tests:
		prob_dist = cl.prob_classify(item[0])
		
		text = item,prob_dist.max(),round(prob_dist.prob("hate"), 2),round(prob_dist.prob("not"), 2)
		if(item[1] != prob_dist.max()):
			print colored(text,'red');
		else:
			print colored(text,'blue');

	
def main():

	cl = setup_classifier();
	run_tests(cl);

	print "send messages to classify to http://yourhost:5000/classify?message=your message here"
	@app.route("/classify")
	def classify():
		message = request.args.get('message')
		prob_dist = cl.prob_classify(message)
		print message,prob_dist.max(),round(prob_dist.prob("hate"), 2),round(prob_dist.prob("not"), 2)
		return prob_dist.max()

if __name__ == "__main__":
	main()
	app.run()	

