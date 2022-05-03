# Location Prediction with ML
### ml-team3

**Authors:** Trenton Metcalfe, Sean Maher, Simon Kwilinski, Jermaine Presbery

## Contents

- readme.md - this file  
- .ebextensions - contains configuration directory for elastic beanstalk
- data - contains all the data
- jupyter - contains all model and pipeline testing
- model - creates the database to be used for the models
- website - contains all the code for creating the website with the model
- requirements.txt - has all of the python requirements for the project
		 
## Functionality
    
This site was made as a destination finder. A user is able to input the time of year and their preferred weather
specifications and the model will suggest locations for the user to go to that match these specifications. The model
does this by using a Voting classifier compiled of a handful of different models all optimized for this task. The models
are trained on a large weather dataset that includes specific locations, temperature, time of year, time of day, and other
more specific weather features (pressure, humidity, precipitation, etc.).
