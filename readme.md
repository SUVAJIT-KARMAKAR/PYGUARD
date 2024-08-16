
# PyGuard
#### PyGuard is a simple yet effective application designed to generate secure random passwords tailored to user specifications. It offers flexibility in password complexity by allowing users to include numbers and special characters.

![LOGO](Resources/LOGO/PyGuard-LOGO.png)

## FEATURES

- **CUSTOMIZABLE PASSWORD GENERATION** : Users can set the minimum password length and choose to include digits and special characters.

- **SIMPLE STREAMLIT INTERFACE** : The application provides a user-friendly interface built with Streamlit, allowing easy configuration and password generation.

- **DATABASE INTEGRATION** : PyGuard seamlessly integrates with MongoDB to store generated passwords securely, associating each password with the application or website for which it was generated.




## USAGE 
- *INPUT CONFIGURATION* : Users can set the minimum password length and choose to include digits and special characters.

- *PASSWORD GENERATION* : Upon clicking the "GET YOUR PASSWORD" button, PyGuard generates a random password based on the configured settings.

- *DATABASE STORAGE* : Generated passwords are stored in a MongoDB database (`pyguard.credentials`), ensuring secure access and retrieval.


## GETTING STARTED 

Git clone the project or fork it 
```bash
    cd PyGuard
```
Install the required packages
```bash
    pip install requirements.txt
```
Configure MongoDB locally or remotely and update the connection string (`mongodb://localhost:27017/`) accordingly in the code.

Create .env file and make necesary changes to it 
```bash
    MONGODB_URI=mongodb: --your-connection-url
    MONGODB_DB_NAME= --your-database-name--
    MONGODB_COLLECTION_NAME= --your-collection-name--
```

```bash
    # DATABASE CONNECTION
    mongo_uri = os.getenv("MONGODB_URI")
    db_name = os.getenv("MONGODB_DB_NAME")
    collection_name = os.getenv("MONGODB_COLLECTION_NAME")

    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
```
To run the project 
```bash
    streamlit run pyGuard.py
```


## BADGE 

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



## AUTHOR

[SUVAJIT-KARMAKAR](https://github.com/SUVAJIT-KARMAKAR)

