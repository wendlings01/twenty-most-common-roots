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

Then you'll want to download the dependencies:
```powershell
pip install requirements.txt
```

If those steps all worked then you're ready to run the code. If something failed before this point you likely have some problem with your python install. 
