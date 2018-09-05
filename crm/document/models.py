from django.db import models

STATUS = (
    ('1', 'На подписи'),
    ('2', 'Есть подписанный оригинал'),
    ('3', 'Подписанный скан'),
)


class CatalogDocuments(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Наименование документа')
    description = models.CharField(max_length=300, verbose_name='Описание')

    class Meta:
        verbose_name = 'Наименование документа'
        verbose_name_plural = 'Наименования документов'

    def __str__(self):
        return self.name


class Document(models.Model):
    catalog_documents = models.ForeignKey(
        CatalogDocuments, blank=True,
        null=True, related_name='catalog_documents',
        on_delete=models.PROTECT, verbose_name='Документ')

    status = models.CharField(
        max_length=1, choices=STATUS,
        default='1', verbose_name='Статус')

    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.catalog_documents.name
