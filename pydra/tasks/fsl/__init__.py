"""Pydra tasks for FSL.

>>> from pydra.tasks import fsl
"""

from .flirt import FLIRT
from .fslmerge import FSLMerge

__all__ = [
    "FLIRT",
    "FSLMerge",
]
