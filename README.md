Python One-Liners.
```
Python can run one-liners from an operating system command line using option -c:

python -c "print(3.0/2)"
Calculates and outputs the result.

python -c "import math;print(math.sin(1))"
Imports a module required and outputs sine value.

python -c "for i in range(1,11):print(i)"
Uses a loop to output numbers from 1 to 10.

python -c "for i in range(1,11):for j in range(1,11): print(i,j)"
Does not work; two loops in a line are an invalid syntax.

python -c "for i, j in ((i,j) for i in range (1,11) for j in range(1,11)): print(i, j)"
Outputs pairs using two analogues of loop within a comprehension.

echo hey | python -c "import sys,re;[sys.stdout.write(line) for line in sys.stdin if re.search('he.', line)]"
Acts as grep: outputs each line of the input containing a substring matching a regular expression. Not a Python one-liner strength.

echo hallo | python -c "import sys,re;[sys.stdout.write(re.sub('h[au]llo', 'hello', line)) for line in sys.stdin]"
Acts as sed: for each line of the input, performs a regex replacement and outputs the results. Again, not a Python one-liner strength.

python -m calendar
Outputs a year's calendar using calendar module.

python -c "import playsound as p;p.playsound(r'C:\WINDOWS\Media\notify.wav')"
On Windows, plays notification sound. Requires installation of playsound module. The module works across platforms; what is Windows specific above is the file path.
```
