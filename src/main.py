from fastapi import FastAPI


DEBUG = True

app = FastAPI(debug=DEBUG,
              title='Service to render users images',
              version='0.1.0')