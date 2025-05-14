# API Endpoints

## Currency Conversion

### GET /convert

Convert an amount from one currency to another.

#### Request Parameters

| Parameter     | Type   | Required | Description                      |
| ------------- | ------ | -------- | -------------------------------- |
| from_currency | string | Yes      | Source currency code (e.g., USD) |
| to_currency   | string | Yes      | Target currency code (e.g., EUR) |
| amount        | number | Yes      | Amount to convert                |

#### Response

**Success Response (200)**

```json
{
  "converted_amount": {
    "converted_amount": 85.5,
    "cached": false
  }
}
```

**Error Response (400)**

```json
{
  "detail": "Invalid currency code"
}
```
