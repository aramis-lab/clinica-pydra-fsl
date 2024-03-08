"""
FUGUE
=====

.. automodule:: pydra.tasks.fsl.fugue.fugue
.. automodule:: pydra.tasks.fsl.fugue.prepare_fieldmap
.. automodule:: pydra.tasks.fsl.fugue.prelude
.. automodule:: pydra.tasks.fsl.fugue.sigloss
"""

from pydra.tasks.fsl.fugue.fugue import FUGUE
from pydra.tasks.fsl.fugue.prelude import Prelude
from pydra.tasks.fsl.fugue.prepare_fieldmap import PrepareFieldmap
from pydra.tasks.fsl.fugue.sigloss import SigLoss

__all__ = ["FUGUE", "PrepareFieldmap", "Prelude", "SigLoss"]
