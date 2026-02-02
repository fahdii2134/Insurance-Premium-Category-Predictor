# Base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy only requirements first (for better caching)
COPY . /app

# Install only necessary packages
RUN pip install --no-cache-dir -r requirement.txt

# Expose Streamlit default port
EXPOSE 8501

# Command to run Streamlit app
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run frontend.py --server.address=0.0.0.0 --server.port=8501"]

