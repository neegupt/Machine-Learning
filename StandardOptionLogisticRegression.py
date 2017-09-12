#The program prints out class predictions in the terminal. Do these look correct? How do you know?

#The predictions should come out as 0 and 1, because you are inputting data based off of the averages of the two different plants. However the averages are really close,
#which explains why the model sometimes predicts incorrectly.

#The program also prints out some probabilities. How do those relate to the class predictions?

#The probabilities represent the probability of the specific data inputted after training the model to be one class over another. For each input,
#if the number is over 50 in the first column, the ooutput is a 0 and vice versa.

#If you change the averages in the generated data, what effects do you see?

#Changing the averages so that they are further apart makes the data more accurate because the randomly generated data for each class is further apart,
#making it easier for the model to determine. Switching the values of the classes flips the sign of the coeffecients, because the opposite class has higher heights/widths than before.


#The program also prints out the intercept and coefficients in the terminal, as the linear regression program did. What does it mean if a coefficient is negative?

#A coeffecient being negative indicates that as the corresponding x value rises, the probability of outputting a 1 is lowered. 
