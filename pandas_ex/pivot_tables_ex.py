# Original Article --> https://towardsdatascience.com/pivot-tables-in-pandas-7834951a8177

# Pivot tables are basically a count of things within a certain bracket.

import pandas as pd
import numpy as np


titanic = pd.read_csv('train.csv') # dataset downloaded from Kaggle.

# let's make sure there are no null values before we begin building our pivot tables.

#print(titanic.isna().sum())
# print(titanic.)

# We have a few nulls so let's get rid of them first.
# This is usually not advised and normally some value is placed instead of null values based on their positions
# specially if our dataset is small. But for now we are demonstrating Pivot tables so let's not worry about that.

# we will drop the cabins column and all rows that have null values.

titanic.drop(axis=1, labels=['Cabin'], inplace=True)
titanic.dropna(axis=0, how='any', inplace=True)

# Now both Fare and Age columns have a lot of distinct values.
# We will create bins for them for easier processing.

# To do this we will use panda's cut and quantile function and method respectively.

fare_bin_edges = [0,
                    titanic['Fare'].quantile(0.2),
                    titanic['Fare'].quantile(0.4),
                    titanic['Fare'].quantile(0.5),
                    titanic['Fare'].quantile(0.8),
                    max(titanic['Fare']) + 1]

titanic['fare_bin'] = pd.cut(titanic['Fare'], fare_bin_edges, labels=[1,2,3,4,5])

# Now let's do the same with ages.
# The first bin include everyone within the age of 10.
age_bin_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 1000]
titanic['age_bin'] = pd.cut(titanic['Fare'],
                                age_bin_edges,
                                labels=['>=10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '80+'])


# Now on to the pivot tables.

# Let's figure out first the count of passengers by age group and gender using Pivot Tables.
pivot1 = pd.pivot_table(titanic,                    # dataframe
                        values=['PassengerId'],     # The column we would like to count. (or apply aggfunc on)
                        index='age_bin',            # How to group the counted values on the row axis.
                        columns=['Sex'],            # How to group in columns.
                        aggfunc='count')            # Function we apply to values (count, sum, mean, min, max etc..)


print(pivot1) # vastly different from the tutorial I am following due to which I believe the dataset may have changed.


# Now let's use pivot tables to answer who was best likely to survive that disaster.
# We can use this information to formulate better ML Algorithms.

# Let's make a pivot table where we group by age_bin in rows and gender and passenger class in columns.

pivot2 = pd.pivot_table(titanic,
                        values=['Survived'],
                        index='age_bin',
                        columns=['Sex', 'Pclass'],
                        aggfunc='mean' # or count/sum)
                        )


print(pivot2.round(2))

# We can understand a lot from this pivot table as to the chances of who survived and who didn't.
# And partly the reason as well.

# let's look at it in another perspective.

pivot3 = pd.pivot_table(
    titanic,
    values=['Survived'],
    index='Pclass',
    columns=['Sex'],
    aggfunc='mean'
)

print(pivot3.round(2))

# Now we can apply a simple ML algorithm such as Decision Tree or Linear Regression to find out the probabilities
# found in the test.csv file.




