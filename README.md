# Notebook
This is a simple notebook with an integrated dictionary feature that offers effortless word lookup functionality. Additionally, it allows you to swiftly get word definitions by taking a screenshot of the word.

Python version: 3.11.6

# How to use the notebook:
1) This is a simple notebook in which you can save the contents on a text file by simply clicking on the 'Save' button and storing the data in a text file on your chosen       file directory.
2) You can load the contents of other text files using the 'Load' button.
3) You can create and use multiple windows at the same time by clicking on the 'New Window' button.

# How to use the dictionary:
In order to use the dictionary feature properly, follow the following steps:
1) Initialize Pytesseract by following the following tutorials:
   i)For Windows: https://www.youtube.com/watch?v=DG5D8A3zi4o&t=2s&pp=ygUbaW5zdGFsbCBweXRlc3NlcmFjdCB3aW5kb3dz
2) Open up the file labelled 'dictionary.py' and replace "Your Account" with your account's username in line 22.
   <img width="831" alt="image" src="https://github.com/Rahbir1518/Notebook/assets/149626522/ee58b8cb-6988-4dea-b571-42fddfa428aa">

4) Create a folder in your "C" drive and label it 'SS'. This will be the primary folder where you can store screenshots.
   **NOTE:** Once you click on the "Convert image to string?" button, the program will automatically delete the screenshot from the folder to ensure that the screenshots do                 not accumulate and clog up space.
   
6) If you wish to change the folder location, open up the file 'screenshot_organizer.py' and manually change the 'file_path' in line 4.
  **NOTE:** If you changed the file path, you would need to open up the file called 'dictionary.py' and modify the codes in line 70 and 71 with your new file directory.

