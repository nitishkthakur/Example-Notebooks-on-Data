### Set Matplotlib Defaults ###
import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt

def load_defaults(fontsize = 17, figsize = [12.0, 6.0], font = 'Calibri', grid = True):
    # Load Overall Theme
    if grid:
        plt.style.use('seaborn-whitegrid')
    else:
        plt.style.use('seaborn-ticks')
        
    # Set Specifics
    mpl.rcParams['figure.figsize'] = figsize
    mpl.rcParams['font.family'] = font
    mpl.rcParams['font.size'] = fontsize
    mpl.rcParams['grid.alpha']= 0.75
    mpl.rcParams['grid.linestyle']= '--'
    mpl.rcParams['image.cmap']= 'coolwarm'    
    mpl.rcParams['legend.framealpha']= 0.6
    mpl.rcParams['axes.spines.right'] = True
    mpl.rcParams['axes.spines.left'] = True
    mpl.rcParams['axes.spines.top'] = True
    mpl.rcParams['axes.spines.bottom'] = True
    mpl.rcParams['figure.dpi'] = 150
    mpl.rcParams['figure.edgecolor']= 'black'
    mpl.rcParams['hist.bins']= 15
    mpl.rcParams['legend.frameon']=True
    mpl.rcParams['axes.edgecolor']= 'black'
    
    # Color
    mpl.rcParams['savefig.dpi']= 120
    
