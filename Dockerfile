FROM python:3.8-slim-buster

# ENV PORT=8501

# Copy the app
COPY src/ /app
COPY requirements.txt /app

WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE $PORT

CMD streamlit run app.py --server.port $PORT