import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#install twython and from nltk.download() get vader_lexicon in models

reddit = praw.Reddit(user_agent='Comment Extraction', client_id='CLIENT_ID', client_secret='CLIENT_SECRET', username='USERNAME', password='PASSWORD')

submission = reddit.submission(url='https://www.reddit.com/r/SquaredCircle/comments/5si8pp/live_raw_discussion_thread_feb_6th_2017/')

sid = SentimentIntensityAnalyzer()

c=1
f=open('Roman.txt','w')
f2=open('Braun.txt','w')
k=1
for comment in submission.comments.list():
    	#print(comment.body)
    	print comment.body
    	print k
    	k+=1
	for i in comment.body.split(' '):
	    	ss=sid.polarity_scores(comment.body)
	    	if i=='Roman':	
	    		f.write(comment.body)
	    		f.write('\n')
	    		f.write(str(c))
	    		f.write('\t')
	    		f.write(str(ss))
	    		f.write('\n')
	    		c=c+1
		if i=='Braun':	
	    		f2.write(comment.body)
	    		f2.write('\n')
	    		f2.write(str(c))
	    		f2.write('\t')
	    		f2.write(str(ss))
	    		f2.write('\n')
	    		c=c+1
	
print c
	   
"""
Arranges comments based on highest points and prints it to console
We need to see the documentation of the comment objects and store accordingly
Need to see about replies and all
"""
