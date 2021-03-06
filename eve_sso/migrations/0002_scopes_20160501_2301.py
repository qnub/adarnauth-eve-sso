# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-01 23:01
from __future__ import unicode_literals

from django.db import migrations

SCOPES = {
    'characterAccountRead': 'Read your account subscription status.',
    'characterAssetsRead': 'Read your assets list.',
    'characterBookmarksRead': 'List your bookmarks and their coordinates.',
    'characterCalendarRead': 'Read your calendar events and attendees.',
    'characterChatChannelsRead': 'List chat channels you own or operate.',
    'characterClonesRead': 'List your jump clones, implants, attributes, and jump fatigure timer.',
    'characterContactsRead': "Allows access to reading your character's contacts.",
    'characterContactsWrite': 'Allows applications to add, modify, and delete contacts for your character.',
    'characterContractsRead': 'Read your contracts',
    'characterFactionalWarfareRead': 'Read your factional warfare statistics.',
    'characterFittingsRead': "Allows an application to view all of your character's saved fits.",
    'characterFittingsWrite': "Allows an application to create and delete the saved fits for your character.",
    'characterIndustryJobsRead': 'List your industry jobs.',
    'characterKillsRead': 'Read your kill mails.',
    'characterLocationRead': "Allows an application to read your character's real-time location in EVE.",
    'characterLoyaltyPointsRead': 'List loyalty points your character has for the different corporations.',
    'characterMailRead': 'Read your EVE Mail.',
    'characterMarketOrdersRead': 'Read your market orders.',
    'characterMedalsRead': 'List your public and private medals.',
    'characterNavigationWrite': "Allows an application to set your ship's autopilot destination.",
    'characterNotificationsRead': 'Receive in-game notifications.',
    'characterOpportunitiesRead': 'List the opportunities your character has completed.',
    'characterResearchRead': 'List your research agents working for you and research progress.',
    'characterSkillsRead': 'Read your skills and skill queue.',
    'characterStatsRead': 'Yearly aggregated stats about your character.',
    'characterWalletRead': 'Read your wallet status, transaction, and journal history.',
    'corporationAssetRead': "Read your corporation's asset list.",
    'corporationBookmarksRead': "List your corporation's bookmarks and their coordinates.",
    'corporationContractsRead': "List your corporation's contracts.",
    'corporationFactionalWarfareRead': "List your corporation's factional warfare statistics.",
    'corporationIndustryJobsRead': "List your corporation's industry jobs.",
    'corporationKillsRead': "Read your corporation's kill mails.",
    'corporationMarketOrdersRead': "List your corporation's market orders.",
    'corporationMedalsRead': "List your corporation's issued medals.",
    'corporationMembersRead': "List your corporation's members, their titles, and roles.",
    'corporationShareholdersRead': "List your corporation's shareholders and their shares.",
    'corporationStructuresRead': "List your corporation's structures, outposts, and starbases.",
    'corporationWalletRead': "Read your corporation's wallet status, transaction, and journal history.",
    'fleetRead': "Allows real time reading of your fleet information (members, ship types, etc.) if you're the boss of the fleet.",
    'fleetWrite': "Allows the ability to invite, kick, and update fleet information if you're the boss of the fleet.",
    'publicData': 'Allows access to public data.',
    'structureVulnUpdate': "Allows updating your structures' vulnerability timers.",
    }

def generate_scopes(apps, schema_editor):
    Scope = apps.get_model('eve_sso', 'Scope')
    for s in SCOPES:
        model, c = Scope.objects.update_or_create(name=s, defaults={'help_text':SCOPES[s]})

def delete_scopes(apps, schema_editor):
    Scope = apps.get_model('eve_sso', 'Scope')
    for s in SCOPES:
        try:
            Scope.objects.get(name=s).delete()
        except:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ('eve_sso', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_scopes, delete_scopes)
    ]
