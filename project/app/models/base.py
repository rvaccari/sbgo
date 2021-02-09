from tortoise import models, fields


class BaseModel(models.Model):
    """Default tortoise model."""

    id = fields.UUIDField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        """Base model meta"""

        abstract = True
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return self.id
