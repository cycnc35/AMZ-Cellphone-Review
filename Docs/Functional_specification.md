### Background
When a customer wants to buy a new cell phone, he or she may wonder 
which product has good reputation and popularity. Our primary goal
is to provide users with a platform where they can refer to. The platform
is a web page, which includes the following features:
1. Visualization of sales volume for cell phones of all brands
2. Comparisons of ratings for different brands.
3. Display of most helpful reviews for a selected type.

### User profile
People who are stuck in decision of which cell phone to purchase are
welcomed to our web page for more information. They aren't neccessarily
programmers, they only need to know how to browse the web. 
Users not familiar with python or bash should be able to view the product.

### Data source
Our data comes from [Kaggle open dataset](https://www.kaggle.com/grikomsn/amazon-cell-phones-reviews),
 which are collected from Amazon. It consists of two data sets:
 1. items.csv: contains item-level information, main attributes include
 product id(key), brand, title, rating, totalReviews.
 2. reviews.csv: gathers user-level reviews for cell phones they bought,
 main attributes include product id(key), rating, review content, 
 helpful votes.

### Use cases
1. Visualization of sales amount and ratings for all brands.
   + What information does user provide ?
     + Users can select a brand of cell phone through a dropdown box
   + What responses does the system provide ?
     + Stacked histogram of ratings for all brands
     + Pie chart of sales amount and rating for a specific brand

2. Retrieve helpful reviews from our data
   + What information does user provide ?
     + Users can select a brand through a dropdown box 
   + What responses does the system provide ?
     + Show all types of cell phones under the brand in a dropdown box
     
   + What information does user provide ?
     + After users select a brand, they can further select a specific type 
   + What responses does the system provide ?
     + Retrieve and display the review with highest votes under this type.
     

   
     