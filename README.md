# FastAPI Template

Create environment before install the requirements:
```
python3 -m venv env
.\env\Scripts\activate
```

Install requirements

```
pip install -r requirements.txt
```

Run uvicorn to start the server
```
uvicorn app.main:app --reload
```
Access http://127.0.0.1:8000/docs to get the swagger html
```
INFO:     Will watch for changes in these directories: ['D:\\Code\\FastAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [15152] using StatReload
INFO:     Started server process [6688]
INFO:     Waiting for application startup.
INFO:     Application startup complete. 
```