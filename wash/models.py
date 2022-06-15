from django.db import models

class Service(models.Model):
    title = models.CharField("Услуга", max_length=100)
    description = models.CharField("Описание", max_length=100)
    coast = models.PositiveIntegerField("Цена")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Order(models.Model):
    TIME = (
        ('08:00', '08:00'),
        ('10:00', '10:00'),
        ('13:00', '13:00'),
        ('15:00', '15:00'),
        ('17:00', '17:00'),
        ('19:00', '19:00'),
    )

    title = models.ForeignKey(Service, verbose_name="Заказ", on_delete=models.CASCADE)
    street = models.CharField("Улица", max_length=30)
    build = models.CharField("Дом", max_length=30)
    home = models.CharField("Квартира", max_length=5, blank=True, null=True)
    time = models.CharField("Время визита", choices=TIME, max_length=6)
    phone = models.CharField("Телефон", max_length=12)
    
    def __str__(self):
        return f'{self.title} - {self.street}: {self.build}/{self.home}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"