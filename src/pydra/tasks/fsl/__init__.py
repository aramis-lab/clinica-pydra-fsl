"""Pydra tasks for FSL.

FSL interfaces are available within the `pydra.tasks.fsl` package.

>>> from pydra.tasks import fsl

.. automodule:: pydra.tasks.fsl.bet
.. automodule:: pydra.tasks.fsl.eddy
.. automodule:: pydra.tasks.fsl.fast
.. automodule:: pydra.tasks.fsl.flirt
.. automodule:: pydra.tasks.fsl.fnirt
.. automodule:: pydra.tasks.fsl.fslmaths
.. automodule:: pydra.tasks.fsl.fugue
.. automodule:: pydra.tasks.fsl.susan
.. automodule:: pydra.tasks.fsl.utils
"""

from . import fslmaths
from .bet import BET, RobustFOV
from .eddy import ApplyTopup, Eddy, Topup
from .fast import FAST
from .flirt import (
    FLIRT,
    ApplyXFM,
    ConcatXFM,
    ConvertXFM,
    FixScaleSkew,
    Img2ImgCoord,
    Img2StdCoord,
    InvertXFM,
    Std2ImgCoord,
)
from .fnirt import FNIRT, ApplyWarp, ConvertWarp, FNIRTFileUtils, InvWarp
from .fugue import FUGUE, FSLPrepareFieldmap, Prelude, SigLoss
from .susan import SUSAN
from .utils import (
    FSLFFT,
    ROI,
    FSLChFileType,
    FSLInfo,
    FSLInterleave,
    Merge,
    Orient,
    Reorient2Std,
    SelectVols,
    Slice,
    SmoothFill,
    Split,
    SwapDim,
)

# TODO: Drop compatibility aliases when 0.x is released.
FSLROI = ROI
FSLMerge = Merge
FSLOrient = Orient
FSLReorient2Std = Reorient2Std
FSLSelectVols = SelectVols
FSLSlice = Slice
FSLSmoothFill = SmoothFill
FSLSplit = Split
FSLSwapDim = SwapDim
