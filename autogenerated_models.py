from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)
    trial199 = models.CharField(db_column='TRIAL199', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
    trial199 = models.CharField(db_column='TRIAL199', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    trial199 = models.CharField(db_column='TRIAL199', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.TextField()  # This field type is a guess.
    object_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()  # This field type is a guess.
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)
    trial199 = models.CharField(db_column='TRIAL199', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    trial199 = models.CharField(db_column='TRIAL199', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.TextField()  # This field type is a guess.
    trial199 = models.CharField(db_column='TRIAL199', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()  # This field type is a guess.
    expire_date = models.TextField()  # This field type is a guess.
    trial203 = models.CharField(db_column='TRIAL203', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'django_session'


class PublicationsChapterlike(models.Model):
    date_time = models.DateField()
    from_user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)
    to_chapter = models.ForeignKey('PublicationsStorychapter', models.DO_NOTHING)
    trial203 = models.CharField(db_column='TRIAL203', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publications_chapterlike'


class PublicationsResourcepublication(models.Model):
    user_name = models.CharField(max_length=45)
    user_lastname = models.CharField(max_length=45)
    text_content = models.TextField()  # This field type is a guess.
    img_content_link = models.CharField(max_length=500)
    privacity = models.IntegerField()
    date_time = models.DateField()
    views = models.IntegerField()
    own_user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)
    active = models.BooleanField()
    title = models.CharField(max_length=500)
    valoration = models.IntegerField()
    trial203 = models.CharField(db_column='TRIAL203', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publications_resourcepublication'


class PublicationsResourcepublicationTag(models.Model):
    resourcepublication = models.ForeignKey(PublicationsResourcepublication, models.DO_NOTHING)
    tag = models.ForeignKey('PublicationsTag', models.DO_NOTHING)
    trial203 = models.CharField(db_column='TRIAL203', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publications_resourcepublication_tag'
        unique_together = (('resourcepublication', 'tag'),)


class PublicationsStorychapter(models.Model):
    text_content = models.TextField()  # This field type is a guess.
    active = models.BooleanField()
    date_time = models.DateField()
    views = models.IntegerField()
    valoration = models.IntegerField()
    quest_answ = models.CharField(max_length=100)
    mainstory = models.ForeignKey('PublicationsStorypublication', models.DO_NOTHING, db_column='mainStory_id')  # Field name made lowercase.
    own_user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)
    prevchapter = models.ForeignKey('self', models.DO_NOTHING, db_column='prevChapter_id', blank=True, null=True)  # Field name made lowercase.
    trial203 = models.CharField(db_column='TRIAL203', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publications_storychapter'


class PublicationsStorychapterTag(models.Model):
    storychapter = models.ForeignKey(PublicationsStorychapter, models.DO_NOTHING)
    tag = models.ForeignKey('PublicationsTag', models.DO_NOTHING)
    trial203 = models.CharField(db_column='TRIAL203', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publications_storychapter_tag'
        unique_together = (('storychapter', 'tag'),)


class PublicationsStorylike(models.Model):
    date_time = models.DateField()
    from_user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)
    to_story = models.ForeignKey('PublicationsStorypublication', models.DO_NOTHING)
    trial203 = models.CharField(db_column='TRIAL203', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publications_storylike'


class PublicationsStorypublication(models.Model):
    text_content = models.TextField()  # This field type is a guess.
    img_content_link = models.CharField(max_length=100)
    date_time = models.DateField()
    views = models.IntegerField()
    valoration = models.IntegerField()
    own_user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)
    active = models.BooleanField()
    title = models.CharField(max_length=120)
    color = models.CharField(max_length=7)
    status = models.CharField(max_length=2)
    trial203 = models.CharField(db_column='TRIAL203', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publications_storypublication'


class PublicationsStorypublicationTag(models.Model):
    storypublication = models.ForeignKey(PublicationsStorypublication, models.DO_NOTHING)
    tag = models.ForeignKey('PublicationsTag', models.DO_NOTHING)
    trial203 = models.CharField(db_column='TRIAL203', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publications_storypublication_tag'
        unique_together = (('storypublication', 'tag'),)


class PublicationsTag(models.Model):
    tag = models.CharField(max_length=80)
    creation_date_time = models.DateField()
    trial203 = models.CharField(db_column='TRIAL203', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publications_tag'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)
    trial203 = models.CharField(db_column='TRIAL203', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    timestamp = models.TextField()  # This field type is a guess.
    trial206 = models.CharField(db_column='TRIAL206', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)
    trial206 = models.CharField(db_column='TRIAL206', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.SmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.TextField()  # This field type is a guess.
    trial206 = models.CharField(db_column='TRIAL206', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)
    trial206 = models.CharField(db_column='TRIAL206', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class UsersCustomuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=35)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.BooleanField()
    date_joined = models.TextField()  # This field type is a guess.
    is_active = models.BooleanField()
    email_verified = models.BooleanField()
    trial206 = models.CharField(db_column='TRIAL206', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_customuser'


class UsersCustomuserGroups(models.Model):
    customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    trial206 = models.CharField(db_column='TRIAL206', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_customuser_groups'
        unique_together = (('customuser', 'group'),)


class UsersCustomuserUserPermissions(models.Model):
    customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
    trial206 = models.CharField(db_column='TRIAL206', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class UsersPubsubscriptionmodelaux(models.Model):
    date_time = models.DateField()
    pub = models.ForeignKey(PublicationsStorypublication, models.DO_NOTHING)
    user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)
    trial206 = models.CharField(db_column='TRIAL206', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_pubsubscriptionmodelaux'


class UsersUserevents(models.Model):
    date_time = models.DateField()
    event_type = models.CharField(max_length=5)
    id_publication = models.IntegerField()
    user = models.ForeignKey('UsersUserprofile', models.DO_NOTHING)
    trial206 = models.CharField(db_column='TRIAL206', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_userevents'


class UsersUserprofile(models.Model):
    link_img_perfil = models.CharField(max_length=350)
    description = models.CharField(max_length=150)
    user = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    is_reported = models.BooleanField()
    trial206 = models.CharField(db_column='TRIAL206', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_userprofile'


class UsersUsersubscriptionmodelaux(models.Model):
    date_time = models.DateField()
    from_user = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)
    to_user = models.ForeignKey(UsersUserprofile, models.DO_NOTHING)
    trial206 = models.CharField(db_column='TRIAL206', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_usersubscriptionmodelaux'