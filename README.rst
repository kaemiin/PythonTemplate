# Python Template

## Use Docker

```
docker run -it -v $(pwd):/usr/src/app --name pythontest  python:3.6.5-jessie bash

docker start pythontest

docker exec -it pythontest bash

cd /usr/src/app
```

## Build

```
make
```
