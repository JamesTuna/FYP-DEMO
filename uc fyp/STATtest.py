#! /usr/bin/env python3
# statistical test for UC FYP 2018
# Algorithm: difference of proportion
import math

def test(n11,n12,n21,n22):
	estimated_pi1 = n11/(n11+n12)
	estimated_pi2 = n21/(n21+n22)
	estimated_diff = estimated_pi1-estimated_pi2
	std = math.sqrt(estimated_pi1*(1-estimated_pi1)/(n11+n22)+estimated_pi2*(1-estimated_pi2)/(n21+n22))
	return estimated_diff,std

# conclusions
est,std = test(8,17+6+6+28,22,29+12+12+43+9)
est,std = test(5,5,14+2+4+3+0+1+2,181-10-(14+2+4+3+0+1+2)) 
est,std = test(16,21,13+10+7,181-16-21-(13+10+7))
est,std = test(12,3,21+8+5+26,25+23+13+45)
est,std = test(12+4+1,14,4+1+2,39)
est,std = test(12,3,35+16+12+46,11+15+6+25)
est,std = test(11,4,26+17+9+37,20+14+9+34)

# one-side test
print('confidence interval',(est-1.65*std,est+1.65*std))
print(est,std,'\ncritical vaule',est/std) 
