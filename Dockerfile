FROM python:3.6


RUN adduser worker
COPY . /home/worker
USER worker
WORKDIR /home/worker

COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PATH="/home/worker/.local/bin:${PATH}"

#COPY --chown=worker:worker . .

LABEL maintainer="Cat Azam <darkness@example.com>" \
      version="1.0.0"
ENTRYPOINT ["python"]
CMD ["app.py"]