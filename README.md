# MyRapidHack2023-BackEnd
 
**The introduced theme for the Hackathon includes;**
1. Service Efficiency
2. Operational Performance
3. Mobility Revolution
4. Customer Experience

**Highlighted Issues / Problem Statement :**
1. Lack of bus operating due to breakdown issues as some of the bus is quite old. 
2. Those problematic buses are required to undergo repairs which take quite some time.
3. Availibility of manpower, tools, facilities and spareparts might associate with length of the downtime period

**Business Case:**
Development of predictive maintenance ML model to enable effective maintenance management eco-system whereby tendency of buses that might have problem can be predictied. On top of that, the maintenance management eco-system shall be serve with a dashboard that enable the maintenance team to be alert on the capacity. 

**Use Cases:**
In order to achieve the business case requirement, the followings use cases shall be identified. We basically need to profile the buses, captains and daily operations. These informations shall be integrated together to establish the first level of data model. 

##### **Buses by Service Demographic**<br>
    |-- Bus capacity
    |-- Bus brand
    |-- Bus length of service (years)
    |-- Accident history
    |-- Maintenance history
    |-- Odometer read

##### **Captains by Service Demographic**<br>
    |-- Length of service 
    |-- Age
    |-- Gender

##### **Daily Operations by Service Demographic**<br>
    |-- Average number of bus operating daily
    |-- Average number of bus in worksyop (for maintenance/repair)
    |-- Average number of bus in daily standby mode 
    |-- Average fuel consumption for specified bus route
    |-- Average distance for specified bus route

**Strategy:**
Using massaged data and insight obtained from the above use cases, a data model shall be established using all available features. As we wanted to established a predictive model for bus maintenance, historical maintenance & repair informations shall be labelled in the data model . At this stage, time series prediction approach shall be neglected as we will focus of quantitative periodical parameters instead , therefore numbers of days before the next maintenance/repair shall be calculated. We also want to calculate numbers of days required for maintenance/repair until the bus being re-deploy for service. The data model which contain the labelled maintenance & repair information shall be diagnosed using any available methods (quantitative vs quantitative, quantitative vs qualittative or qualitative vs quantitative features), whereby the most significant features that can be implement to develop the predictive model can be identified. For this hackathon purpose, we shall only implement binary classification prediction whereby the model will only predict 'YES' or 'NO' for maintenance after a period of time. 

**Data Source:**
The data source shall be using data provided by MyRapidHack organiser

**Data Visualisation:**
Data shall be presented using any visualisation tools available in the market . The most important aspect is the enablement in visualising all the use cases and the prediction result. 
