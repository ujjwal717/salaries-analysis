# salaries-analysis
This data analytics project named "salary analysis" basically analyses the salaries of different job titles such as "ML Engineer", "Data Scientist", "Data Engineer", "Data Analyst" and more according to various factors.

I have used data from kaggle.

I have used panndas to manipulate and analyse data and used plotly to visualize the data and python for programming.

Before discussing each and every analysis in details, first see the two additional visuals showing that outliers from the dataset has been removed.

A) **Data with Outliers**

![data with outliers](https://github.com/ujjwal717/salaries-analysis/assets/93403224/563c6b1a-9cca-45b9-84ad-6ac084150d49)



B) **Data without Outliers**

![data without outliers](https://github.com/ujjwal717/salaries-analysis/assets/93403224/ea816ef1-f4b1-4be7-9dd3-7e2fb117a15c)






Different analysis given below :- 


1) **Average Salary in different titles across different Experience level**


![average salary in ndifferent job titles across various experience level](https://github.com/ujjwal717/salaries-analysis/assets/93403224/9d91048e-07b9-46e0-b3b6-26fcad361339)


**Explanation** :- It uses multiple charts that are divided according to multiple experience level and each visual has different job 
  titles.So, basically there are 3 visuals for 3 different experience level - "Entry", "Mid" , "Senior" and all these experience level 
  contains different job titles in the X-axis and salary in the Y-axis


  **Insight 1 :-** I found that in general scenarios, entry level roles are paid least as compared to mid level or senior level.

  **Reason 1 :-** The reason for entry level getting less salary is the fact that when an employee joins as a entry level data analyst or any 
  other title for that matter, it takes time and requires supervision from his/her senior that may be mid level or senior level and in 
  beginning they are not given really crucial tasks due to which they are paid less initially. 


  **Insight 2 :-** "Machine Learning Engineer" earns more than other mentioned or considered titles such as "data analyst","data engineer" and 
  more in all the different experience levels.

  **Reason 2 :-** The ratio between job available and skilled machine learning engineer is not that great, so when there is high demand and 
  low supply of good machine learning engineer as compared to other job titles, "Machine Learning Engineer" tends to earn more than other job 
  titles.



2) **The average salary in different countries**


![average salary for different countries](https://github.com/ujjwal717/salaries-analysis/assets/93403224/d3626e20-b3fc-4fe3-8a1e-0fdf0c06208c)




  **Explanation :-** It again contains multiple visuals according to the experience level. After that, the legend has different country names 
  and the bars of the visuals are coded according to those legend colors so that it is easier for the viewer to understand which country is 
  bascially represented in the visual. Note that the Y-axis displays the sum of average salaries and each and every visual supports hover tool 
  so the visuals will show details about specific part on placing cursor on required part of visuals.


  **Insight :-** I have found that in maximum scenarios(combination of job titles and experience level), United States pays maximum to the 
  employees followed by Canada and United Kingdom. I have also noticed that France pays relatively lower than other countries.

  **Reason :-** The most glaring reason that might have lead to the conclusion that United States pays more than other countries is the fact 
  that it is very easy for citizens or companies to start a startup. The government is very open for such things and loans are often provided 
  without much hassle for startups. Now I am not saying that other countries are not open to startups as other countries are also paying 
  really well, but the ease that US has in that aspect seems a bit better. Also, these startup generally hires employees remotely which leads 
  to more pay as the company/startup doesn't need to setup offices and ultimately pay there employees a bit more.



3) **The Average Salary range from 2021-2023 in different Job Titles**


![average salary from 2021-2023](https://github.com/ujjwal717/salaries-analysis/assets/93403224/904747fa-ccab-4cef-bbd3-123d76c26896)




**Explanation :-** These visuals include a line chart and there are different visuals according to the Job title. Also, X-axis has the year from 2021-2023 and Y-axis has the average salary. 
  The line chart basically shows the trend of average salary of various job titles according to the years that are from 2021-2023.


  **Insight :-** We are considering various job titles such as "Data Engineer", "Data Scientist", "Machine Learning Engineer" and "Data Analyst". Each and every role sees growth in terms of 
  salary over the years. But we also see a little decrease in the machine learning(which is present because of data that will be explained in reason below). Other than that every job title 
  has grown and machine learning also increases substantially in the next year. Also, note that, I have not considered experience level as a criteria in this analysis because I wanted to do 
  this particular analysis over the fact that "how much that specific job title has increased or grown in those given years irrespective of the experience level as it is really obvious that 
  entry level has less salary than mid level and mid level has less salary than senior level roles normally.


  **Reason :-** The reason for little dip in the machine learning engineer might be from the fact that the year of dip(2022) might have more entry level roles in the dataset due to which the 
  average of that year as a whole depleted a bit in the machine learning engineer title which might not be the fact in the other job titles. Other than that, the increase or growth of these 
  roles is really great as with the growth of AI/ML, the data related roles such as data analyst, data engineering etc have also flourished as the creating ETL pipelines for the data and the 
  effective analysis for the data is also required and that requirement is increasing because AI/ML are more related to data and modelling in ML can only be done effectively if the data is 
  cleaned and usable which gave this boost to data related roles as well.




4) **The Average Salary for different Experience level according to Company Size**


