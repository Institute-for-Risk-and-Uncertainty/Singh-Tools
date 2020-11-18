# Singh-Tools
Tools for generating Singh plots

The function singhvals returns a sorted list of values in the interval [0,1] which should be used as x-coordinates in a 2D plot on the unit square, with a uniform function plotted on the y-axis.

The input c_struct should define a confidence structure which determines the alpha confidence level required to cover the supplied parameter for a given data set. This can be imprecise, but in this case the imprecision should be represented by a list or array of endpoints. Support for pba intervals will be added in the future.

The input target_dist should be any function which can be passed a variable 'size' and return a corresponding number of sample sets. For example, if a method is to be checked for a normal distribution with sample size 10, targetdist(2) should return two length 10 samples.

If true_param is left at none the structure is assumed to be predictive. This will be refiend at a laetr date.

Increasing n_samples increases the granularity of the result, but 1000 is generally enough to get a reasonable estimation of the properties of the structure.