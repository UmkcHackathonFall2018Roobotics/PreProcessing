
class Word:
	def __init__(self, _emotion):
		self.word = _emotion;
		self.emotions = [];
	
	def set_word(self, _word):
		self.word = _word;
	
	def add_emotion(self, _emotion, _bit):
		self.emotions.append((_emotion, _bit));
	
	def clear_emotions(self):
		self.emotions = [];
	

if __name__ == "__main__":
	list = [];
	contents = "";
	
	with open('dictionary.txt') as reader:
		contents = reader.read();
	
	word = Word("");
	for line in contents.split("\n"):
		text = "";
		emotion = "";
		bit = "";
		for data in line.split("\t"):
			if text == "":
				text = data;
			elif emotion == "":
				emotion = data;
			elif bit == "":
				bit = data;
		#print(text, emotion, bit);
		if not text == word.word:
			list.append(word);
			word = Word(text);
			#word.set_word(text);
			word.clear_emotions();
		word.add_emotion(emotion, bit);
	
	dictionary = {};
	for word in list:
		print("loading " + word.word);
		for emotion in word.emotions:
			wordlist = [];
			if emotion[0] in dictionary.keys():
				wordlist = dictionary.get(emotion[0]);
			else:
				dictionary[emotion[0]] = [];
				wordlist = dictionary.get(emotion[0]);
			#print(wordlist);
			if not wordlist == None:
				wordlist.append([word.word, emotion[1]]);
				dictionary.update({emotion: wordlist});
	print(dictionary);
	for emotion in dictionary.keys():
		print(str(emotion));
		print("exporting . . .");# + emotion);
		contents = "";
		for word in dictionary[emotion]:
			token = str(word[0]);
			average = str(word[1]) if not word[1] == '' else "0";
			sd = "0";
			rating_list = [int(average) for i in range(10)];
			contents += token + "\t" + average + "\t" + sd + "\t" + str(rating_list) + "\n";
		
		with open("lexicons/" + str(emotion) + ".txt", "w+") as writer:
			writer.write(contents);
	

