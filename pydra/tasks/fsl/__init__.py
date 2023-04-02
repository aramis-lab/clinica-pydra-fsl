"""Pydra tasks for FSL.

>>> from pydra.tasks import fsl
"""

from .bet import BET, RobustFOV
from .eddy import Eddy
from .fast import FAST
from .flirt import FLIRT, ApplyXFM, ConcatXFM, ConvertXFM, InvertXFM
from .fnirt import FNIRT, ApplyWarp, ConvertWarp, InvWarp
from .susan import SUSAN
from .utils import (FSLROI, FSLInfo, FSLMerge, FSLReorient2Std, FSLSplit,
                    fslmaths)
