In this zillow project, I will do research on the drivers of the values of single family residential properties in the United States. The data I am going to use is collected from zillow database.

I'm going to use the properties' features such as number of bedrooms, number of bathrooms, squarefeet as independent variables, the aproperties' tax value as dependent variables, to look over relationships among independent variables as well as relationships between independent variables and dependent variabe.

I did six correlation tests among independent variables (bathroomcnt,bedroomcnt,sqft) and dependent variable (tax_value), and found out that there is a weak-postive linear relatioship between sqft and tax_value; there is also a weak-positive linear relatioship between bathroomcnt and tax_value; there is a very weak-positive linear relatioship between bedroomcnt and tax_value,

In addition, among independent variables themsleves, there is a strong-postive linear relationship between bathroomcnt and sqft; there is a moderate-postive linear relatioship between bathroomcnt and bedroomcnt; there is also a moderate-postive linear relationship between bedroomcnt and sqft.

 During modeling, I built seven models using all possible combinations among features, then I used a lambda function to calculate the mean_squared_errors for those models, and found the best model is the model with the combination of all three independent variables(bathroomcnt&bedroomcnt&sqft).
