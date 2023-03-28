"""Pydra tasks for FSL.

>>> from pydra.tasks import fsl
"""

__all__ = [
    "Eddy",
    "FAST",
    "FNIRT",
    "FSLMerge",
    "FSLReorient2Std",
    "FSLROI",
    "SUSAN",
    "fslmaths",
]

from . import bet, flirt, fslmaths
from .eddy import Eddy
from .fast import FAST
from .fnirt import FNIRT
from .fslmerge import FSLMerge
from .fslreorient2std import FSLReorient2Std
from .fslroi import FSLROI
from .susan import SUSAN

__all__ += bet.__all__
__all__ += flirt.__all__
