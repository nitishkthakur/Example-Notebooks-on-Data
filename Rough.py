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
    
    
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.graphics.regressionplots import plot_leverage_resid2
from statsmodels.graphics.regressionplots import influence_plot
fig, axes = plt.subplots(2, 2, figsize = (15, 8), tight_layout = True)

        # Autocorrelation between Residuals
        plot_acf(model_for_report.resid, ax = axes[0,0])
        axes[0, 0].set_title('Residual Autocorrelation')

        # Leverage Plot
        plot_leverage_resid2(model_for_report, alpha=0.05, ax = axes[0, 1])

        # Influence Plot
        influence_plot(model_for_report, external=True, alpha=0.05, criterion='cooks', size=48, plot_alpha=0.75, ax=axes[1, 0])

        # PPPlot
        resid = model_for_report.resid.values
        resid = resid[resid.argsort()]
        #resid = standardize(resid)
        resid = stats.zscore(resid)
        sm.ProbPlot(resid).ppplot(line = '45', ax = axes[1,1])
        save('Diagnostics.png', output_feature_directory)
