from django.db import models

# Create your models here.
class Post(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        (STATUS_DRAFT, "下書き"),
        (STATUS_PUBLIC, "公開"),
    )
    AUTHOR_JIRO = "jiro"
    AUTHOR_SET = (
        (AUTHOR_JIRO, "Jiro"),
    )

    title = models.CharField("タイトル", max_length=100)
    image = models.ImageField("画像", upload_to="uploads/", null=True, blank=True)
    content = models.TextField("本文", blank=True, null=True)
    author = models.CharField("著者", choices=AUTHOR_SET, default=AUTHOR_JIRO, max_length=10)
    status = models.CharField("公開", choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)

    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title