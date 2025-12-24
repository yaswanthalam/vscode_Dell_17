Here are 30 “one step advanced” questions (a bit harder than the previous set). You still write the code to produce the expected outputs.

## Strings and formatting

1.  
Question: Ask the user for their first name and favorite color, then print:  
`<name>'s favorite color is <color>.`  
Example input: `Alice`, `blue`  
Expected output:  
`Alice's favorite color is blue.`

2.  
Question: Ask the user for a sentence and print how many words it has (words are separated by spaces).  
Example input: `I like learning Python`  
Expected output:  
`4`

3.  
Question: Ask the user for an email address and print everything before the `@` symbol.  
Example input: `user123@gmail.com`  
Expected output:  
`user123`

4.  
Question: Given `text = "hello world"`, print the same string but with each word capitalized.  
Expected output:  
`Hello World`

5.  
Question: Ask the user for a sentence and print the number of vowels (`a, e, i, o, u`, both cases).  
Example input: `Hello Python`  
Expected output:  
`3`

6.  
Question: Ask the user for a string and print it reversed, but without using slicing (`[::-1]`).  
Example input: `abcde`  
Expected output:  
`edcba`

7.  
Question: Ask the user for a sentence and a word, and print `Found` if the word is in the sentence, otherwise `Not found`.  
Example input: sentence: `Python is great`, word: `Python`  
Expected output:  
`Found`

## Lists and list operations

8.  
Question: Ask the user for 5 integers (space separated) and store them in a list, then print the list sorted in ascending order.  
Example input: `5 2 9 1 3`  
Expected output:  
`[1, 2, 3, 5, 9]`

9.  
Question: Ask the user for 5 integers (space separated) and print the average of these numbers.  
Example input: `2 4 6 8 10`  
Expected output:  
`6.0`

10.  
Question: Given `nums = [1, 2, 3, 2, 4, 2, 5]`, remove all occurrences of `2` and print the new list.  
Expected output:  
`[1, 3, 4, 5]`

11.  
Question: Ask the user for a list of numbers (space separated) and print only the unique numbers in the same order they first appeared.  
Example input: `1 2 2 3 1 4`  
Expected output:  
`[1, 2, 3, 4]`

12.  
Question: Given `words = ["apple", "banana", "cherry", "date"]`, print the longest word.  
Expected output:  
`banana`

13.  
Question: Ask the user for two lists of integers (space separated) and print a list containing elements that appear in both (intersection, no duplicates).  
Example input:  
First: `1 2 3 4`  
Second: `3 4 5 6`  
Expected output:  
`[3, 4]`

14.  
Question: Ask the user for a list of integers and print a new list where each element is squared.  
Example input: `1 2 3`  
Expected output:  
`[1, 4, 9]`

## Dictionaries

15.  
Question: Create a dictionary for a student: `{"name": "Alex", "age": 20, "grade": "A"}` and print the value of `"grade"`.  
Expected output:  
`A`

16.  
Question: Ask the user for 3 pairs of `word meaning` (e.g. `apple fruit`) and store them in a dictionary, then print the dictionary.  
Example input:  
`apple fruit`  
`table furniture`  
`python language`  
Expected output:  
`{'apple': 'fruit', 'table': 'furniture', 'python': 'language'}` (order may vary)

17.  
Question: Given `scores = {"Alice": 80, "Bob": 65, "Charlie": 90}`, print the name of the student with the highest score.  
Expected output:  
`Charlie`

18.  
Question: Ask the user for a sentence and build a dictionary counting how many times each word appears, then print the dictionary.  
Example input: `one two two three three three`  
Expected output:  
`{'one': 1, 'two': 2, 'three': 3}` (order may vary)

19.  
Question: Ask the user for 5 names and their ages, store in a dictionary, then print only the names of people who are 18 or older.  
Example data example:  
`Tom 17`, `Anna 20`, `John 18`, `Eva 15`, `Mia 30`  
Expected output:  
`Anna`  
`John`  
`Mia`

