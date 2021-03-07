# How to develop the dogu

```
vagrant up
ssh ces-admin@<ip>

```

Copy `dist`folder to machine.

`ces-admin@ces:~$ sudo cesapp build estimo`

> ...
> 
> Successfully tagged local/estimo:1.0.0-0

`ces-admin@ces:~$ sudo cesapp healthy build`

Take care that lines

`ENV SERVICE_TAGS webapp`
`EXPOSE 8080` 

are present in [Dockerfile](./Dockerfile). Otherwise, the container will run
but the application will not be made available by nginx. 

