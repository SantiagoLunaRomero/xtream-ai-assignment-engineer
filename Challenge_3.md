# Diamond Evaluation API Documentation

## Overview
This API allows users to get price evaluations for diamonds based on their features. It uses a previously trained Random Forest model to predict the price of a diamond given its carat weight, cut, color, clarity, and physical dimensions.

## Usage

### Endpoint
`POST /predict`

This endpoint accepts diamond data in JSON format and returns a price prediction.

### Input Data Format
Input data should be sent as a JSON object with the following keys:

- `carat`: The weight of the diamond in carats (float).
- `depth`: The total depth percentage (float).
- `table`: The width of the top table compared to the widest point of the diamond (float).
- `x`: Length in mm (float).
- `y`: Width in mm (float).
- `z`: Depth in mm (float).
- Categorical variables (cut, color, clarity) should be provided as one-hot encoded variables. For example, for `cut` you should provide: `cut_Good`, `cut_Ideal`, `cut_Premium`, `cut_Very Good`, each with a value of 0 or 1.

### Request Example
To make a prediction, send a POST request to `/predict` with a JSON body like the following:

```json
{
  "carat": 0.8,
  "depth": 62.3,
  "table": 57,
  "x": 5.8,
  "y": 5.85,
  "z": 3.62,
  "cut_Good": 0,
  "cut_Ideal": 1,
  "cut_Premium": 0,
  "cut_Very Good": 0,
  "color_D": 0,
  "color_E": 1,
  "color_F": 0,
  "color_G": 0,
  "color_H": 0,
  "color_I": 0,
  "color_J": 0,
  "clarity_I1": 0,
  "clarity_IF": 0,
  "clarity_SI1": 1,
  "clarity_SI2": 0,
  "clarity_VS1": 0,
  "clarity_VS2": 0,
  "clarity_VVS1": 0,
  "clarity_VVS2": 0
}