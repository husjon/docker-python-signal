FROM ubuntu

RUN apt update && apt install -y python

COPY ./test.py ./test.py
# RUN chmod +x ./test.py

ENTRYPOINT ["python", "./test.py"]
