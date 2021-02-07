# A tiny Scrum Estimation tool
As a single page app implemented with [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Vue.js](https://vuejs.org).

## How to start

For development two debug servers are started (by `npm run serve`
and starting flask in debug mode). To make sessions work across 
domains (different ports equal different domains), a local
nginx docker container can be used. 

1. Run the Flask backend in folder [backend](./backend):

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
   > "backend server up and running"
   
2. Run the Vue.js client in folder [client](./client):

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
   
4. Build for production
    ```sh
    cd client    
    npm run build
    ``` 

## Run like in production:
```
docker build . -t estimationgame && docker run --name estimationgame -p 80:80 estimationgame
```

### Log files
  Stdout and log from python gets into `/var/log/gunicorn/error.log`.
  Note that output before execution of `socketio.run` seems to get swallowed.
  Access log is visible in `/var/log/gunicorn/access.log` and on stdout. 


3. *Obsolete:* Proxying is done by vue-cli now (but this may be helpful for debugging).
   
   [nginx.conf](docker/nginx.conf) needs your local IP in line `proxy_pass http://192.168.178.29:8080`
   Then start the development docker container with nginx as reverse proxy
     ```
     cd docker
     docker-compose up
     ```

   Test availability:
      ```
      xdg-open http://localhost:8000/
      ```
   Calls should now be forwarded to the running backend and client servers.

## Notes

Working with websockets makes things tough. Did not manage to make 
them work with uwsgi. Gunicorn (the current solution) can use
only a single worker. Setting is done in [start.sh](start.sh)

- https://flask-socketio.readthedocs.io/en/latest/#gunicorn-web-server
- https://github.com/miguelgrinberg/Flask-SocketIO/issues/402