# flask-web-app
##  precondition
``` 
   install redis
```
```
  flask-web-app It's a helm bag
  In templates, flask-web-app/config.yaml changes the redis connection 
  helm install appname ./flask-web-app -n namespace
  information
```
## local run
```
  pip install -r requirements.txt
  python app.py
  curl http://localhost:5000
```
## docker run
```
  cp config-example.yaml config.yaml
  docker build -t flask-web-app .
  docker run -d -v `pwd`:/app/config.yaml -p 5000:5000 flask-web-app 
  curl http://localhost:5000

```