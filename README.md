## The model of the network for the sale of electronics.
The project is being rolled on Docker.
## Description of the technical task
* Develop a 3-level network model
* Develop for the admin panel
  - link to "Supplier"
  - filter by city name
  - "admin action" that clears the arrears
* For DRF
  - prohibit updating "arrears to the supplier" field
  - add the ability to filter objects by country
* Configure API access rights
## Prepare 
* prepare /app/.env file (examples in /app/.env_sample)
## Start service
* run command docker-compose up

Test data will be automatically added at the first launch
  - test users configuration load with app/users/management/commands/prepare_users.py
  - test data configuration load with app/users/management/commands/prepare_data.py
## Description of database
![img.png](img/img.png)
## Examples work with interface


## Work with API (trading-network)
* http://127.0.0.1:8000/api/v1/trading-network/ - show all trading-network
* http://127.0.0.1:8000/api/v1/trading-network/<int:pk>/ - show trading-network detail information
* http://127.0.0.1:8000/api/v1/trading-network/create/ - create trading-network
* http://127.0.0.1:8000/api/v1/trading-network/update/<int:pk>/ - update trading-network
* http://127.0.0.1:8000/api/v1/trading-network/delete/<int:pk>/ - delete trading-network
## Work with API (product) 
* http://127.0.0.1:8000/api/v1/product/ - show all products
* http://127.0.0.1:8000/api/v1/product/<int:pk>/ - show product detail information
* http://127.0.0.1:8000/api/v1/product/create/ - create product
* http://127.0.0.1:8000/api/v1/product/update/<int:pk>/ - update product
* http://127.0.0.1:8000/api/v1/product/delete/<int:pk>/ - delete product
## Work with API (unit) 
* http://127.0.0.1:8000/api/v1/unit/ - show all units
* http://127.0.0.1:8000/api/v1/unit/<int:pk>/ - show unit detail information
* http://127.0.0.1:8000/api/v1/unit/create/ - create unit
* http://127.0.0.1:8000/api/v1/unit/update/<int:pk>/ - update unit
* http://127.0.0.1:8000/api/v1/unit/delete/<int:pk>/ - delete unit
## Work with API (users)
* http://127.0.0.1:8000/api/v1/users/show/ - show all users
* http://127.0.0.1:8000/api/v1/users/show/<int:pk>/ - show user's detail information
* http://127.0.0.1:8000/api/v1/users/update/<int:pk>/ - update user information
* http://127.0.0.1:8000/api/v1/users/delete/<int:pk>/ - delete user information
* http://127.0.0.1:8000/api/v1/users/registration/ - register user
* http://127.0.0.1:8000/api/v1/users/token/ - get token for user
* http://127.0.0.1:8000/api/v1/users/token/refresh/ - refresh user token
* 



## Additional
* Author: Avramenko Nikolay
* Date of release: 2023/09/01