![average salary according to company size](https://github.com/ujjwal717/salaries-analysis/assets/93403224/af7eb804-789c-4a13-b45b-11b5f2ee6e22)





  **Explanation :-** This analysis includes different visuals according to different experience level and includes bubble chart representing the average salary. The size of bubbles are 
  according to the amount of average salary and is directy proportional that is higher the average salary, bigger the bubble. Also, legends are supported and legends are according to the 
  company size.

  **Insight 1 :-** I found that medium sized companies often pay more than small size and large size company in almost all the roles.

  **Reason 1 :-** The possible reason for that is the fact that, a medium sized company has more scope of growth which means the growth potential and possibility of growth is higher as 
  compared to large sized companies(they are already big and they may also have growth potential but it won't be as much as a medium sized company). The medium sized companies might be 
  paying more than small sized companies because they generally have more clients for which they might need more employees and are ready to pay good salaries as they have growth scope and 
  they want to expand. Medium sized give more average salaries than large sized companies because the large sized companies often include a lot of employees in specific job titles and are 
  often able to meet the clients requirements. Also, due to the large amount of employees, the salary ceiling is generally set to a fixed level which might not be the case with medium sized 
  or small sized companies. 



  **Insight 2 :-** I found that in entry level roles, the small sized companied often pay more than the large sized companies.


  **Reason 2 :-** The reason for that might be the fact that the small sized companies often work in a really fast and paced environment and are not reluctant to hire somoeone who might not 
  have industry experience but is skilled and can help in variety of tasks to help the company grow. On the other hand, the large sized companies often look for experienced candidates who 
  can deliver efficiently to high profile, regular clients so that the acquisition of clients improves. Also, the opening for entry level roles is generally less in large sized companies.


  **Insight 3 :-** I found that in senior level roles, the large sized companies often pay significantly more than small sized companies.


  **Reason 3 :-** This analyis and insight is related with the "insight 2" as I discussed in **Reason 2** that the large size companies want more experienced candidates which is verified by 
  this insight of analysis. The large sized companies pay significantly more than small sized companies for senior level roles as large sized companies require experience candidates to 
  handle important and big projects and also for the management of various project which is not a strict requirement in small sized companies.


  **Insight 4 :-** The large sized companies are paying more than small sized companies for most of the mid experience level roles.


  **Reason 4 :-** The reason for that would be the fact that large sized companies has a lot of projects which are not very important but need some experience from the candidates for 
  effective completion of those projects, so what happens is that, these mid level employees are managed by the senior level employees and they provide guidance foe smooth and effective 
  execution of those projects and as senior level employees are working on more important projects, they provide guidance to mid level employees. So, for this needs large sized companies pay 
  more than small sized companies as this kind of working or mechanism is not that extensively used in small sized companies generally. 




5) **The Average Salary for different Experience level according to Employee residence**


![average salary according to employee residence](https://github.com/ujjwal717/salaries-analysis/assets/93403224/fcef8c90-b497-45af-882d-bcb579f8c1c0)





**Explanation :-** This analysis also contains different visuals according to the experience level and contains job titles on the y-axis and "sum of average salary" on the x-axis. It also 
  includes the legend which is "Employee Residence".

  **Insight :-** I found that the employees from US earns more in most of the cases. Also, the salaries of canada's employees and UK's employee is really close but for most situations, it is little more in canada's employees but the different is not that much. Employees from Germany also have satisfying amount of average salary.

  **Reason :-** The cost of living in high in US which explains why their employees earn more than other countries. 


  




  

  


  







   





  
