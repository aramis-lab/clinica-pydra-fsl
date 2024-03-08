"""
FLIRT
=====

.. automodule:: pydra.tasks.fsl.flirt.flirt
.. automodule:: pydra.tasks.fsl.flirt.convertxfm
.. automodule:: pydra.tasks.fsl.flirt.img2imgcoord
.. automodule:: pydra.tasks.fsl.flirt.img2stdcoord
.. automodule:: pydra.tasks.fsl.flirt.std2imgcoord
"""

from pydra.tasks.fsl.flirt.convertxfm import ConcatXFM, ConvertXFM, FixScaleSkew, InvertXFM
from pydra.tasks.fsl.flirt.flirt import FLIRT, ApplyXFM
from pydra.tasks.fsl.flirt.img2imgcoord import Img2ImgCoord
from pydra.tasks.fsl.flirt.img2stdcoord import Img2StdCoord
from pydra.tasks.fsl.flirt.std2imgcoord import Std2ImgCoord

__all__ = [
    "ConcatXFM",
    "ConvertXFM",
    "FixScaleSkew",
    "InvertXFM",
    "FLIRT",
    "ApplyXFM",
    "Img2ImgCoord",
    "Img2StdCoord",
    "Std2ImgCoord",
]
