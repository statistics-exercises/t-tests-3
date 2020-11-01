# Histogram

OK now that we can sample from this distribution lets see if we can characterise the distribution.  __To complete this task you need to use the outline code in `main.py` to generate a histogram by repeatedly taking samples from the distribution that was introduced in the previous task with N=5.__

The outline code that I have written calls on you to copy the function  (`generate_t_variable`) that you wrote for the previous task. This function will be used to generate the random variable that we are interested in.  I have then created and stored the midpoints for a series of histogram bins that start at `xmin` and that finishes at `xmax` in a NumPy array called `xvals`.  Your task is to write a loop that generates 200 random variables using the  `generate_t_variable` function.  Within this loop, you should use the NumPy array called `counts` to count how many of these random variables fall within each of the `nbins` histogram bins.  

Once you have generated all your random variables you will need to normalise the histogram that is stored in `counts`.  

When your code is complete it should generate a graph showing the histogram that you have generated in red.  For comparison the probability density function for the random variable:

![](https://render.githubusercontent.com/render/math?math=Y=\frac{1}{n}\sum_{i=1}^nX_i)

is shown as a blue line.  In this expression, each ![](https://render.githubusercontent.com/render/math?math=X_i) is a standard normal random variable.  Make sure you look at the graph that is generated in order to compare the distribution that is sampled in `generate_t_variable` and the distribution for the random variable above.
