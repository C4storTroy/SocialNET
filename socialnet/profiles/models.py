from django.db import models
from django.contrib.auth.models import User

'''Class to create a Profile and save in a table on DB'''
class Profile(models.Model):

    name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=15, null=False)
    company = models.CharField(max_length=255, null=False)
    contacts = models.ManyToManyField('self')
    user = models.OneToOneField(User, related_name="profile")

    @property
    def email(self):
        return self.user.email

    def invite(self, profile_invited):
        Invite(requester=self, invited=profile_invited).save()

class Invite(models.Model):
    requester = models.ForeignKey(Profile, related_name='done_invites')
    invited = models.ForeignKey(Profile, related_name='received_invites')

    def accept(self):
        self.invited.contacts.add(self.requester)
        self.requester.contacts.add(self.invited)
        self.delete()