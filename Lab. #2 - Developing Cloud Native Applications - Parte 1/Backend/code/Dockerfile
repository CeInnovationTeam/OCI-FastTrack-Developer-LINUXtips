FROM python:3.8 as dependency
WORKDIR /reqs
COPY requirements.txt /reqs
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.8
WORKDIR /home/app
COPY backend.py .
COPY --from=dependency /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
CMD ["python","./backend.py"]
EXPOSE 5000