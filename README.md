# pydra-fsl

[![PyPI - Version][pypi-version]][pypi-project]
[![PyPI - Python Version][pypi-pyversions]][pypi-project]
![][status-docs]
![][status-test]

----

Pydra tasks for FSL designed for Clinica.

[Pydra][pydra] is a dataflow engine which provides
a set of lightweight abstractions for DAG
construction, manipulation, and distributed execution.

[FSL][fsl] is a comprehensive library of analysis tools
for FMRI, MRI and DTI brain imaging data.

## Available tasks

| Module | Tasks                                                                                                              |
|--------|--------------------------------------------------------------------------------------------------------------------|
| bet    | BET, RobustFOV                                                                                                     |
| eddy   | Eddy, ApplyTopup, Topup                                                                                            |
| fast   | FAST                                                                                                               |
| flirt  | FLIRT, ApplyXFM, ConcatXFM, ConvertXFM, InvertXFM, FixScaleSkew, Img2ImgCoord, Img2StdCoord, Std2ImgCoord          |
| fnirt  | FNIRT, FNIRTFileUtils, ApplyWarp, ConvertWarp, InvWarp                                                             |
| fugue  | FUGUE, PrepareFieldmap, Prelude, SigLoss                                                                           |
| maths  | (**experimental**) Maths, Mul                                                                                      |
| susan  | SUSAN                                                                                                              |
| utils  | ChFileType, FFT, Info, Interleave, Merge, Orient, Reorient2Std, ROI, SelectVols, Slice, SmoothFill, Split, SwapDim |

## Installation

```console
pip install clinica-pydra-fsl
```

A separate installation of FSL is required to use this package.
Please review the FSL [installation instructions][fsl-install]
and [licensing details][fsl-license].

## Development

This project is managed with [Hatch][hatch]:

```console
pipx install hatch
```

To run the test suite:

```console
hatch run test
```

To fix linting issues:

```console
hatch fmt
```

## License

This project is distributed under the terms of the [Apache License, Version 2.0][license].

[pypi-project]: https://pypi.org/project/clinica-pydra-fsl

[pypi-version]: https://img.shields.io/pypi/v/clinica-pydra-fsl.svg

[pypi-pyversions]: https://img.shields.io/pypi/pyversions/clinica-pydra-fsl.svg

[status-docs]: https://github.com/aramis-lab/clinica-pydra-fsl/actions/workflows/docs.yaml/badge.svg

[status-test]: https://github.com/aramis-lab/clinica-pydra-fsl/actions/workflows/test.yaml/badge.svg

[pydra]: https://pydra.readthedocs.io/

[fsl]: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSL

[fsl-install]: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation

[fsl-license]: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Licence

[hatch]: https://hatch.pypa.io/

[license]: https://spdx.org/licenses/Apache-2.0.html
