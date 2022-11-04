# Biology-Covid_Model

#### Created by:
- Raviv Haham
- Peleg Haham

Project Description
-
One of the interesting phenomena in the corona disease is the appearance of "waves" of the disease, the purpose of the exercise is to find the conditions under which such a phenomenon can occur.
In this project, we worked on several features:
We created a desktop application resource that simulates an infection model for the corona virus (according to the instructions provided to us in the exercise).
The application has an accessible and user-friendly interface so even a person who doesn't know how to program at all can easily run the program and enjoy it.

#### The different screens:
The first screen-
![UML](https://imgur.com/W2JYspE.png)

The meaning of the colors in the model we created-
![UML](https://imgur.com/B4gpUN5.png)
Black cell - indicates an empty cell (a cell without a creature).
White cell - indicates a full cell that has a healthy creature in it.
Red cell - indicates a full cell that has a creature that is still sick.
Yellow cell - indicates a full cell that has a recovering creature (a cell with a creature that was sick in the past and has already recovered, meaning that X generations have passed and now it is not sick and will not be able to be infected again).

The second screen-
At first the model will look like this (the board is initialized with a percentage of D patients)
![UML](https://imgur.com/uVihqpr.png)

After that some creatures will be healed and other creatures will be sick
![UML](https://imgur.com/m1jHcpo.png)

Finally, in some cases, the board will look like this
![UML](https://imgur.com/KyhnEiF.png)

At the end of the program, a graph is shown that indicates a phenomenon of waves in the infection of the disease
![UML](https://imgur.com/1AdvLyv.png)



### Running
To run, double-click the covidModel.exe file that appears in the zip folder we uploaded.
You need to make sure that the following libraries are installed on the device before running:
pygame, matplotlib, numpy, tkinter.


## Future improvements:

As we continue to work on this app, we encourage anyone that wants to help out to do so!
Just open the project in Visual Studio Code and add your own touches!
Other than that, we would appreciate if you would try to stick to our design language and patterns.
Have fun with this project and don't forget to create a pull request once you're done so this project could have a little bit of YOU in it!
