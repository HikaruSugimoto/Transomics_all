import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from matplotlib.gridspec import GridSpec
from networkx.algorithms import bipartite
from networkx.drawing.layout import bipartite_layout
from scipy.optimize import curve_fit
import random
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from bs4 import BeautifulSoup
import requests
import urllib.request
import xml.etree.ElementTree as ET
from pyvis.network import Network
import streamlit.components.v1 as components
import zipfile
import os
import scipy.io
import scipy.stats as stats
from scipy.stats import fisher_exact
import statsmodels.stats.multitest as multi
from matplotlib_venn import venn3
from PIL import Image
import statsmodels.api as sm
import gc
#plt.rcParams['font.family']= 'sans-serif'
#plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'out'
plt.rcParams['xtick.major.width'] = 1.2
plt.rcParams['ytick.major.width'] = 1.2
plt.rcParams['font.size'] = 12 
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['figure.dpi'] = 300

#Main
st.set_page_config(layout="wide")
st.title("iTraNet: integrated Trans-omics Network visualization and analysis")
st.write("This website is free and open to all users and there is no login requirement.")

image = Image.open('./Fig/0.png')
st.image(image, caption='',use_column_width=True)

st.subheader('Analysis methods')
image = Image.open('./Fig/2.png')
st.image(image, caption='',use_column_width=True)
f=open('./Fig/2A.txt', 'r')
st.write(f.read()) 
f=open('./Fig/2B.txt', 'r')
st.write(f.read()) 
f=open('./Fig/2C.txt', 'r')
st.write(f.read()) 
f=open('./Fig/2D.txt', 'r')
st.write(f.read()) 

st.subheader('License')
f=open('./Fig/4.txt', 'r')
st.write(f.read())
f.close()

st.subheader('Help')
st.write("If loading bars of interactive networks show 0%, please visit the following URL: https://github.com/WestHealth/pyvis/issues/25")

#sidebar
st.sidebar.title('Select an analysis method')
urla = "https://itranet-a.streamlit.app/"
urlb = "https://itranet-b.streamlit.app/"
urlc = "https://itranet-c.streamlit.app/"
urld = "https://itranet-d.streamlit.app//"
url = "https://github.com/HikaruSugimoto/Transomics_iTraNet"

st.sidebar.subheader("[A, gene regulatory network](%s)" % urla)
st.sidebar.subheader("[B, mRNA (protein)-mRNA (protein) interaction](%s)" % urlb)
st.sidebar.subheader("[C, metabolic network](%s)" % urlc)
st.sidebar.subheader("[D, metabolite exchange network](%s)" % urld)
st.sidebar.subheader("[Download codes and run iTraNet on a local machine](%s)" % url)
