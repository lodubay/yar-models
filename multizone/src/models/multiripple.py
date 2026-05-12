"""
A modification to the fiducial SFE prescription with multiple short, 
gaussian bursts rippling out in radius with time.
"""

from .utils import gaussian
from .fiducial_sf_law import fiducial_sf_law

_AMPLITUDE_ = 0.8
_PATTERN_SPEED_ = 2 # kpc/Gyr
_NBURSTS_ = 2 # Number of rippling bursts
_START_TIMES_ = [1.2, 6.2] # Gyr, time after simulation start
_BURST_WIDTH_ = 0.5 # Gyr, standard deviation of Gaussian

class multiripple(fiducial_sf_law):
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
    
    All attributes and functionality are inherited from ``fiducial_sf_law``.
    """
    def __init__(self, area, radius, **kwargs):
        super().__init__(area, mode="ifr", **kwargs)
        bursts = []
        for i in range(_NBURSTS_):
            tburst = _START_TIMES_[i] + radius / _PATTERN_SPEED_
            bursts.append(
                gaussian(mean=tburst, amplitude=_AMPLITUDE_, std=_BURST_WIDTH_)
            )
        self._bursts = bursts
        
    
    def __call__(self, time, arg2):
        return super().__call__(time, arg2) * (
            1 - sum([b(time) for b in self._bursts])
        )
