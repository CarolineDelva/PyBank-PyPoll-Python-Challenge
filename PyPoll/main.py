print ("Election Results")
print ("--------------------------------------------")

#modules
import os 
import csv
import collections 


# Set path for files
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

Total_votes = 0

#1 

sumkhan = 0 
d=[]
with open (csvpath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    result = {}
    for line in reader:
        candidate = line[2]
        Total_votes += 1
        if candidate in result:
            result[candidate]['vote_count'] += 1
        else:
            result[candidate] = {'vote_count': 1}
    winner = list(result.keys())[0]
    output = []
    for candidate in result:
        result[candidate]['percentage_vote'] = (result[candidate]['vote_count']/ Total_votes) * 100
        result[candidate]['candidate'] = candidate
        if result[winner]['vote_count'] < result[candidate]['vote_count']:
            winner = candidate
        output.append(result[candidate])    
            #winner =
with open('output.txt', 'w') as output_file:
    print('Total Votes: ', Total_votes)
    output_file.write('Total Votes: {} \n'.format(Total_votes))
    print('-------------------------')
    output_file.write('------------------------- \n')
    for candidate in sorted(output, key= lambda x: x['vote_count'], reverse=True):     
        print('{}: {}% ({})'.format(candidate['candidate'], round(candidate['percentage_vote'], 3), candidate['vote_count']))
        output_file.write('{}: {}% ({}) \n'.format(candidate['candidate'], round(candidate['percentage_vote'], 3), candidate['vote_count']))
    print('-------------------------')
    output_file.write('------------------------- \n')
    print('Winner: ',winner)
    output_file.write('Winner: {}'.format(winner))
    

  
    

    
    
    
    
    
    
            
           


      
  
  
      
      
      


# 
