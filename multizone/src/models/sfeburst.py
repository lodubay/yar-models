"""
A modification to the fiducial SFE prescription with a short, gaussian burst.
"""

from .utils import gaussian
from .fiducial_sf_law import fiducial_sf_law

_AMPLITUDE_ = 0.5
_BURST_TIME_ = 2.2 # Gyr, time after simulation start
_BURST_WIDTH_ = 0.5 # Gyr, standard deviation of Gaussian

class sfeburst(fiducial_sf_law, gaussian):
    """
    A star formation efficiency prescription with a Gaussian burst rippling
    outwards in radius over time.

    Parameters
    ----------
    area : real number
        The surface area in kpc^2 of the corresponding annulus in a 
        ``milkyway`` disk model.
    radius : real number
        The mean radius in kpc of the annulus.
    **kwargs : varying types
        Keyword arguments passed to ``fiducial_sf_law``.
    
    All attributes and functionality are inherited from ``fiducial_sf_law``
    and ``utils.gaussian``.
    """
    def __init__(self, area, **kwargs):
        fiducial_sf_law.__init__(self, area, mode="ifr", **kwargs)
        gaussian.__init__(self, mean=_BURST_TIME_, amplitude=_AMPLITUDE_, std=_BURST_WIDTH_)
    
    def __call__(self, time, arg2):
        return fiducial_sf_law.__call__(self, time, arg2) * (
            1 - gaussian.__call__(self, time)
        )
    
