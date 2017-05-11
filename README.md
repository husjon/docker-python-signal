# docker-python-signal

A quick example showing how to send and handle signals in a python script within a docker container.

```bash
# Clone the repo
git clone https://github.com/husjon/docker-python-signal.git && cd docker-python-signal

# Build and run the image
docker build -t docker-python-signal . && docker run --name=dps docker-python-signal

# From another terminal
docker stop dps

# Docker will now send a SIGTERM to the container then wait for the defaulted 10 seconds before sending a SIGKILL.
# Since we're catching the SIGTERM, we're able to stop the python script gracefully.
```
