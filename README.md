# train_diagrams
train diagrams

# Run in Docker

docker run alpine -it -v c:\trolleway\train_diagrams\:/data /bin/sh


docker run --name train_diagrams -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done" 