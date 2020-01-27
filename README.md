# Run
```
cd etest
mkvirtualenv -p $(which python3.6) etest
pip install -r requirements.txt
python main.py
```

# Test
```
cd src
pytest tests.py
```