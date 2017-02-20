import praw
import nltk
from nltk import word_tokenize
def preprocessing(sentence):
    
    sentence=word_tokenize(sentence)
    porter = nltk.PorterStemmer()
    sentence=[porter.stem(t) for t in sentence]
    wnl = nltk.WordNetLemmatizer()
    sentence=[wnl.lemmatize(t) for t in sentence]
    sentence=' '.join(sentence)
    return sentence

from nltk.sentiment.vader import SentimentIntensityAnalyzer
#install twython and from nltk.download() get vader_lexicon in models
reddit = praw.Reddit(user_agent='Comment Extraction (by /u/paddy1709)', client_id='', client_secret='', username='', password='')

#submission = reddit.submission(url='https://www.reddit.com/r/SquaredCircle/comments/5si8pp/live_raw_discussion_thread_feb_6th_2017/')
#submission.comments.replace_more(limit=100)
#flat_comments = praw.helpers.flatten_tree(submission.comments)
sid = SentimentIntensityAnalyzer()
#submission.comments.replace_more(limit=0)
c=1
#f=open('Roman.txt','w')
#f2=open('Braun.txt','w')
k=1
episodes=['https://www.reddit.com/r/asoiaf/comments/4gavuu/spoilers_extended_game_of_thrones_season_6/',
 'https://www.reddit.com/r/asoiaf/comments/4hcv56/spoilers_extended_game_of_thrones_season_6/',
 'https://www.reddit.com/r/asoiaf/comments/4ih5ya/spoilers_extended_game_of_thrones_season_6/',
 'https://www.reddit.com/r/asoiaf/comments/4jisvr/spoilers_extended_game_of_thrones_season_6/',
 'https://www.reddit.com/r/asoiaf/comments/4klca8/spoilers_extended_game_of_thrones_season_6/',
 'https://www.reddit.com/r/asoiaf/comments/4ln1bl/spoilers_extended_game_of_thrones_season_6/',
 'https://www.reddit.com/r/asoiaf/comments/4mq9lg/spoilers_extended_game_of_thrones_season_6/',
 'https://www.reddit.com/r/asoiaf/comments/4nt78z/spoilers_extended_game_of_thrones_season_6/',
 'https://www.reddit.com/r/asoiaf/comments/4ow37m/spoilers_extended_game_of_thrones_season_6/',
 'https://www.reddit.com/r/asoiaf/comments/4q0ndz/spoilers_extended_game_of_thrones_season_6/']
count=0
for e in episodes:
    submission=reddit.submission(url=e)
    submission.comments.replace_more(limit=10)
    pos_total=neg_total=0.0
    flag=False
    k=0
    count+=1
    for comment in submission.comments:
        #print(comment)
        preprocessing(comment.body)
        #print("score for the below comment is"+str(comment.score))
        #print comment.body
        flag=False
        for i in comment.body.split(' '):
            
            if i=='Tyrion' or i=='tyrion':
                k=k+1
                flag=True
                #print k
        if flag==False:
            continue

        ss=sid.polarity_scores(comment.body)
        print ss["pos"],ss["neg"], k
        pos_total+=ss["pos"]
        neg_total+=ss["neg"]
        #print comment.body
        #commentSubmission = reddit.submission(url="https://www.reddit.com"+comment.permalink(fast=True))
        print "Episode :",count," Summary : "," Positive : ", pos_total, " Negative : ",neg_total, " No. of comments: ",k	

"""
		print("https://www.reddit.com"+comment.permalink(fast=True))
		print("replies for the comment")
		for repy in comment.replies:
			print(repy.body)
		#print(commentSubmission.comments[1])
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
			
	
#print c
	   
Arranges comments based on highest points and prints it to console
We need to see the documentation of the comment objects and store accordingly
Need to see about replies and all
"""
