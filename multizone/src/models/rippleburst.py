"""
A modification to the fiducial SFE prescription with a short, gaussian burst
rippling out in radius with time.
"""

from .utils import gaussian
from .fiducial_sf_law import fiducial_sf_law

_AMPLITUDE_ = 0.5
_PATTERN_SPEED_ = 2 # kpc/Gyr
_START_TIME_ = 3.2 # Gyr, time after simulation start
_BURST_WIDTH_ = 0.5 # Gyr, standard deviation of Gaussian

class rippleburst(fiducial_sf_law, gaussian):
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
    def __init__(self, area, radius, **kwargs):
        fiducial_sf_law.__init__(self, area, mode="ifr", **kwargs)
        tburst = _START_TIME_ + radius / _PATTERN_SPEED_
        gaussian.__init__(self, mean=tburst, amplitude=_AMPLITUDE_, std=_BURST_WIDTH_)
    
    def __call__(self, time, arg2):
        return fiducial_sf_law.__call__(self, time, arg2) * (
            1 - gaussian.__call__(self, time)
        )
