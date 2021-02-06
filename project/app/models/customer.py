from tortoise import fields, models


class Customer(models.Model):
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)
    uuid = fields.UUIDField(index=True, unique=True)
    cpf = fields.CharField(max_length=11, index=True, unique=True)
    birth_date = fields.DateField()
    email = fields.TextField()
    phone = fields.CharField(max_length=30)
    salary = fields.DecimalField(14, 2)

    def __str__(self):
        return self.uuid
