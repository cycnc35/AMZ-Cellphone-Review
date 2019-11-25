### Software components
1. Data cleaning and merging: contains functions to merge items.csv and
reviews.csv based on product id.
   + ``Inputs``: Two dataframes of raw data
   + ``Outputs``: A merged and clean dataframe containing both item-level
   and user-level information.

2. Visualization manager: extract and gather sales amount, ratings, review,
etc. from the merged dataframe.
   + ``Inputs``: A clean and merged dataframe, and a specific query.
   + ``Outputs``: Visualization of the query (e.g. histogram, pie chart)

3. Web manager: build an web interface which manipulates HTML DOM object,
enable users to interact with our system.
   + ``Inputs``: Get the values from the drop down box
   + ``Outputs``: Plots from visualization manager

### Interactions to accomplish use cases
Users can select a certain value from drop down boxes, and the value would 
be sent to the visualization manager as a query. After the visualization 
manager finishes processing data and generating plot. The plot would be
sent back to web manager, and is updated on the web.

### Preliminary plan
   + Data inspection, preprocessing, and merging
   + Build interface, and visualization manager.

