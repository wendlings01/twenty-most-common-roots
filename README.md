# Setting up and running
## Initial setup
If you don't already have python, then you'll need to get it. I found that there were problems with the Windows app store's install blocking the path to the accessible executable. Also it didn't play well with Git Bash, which is a shame.

Optionally you can set up the python virtual environment using the following on Windows:
```powershell
python -m venv env
.\env\Scripts\activate.ps1
```
Or the following in Unix:
```bash
python -m venv env
source env/Scripts/activate
```

Whether you use the virtual environment or not, you'll want to download the dependencies:
```powershell
pip install requirements.txt
```

If those steps all worked then you're ready to run the code. If something failed before this point you likely have some problem with your python install. 

## Running the program
The main python script takes 2 inputs. The stopwords file and the target text file. Both have been left in the root directory for ease of access.

Running the program on the declaration of independence gives me this:
```powershell
(env) PS C:\Users\wendl\twenty-most-common-roots> python .\main.py .\stopwords.txt .\Text1.txt
['us', 'peopl', 'right', 'govern', 'law', 'state', 'power', 'time', 'among', 'declar', 'establish', 'refus', 'form', 'abolish', 'new', 'coloni', 'assent', 'larg', 'legislatur', 'legisl']
```

Running it on Alice in Wonderland gives me this:
```powershell
(env) PS C:\Users\wendl\twenty-most-common-roots> python .\main.py .\stopwords.txt .\Text2.txt
['said', 'alic', 'littl', 'look', 'one', 'like', 'know', 'went', 'thought', 'thing', 'time', 'go', 'queen', 'say', 'get', 'see', 'think', 'king', 'turtl', 'head']
```

The test suite can be ran with a straightforward
```powershell
(env) PS C:\Users\wendl\twenty-most-common-roots> python .\test.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK
```

# General Overview
My program takes the two input files and parses them in nearly identical ways. It starts with the stop words, pulls out whitespace delineated words from every line, strips off all remaining non-alphabetical characters, and `tolower`s that result. Then it stems each stop word. I was debating not stemming these, but it simplified the process in my mind and I didn't seem to lose meaningful performance. These stemmed stop words are stored in a dictionary with the stem as the key and their count as the value.

Then the text we care about parsing gets dealt with the same way, except that the stemmed words only get counted if they're not equal to a stemmed stop word. Since this is the same function as for stems, we now have a dictionary of stem:count.

The last step before printing is to order the dictionary and slice off the top 20. Ordering is a one-liner with list comprehensions, the `sorted` function, and a lambda to tell `sorted` to order based off of the value and not whatever the default is for tuples. The choosing the top 20 is just slicing off the first 20 items in the list.

There wasn't a request for a specific output format so I left it printing the bare list object, which is decently readable for me at this size.

# Assumptions
- We don't need to worry about non-english languages. I started looking at making a test for this, but the data wasn't straight-forward to read and so was deprioritized. And any special non-english syntax wouldn't be thought of
- Function input will be of the correct type, within reason. No one else is calling these functions for now.
- Users will use main.py as intended. There's a note within its main function addressing how command line input could be improved for later iterations.

# General Notes
- My commits got pretty sloppy once I really got into the main function. It's hard to justify cleaning them up on this young of a repo too.
- I tried to keep comments limited to describing blocks at a high level, noting where I break convention or intentionally cut corners, or further describing tests.
