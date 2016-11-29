## Cikibike Null Hypothesis project review

Your notebook begins with a code chell that is not run: it is a code cell but marked as a markdown cell (or non-code cell). You should clean the presentation notebook from these "commented cells", if that is what was intended. But I think that was intended to be run and state the Null hypothesis.

The mathematical formulation of the Null is missing (N_WD - N_WE = ...)

The question and Null hypothesis are well formulated.

The data supports the question but there are several mistakes in the data munging portion.

The pylab import is missing causing the notebook not to run!

The following line of code has your path hard coded in. Nobody but you have access to your own home directory, so your notebooks is NOT REPRODUCIBLE.
All references to the file must use the environmental variables for it to be reproducible without modifying the code.

```
dataframe = pd.read_csv('/home/cusp/cjs676/PUIdata/201-citibike-tripdata.csv')
```

```
dataframe = pd.read_csv(os.getenv("PUIDATA")+"/"+datestring+....csv')
```

notice that you should also use datestring to create the file name so that if you want to use a different input file you need to change values only in one place. i left the line incomplete because I want you to complete it and understand it, not just copy and paste it.



the following chunk of code has some mistakes and can be vastly improved in style and efficiency:

```
        working_day_trip = 0
        weekend_day_trip = 0

        for i in range(0 , 4):  
            working_day_trip = data_count[i] + working_day_trip

        for i in (5,6):
            weekend_day_trip = data_count[i] + weekend_day_trip
    
```
1. MISTAKE: range(0 , 4)  returns [0,1,2,3], which for you is [M, T, W, Th]. So  you are skipping friday altogether (but accounting for them in the mean so your mean is wrong)


For efficiency those loops should be changed with

```
        working_day_trip  = data_count[:5].sum(),
        weekend_day_trip = ...
        
```

What is up with the norm_w = 1 and division by norm_1??

Once the mistakes are fixed you have to averages, so you can do a test of means, **but for that you also have to extract the standard deviations of the distributions to assess statistical significance, and the way you worked with the data does not help much obtaining it because your data is now grouped by weekday so you can get the std and mean per day of the week (mean trips number on monday over a month, mean trip number on tuesday over the month etc), but to get the mean and std of all weekdays you are going to have to do some more work**.
