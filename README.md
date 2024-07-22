This project is to make a visualization analysis of internship positions on ShixiSeng, a website that specializes in providing internship recruitment services in China.

After entering the website and clicking into 'All positions around the country', you can find 500 pages of internship positions that are latest released. Click on one position, you will enter the detail page and get complete
information about that position.

We first write a python craweler to get the urls of detail pages of internship. The completed py file is 'craweler_for_internship_url.py'. It has craweled 9988 urls, which are saved in the csv file 'urls for internships.csv'. Then,
we write another python craweler to use the urls we have obtained to crawel detailed information of internships. The completed py file is 'craweler_for_each_internship_data.py'. The craweled data is saved in 
the csv file 'internship data.csv'.
