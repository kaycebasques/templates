# sphinx/theme/bazel

## Running Sphinx Directly

You can run the Sphinx binary directly for debugging or faster iteration:

```bash
./bazel-bin/docs/sphinx \
  bazel-out/k8-fastbuild/bin/docs/_docs/_sources \
  bazel-out/k8-fastbuild/bin/docs/docs/_build/html \
  --builder=html \
  --show-traceback \
  --jobs=auto \
  --doctree-dir=bazel-out/k8-fastbuild/bin/docs/docs/_build/html_doctrees \
  --fail-on-warning
```

## Packaging and Publishing to PyPI

This project is configured to build a Python wheel for distribution on PyPI.

### 1. Build the Wheel

To build the wheel package:

```bash
./bazelisk/linux/amd64 build //theme:wheel
```

The generated wheel will be located at:
`bazel-bin/theme/sphinx_theme_bazel-[version]-py3-none-any.whl`

### 2. Publish to PyPI

You can use `twine` to upload the built wheel to PyPI:

```bash
pip install twine
twine upload bazel-bin/theme/sphinx_theme_bazel-*.whl
```

Before publishing, ensure you update the `version` and `distribution` (package name) in the `py_wheel` target in [theme/BUILD.bazel](file:///usr/local/google/home/kayce/templates/sphinx/theme/bazel/theme/BUILD.bazel).
