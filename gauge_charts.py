import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=65,
    title={'text': "Speed"},
    gauge={'axis': {'range': [0, 100]},
        'bar': {'color': "darkblue"},
        'steps': [{'range': [0, 50], 'color': "lightgray"},
            {'range': [50, 100], 'color': "gray"}],
        'threshold': {'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 80}}))
fig.show()

# This code creates a gauge chart using Plotly's graph_objects module.
# The gauge chart displays a speed indicator with a value of 65.
# The gauge has a range from 0 to 100, with a bar color of dark blue.
# It includes steps for different ranges: light gray for 0-50 and gray for 50-100.
# A threshold is set at 80, with a red line indicating the threshold value.
# The chart is displayed using the `show()` method.
# The `go.Figure` and `go.Indicator` classes are used to create the
# gauge chart, and the `mode` is set to "gauge+number" to display both the gauge and the numeric value.
# The `title` parameter sets the title of the gauge to "Speed".
# The `gauge` parameter defines the properties of the gauge, including the axis range,
# bar color, steps, and threshold.
# The `steps` parameter defines the color ranges for different segments of the gauge,
# while the `threshold` parameter sets a specific value with a line and thickness.
# The `fig.show()` method renders the gauge chart in a web browser or notebook environment.
# The code uses the Plotly library, which is a powerful tool for creating interactive visualizations in Python.
# To run this code, ensure you have the Plotly library installed:

# pip install plotly
       
