"""
α = 0.0
β = 0.0
γ = 0.5
ζ = 0.25
S = -1.0
x_r = -0.2
w_r = 0.1
"""
import numpy as np


#def ddf(x):
    #b = 10 ** -1.111
    #return np.exp(-(x / b) ** 2) / (b * np.sqrt(np.pi))


α = float(input())
β = float(input())
γ = float(input())
ζ = float(input())
S = float(input())
x_r = float(input())
w_r = float(input())

# computing w_b
if w_r >= 0:
    w_b = 1.
else:
    w_b = -1.

# computing x_b
if x_r < -1:
    x_b = -1.
elif -1 <= x_r < 0:
    x_b = x_r ** 2. + 2. * x_r
elif 0 <= x_r < 1:
    x_b = -x_r ** 2. + 2. * x_r
else:
    x_b = 1.

# computing δx_b/δx_r
if -1 <= x_r < 0:
    δx_b_δx_r = 2. * x_r + 2.
elif 0 <= x_r < 1:
    δx_b_δx_r = -2. * x_r + 2.
else:
    δx_b_δx_r = 0.

# what is x?
x = x_b * w_b

# computing δL/δx_b
if (x - α) > 0 and γ * (x - α) > S:
    δL_δx_b = γ * w_b
elif (x - α) <= 0 and ζ * (x - α) > S:
    δL_δx_b = ζ * w_b
else:
    δL_δx_b = 0.

# computing δL/δw_b
if (x - α) > 0 and γ * (x - α) > S:
    δL_δw_b = γ * x_b
elif (x - α) <= 0 and ζ * (x - α) > S:
    δL_δw_b = ζ * x_b
else:
    δL_δw_b = 0.

# computing δL/δw_r
#δL_δw_r = δL_δw_b * 2 * ddf(w_r)
δL_δw_r = δL_δw_b

# computing δL/δx_r
δL_δx_r = δL_δx_b * δx_b_δx_r

print(δL_δx_r)
print(δL_δw_r)
