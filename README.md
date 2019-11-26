[![Build Status](https://travis-ci.com/cycnc35/AMZ-Cellphone-Review.svg?branch=master)](https://travis-ci.com/cycnc35/AMZ-Cellphone-Review)
# AMZ-Cellphone-Review

This project is about to analyze consumers' opinions about cellphones they bought on Amazon.
Also, we visualize results with visualization tool (i.g Plotly) to make results easy to realize.

## Data Source

[Amazon Cell Phone Reviews](https://www.kaggle.com/grikomsn/amazon-cell-phones-reviews)

## Libraries we need

1. Numpy
    - Numpy is a useful tool to handle vectors and matrix.
2. Pandas
    - Pandas is a library that can easily help us manipulate data.
3. Matplotlib
    - Matplotlib is a powerful visualization tool to help users understand the result easily.
4. Plotly
    - Plotly is a powerful plotting library that can help users design interactive graphs.
5. Dash
    - Dash is a Open Source Python library for creating reactive, Web-based applications.

To install these libraries you can simply type the command below in your terminal:
`pip install -r requirements.txt`

## Directory Structure
```
|-- AMZ-Cellphone-Review
|   |   | interface.py
|   |   | visualization_functions.py
|   |   | data
|   |   |   | items.csv
|   |   |   | reviews.csv
|   |   | test
|   |   |   | test_visualization_functions.py
|-- Docs
|   | Component_specification.md
|   | Functional_specification.md
|   | Homework\ 5_\ Project\ Design.docx
|   | technologies_reviews.pptx
|-- images
|   | images1.png
|   | images2.png
|-- LICENSE
|-- README.md
|-- requirements.txt
|-- setup.py
|-- .gitignore
```

## Tutorial
After cloning the repository using `git clone https://github.com/cycnc35/AMZ-Cellphone-Review.git`, 
you can simply run the interface.py file in your terminal. After running the file, there is an url
link showing in the result, copy the link and paste to the browser. Now, you can start using the dashboard.
In the dashboard, there are some dropdowns that you can choose which brand you are interested in.

If you are interested in ASUS, then choose ASUS.
![Tutorial](https://github.com/cycnc35/AMZ-Cellphone-Review/blob/master/images/image1.png)

If you are interested in Apple, then choose Apple.
![Tutorial](https://github.com/cycnc35/AMZ-Cellphone-Review/blob/master/images/image2.png)
