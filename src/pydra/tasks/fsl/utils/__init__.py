"""
Utils
=====

.. automodule:: pydra.tasks.fsl.utils.fslchfiletype
.. automodule:: pydra.tasks.fsl.utils.fslfft
.. automodule:: pydra.tasks.fsl.utils.fslinfo
.. automodule:: pydra.tasks.fsl.utils.fslinterleave
.. automodule:: pydra.tasks.fsl.utils.fslmerge
.. automodule:: pydra.tasks.fsl.utils.fslorient
.. automodule:: pydra.tasks.fsl.utils.fslreorient2std
.. automodule:: pydra.tasks.fsl.utils.fslroi
.. automodule:: pydra.tasks.fsl.utils.fslselectvols
.. automodule:: pydra.tasks.fsl.utils.smoothfill
.. automodule:: pydra.tasks.fsl.utils.split
.. automodule:: pydra.tasks.fsl.utils.swapdim
"""

from .fslchfiletype import FSLChFileType
from .fslfft import FSLFFT
from .fslinfo import FSLInfo
from .fslinterleave import FSLInterleave
from .fslmerge import FSLMerge
from .fslorient import FSLOrient
from .fslreorient2std import FSLReorient2Std
from .fslroi import FSLROI
from .fslselectvols import FSLSelectVols
from .smoothfill import SmoothFill
from .split import Slice, Split
from .swapdim import SwapDim
