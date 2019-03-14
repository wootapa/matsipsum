FROM python:2.7-alpine
COPY matsipsum.py /
ENTRYPOINT [ "python", "./matsipsum.py" ]
CMD []
