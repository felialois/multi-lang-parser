# Multi-Language Parser

The project is divided in two simple parts. The api and the engine. The api handles requests, exceptions and flask functions while the engine is in charge of all the natural language operations.
The supported languages are english, spanish, portuguese and french. All the tokenizing is done using spacy. 

## Endpoints
* **Root URL**
`https://multi-lang-parser.herokuapp.com`

**Tokenize**
----
* **URL**

  `\tokenize`

* **Method:**
  
  `POST` 

* **Data Params**
   
   **Required:**
 
   `text=[string]`
   The text to be tokenized. 

   **Optional:**
 
   `lang=[string]`
   Available languages are english(`en`), portuguese (`pt`), french (`fr`) and spanish (`es`). If the parameter is missing 


* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** `{ tokens : [list] }`

  * **Code:** 200 <br />
    **Content:** `{ tokens : [list] , lang: [string]}`
 
* **Sample Call:**

  * **Curl**
  ```
    curl 
    --location 
    --request POST 'https://multi-lang-parser.herokuapp.com/tokenize' \
    --header 'Content-Type: application/json' \
    --data-raw '{"text": "This is text.", "lang": "en"}'
  ```
  


## Running

* **Using docker**

```
docker build -t multi_lang_parser:latest

docker run -d -p 5000:5000 multi_lang_parser
```

## Tests

The tests are done using pytest. In order to run them all in detail just run:
```
python -m pytest -vv
```