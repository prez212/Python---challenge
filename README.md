**Python---challenge** 

Within this folder there are two folders Pybank and Pypoll

For **Pybank** 
This challenge was a Financial Analysis using Python to analyze a csv file for a UofT Bootcamp
Please note: This challenge was tackled as a cohort between Muneeb Samad, Rob Molenda, Sultan Raheem and I.
In this file there are two folders 'Resources' and 'Analysis'.
In Analysis folder there is the txt file which is generated from the script 'mainPyPankLP.py'
In the Resource there csv that must be on you PC to use the script 'mainPyBankLP.py" file to run

To Run "mainPyBankLP.py':
Clone entire "Python---challenge" to PC and when using VSCode ensure directory is 'Python---Challenge'
Change Directory into 'Pybank'
csv file needs to be 'Resources\budget_data.csv'

Understanding the script:
Used this to understand #import csv, #file path in read mode and #open data csv
https://stackoverflow.com/questions/60190232/how-to-access-csv-file-using-os-module

This also helped with #open data csv
https://stackoverflow.com/questions/16823695/how-to-use-delimiter-for-csv-in-python

Muneeb Samad achieved these with the for loop in #Calculations:

 for row in csv_reader:
       
        dates.append(row [0])
        value = int(row[1])
        totalprofit += value
        if lastmonthprofit is not None:
            change = value - lastmonthprofit
            totalchanges = change
            newvalue += 1

As well as https://discuss.python.org/t/difference-between-and-operator-in-python/12899/4 to better understand this set.

Rob Molenda achieved these:

grtsincrease = ['',0]
grtsdecrease = ['',9999999999]

And the #Calculations regarding:

 if change > grtsincrease [1]:
                grtsincrease = (row[0], change)
            if change < grtsdecrease [1]:
                grtsdecrease = (row[0], change)
        lastmonthprofit = value
totalmonths = len(dates)
if newvalue >0:
    averagechanges = totalchanges/newvalue
else:
    averagechanges = 0'


#Print total months and #Print in textile were a collaboration of the below links:
https://www.geeksforgeeks.org/reading-writing-text-files-python/
https://note.nkmk.me/en/python-csv-reader-writer/#read-csv-files-csvreader

For **PyPoll**
This challenege is the Analysis of the Accumulation of Electoral Ballots of an Election  using Python the Analyze the results for a UofTBootcamp.
In this file there is a folder called 'Resources'. In resources there cvs that must be in your PC. 
To Run: 
Change Directory into 'PyPoll'
csv file needs to be 'Rvesources\election_data.csv'

Similar logic was used to import csv #open data csv, #retrieve nominee name from row, #add the candidate ballot counts with what I learned from the "Pybank" assignment.
However I was unavailable to run it successfully. 


