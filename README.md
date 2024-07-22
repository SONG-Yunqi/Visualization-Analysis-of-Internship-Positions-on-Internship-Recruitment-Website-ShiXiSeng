This project is to make a visualization analysis of internship positions on ShixiSeng, a website that specializes in providing internship recruitment services in China.

After entering the website and clicking into 'All positions around the country', you can find 500 pages of internship positions that are latest released. Click on one position, you will enter the detail page and get complete
information about that position.

We first write a python craweler to get the urls of detail pages of internship. The completed py file is 'craweler_for_internship_url.py'. It has craweled 9988 urls, which are saved in the csv file 'urls for internships.csv'. Then,
we write another python craweler to use the urls we have obtained to crawel detailed information of internships. The completed py file is 'craweler_for_each_internship_data.py'. The craweled data is saved in 
the csv file 'internship data.csv'.

For each internship, we get 13 features. They are listed below.
+ name: string, the name of the internship
+ company: string, the name of the company which provides the position
+ city: string, the city you work in
+ day: integer, range from 1 to 7, the number of days you have to work in a week
+ salary: string, the salary you earn for each day, for some internships this feature is displayed as '面议', which means you have to negotiate with the manager to determine your salary
+ academic: string, the minimum educational requirement for this position, can take value '大专', '本科', '硕士', '博士' and '不限', referring to 'Associate Degree', 'Bachelor Degree', 'Master Degree', 'Ph.D' and 'No Limit', respectively
+ duration: integer, the number of month this internship lasts
+ industry: string, the industry of this position
+ company_size: string, the scale of employees in this company
+ goodlist: string, advantages or well_beings of the position
+ info: str, detailed information about the position, including position responsibility, position requirements and so on

We then clean the data. The data cleaning process can be seen in the ipynb file 'data_cleaning.ipynb'. The cleaned data is saved in the csv file 'internship data(2).csv'.

Finally, we begin our visualization analysis. Details can be seen in the ipynb file 'data analysis.ipynb'.
