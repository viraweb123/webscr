import pytest

from webscr.pipelines.content import ContentPipeline

__author__ = "maso"
__copyright__ = "maso"
__license__ = "MIT"


def test_instance():
    a = ContentPipeline()
    assert a is not None
    assert hasattr(a, 'process_item')
