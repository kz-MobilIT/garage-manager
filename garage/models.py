from django.db import models

class Customer(models.Model):
    name = models.CharField('顧客名', max_length=100)
    phone = models.CharField('電話番号', max_length=20)
    email = models.EmailField('メールアドレス', blank=True)
    address = models.CharField('住所', max_length=255, blank=True)
    note = models.TextField('メモ', blank=True, null=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name='顧客')
    name = models.CharField('車名', max_length=100)
    plate_number = models.CharField('ナンバー', max_length=20)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.plate_number}) "
    
class Reservation(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "保留"
        CONFIRMED = "confirmed", "予約確定"
        IN_PROGRESS = "in_progress", "作業中"
        COMPLETED = "completed", "完了"
        CANCELED = "canceled", "キャンセル"

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField()
    menu = models.CharField(max_length=200, default="未設定")
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    def __str__(self):
        return f"{self.customer.name} - {self.vehicle.name} ({self.date} {self.time})"
    