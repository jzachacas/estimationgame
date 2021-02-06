# A tiny Scrum Estimation tool
As a single page app implemented with [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Vue.js](https://vuejs.org).

## How to start

For development two debug servers are started (by `npm run serve`
and starting flask in debug mode). To make sessions work across 
domains (different ports equal different domains), a local
nginx docker container can be used. 

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
   

3. Start docker container with nginx 
  add text here...
   
4. Build for production
    ```sh
    cd client    
    npm run build
    ```
5. Run like in production:
```
docker build . -t flask_hello && docker run --name flask_container -p 80:80 flask_hello
```

## Notes

Working with websockets makes things tough. Did not manage to make 
them work with uwsgi. Gunicorn (the current solution) can use
only a single worker. Setting is done in [start.sh](start.sh)

- https://flask-socketio.readthedocs.io/en/latest/#gunicorn-web-server
- https://github.com/miguelgrinberg/Flask-SocketIO/issues/402