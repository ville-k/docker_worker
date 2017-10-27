git_repository(
    name = "io_bazel_rules_docker",
    remote = "https://github.com/bazelbuild/rules_docker.git",
    tag = "v0.3.0",
)

git_repository(
    name = "io_bazel_rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "c208292d1286e9a0280555187caf66cd3b4f5bed",
)

# Only needed for PIP support:
load(
    "@io_bazel_rules_python//python:pip.bzl",
    "pip_repositories",
    "pip_import"
)

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
    container_repositories = "repositories",
)

load(
    "@io_bazel_rules_docker//python:image.bzl",
    _py_image_repos = "repositories",
)


container_pull(
    name = "tensorflow_image",
    registry = "index.docker.io",
    repository = "tensorflow/tensorflow",
    tag = "1.3.0-py3",
)
container_repositories()


_py_image_repos()
pip_repositories()


pip_import(
   name = "worker_packages",
   requirements = "//worker:requirements.txt",
)
load("@worker_packages//:requirements.bzl", "pip_install")
pip_install()