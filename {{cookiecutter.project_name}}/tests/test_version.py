"""Test the version of the package."""
import {{cookiecutter.package_name}}


def test_glue_version() -> None:
    """Test that the glue version is correct."""
    assert {{cookiecutter.package_name}}.__version__ == "0.1.0"
