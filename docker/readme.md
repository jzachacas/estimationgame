# Nginx-Container for development

*Note:* This solution *can* serve as an alternative to the proxy server configured for the vue-cli-service serve command. It is currently undocumented and will probably go away soon.  

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