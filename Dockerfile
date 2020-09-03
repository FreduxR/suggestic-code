FROM python
ADD . /suggestic-code
WORKDIR /suggestic-code
ENV PYTHONPATH "${PYTHONPATH}:/suggestic-code"
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python","run.py"]