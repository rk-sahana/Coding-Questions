

from datetime import datetime
now=datetime.now()
#print(now.strftime("%d/%m/%y [%H:%M:%S]")) # to print the date and time in specified format
print("RECEPTIONIST IS SUPPOSSED TO TAKE ONLY FIRST 10 CANDIDATES")
dict={} #using a dictionary to store the details of Candidate
ppl=0 #As the number of people attending the interview in unknown,we will collect only the details of fisrt 10 Candidate

while(ppl<=10):
    name=input("Enter name and degree:") #takes name,degree from user
    time=now.strftime(" %d/%m/%y [%H:%M:%S]")# the current time is stored here
    dict[name]=time# the values are put in dictionary
    '''and simultaneously we also insert the data in a doc file'''
    filewrite=name+" - "+time #concatanate the input, to put  it into  the file
    filepath='C:/Users/Sahana R K/Desktop/sahana.doc'#path of file,where data is written
    with open(filepath,'a') as fhand: #opening the file in append mode to insert data
        fhand.write(filewrite) #writing contents into file
        fhand.write("\n")
    ppl=ppl+1
    
print("We have got the first 10 candidate details:\n")  
print("The Candidate details are :")    
print(dict)




