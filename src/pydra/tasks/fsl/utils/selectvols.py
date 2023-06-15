"""
SelectVols
==========

Examples
--------

Select volumes from a list and concatenate them:

>>> task = SelectVols(input_image="input.nii", volumes=[0, 1, 6, 7])
>>> task.cmdline
'fslselectvols --in input.nii --out .../input_selectvols.nii --vols 0,1,6,7'

Select volumes from a file and calculate their mean:

>>> task = SelectVols(
...     input_image="input.nii",
...     output_image="mean.nii",
...     volumes="volumes.txt",
...     calculate_mean=True,
... )
>>> task.cmdline
'fslselectvols --in input.nii --out mean.nii --vols volumes.txt -m'

Select volumes from a file and calculate their variance:

>>> task = SelectVols(
...     input_image="input.nii",
...     output_image="variance.nii",
...     volumes="volumes.txt",
...     calculate_variance=True,
... )
>>> task.cmdline
'fslselectvols --in input.nii --out variance.nii --vols volumes.txt -v'
"""

__all__ = ["SelectVols"]

import os
import typing as ty

import attrs

import pydra


@attrs.define(slots=False, kw_only=True)
class SelectVolsSpec(pydra.specs.ShellSpec):
    """Specifications for fslselectvols."""

    input_image: os.PathLike = attrs.field(metadata={"help_string": "input image", "mandatory": True, "argstr": "--in"})

    output_image: str = attrs.field(
        metadata={"help_string": "output image", "argstr": "--out", "output_file_template": "{input_image}_selectvols"}
    )

    volumes: ty.Union[os.PathLike, ty.Iterable[int]] = attrs.field(
        metadata={
            "help_string": "volumes to select (from a file or as a list)",
            "mandatory": True,
            "formatter": lambda field: (
                f"--vols {str(field) if isinstance(field, (os.PathLike, str)) else ','.join(map(str, field))}"
            ),
        }
    )

    calculate_mean: bool = attrs.field(
        metadata={
            "help_string": "calculate mean instead of concatenating",
            "argstr": "-m",
            "xor": {"calculate_variance"},
        }
    )

    calculate_variance: bool = attrs.field(
        metadata={
            "help_string": "calculate variance instead of concatenating",
            "argstr": "-v",
            "xor": {"calculate_mean"},
        }
    )


class SelectVols(pydra.engine.ShellCommandTask):
    """Task definition for fslselectvols."""

    executable = "fslselectvols"

    input_spec = pydra.specs.SpecInfo(name="Input", bases=(SelectVolsSpec,))
