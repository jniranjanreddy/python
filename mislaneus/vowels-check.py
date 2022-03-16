#!/usr/bin/env python3

def switch(alphabet):
    dict={
        'a': 'Vowel',
        'e': 'Vowel',
        'i': 'Vowel',
        'o': 'Vowel',
        'u': 'Vowel',
        'A': 'Vowel',
        'E': 'Vowel',
        'I': 'Vowel',
        'O': 'Vowel',
        'U': 'Vowel',
    }
    return dict.get(alphabet, 'Consonant')

alphabet= input('Enter an alphabet to check: ')
print('The entered alphabet is: ', switch(alphabet))