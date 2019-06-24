from django.utils.translation import gettext_lazy as _

from wagtail.core import blocks
from wagtail.contrib.table_block.blocks import TableBlock


class MarkdownBlock(blocks.TextBlock):
    class Meta:  # noqa
        template = 'base/blocks/markdown_block.html'


class ContentBlock(blocks.StreamBlock):
    richtext = blocks.RichTextBlock(label=_('Editor'))
    markdown = MarkdownBlock(label=_('Raw Markdown'))
    table = TableBlock(label=_('Table'))
