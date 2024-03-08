"""
Eddy
====

.. automodule:: pydra.tasks.fsl.eddy.eddy
.. automodule:: pydra.tasks.fsl.eddy.topup
.. automodule:: pydra.tasks.fsl.eddy.applytopup
"""

from pydra.tasks.fsl.eddy.applytopup import ApplyTopup
from pydra.tasks.fsl.eddy.eddy import Eddy
from pydra.tasks.fsl.eddy.topup import Topup

__all__ = ["ApplyTopup", "Eddy", "Topup"]
