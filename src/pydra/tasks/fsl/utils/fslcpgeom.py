"""
FSLCpGeom
=========

Copy geometry metadata from one image to another.

Examples
--------

>>> task = FSLCpGeom(source_image="source.nii", destination_image="target.nii")
>>> task.cmdline
'fslcpgeom source.nii target.nii'
"""

__all__ = ["FSLCpGeom"]

from attrs import define, field
from pydra.engine import ShellCommandTask
from pydra.engine.specs import File, ShellOutSpec, ShellSpec, SpecInfo


@define(slots=False, kw_only=True)
class FSLCpGeomSpec(ShellSpec):
    """Specifications for fslcpgeom."""

    source_image: File = field(metadata={"help_string": "source image", "mandatory": True, "argstr": ""})

    # fslcpgeom operates inplace, hence the necessity to copy first.
    destination_image: File = field(
        metadata={"help_string": "destination image", "mandatory": True, "argstr": "", "copyfile": True}
    )


@define(slots=False, kw_only=True)
class FSLCpGeomOutSpec(ShellOutSpec):
    """Output specifications for fslcpgeom."""

    destination_image: File = field(
        metadata={"help_string": "destination image", "output_file_template": "{destination_image}"}
    )


class FSLCpGeom(ShellCommandTask):
    """Task definition for fslcpgeom."""

    executable = "fslcpgeom"

    input_spec = SpecInfo(name="Inputs", bases=(FSLCpGeomSpec,))

    output_spec = SpecInfo(name="Outputs", bases=(FSLCpGeomOutSpec,))
