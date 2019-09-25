# import pytest

# from .models import Contact, Group, ContactGroups


# DEPRECATED: Priority no longer used for contact ordering.
# @pytest.mark.django_db
# def test_contact_ordering():
#     g1 = Group.objects.create(name="G1", priority="1")
#     g2 = Group.objects.create(name="G2", priority="2")
#     g3 = Group.objects.create(name="G3", priority="3")

#     a = Contact.objects.create(last_name="A", priority="4")
#     b = Contact.objects.create(last_name="B", priority="3")
#     c = Contact.objects.create(last_name="C", priority="2")
#     d = Contact.objects.create(last_name="D", priority="1")

#     ContactGroups.objects.bulk_create([
#         ContactGroups(group=g1, contact=a),
#         ContactGroups(group=g2, contact=b),
#         ContactGroups(group=g3, contact=c),
#         ContactGroups(group=g3, contact=d),
#     ])

#     assert list(Contact.objects.all()) == [c, d, b, a]
