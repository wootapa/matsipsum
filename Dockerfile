FROM python:3.9.0-alpine
COPY matsipsum.py /
ENTRYPOINT [ "python", "./matsipsum.py" ]
CMD ["5"]
