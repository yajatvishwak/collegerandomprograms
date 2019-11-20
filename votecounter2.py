# Vote Counter
# scans throug 40 lakh files and makes a unique list of all candidates and their votes
# used pandas, probably gonna explore more
# outputs on terminal and text file called output.txt 
# Prerequities: 
# keep the csv files in the same dir, the output file will be generated in the same.
# I fucking hate you for this eshan but i enjoyed gimme more ily<3 also, less than 50 lines ;)
# Written on : 20th Nov, 2019
import pandas as pd
import numpy ,json
def total_votes(d1,d2):
    total = 0
    for key, value in d1.items():
        total += value
    for key, value in d2.items():
        total += value
    return total
def appenddic(d1,d2):
    final = {}
    for key, value in d1.items():
        final[key] = value
    for key, value in d2.items():
        final[key] = value
    return final
def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]
def uniquecandidates(d):
    return list(d.keys())

data = list(pd.read_csv('election_data_1.csv')['Candidate'])
data2 = list(pd.read_csv('election_data_2.csv')['Candidate'])
#print('lib done.')
d1 = pd.Series(data).value_counts().to_dict()
d2 = pd.Series(data2).value_counts().to_dict()
#print(d1,d2)
print(total_votes(d1,d2)) # counts the total votes
final = appenddic(d1,d2)
print(uniquecandidates(final)) #List the unique candidates
print(final) # tally the votes of each candidate
print(keywithmaxval(final)) #Find the winner 
with open('output.txt', 'w') as f:
    f.write('Total Votes recored: '+ str(total_votes(d1,d2))+'\n')
    f.write('Unique Candidates: \n '+  str(uniquecandidates(final)))
    f.write('\n \n')
    f.write('Candidates with Votes: \n '+ json.dumps(final))
    f.write('\n \n')
    f.write('Winner:'+ str(keywithmaxval(final)))




    

