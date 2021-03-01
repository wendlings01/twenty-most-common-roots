# Instructions:

Create a program in the language of your choice which reads in a text file, removes stop words (see explanation below), removes all non-alphabetical text, stems words into their root form (see explanation below), computes the frequency of each term, and prints out the 20 most commonly occurring terms (not including stop words) in descending order of frequency. 

Your solution should seek to achieve the following in order of priority:

- **Correctness**: The solution fulfills the above requirements and all logic is verified through unit testing.
- **Maintainability**: The code is easy to understand and maintain.
- **Performance**: The solution completes the task quickly.

SOME parts of the solution include: 
- **Data Source**: Input files are provided. Your program must be able to run both of them without breaking. The test files are the Declaration of Independence (text1.txt) and the text of Alice in Wonderland (text2.txt)
- **Stop word removal**. The list of “stop words” is contained in “stopwords.txt”.   

- **Stemming algorithm**. You will need to apply a standard stemming algorithm in order to stem all words to a morphological root (for example: jumping, jumps, jumped -> jump). You should use Porter Stemmer algorithm. Support for most languages can be found here: https://tartarus.org/martin/PorterStemmer/

Please return an email with a link to a GitHub repo containing your code. Make sure to include in the readme how to run your program.  Also, please provide a brief explanation of what your program does, any assumptions that you needed to make, and the output from your program (although, we will be running it again to ensure we get the same results).

