# The PRIM module for Python is a standalone version of the Patient Rule
# Induction Method (PRIM) algorithm implemented in the EMA Workbench by Jan
# Kwakkel, which is itself derived from the sdtoolkit R package developed by
# RAND Corporation.  This standalone version of PRIM was created and maintained
# by David Hadka.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division

import logging
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>

COLOR_LIST = ['b',
              'g',
              'r',
              'c',
              'm',
              'y',
              'k',
              'b',
              'g',
              'r',
              'c',
              'm',
              'y',
              'k'
                ]

def pairwise_labels(ax, i, j, field1, field2, ylabels, outcomes_to_show):
    """Adds text and labels to pairwise scatter plot.
    
    Parameters
    ----------
    ax : axes
    i : int
    j : int
    field1 : str
    field2 : str
    ylabels : dict, optional
    outcomes_to_show : str
    """
    #text and labels
    if i == j:
        #only plot the name in the middle
        if ylabels:
            text = ylabels[field1]
        else:
            text = field1
        ax.text(0.5, 0.5, text,
                horizontalalignment='center',
                verticalalignment='center',
                transform = ax.transAxes)  
    
    # are we at the end of the row?
    if i != len(outcomes_to_show)-1:
        #xaxis off
        ax.set_xticklabels([])
    else:
        if ylabels:
            try:
                ax.set_xlabel(ylabels.get(field2))
            except KeyError:
                logging.getLogger(__name__).info("no label specified for "+field2)
        else:
            ax.set_xlabel(field2) 
    
    # are we at the end of the column?
    if j != 0:
        #yaxis off
        ax.set_yticklabels([])
    else:
        if ylabels:
            try:
                ax.set_ylabel(ylabels.get(field1))
            except KeyError:
                logging.getLogger(__name__).info("no label specified for "+field1) 
        else:
            ax.set_ylabel(field1)   
