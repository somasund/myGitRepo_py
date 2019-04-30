FROM python:3
COPY DeepDive_Module1.py /usr/src/myapp/
WORKDIR /usr/src/myapp/
CMD ["python", "./DeepDive_Module1.py"]
