import altair as alt
from vega_datasets import data
# load a simple dataset as a pandas DataFrame

cars = data.cars()

alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive().save('C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\t1.png')

