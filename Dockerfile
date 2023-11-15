FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1 
WORKDIR /app
COPY requirements.txt .
#RUN python -m venv venv 
#RUN /bin/bash -c "source venv/bin/activate"
RUN pip install -r requirements.txt
COPY . . 
EXPOSE 8000
CMD [ "uvicorn", "Main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]
