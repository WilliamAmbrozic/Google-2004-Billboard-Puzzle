# Google 2004 Billboard Puzzle
<img align="right" src="http://media.npr.org/programs/morning/features/2004/sep/googlead/billboard_large.jpg" width="200">

>"Mysterious banners at a Cambridge, Mass., subway stop have commuters scratching their heads. The signs, challenging passers-by to solve a complicated math problem, are actually a cryptic pitch by Google, which is looking to hire more brainy engineers. Andrea Shea reports. The message at Harvard Square also appears on a billboard in California's Silicon Valley, but Google's name is nowhere to be found on the ads. It simply states: {first 10-digit prime found in consecutive digits of e}.com In case you're wondering -- or forgot -- e is the base of the natural system of logarithms, having a numerical value of about 2.71828 (though the number goes on forever). The correct answer to the banner problem leads to a Web site that poses yet another puzzle. Eventually, the determined problem-solver lands at a Google Web page that asks the smart, or lucky, few for a resume" ([npr](https://www.npr.org/templates/story/story.php?storyId=3916173) 2004).

## About the Program
The program uses two infinite series that converge to e:

#1: [The Maclaurin Expansion of f(x) = eˣ](http://blogs.ubc.ca/infiniteseriesmodule/units/unit-3-power-series/taylor-series/maclaurin-expansion-of-ex/) |ₓ₌₁: {<img align="center" src="http://wiki.ubc.ca/images/math/8/d/a/8dac8d1875ec09d0a777888da4622f30.png" width="300"> }

#2: [The Brothers Formulae](http://www.brotherstechnology.com/math/e-formulas.html): {<img align="center" src="http://www.brotherstechnology.com/images/e-formulas/e-series2.gif" width="450"> }

The program simply calculates both series and conflates the two into one value for a variable e. This makes it so that the program can only search for legitimate digits of e rather than digits that have not been completed in a single infinite series. For instance, when k = 5 for [The Maclaurin Expansion of f(x) = eˣ](http://blogs.ubc.ca/infiniteseriesmodule/units/unit-3-power-series/taylor-series/maclaurin-expansion-of-ex/) |ₓ₌₁ it will not accurately give the latter digits of e. I do not want to search through these; they could yield a false solution. When the two series have the same digits they are added to said variable e. As e gets larger every time a digits is added a 10 digit number formed at that point is checked for primality. The time compexity of the entire algorithm was not taken into account too much (Thanks to the Prime Number Theorem) (luckily we are looking for a 10 digit prime in consecutive digits of e).

From this program I figured out that the answer is: [7427466391.com](7427466391.com) (does not redirect anymore)

Check for yourself by running the program (quickly check by pasting the contents of the .py file [here](https://www.tutorialspoint.com/execute_python_online.php))

## Find Me <img src="https://imgur.com/download/HT8IjZ5" width="25"> 

- [Youtube](https://www.youtube.com/channel/UCL-VushY6SO0ofPTZ8iB3ag)
- [Instagram](https://www.instagram.com/williamambrozic)
- [Twitter](https://twitter.com/WilliamAmbrozic)
