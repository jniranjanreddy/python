## Regular Expression.
```
Regular Expression is a set of characters that helps one identify Strings of a specific pattern.
```
```
This module exports the following functions:
        match     Match a regular expression pattern to the beginning of a string.
        fullmatch Match a regular expression pattern to all of a string.
        search    Search a string for the presence of a pattern.
        sub       Substitute occurrences of a pattern found in a string.
        subn      Same as sub, but also return the number of substitutions made.
        split     Split a string by the occurrences of a pattern.
        findall   Find all occurrences of a pattern in a string.
        finditer  Return an iterator yielding a Match object for each match.
        compile   Compile a pattern into a Pattern object.
        purge     Clear the regular expression cache.
        escape    Backslash all non-alphanumerics in a string.

```

| Special character               | Usage                          |
| ------------------------------- | --------------------------------------------- |
| [] | A set of characters	"[a-m]" |
| \ | Signals a special sequence (can also be used to escape special characters) "\d" |
| . | Any character (except newline character)	"he..o" |
| ^ | Starts with	"^hello" |
| *| Zero or more occurrences	"he.*o" |
| $| Ends with	"planet$" |
| + | 	One or more occurrences	"he.+o" |
| ? | 	Zero or one occurrences	"he.?o" |
|{}| Exactly the specified number of occurrences	"he.{2}o" |
| pipe | Either or	"falls|stays" |
|() |	Capture and group |


# Special Sequence
| Special Sequence               | Usage                          |
| ------------------------------- | --------------------------------------------- |
| \A |	Returns a match if the specified characters are at the beginning of the string	"\AThe"	 |
| \b |	Returns a match where the specified characters are at the beginning or at the end of a word  (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"  r"ain\b"	|
| \B | Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word  (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain" r"ain\B"	|
| \d  | Returns a match where the string contains digits (numbers from 0-9)	"\d"	|
| \D  | Returns a match where the string DOES NOT contain digits	"\D"	|
| \s  | Returns a match where the string contains a white space character	"\s"	|
| \S  | Returns a match where the string DOES NOT contain a white space character	"\S" |
| \w  | Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) "\w" |	
| \W  | Returns a match where the string DOES NOT contain any word characters	"\W"	|
| \Z  | Returns a match if the specified characters are at the end of the string |

```
{2} # exactly 2 matches
{2,4} # 2,3, or 4 times
```