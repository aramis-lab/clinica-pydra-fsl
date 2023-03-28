"""Pydra tasks for FSL.

>>> from pydra.tasks import fsl
"""

__all__ = [
    "ApplyXFM",
    "BET",
    "ConcatXFM",
    "ConvertXFM",
    "Eddy",
    "FAST",
    "FLIRT",
    "FNIRT",
    "FSLMerge",
    "FSLReorient2Std",
    "FSLROI",
    "InvertXFM",
    "RobustFOV",
    "fslmaths",
]

from . import fslmaths
from .apply_xfm import ApplyXFM
from .bet import BET
from .concat_xfm import ConcatXFM
from .convert_xfm import ConvertXFM
from .eddy import Eddy
from .fast import FAST
from .flirt import FLIRT
from .fnirt import FNIRT
from .fslmerge import FSLMerge
from .fslreorient2std import FSLReorient2Std
from .fslroi import FSLROI
from .invert_xfm import InvertXFM
from .robustfov import RobustFOV
