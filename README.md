# Web-Crawler-Analysis
For each attribute X in S,we consider only Table A and discuss the following in the report: 
Basically we use jupyter notebook to analyze the data. We use package such as Panda and Matplotlib.

Missing values: report the percentage of missing values for X. For example, if there are 20 tuples in Table A but X has value in only 5 of them, then the percentage of missing values for X in Table A is 75%. (Report both the fraction and the percentage.)

We often have to fill in these missing values somehow for machine learning in subsequent steps. We Discussed solutions we may use to fill in these missing values.

Classify the attribute X as numeric, textual, categorical, or boolean. 

If the attribute X is textual, report the average length of its values, report the minimal and the maximal length of its values (length is measured in the number of characters in the value). 

Find and report possible outliers and anomalies among the attribute values. For example, if attribute price typically has values in the range $1-20, and then there is a value of $200, then this value is an outlier, and it can also be an anomaly (that is, an incorrect value in this case). You can detect outliers by creating a histogram on some property of the attribute values. For example, a histogram on price values will help detect price outliers. As another example, if an attribute is textual, then a histogram on the length of the values (as measured by the number of characters in the value) can help detect values that are very long or very short. 

If the attribute value is supposed to follow a certain format (e.g., dates), we discuss if all values follow the same format, or if there is some problem with the format and we will have to standardize the formats later. 

Sometimes attribute values are "sprinkled" all over the item. For example, a book may have an attribute "publisher", but its value is missing. Instead, the book title contains the publisher (e.g., "Principles of Data Integration by Springer"). 
