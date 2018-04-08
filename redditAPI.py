import praw
from praw.models import MoreComments

reddit = praw.Reddit(user_agent='theRealBakhtar by u/theRealBakhtar',
					 client_id='Ce0jyTV4usdsIQ',
					 client_secret='SBJS1LhLqWSGshviLdgNQJSRM3Q')
submission = reddit.submission(url='https://www.reddit.com/r/politics/comments/6q1sl0/us_senate_healthcare_repeal_bill_fails/')

pew = []

submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
	if len(comment.body.split()) > 100:
		pew.append(comment.body)

file = open('HealthcareTest.csv', 'w')
file.write('comment,\n')
for i in pew:
	results_str=i.replace('\n', '')
	results_str2=results_str.replace(',', '')
	file.write(results_str2 + ',\n')
file.close()
