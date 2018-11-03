import csv;

if __name__ == "__main__":
	
	content = "";
	with open('sentiment_values.csv', newline='\n') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',', quotechar='"');
		for row in csvreader:
			print(row[0]);
			count = 0;
			if row[0].startswith("20"):
				date = row[0];
				title = row[1];
				count += 2;
				content += date + "," + title + ",";
				for i in range(2, len(row)):
					if str(row[i]) == "0.0":
						content += "0";
					else:
						content += "1";
						
					if not count == len(row) - 1:
						content += ",";
						
					
					count += 1;
					
				
			else:
				for heading in row:
					content += heading;
					if not count == len(row) - 1:
						content += ",";
					count += 1;
				
			content += "\n";
			
		
	
	with open("sentiment_values_binary.csv", "w+") as writer:
		writer.write(content);
		
	

