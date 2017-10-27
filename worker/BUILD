load(
   "@io_bazel_rules_docker//python:image.bzl",
   "py_image"
)
load(
  "@io_bazel_rules_python//python:python.bzl",
  "py_binary", "py_library", "py_test",
)
load(
  "@worker_packages//:requirements.bzl",
  "requirement"
)
load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_image",
)


container_image(
    name = "worker_image",
    base = "@tensorflow_image//image",
    files = ["configs/config.json"],

)

py_image(
    name = "worker",
    base = ":worker_image",
    srcs = ["main.py"],
    default_python_version = "PY3",
    deps = [
	    requirement("zeroconf"),
    ],
    main = "main.py",
)
