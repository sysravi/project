# Task 1 submission
Objective is to scrape following details from an Amazon page
1)  Product Title
2)  Product Image URL
3)  Price of Product
4)  Product Details

Steps involved:
1) Importing necessary libraries : 
    bs4 (BeautifulSoup) to extract data from webpage using soup object;
    csv to interact with provided csv file
    requests to obtain the webpage content using GET method

2) Defining necessary header
    Web scraping bots are often not provided all information (part of html code is hidden), to ensure the entire HTML content
    is available, defined a header composed of multiple user agents (comprising of popular browsers including Safari, Chrome, Firefox)
    This header allows us to obtain ALL html content and not just partial content

3) Defining containers to store data:
    4 dedicated lists each for product title, image urls, price and product details 

4) Functions to extract each required item
    product title is contained in span tag with a "prodtitle" attribute as ID
    product image url is present WITHIN the img tag, and has to be extracted using tag.attrs
    product price is again present in a span tag with "price" attribute as ID
    details are contained in a div tag with 'class':'a-section a-spacing-small a-padding-small' as the attribute

5) Openinng the csv file in read mode
    We need to generate URLs from the provided csv file, replacing the country suffix (de,fr,it) and the ASIN for the specific product
    From analysis, all URLs with ASIN less than 10 alphanumeric characters in length led to either 404 or 503 errors (page not found and server errors, respectively)
    The line object of the csv read is checked for ASIN length<10, if not it is used to generate a working url
    Same url is used to generate webpage content (using previously defined header), which is then used to make the soup object from which data is extracted

6) JSON dump
    From the 4 lists which have updated after the csv read-through operation, they are packed in a list-of-dictionary format, which is then written to a JSON file.
    
