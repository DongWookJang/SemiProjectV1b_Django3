from datetime import datetime
from django.db import models

# Create your models here.
# on_delete : CASCADE, DO_NOTHING

from member.models import Member


class Board(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    userid=models.ForeignKey(Member, db_column='userid',
                                on_delete=models.CASCADE)
    regdate=models.DateTimeField(default=datetime.now)
    views=models.IntegerField(default=0)
    contents=models.TextField(null=False, blank=False)

    class Meta:
        db_table = 'board'     # 생성할 테이블 이름 지정
        ordering = ['-regdate'] # 정렬기준 지정 최근가입일부터 정렬

    def __str__(self):
        return self.title     # 객체 출력시 출력형태 정의