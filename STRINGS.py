# python-6
STRINGS

1.Different ways creating a string?


Strings can be created by enclosing characters inside a single quote or double-quotes. Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

# defining strings in Python
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


2.Concatentating two strings using + operator

* The + operator can be used to concatenate two different strings.

example:
str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str=str1+str2
print("Concatenated two different strings:",str)


3.Finding the length of the string

# Python code to demonstrate string length 
# using len
  
str = "geeks"
print(len(str))


# using for loop  
# Returns length of string
def findLen(str):
    counter = 0    
    for i in str:
        counter += 1
    return counter
  
  
str = "geeks"
print(findLen(str))


# using while loop.  
# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter
  
str = "geeks"
print(findLen(str))



4.Extract a string using Substring

* Python offers many ways to substring a string. It is often called ‘slicing’.
syntax:
string[start: end: step]

Example:
string = "freeCodeCamp"
print(string[0:5])



5.Searching in strings using indexOf()
* In python there are 5 Ways to Find the Index of a Substring in Strings
str.find()
str.rfind()
str.index()
str.rindex()
re.search()


6.Mathching a string Against a Regular Expression with matches()
* The “re” module of python has numerous method, and to test whether a particular regular expression matches a specific string, you can use re.search(). The re.MatchObject provides additional information like which part of the string the match was found.

Syntax:
matchObject = re.search(pattern, input_string, flags=0)


7.Comparing strings using the methods equals()
 * Equals is the relational operators compare the Unicode values of the characters of the strings from the zeroth index till the end of the string. It then returns a boolean value according to the operator used.
 “Aravind” == “Aravind” will return True as the Unicode of all the characters are equal
print('Aravind'='Aravind')



8.equalsIgnaoreCase(),startsWith(),endsWith() and compare To()

* Python library provides a number of built in methods, one such being startswith() and endswith() function which used in string related operations.

startswith()

Syntax

str.startswith(search_string, start, end)

endswith()

Syntax :

str.endswith( search_string, start, end)



9.Trimming strings with trim()

* Python provides three methods that can be used to trim whitespaces from the string object.

Python Trim String
strip(): returns a new string after removing any leading and trailing whitespaces including tabs (\t).
rstrip(): returns a new string with trailing whitespace removed. It’s easier to remember as removing white spaces from “right” side of the string.
lstrip(): returns a new string with leading whitespace removed, or removing whitespaces from the “left” side of the string.
All of these methods don’t accept any arguments to remove whitespaces. If a character argument is provided, then they will remove that characters from the string from leading and trailing places.


s1 = '  abc  '

print(f'String =\'{s1}\'')

print(f'After Removing Leading Whitespaces String =\'{s1.lstrip()}\'')

print(f'After Removing Trailing Whitespaces String =\'{s1.rstrip()}\'')

print(f'After Trimming Whitespaces String =\'{s1.strip()}\'')




10.Replacing characters in strings with replace()

* Replacing each occurrence of a character in a string creates a new string where each occurrence is replaced with another character. For example, replacing "a" with "b" in "aba" results in "bbb".

USE str.replace() TO REPLACE CHARACTERS IN A STRING
* Use str.replace(old, new) to replace all occurrences of a character old with the desired character new. This will replace multiple occurrences of the character anywhere in the string.

Example:

a_string = "aba"
a_string = a_string.replace("a", "b")
Replace in a_string

print(a_string)



11.Splitting strings with split()

* split() method in Python split a string into a list of strings after breaking the given string by the specified separator.

Syntax : str.split(separator, maxsplit)




12.Converting Numbers to Strings with ValueOf()

* To convert an integer to string in Python, use the str() function. This function takes any data type and converts it into a string, including integers. Use the syntax print(str(INT)) to return the int as a str, or string.



13.Converting integer objects to strings

* To convert an integer to string in Python, use the str() function. This function takes any data type and converts it into a string, including integers. Use the syntax print(str(INT)) to return the int as a str, or string.



14.Converting to uppercase and lowercase

* The functions upper() and lower() returns the string by converting all the characters of the string to upper case or lower case respectively

Syntax :

string.lower()

Parameters:
lower() does not take any parameters

Returns :
It converts the given string in into lowercase and returns the strings.


Syntax :

string.upper()

Parameters:
upper() does not take any parameters

Returns :
It converts the given string in into uppercase and returns the string.
