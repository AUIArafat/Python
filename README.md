# Regular Expression
## Character Classes
### Shorthand code for character classes
| Shorthand Codes for Common Character Classes | Represents |
| :---: | :---: |
| \d | Any numeric digit from 0 to 9. | 
| \D | Any character that is not a numeric digit from 0 to 9. | 
| \w | Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.) | 
| \W | Any character that is not a letter, numeric digit, or the underscore character. | 
| \s | Any space, tab, or newline character. (Think of this as matching “space” characters.) | 
| \S | Any character that is not a space, tab, or newline. | 
| ^ | At the start of a regex to indicate that a match must occur at the beginning of the searched text | 
| $ | At the end of the regex to indicate the string must end with this regex pattern. |
| ^somthing$ | ^ and $ together to indicate that the entire string must match the regex |
| ? | matches zero or one of the preceding group. |
| * | matches zero or more of the preceding group. |
| + | matches one or more of the preceding group. |
| {n} | matches exactly n of the preceding group. |
| {n,} | matches n or more of the preceding group. |
| {,m} | matches 0 to m of the preceding group. |
| {n,m} | matches at least n and at most m of the preceding group. |
| {n,m}? or *? or +? | performs a non-greedy match of the preceding group. |
| . | matches any character, except newline characters. |
| [abc] | matches any character between the brackets (such as a, b, or c). |
| [^abc] | matches any character that isn’t between the brackets. |
