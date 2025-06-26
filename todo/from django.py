from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from .models import Task

# python

class TestTaskIsOverdueNone(TestCase):
    def test_is_overdue_none(self):
        # 締め切りなしのタスクを作成
        task = Task(title='no due')
        task.save()
        # 2024/7/1 0:00:00のawareなdatetime
        current = timezone.make_aware(datetime(2024, 7, 1, 0, 0, 0))
        # is_overdueがFalseを返すことを検証
        self.assertFalse(task.is_overdue(current))