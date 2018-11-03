from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer;
import os;
import csv;
import time;
import Remove_unwanted;

class SIA(object):
	
	def __init__(self, lexicon_path):
		self.analyser = SentimentIntensityAnalyzer(lexicon_path);
		
	
	def get_sentiment_scores(self, sentence):
		snt = self.analyser.polarity_scores(sentence);
		#print("{:-<40} {}".format(sentence, str(snt)));
		return snt;
		
	

if __name__ == "__main__":
	
	#'''
	start_time = int(round(time.time() * 1000));
	sia_list = []
	
	emotions = os.listdir("lexicons")
	for emotion in emotions:
		sia = SIA("lexicons/" + emotion);
		sia_list.append(sia);
		
	
	output = "";
	with open('RedditNews.csv', newline='\n') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',', quotechar='"');
		for data in csvreader:
			if data[0].startswith("20"):
				date = data[0];
				title = data[1];
				title = Remove_unwanted.clean_text(title);
				if title.startswith("b "):
					title = title[2 : len(title)];
				print(int(round(time.time() * 1000)) - start_time, date, title);
				output += date + "," + title + ",";
				count = 0;
				for sia in sia_list:
					scores = sia.get_sentiment_scores(title);
					output += str(scores["neg"]) + ",";
					output += str(scores["neu"]) + ",";
					output += str(scores["pos"]) + ",";
					output += str(scores["compound"]);
					if not count == len(sia_list) - 1:
						output += ",";
						
					count += 1;
					
				output += "\n";
				
			
		
	
	count = 0;
	header = "Date,Title,"
	for emotion in emotions:
		em = emotion.replace(".txt", "")
		header += "neg " + em + ",";
		header += "neu " + em + ",";
		header += "pos " + em + ",";
		header += "compound " + em;
		if not count == len(emotions) - 1:
			header += ",";
			
		count += 1;
		
	
	with open("sentiment_values.csv", "w+") as writer:
		writer.write(header + "\n" + output[0 : len(output) - 1]);
		
	#'''


