import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

class plot:

    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y
        self.kwargs = kwargs

        # Dislay when show is true
        self.change_rc()
        self.set_axis()
        self.font_set()
        self.set_ticks()
        self.set_axistitle()
        self.display()
    
    def change_rc(self):
        kwargs = self.kwargs
        if 'tickwidth' in kwargs:
            tickwidth=kwargs['tickwidth']
        else:
            tickwidth=2
        plt.rc('axes', lw=tickwidth)
        plt.rcParams.update({
                            "text.usetex": True,
                            "font.family": "sans-serif",
                            "font.sans-serif": ["Times"]
                            })

    def set_axis(self):
        #if axis keyword is given
        kwargs = self.kwargs
        if 'ax' in kwargs.keys():
            self._ax = kwargs['ax']
        elif 'size' in kwargs.keys():
            self.fig, self._ax = self.create_fig(size=kwargs['size'])
        else:
            self.fig, self._ax = self.create_fig()

    def set_ticks(self):
        kwargs = self.kwargs
        if 'ticklength' in kwargs:
            ticklength=kwargs['ticklength']
        else:
            ticklength=8
        if 'tickwidth' in kwargs:
            tickwidth=kwargs['tickwidth']
        else:
            tickwidth=2
        self._ax.xaxis.set_minor_locator(AutoMinorLocator())
        self._ax.yaxis.set_minor_locator(AutoMinorLocator())
        self._ax.tick_params(axis='both', which='major', labelsize=self.font['size']-2, width=tickwidth, length=ticklength)
        self._ax.tick_params(axis='both', which='minor', labelsize=self.font['size']-2, width=tickwidth, length=0.5*ticklength)

        if 'xticks' in kwargs:
            self._ax.set_xticks(kwargs['xticks'])
        if 'yticks' in kwargs:
            self._ax.set_yticks(kwargs['yticks'])
    
    def display(self):
        kwargs = self.kwargs
        if 'show' in kwargs.keys():
            self.show = kwargs['show']
        else:
            self.show = True
        self._ax.plot(self.x, self.y)
        if self.show : plt.show()

    
    #axis titles
    def set_axistitle(self):
        kwargs = self.kwargs
        if 'xtitle' in kwargs.keys():
            self._ax.set_xlabel(kwargs['xtitle'], fontdict=self.font)
        if 'ytitle' in kwargs.keys():
            self._ax.set_ylabel(kwargs['ytitle'], fontdict=self.font)

    def font_set(self):
        #Font styles
        kwargs = self.kwargs    
        if not ('fontweight' in kwargs):
            fontweight='normal'
        else:
            fontweight=kwargs['fontweight']
        
        if not ('fontsize' in kwargs):
            fontsize=30
        else:
            fontsize=kwargs['fontsize']
        
        self.font = {'family': 'serif',
                    'color':  'black',
                    'weight': fontweight,
                    'size': fontsize
                    }
    def save(self, filename):
        self.fig.savefig(filename)

    #Function that create default figure and axis
    def create_fig(self, size=(10,10)):
        """
        This function will create a figure of default size. 
        """
        fig, _ax = plt.subplots(1,1, figsize=size)
        return fig, _ax