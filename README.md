# Suicide-Attempts-in-ShanDong
The work in this repo is part of the semester project in the course: Mathematical Foundations of Data Science
# Introduction
The annual global suicide mortality rate is about 14-15 per 100,000, which results in the loss of 1 million lives globally each year, equivalent to one death by suicide every 40 seconds. Suicide is one of the top ten causes of death in Western countries. Early studies have shown that the suicide death rate in China is 22-30 per 100,000 people. Although China's suicide rate is lower than that of Western countries, due to its large population base, China accounts for 30-40% of global suicides. The suicide rate in rural areas of China is 3-5 times higher than that in urban areas, making rural areas the most serious suicide problem in China. Suicide has become one of the major public health problems in China, bringing a heavy burden of disease and socio-economic burden to the state and society. In order to propose targeted preventive interventions, it is necessary to accurately measure and characterize the suicidal perceptions and attitudes of the population. As a large agricultural province, Shandong Province has a high percentage of rural areas nationwide, and the suicide rate in Shandong Province is among the highest in all provinces and cities. Studying its suicide situation can significantly study the situation of farmers' suicides and serve as a microcosm to study the suicide problem of Chinese people.
# File description
A sample of 2571 individuals was surveyed for hospitalised,died,urban,year,month,sex,age,education,occupation,method.
https://github.com/wyl0923/Suicide-Attempts-in-ShanDong/assets/172492456/19cec7af-41ea-471f-b76c-0c8213185d1f
# Tech used:
・ statistical hypothesis testing  

・ modeling (logistic regress)  

・ data visualization  
# Installation/Run the py script
First make sure python is installed.

Using pandas，seaborn，sklearn.preprocessing in matplotlib.pyplot，LabelEncoder，warnings，pyodbc,stats in scipy, metrics in sklearn,linear_model in sklearn,preprocessing in sklearn,train_test_split in sklearn.model_selection ,RandomForestClassifier in sklearn.ensemble.  

Starting SQL Server services can be done in several different ways.
SQL Server is a powerful relational database management system that provides a variety of data services and solutions, including data analysis, reporting, integration, and collaboration. Before using SQL Server, it is important to ensure that its services are started so that you can establish a connection to the database and perform various operations. Several ways to start SQL Server services are detailed below:
Using Command Prompt (CMD): open CMD and run it as administrator, enter the command net start mssqlserver, and after pressing the Enter key, the system will start the SQL Server service. This method is suitable for starting the service quickly, especially when the server cannot be accessed through the graphical interface.
Use Configuration Manager: Search for and open "SQL Server Configuration Manager" from the Start menu, find "SQL Server Services", and then right-click the service you want to start and select "Start". Start". This method allows you to manage multiple services and view the status and properties of each service.
Using Service Manager: Search for "Services" in the Start menu, locate the service called "SQL Server (MSSQLSERVER)", right-click and select "Start Start". This method allows you to manage the SQL Server service directly from the Windows service list.
Using PowerShell: If you are familiar with PowerShell scripting, you can also write a script to start the SQL Server service. However, note that for named instances, you may need to switch to CMD mode to execute the appropriate commands.
When choosing a startup method, you need to consider your specific needs and operating environment. For example, if you are a developer or database administrator, you may prefer to use Configuration Manager or SSMS because they offer more options and flexibility. Whereas if you are doing automated deployment or scripting, using CMD or PowerShell commands may be more appropriate.
One thing to keep in mind is to make sure that you run these tools with sufficient privileges, especially if you are trying to start a service. Without sufficient permissions, the operation may fail. In addition, if you are working in a corporate environment, you also need to consider security and compliance issues, ensuring that only authorised users can start or stop critical services.
Overall, there are a variety of ways to start SQL Server, and choosing the right method relies on specific application scenarios and personal preferences. Whether it's through Configuration Manager, Service Manager, or the command line, the key is to understand the features and scenarios for each method to effectively manage and monitor SQL Server services.
# Bibliography
[1]答旦.中国自杀研究五十年[J].医学与社会,2001(04):15-17.  

[2]Zhang J,Jiang C,Jia S,et al. An overview of suicide research in Chinal[J]. Arch Suicide Res,2002,6(2):167-184.  

[3]费立鹏.国内外自杀预防研究的进展与思考[J].广西医科大学学报,2022,39(09):1355-1362.DOI:10.16190/j.cnki.45-1211/r.2022.09.001.  

[4]Cheon, Y., Park, J., Jeong, B.Y. et al. Factors associated with psychological stress and distress among Korean adults: the results from Korea National Health and Nutrition Examination Survey. Sci Rep 10, 15134 (2020).   

[5]Daisuke Nishi, Kotaro Imamura, Kazuhiro Watanabe, Hanako Ishikawa, Hisateru Tachimori, Tadashi Takeshima, Norito Kawakami,Psychological distress with and without a history of depression: Results from the World Mental Health Japan 2nd Survey (WMHJ2),Journal of Affective Disorders,Volume 265,2020,Pages 545-551,ISSN 0165-0327.  

[6]Louis Favril, PhD , Rongqin Yu, PhD ,Prof John R Geddes, MD. Prof Seena Fazel, MD.Individual-level risk factors for suicide mortality in the general population: an umbrella review.November 2023,Volume 8Number 11e827-e904.

# Todos
Obtain correlation analysis of different labels in the dataset, and prediction of the data.
