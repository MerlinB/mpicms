from django.utils.translation import gettext_lazy as _

from wagtail.core import blocks
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock as WagtailTableBlock


class ContactBlock(blocks.StructBlock):
    contact = SnippetChooserBlock('personal.Contact', label=_("Contact"))
    information = blocks.TextBlock(required=False, label=_('Information'))

    class Meta:  # noqa
        icon="user"
        template='base/blocks/contact_block.html'

class MarkdownBlock(blocks.TextBlock):
    class Meta:  # noqa
        template = 'base/blocks/markdown_block.html'

class TableBlock(WagtailTableBlock):
    class Meta:  # noqa
        template = 'base/blocks/table_block.html'


class ContentBlock(blocks.StreamBlock):
    richtext = blocks.RichTextBlock(label=_('Editor'))
    markdown = MarkdownBlock(label=_('Raw Markdown'))
    table = TableBlock(label=_('Table'))
    contact = ContactBlock(label=_('Contact'))

    class Meta:  # noqa
        label = _('content')
