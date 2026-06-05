# sphinx/theme/bazel

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
