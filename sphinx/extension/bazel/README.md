# sphinx/extension/bazel

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

## Running Tests

This project uses Bazel for running tests. A wrapper for `bazelisk` is provided in the repository.

### Run All Tests

To run all tests in the repository:

```bash
./bazelisk test //...
```

### Run a Specific Test Target

To run a specific test, such as `test_runtime`:

```bash
./bazelisk test //tests:test_runtime
```

### Inspecting Test Output

When a test fails, Bazel will print a summary and point to the log file.

*   **Test Logs**: Detailed logs for each test run are stored in the `bazel-testlogs` directory. For example, the log for `test_runtime` can be found at:
    `bazel-testlogs/tests/test_runtime/test.log`
    This is a symlink to the actual log file in the Bazel execution root.

### Verbose Output and Debugging

By default, Bazel may suppress test output unless the test fails. You can control this behavior with the `--test_output` flag:

*   **Show all output (even for passing tests)**:
    ```bash
    ./bazelisk test //tests:test_runtime --test_output=all
    ```
*   **Stream output in real-time**: Useful for debugging hung tests.
    ```bash
    ./bazelisk test //tests:test_runtime --test_output=streamed
    ```
*   **Force rerun tests (bypass cache)**: Bazel caches successful test results. To force a rerun:
    ```bash
    ./bazelisk test //tests:test_runtime --nocache_test_results
    ```

---

## FAQ: `bazelisk test` vs `bazelisk run`

What is the difference between `./bazelisk test //tests:test_runtime` and `./bazelisk run //tests:test_runtime`?

*   **`test` command**:
    *   Runs the test inside a **sandbox** environment.
    *   **Caches** the results. If the test code and its inputs haven't changed, subsequent runs will be instant and display `(cached) PASSED`.
    *   Redirects stdout/stderr to log files (e.g., `bazel-testlogs/.../test.log`).
    *   Enforces test timeouts and limits.
    *   Designed for CI and automated test suites.

*   **`run` command**:
    *   Builds the test and then **executes it directly** on your host machine, bypassing the sandbox.
    *   **Never caches** the execution. It will run the test every time.
    *   Streams stdout/stderr directly to your terminal.
    *   Allows interactive debugging (e.g., if you insert `breakpoint()` in your Python code, you can interact with it).
    *   Useful for local development and debugging.

---

## Packaging and Publishing to PyPI

This project is configured to build a Python wheel for distribution on PyPI.

### 1. Build the Wheel

To build the wheel package:

```bash
./bazelisk build //src:wheel
```

The generated wheel will be located at:
`bazel-bin/src/extension-[version]-py3-none-any.whl`

### 2. Publish to PyPI

You can use `twine` to upload the built wheel to PyPI:

```bash
pip install twine
twine upload bazel-bin/src/extension-*.whl
```

Before publishing, ensure you update the `version` and `distribution` (package name) in the `py_wheel` target in [src/BUILD.bazel](file:///usr/local/google/home/kayce/k/templates/sphinx/extension/bazel/src/BUILD.bazel).
