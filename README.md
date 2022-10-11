# api_flask
  
  
  ### Docker Setup
  ``` 
  # Clone source code
   $ git clone https://github.com/sa2z/api_flask.git
  
  # Build docker image
   $ cd api_flask
   $ docker build -f Dockerfile.flask -t sa2z/flask:OCR . 
  
  # Run docker container
   $ docker run -d --name flask_ocr sa2z/flask:OCR
  ```