from django.db import models


# Soldier Model
class Soldier(models.Model):
    RANK_CHOICES = [
        ('General', 'General'),
        ('Colonel', 'Colonel'),
        ('Major', 'Major'),
        ('Captain', 'Captain'),
        ('Lieutenant', 'Lieutenant'),
        ('Soldier', 'Soldier'),
    ]

    STATUS_CHOICES = [
        ('On Duty', 'On Duty'),
        ('Leave', 'Leave'),
    ]

    soldier_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    rank = models.CharField(max_length=20, choices=RANK_CHOICES)
    posting = models.CharField(max_length=100, blank=True)
    blood_group = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    photo = models.ImageField(upload_to='soldiers/', blank=True, null=True)

    def save(self, *args, **kwargs):
        posting_map = {
            'General': 'Headquarters',
            'Colonel': 'Division Office',
            'Major': 'Battalion HQ',
            'Captain': 'Border Post',
            'Lieutenant': 'Patrol Unit',
            'Soldier': 'Check Post',
        }
        self.posting = posting_map.get(self.rank, '')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Patrol Route Model
class PatrolRoute(models.Model):
    route_name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.route_name