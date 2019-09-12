# Docker Demo
## Build demo image
```docker build -t demo```

## Check new image is created
```docker image ls```

## Run that image.
```docker run -d -p 8000:80 demo``` or
```docker run --name demo -e NAME=AVIRIANS -d -p 8000:80 demo```

## Docker run options 
`-p` map your laptop’s port 8000 to the container’s exposed port 80 (defined in app.py)

`-d` detached mode

Open “http://[IP address]:8000/” in your browser.
