# Amazon_Vine_Analysis
## Overview
The Amazon Vine program is a service that allows manufacturers and publishers to receive reviews for their products. For this project we will analyze reviews from customers (unpaid) and the vine program (paid) and determine if the differences for the review of the Amazon's software. Ironically, we will use Amazon Web services’ Postgress database and bucket S3 services to extract, transform, load, and analyze the reviews.   
## Results
The was three (3) key findings when analyzing paid (vine program) and unpaid (customer reviews). 
1. There are significantly less paid reviews than unpaid reviews. This will play to our favor, since we will have a good "control" group of reviews. 

![Total_Reviews](https://github.com/rick2stack/Amazon_Vine_Analysis/blob/main/Resources/total_reviews.PNG)

2.  There is a higher percentage of 5-star reviews for the paid reviews than the unpaid reviews. The paid reviews and the unpaid reviews had percentages of 30% and 41%.respectively. 

![Percent_5Star_Reviews](https://github.com/rick2stack/Amazon_Vine_Analysis/blob/main/Resources/percent_reviews_5star.PNG)

3.  There is a higher percentage of bad reviews (2 stars and below) from unpaid reviews than paid reviews. The paid reviews and the unpaid reviews had percentages of 8% and 37%. 
![Percent_Bad_Reviews](https://github.com/rick2stack/Amazon_Vine_Analysis/blob/main/Resources/perct_bad_reviews.PNG)
## Summary
From the percentage of 5-star reviews, it appears that the vine program has bias in favor of higher reviews for amazon's software. There was a significantly smaller sample size of paid reviews (vine program) in comparison to the unpaid reviews, there was a difference in 10% for the 5-star reviews between the two groups. This was even noticeable in the percentage of bad reviews, with an almost 30% difference in the two groups. However, one question that needs to be address is who is more likely to leave a review from the unpaid group, unhappy customers, or unhappy customers. 