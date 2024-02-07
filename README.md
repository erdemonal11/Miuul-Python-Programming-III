# This repository is published as Case Study III, with sample answers written by me for the Miuul Python Programming for Data Science course.

Case Study questions are given below:

# List Comprehension

# Task 1: 
Answer the following questions:

Q1: Read the miuul_gezinomi.xlsx file and show general information about the data set.
<br/>
Q2: How many unique cities are there? What are the frequencies?
<br/>
Q3: How many unique concepts are there?
<br/>
Q4: How many sales were realised from which Concept?
<br/>
Q5: What is the total amount earned from sales by city?
<br/>
Q6: How much is earned according to concept types?
<br/>
Q7: What are the PRICE averages by city?
<br/>
Q8: What are the PRICE averages according to concepts?
<br/>
Q9: What are the PRICE averages in City-Concept breakdown?

# Task 2: 
Change the variable SaleCheckInDayDiff to a categorical variable.

The variable SaleCheckInDayDiff indicates how long before the CheckIn date the customer has completed the purchase.
- Create the ranges in a convincing way.
For example: '0_7', '7_30', '30_90', '90_max'.
- You can use the names "Last Minuters", "Potential Planners", "Planners", "Early Bookers" for these ranges.

# Task 3: 
What are the average earnings by COUNTRY, SOURCE, SEX, AGE?
In terms of average fee paid and number of transactions in City-Concept-EB Score, City-Concept- Season, City-Concept-CInDay breakdown analyse ?

Expected output:
<br/>
![image](https://github.com/erdemonal11/Miuul-Python-Programming-III/assets/137915983/6f063852-3ec4-464f-8e8d-d49cce75946f)

# Task 4: 
Sort the output of the City-Concept-Season breakdown by PRICE.
Save the output as agg.

Expected output:
<br/>
![image](https://github.com/erdemonal11/Miuul-Python-Programming-III/assets/137915983/75629b5a-5bc3-4084-885c-0dcdb681fc57)

# Task 5: 
Convert the names in the index to variable names.
All variables in the output of the third question except PRICE are index names. Convert these names to variable names

# Task 6:
Define new level based customers (persona).
- Define new level based sales and add them as a variable to the dataset.
- Name of the new variable to be added: sales_level_based
- You need to create the variable sales_level_based by combining the observations in the output you will obtain in the previous question.

  The observations in this table will come together   Expected output
  <br/>
  ![image](https://github.com/erdemonal11/Miuul-Python-Programming-III/assets/137915983/1cad5b21-63be-45c1-89e5-3ed43729c9d4)

# Task 7:
Segment new customers (personas).
- Divide new personas into 4 segments according to PRICE.
- Add the segments to agg_df as a variable with SEGMENT naming.
- Describe the segments (group by segments and get price mean, max, sum).

# Task 8:
Categorise new customers and estimate how much revenue they can bring in.
- How much income is a person who wants to have an all-inclusive holiday in Antalya in high season expected to bring in on average?
- In which segment will a holidaymaker who goes to a half board hotel in Kyrenia in low season be placed?








