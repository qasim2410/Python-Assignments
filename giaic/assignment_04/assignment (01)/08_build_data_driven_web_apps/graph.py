# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px

# # data  = pd.DataFrame({
# #     'x': np.arange(1, 101),
# #     'y': np.random.randn(100)
# # })

# # fig = px.line(data, x='x', y='y', title='Line Chart Example')

# # st.plotly_chart(fig, use_container_width=True)
# # st.write("This is a simple line chart example using Plotly Express.")


import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({
    'x': np.arange(1, 101),
    'y': np.random.randn(100)
})

plt.figure(figsize=(10, 5))
sns.scatterplot(data=data, x='x', y='y')


st.pyplot(px.line(data, x='x', y='y', title='Line Chart Example'))
