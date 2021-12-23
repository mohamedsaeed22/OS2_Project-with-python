
def freq_words(str):

	str = str.split()		
	str2 = []
	for i in str:			
		if i not in str2:
		    str2.append(i)       
	for i in range(0, len(str2)):
            print('Frequence of Word', str2[i], 'is :', str.count(str2[i]))

def freq_letters(str):
    str2 = []
    for i in str:		
        if i not in str2:	
            str2.append(i)
    for i in range(0, len(str2)):
        if str2[i] != " ":
         print('Frequency of letter', str2[i], 'is :', str.count(str2[i]))

def main():
    str =input("Please Enter The Words : ")
    freq_words(str)
    freq_letters(str) 
    
if __name__=="__main__":
    	main()			 # call main function




