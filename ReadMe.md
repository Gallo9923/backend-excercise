# Backend Exercise
Nextail is thinking about expanding its business and not only forecast sales in the stores but also manage the cash register. The first store where we will introduce our software will sell the following 3 products.

| **Code** | **Name**       | **Price** |
|----------|----------------|-----------|
| VOUCHER  | Gift Card      | 5.00 EUR  |
| TSHIRT   | Summer T-Shirt | 20.00 EUR  |
| PANTS    | Summer Pants   | 7.50 EUR  |

The different departments have agreed the following discounts:
- A 2-for-1 special on VOUCHER items.
- If you buy 3 or more TSHIRT items, the price per unit should be 19 00€.
- Items can be scanned in any order, and the cashier should return the  total amount to be paid.

The interface for the checkout process has the following specifications:
- The Checkout constructor receives a pricing_rules object
- The Checkout object has a scan method that receives one item at a time

**Examples:**
- Items: VOUCHER, TSHIRT, PANTS - Total: 32.50€  
- Items: VOUCHER, TSHIRT, VOUCHER - Total: 25.00€
- Items: TSHIRT, TSHIRT, TSHIRT, VOUCHER, TSHIRT - Total: 81.00€
- Items: VOUCHER, TSHIRT, VOUCHER, VOUCHER, PANTS, TSHIRT, TSHIRT - Total: 74.50€


## Solution


### Class Diagram

![Class diagram](./docs/Class%20Diagram/Class%20Diagram.png)
<<<<<<< HEAD
<<<<<<< Updated upstream
[See the actual diagram file.](./docs/Class%20Diagram/Class%20Diagram.pdf)
=======
=======
>>>>>>> master
[See the actual diagram file.](./docs/Class%20Diagram/Class%20Diagram.pdf)

### Test it!

1. Install Poetry dependency management [Link](https://python-poetry.org/docs/)

2. Install dependencies
```
poetry install
```
3. Run python app.

```
poetry run python src/store/main.py
```


4. Run the following examples in a command line.

#### Example 1: 

Items: VOUCHER, TSHIRT, PANTS - Total: 32.50€ 


```
curl -X 'POST' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
  {
    "code": "VOUCHER",
    "name": "Gift Card",
    "price": 5.0
  },
  {
    "code": "TSHIRT",
    "name": "Summer T-Shirt",
    "price": 20.0
  },
  {
    "code": "PANTS",
    "name": "Summer Pants",
    "price": 7.5
  }
]'
```

#### Example 2: 

- Items: VOUCHER, TSHIRT, VOUCHER - Total: 25.00€

```
curl -X 'POST' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
  {
    "code": "VOUCHER",
    "name": "Gift Card",
    "price": 5.0
  },
  {
    "code": "TSHIRT",
    "name": "Summer T-Shirt",
    "price": 20.0
  },
  {
    "code": "VOUCHER",
    "name": "Gift Card",
    "price": 5.0
  }
]'
```

#### Example 3: 

- Items: TSHIRT, TSHIRT, TSHIRT, VOUCHER, TSHIRT - Total: 81.00€

```
curl -X 'POST' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
  {
    "code": "TSHIRT",
    "name": "Summer T-Shirt",
    "price": 20.0
  },
  {
    "code": "TSHIRT",
    "name": "Summer T-Shirt",
    "price": 20.0
  },
  {
    "code": "TSHIRT",
    "name": "Summer T-Shirt",
    "price": 20.0
  },
  {
    "code": "VOUCHER",
    "name": "Gift Card",
    "price": 5.0
  },
  {
    "code": "TSHIRT",
    "name": "Summer T-Shirt",
    "price": 20.0
  }
]'
```

#### Example 4: 


- Items: VOUCHER, TSHIRT, VOUCHER, VOUCHER, PANTS, TSHIRT, TSHIRT - Total: 74.50€

```
curl -X 'POST' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
   {
    "code": "VOUCHER",
    "name": "Gift Card",
    "price": 5.0
  },
  {
    "code": "TSHIRT",
    "name": "Summer T-Shirt",
    "price": 20.0
  },
  {
    "code": "VOUCHER",
    "name": "Gift Card",
    "price": 5.0
  },
  {
    "code": "VOUCHER",
    "name": "Gift Card",
    "price": 5.0
  },
  {
    "code": "PANTS",
    "name": "Summer Pants",
    "price": 7.5
  },
  {
    "code": "TSHIRT",
    "name": "Summer T-Shirt",
    "price": 20.0
  },
  {
    "code": "TSHIRT",
    "name": "Summer T-Shirt",
    "price": 20.0
  }
]'
<<<<<<< HEAD
```

### Run tests

```
poetry run python .\tests\store\checkout\test_suite.py
```
>>>>>>> Stashed changes
=======
```
>>>>>>> master
