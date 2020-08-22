from django.db import migrations

from guardian.shortcuts import assign_perm
from guardian.compat import get_user_model, Group

PERMISSION_NAME = 'can_view_results'
PERMISSION_FULL_NAME = f'survey.{PERMISSION_NAME}'

def make_can_view_survey_results_perm(apps, schema_editor):
    Survey = apps.get_model('survey', 'Survey')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Permission = apps.get_model('auth', 'Permission')
    content_type = ContentType.objects.get_for_model(Survey)
    permission = Permission.objects.create(
      codename=PERMISSION_NAME,
      name='Can view survey results',
      content_type=content_type
    )

def assign_can_view_survey_results_perms(apps, schema_editor):
    User = get_user_model()
    Survey = apps.get_model('survey', 'Survey')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Permission = apps.get_model('auth', 'Permission')
    surveys = Survey.objects.all()
    for survey in surveys:
        group_name = f"survey_{survey.id}_result_viewers"
        group = Group.objects.create(name=group_name)
        assign_perm(PERMISSION_FULL_NAME, group, survey)
        creator = User.objects.get(pk=survey.created_by.id)
        creator.groups.add(group)
        creator.save()

class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20200816_1121'),
    ]

    operations = [
      migrations.RunPython(make_can_view_survey_results_perm),
      migrations.RunPython(assign_can_view_survey_results_perms)
    ]