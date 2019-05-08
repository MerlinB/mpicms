import pytest
from wagtail.core.models import Page


@pytest.mark.django_db
def test_data_migrations():
    root_page = Page.objects.first()
    assert root_page.title