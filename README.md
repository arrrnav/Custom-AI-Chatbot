# Chatbot-WebApp
 OpenAI driven chatbot that responds to investment-related queries using a custom knowledge base derived from inputted PDF documents.

## How to Use:
 If you are using text files for a knowledge base, skip to step 3

 After step 1, you will need an active OpenAI key to proceed with running the required programs. In steps 2 and 3, you will be prompted to enter the key, and your input will be hidden from view for privacy.
 
### 1. Activate a virtual environment
 Creaate a virtual environment (this may be easier if you isntall virtualenv from pip) and activate it.
 
 Activate the virtual environment and install the dependencies from the ```requirements.txt``` file:

  ```pip install -r requirements.txt```
### 2. Convert PDFs to txt Files
 Create a directory in your project folder to store text files. In this directory, create separate ```.txt``` files for each PDF you want to convert. A more streamlines approach to conveting several PDFs at once is a pending task.

 Open ```indexing.py``` and run the following code snippet for each PDF and corresponding text file that you want to write to:
 ```
outstream = open(INSERT PATH TO TXT FILE TO WRITE TO HERE, "w", encoding='utf-8')
outstream.write(generate_text_file(INSERT PATH TO PDF TO CONVERT HERE))
outstream.close()
```
 It is currently commented in the repository. Simply uncomment it, replace the paths, and run ```python indexing.py``` in the terminal, and input the API key as prompted. Comment it back when finished with PDF conversion.

### 3. Index the text files
 You should have all the text files you want to act as a knowledge base sitting in one single directory within your project folder. 

 Open ```indexing.py``` and run the following code snippet for the folder containing all your text files:
 ```
 construct_index(INSERT PATH TO FOLDER CONTAINING TXT FILES TO INDEX HERE)
 ```
 It is currently commented in the repository. Simply uncomment it, replace the path, and run ```python indexing.py``` in the terminal, and input the API key as prompted. Comment it back when finished with index creation.
 
### 4. Running the Actual Web Application
 Proceed to ```app.py``` and update ```os.environ["OPENAI_API_KEY"] = "INSERT OPENAI KEY HERE"``` with your active OpenAI API key (it should remain in a string).
 
 Run ```python app.py``` and wait for the app to finish running. The web application will be live on localhost server with the URL shown in your terminal. Navigate to this URL and you should be able to interact your custom AI chatbot.

## Enjoy!
