import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import altair as alt

# --- 1. Business Understanding & 2. Data Understanding ---
st.set_page_config(page_title="Interactive Linear Regression Analysis", layout="wide")
st.title("Interactive Linear Regression Simulation")
st.write("""
### Project Goal (Business Understanding)
This tool is designed to help users visually understand simple linear regression.
You can adjust parameters to generate data and observe how the model fits the data, thereby deepening your understanding of linear relationships, noise, and model fitting.
""")

st.write("---")

# --- 3. Data Preparation ---
st.sidebar.header("Parameter Settings (Data Preparation)")
st.sidebar.write("Adjust the following parameters to generate new data points:")

# Allow user to modify parameters
a_param = st.sidebar.slider("Slope (a)", min_value=0.0, max_value=10.0, value=2.5, step=0.1)
num_points = st.sidebar.slider("Number of Points", min_value=10, max_value=500, value=100, step=10)
noise_level = st.sidebar.slider("Noise Level", min_value=0.0, max_value=50.0, value=10.0, step=1.0)

# We fix 'b' for simplicity
b_param = 5.0

# Generate data
np.random.seed(42)
X = np.random.rand(num_points, 1) * 10
# y = a*X + b + noise
y_true = a_param * X.ravel() + b_param
y_noisy = y_true + np.random.randn(num_points) * noise_level

df = pd.DataFrame({
    'x': X.ravel(),
    'y_noisy': y_noisy,
    'y_true': y_true
})

st.write("### 3. Data Preparation")
st.write(f"Based on your settings (a={a_param}, points={num_points}, noise={noise_level}), we have generated the following data:")
st.dataframe(df.head())

# --- 4. Modeling ---
st.write("### 4. Modeling")
st.write("We use Scikit-learn's `LinearRegression` to fit the noisy data points above.")

model = LinearRegression()
model.fit(X, y_noisy)

# Get model parameters
model_a = model.coef_[0]
model_b = model.intercept_
st.write(f"**Model Fit Results:**")
st.markdown(f"- Fitted Slope (a): `{model_a:.2f}` (True slope: {a_param})")
st.markdown(f"- Fitted Intercept (b): `{model_b:.2f}` (True intercept: {b_param})")


# --- 5. Evaluation ---
st.write("### 5. Evaluation")
st.write("The chart below visualizes the entire process:")

# Create the chart
# Scatter plot for noisy data
scatter_plot = alt.Chart(df).mark_circle(size=60, opacity=0.7).encode(
    x=alt.X('x', title='X'),
    y=alt.Y('y_noisy', title='Y'),
    tooltip=['x', 'y_noisy']
).properties(
    title="Linear Regression Visualization"
)

# True line
true_line = alt.Chart(df).mark_line(color='green', strokeDash=[5,5]).encode(
    x='x',
    y='y_true'
)

# Model line
model_df = pd.DataFrame({
    'x': X.ravel(),
    'y_model': model.predict(X)
})
model_line = alt.Chart(model_df).mark_line(color='red').encode(
    x='x',
    y='y_model'
)

# Combine charts
final_chart = (scatter_plot + true_line + model_line).interactive()

st.altair_chart(final_chart, use_container_width=True)
st.markdown("""
**Chart Legend:**
- **Blue Circles**: The noisy data points generated based on your settings.
- **Green Dashed Line**: The true underlying relationship (`y = ax + b`).
- **Red Solid Line**: The prediction line fitted by the model based on the blue data points.
""")

# --- 6. Deployment ---
st.write("---")
st.write("### 6. Deployment")
st.success("This application itself is the deployment! It has been successfully deployed as an interactive web app using the Streamlit framework.")