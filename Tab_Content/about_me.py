import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
from app import app


about_me_LO = html.Div([


    html.Div([

        html.H4("About me:"),

        html.Div([

            html.P("I am Shreyas Lengade, with experience in software development, data analysis, data engineering, and quality assurance. My passion lies in developing data-driven applications, crafting dynamic dashboards, and gathering requirements to deliver impactful solutions. I take great satisfaction in analyzing complex datasets, uncovering hidden insights, and turning them into actionable results that drive business value. As a tech enthusiast and lifelong learner, I am always eager to explore the latest advancements in the ever-evolving world of technology. "),

            html.P([html.A("LinkedIn", href='https://www.linkedin.com/in/shreyas-lengade-6b32971a3/',
                           target='_blank', className='libutton')], className='home_text'),

            html.P([html.A("GitHub", href='https://github.com/ShreyasLengade',
                           target='_blank', className='libutton')], className='home_text'),

            html.P([html.A("Portfolio", href='https://my-portfolio-eight-delta-14.vercel.app/',
                           target='_blank', className='libutton')], className='home_text'),

        ], className='description')


    ], className='aboutme_container_first_section'),

    html.Div([
        html.H4('Some great Python Resources from Youtube:'),

        html.Li([html.A("Python for Data Visualization with Dash/Plotly",
                        href='https://www.youtube.com/@CharmingData', target='_blank')], className='anchor_r'),

        html.Li([html.A("Python Programming tutorials",
                        href='https://www.youtube.com/@sentdex', target='_blank')], className='anchor_r'),

        html.Li([html.A("Python for Machine Learning and Data Science",
                        href='https://www.youtube.com/@krishnaik06', target='_blank')], className='anchor_r'),

        html.Li([html.A("Python for Machine Learning with emphasis on Image Processing ",
                        href='https://www.youtube.com/@DigitalSreeni', target='_blank')], className='anchor_r'),

        html.Li([html.A("Python for Quantitative Finance ",
                        href='https://www.youtube.com/@QuantPy', target='_blank')], className='anchor_r'),

        html.Li([html.A("Python for Algo Trading ",
                        href='https://www.youtube.com/@ComputerSciencecompsci112358', target='_blank')], className='anchor_r'),

    ], className='reference')


], className='main_container')