## Functions

20.  
Question: Write a function `is_even(n)` that returns `True` if `n` is even, otherwise `False`. Call it with `n = 7` and print the result.  
Expected output:  
`False`

21.  
Question: Write a function `greet(name)` that returns the string `Hello, <name>!`. Call it with `name = "Sam"` and print the result.  
Expected output:  
`Hello, Sam!`

22.  
Question: Write a function `max_of_three(a, b, c)` that returns the largest of three numbers. Call it with `3, 10, 5` and print the result.  
Expected output:  
`10`

23.  
Question: Write a function `factorial(n)` that returns the factorial of `n` using a loop. Call it with `n = 4` and print the result.  
Expected output:  
`24`

24.  
Question: Write a function `count_vowels(s)` that returns how many vowels are in the string `s`. Call it with `"Programming"` and print the result.  
Expected output:  
`3`

25.  
Question: Write a function `reverse_list(lst)` that returns a new list with the elements of `lst` reversed (do not use `lst.reverse()` or slicing). Call it with `[1, 2, 3]` and print the result.  
Expected output:  
`[3, 2, 1]`

## Loops, logic, and small algorithms

26.  
Question: Ask the user for an integer `n` and print all numbers from `1` to `n` that are divisible by 3 but not by 5.  
Example input: `20`  
Expected output:  
`3 6 9 12 18`

27.  
Question: Implement the classic FizzBuzz for numbers from 1 to 20:  
- Print `Fizz` for multiples of 3.  
- Print `Buzz` for multiples of 5.  
- Print `FizzBuzz` for multiples of both.  
- Otherwise print the number.  
Expected output begins:  
`1`  
`2`  
`Fizz`  
`4`  
`Buzz`  
... up to `20`.

28.  
Question: Ask the user for a list of integers and print the second largest number.  
Example input: `1 5 3 9 7`  
Expected output:  
`7`

29.  
Question: Ask the user for a number `n` and check if it is a prime number. Print `Prime` or `Not prime`.  
Example input: `11`  
Expected output:  
`Prime`

30.  
Question: Ask the user for a string and check if it is a pangram (contains every letter from `a` to `z` at least once, ignore case and spaces). Print `Pangram` or `Not pangram`.  
Example input: `The quick brown fox jumps over a lazy dog`  
Expected output:  
`Pangram`

These questions step into dictionaries, functions, and slightly more complex logic, similar to intermediate practice exercises used on popular learning sites.[1][2][3]

[1](https://www.w3resource.com/python-exercises/)
[2](https://pynative.com/python-exercises-with-solutions/)
[3](https://www.w3schools.com/python/python_exercises.asp)
[4](https://holypython.com/intermediate-python-exercises/)
[5](https://www.geeksforgeeks.org/python/python-exercises-practice-questions-and-solutions/)
[6](https://www.youtube.com/watch?v=bE6mSBNp4YU)
[7](https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md)
[8](https://pynative.com/python-basic-exercise-for-beginners/)
[9](https://pynative.com/python-dictionary-exercise-with-solutions/)
[10](https://olibr.com/blog/top-python-intermediate-interview-questions-answers-in-2024/)
[11](https://www.101computing.net/python-challenges-intermediate-level/)
[12](https://www.dataquest.io/blog/data-structures-in-python/)
[13](https://www.geeksforgeeks.org/python/intermediate-coding-problems-in-python/)
[14](https://www.reddit.com/r/learnpython/comments/zb92nc/good_python_exercises/)
[15](https://realpython.com/iterate-through-dictionary-python/)
[16](https://www.ccbp.in/blog/articles/python-coding-questions)
[17](https://github.com/zhiwehu/Python-programming-exercises/blob/master/100+%20Python%20challenging%20programming%20exercises%20for%20Python%203.md)
[18](https://www.geeksforgeeks.org/python/python-list-exercise/)
[19](https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners)
[20](https://python-fiddle.com/challenges/levels/intermediate)