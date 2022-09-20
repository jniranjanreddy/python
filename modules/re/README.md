## regular Expression.
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
|'|'| Either or	"falls|stays" |
|() |	Capture and group |

