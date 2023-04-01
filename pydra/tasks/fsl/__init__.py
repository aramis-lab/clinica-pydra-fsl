"""Pydra tasks for FSL.

>>> from pydra.tasks import fsl
"""

from . import fslmaths
from .bet import BET, RobustFOV
from .eddy import Eddy
from .fast import FAST
from .flirt import FLIRT, ApplyXFM, ConcatXFM, ConvertXFM, InvertXFM
from .fnirt import FNIRT, ApplyWarp, ConvertWarp, InvWarp
from .fslmerge import FSLMerge
from .fslreorient2std import FSLReorient2Std
from .fslroi import FSLROI
from .susan import SUSAN
