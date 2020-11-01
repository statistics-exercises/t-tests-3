import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_histogram(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[1].get_xydata()
        this_x, this_y = zip(*figdat)
        dx = this_x[1] - this_x[0]
        for i in range(len(this_x)) :
            l, u = this_x[i] - 0.5*dx, this_x[i] + 0.5*dx
            p = scipy.stats.t.cdf(u,4) - scipy.stats.t.cdf(l,4)
            var = p*(1-p)
            confl = scipy.stats.norm.ppf(0.01,loc=0,scale=np.sqrt(var))
            confu = scipy.stats.norm.ppf(0.99,loc=0,scale=np.sqrt(var))
            self.assertTrue( this_y[i]*dx > confl and this_y[i]*dx < confu, "your histogram appears to  be incorrect" )
            
   def test_t_distribution(self) :
        for i in range(2,11) :
            ttt = gen_t_variable(i)
            self.assertTrue( ttt>scipy.stats.t.ppf(0.01,i) and ttt<scipy.stats.t.ppf(0.99,i), "your function for generating the t distribution appears to be sampling the wrong distribution" )
            
   def test_normalisation(self) :
       fighand=plt.gca()
       figdat = fighand.get_lines()[1].get_xydata()
       this_x, this_y = zip(*figdat)
       self.assertTrue( np.abs( sum(this_y)*(this_x[1]-this_x[0]) - 1 )<1e-7, "your histogram has not been normalised" )
