from wagtail.api.v2.serializers import StreamField


class OptionalStreamField(StreamField):
    """
    This serializer is necessary due to a bug in the wagtail API.
    The only change is that it catches the case of an empty StreamField,
    which would produce an error instead.
    It sould be used everywhere a StreamField has blank=True.
    See https://github.com/wagtail/wagtail/issues/3641.
    """

    def to_representation(self, value):
        return value.stream_block.get_api_representation(value, self.context) if value else None
