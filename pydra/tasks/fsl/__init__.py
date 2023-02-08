"""Pydra tasks for FSL.

>>> from pydra.tasks import fsl
"""

from .bet import BET
from .flirt import FLIRT
from .fnirt import FNIRT
from .fslmerge import FSLMerge

__all__ = [
    "BET",
    "FLIRT",
    "FNIRT",
    "FSLMerge",
]
