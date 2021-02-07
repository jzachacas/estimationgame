# A tiny Scrum Estimation tool
As a single page app implemented with [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Vue.js](https://vuejs.org).

## How to start

1. Run the Flask backend in folder [server](./server/):

    ```sh    
    cd server
    python3.7 -m venv venv
    source venv/bin/activate
    python app.py
    pip install -r requirements.txt    
    ```
   
    Test availability:  
    ```
   curl http://localhost:5000/
    ```
   > "server up and running"
   
2. Run the Vue.js client in folder [client](./client/):

    ```sh
    cd client
    npm install
    npm run serve
    ```
 
   Test availability:
    ```
   curl http://localhost:8080/
    ```
   
   > HTML output...
   
