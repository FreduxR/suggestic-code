# Suggestic Code
Convert nested list to plain list, the project is based on [Flask](https://flask.palletsprojects.com/en/1.1.x/) framework.


## Usage
You can use postman to import Suggestic Code.postman_collection and try it


## Execution
Use the docker file, move to project directory
```
docker build --no-cache -t suggestic-code:v1 .
docker run -p 5000:5000  --name=SuggestCode  suggestic-code:v1
```