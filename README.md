## Steps to run and test
* Create .env with new relic token.
* Run: `docker compose build`
* Run: `docker compose run -d`
* Check through: 
``` 
curl -s http://localhost:5001/cart | jq  
AND
curl -s http://localhost:5002/pay | jq
AND
curl -s http://localhost:5003/checkout | jq
```