import csv;

if __name__ == "__main__":
	
	up_or_down = {};
	with open('Combined_News_DJIA.csv', newline='\n') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',', quotechar='"');
		for row in csvreader:
			print("reading" + row[0]);
			if row[0].startswith("20"):
				date = row[0];
				direction = row[1];
				up_or_down[date] = direction;
			
	print(up_or_down);
	
	content = "";
	with open('sentiment_values_binary.csv', newline='\n') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',', quotechar='"');
		for row in csvreader:
			try:
				direction = "";
				print("writing" + row[0]);
				count = 0;
				if row[0].startswith("20"):
					date = row[0];
					direction = up_or_down[date];
					for data in row:
						content += data + ",";
						
					content += direction;
					
				else:
					count = 0;
					for data in row:
						content += data;
						if not count == len(row) - 1:
							content += ",";
					content += "price action";
					
				content += "\n";
			except:
				print("exception");
			
		
	with open("sentiment_priceaction_combined_binary.csv", "w+") as writer:
		writer.write(content);
	
