#!/usr/bin/env python3
words_upto_19 = ['','one','Two','Three','Four',
                'Five','six','Seven','Eight','Nine',
                'Ten','Eleven','Twelve','Thirteen',
                'Fourteen','Fifteen','Sixteen', 'Seventeen',
                'eighteen','Nineteen']
words_for_tens = ['','','Twenty','Thirty','forty','fifty',
                 'sixty','Seventy','Eighty','Ninety']
n = int(input("Enter a number: "))
output = ''
if n==0:
  output = 'Zero'
elif n<=19:
  output = words_upto_19[n]
elif n<=99:
  output = words_for_tens[n//10]+" "+words_upto_19[n%10]
else:
  output = "Please enter a value from 0 to 99 ONLY "
print(output)
