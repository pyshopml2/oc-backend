from django.db import models

STATUS = (
    ('НП', 'На подписи'),
    ('ПО', 'Есть подписанный оригинал'),
    ('ПС', 'Подписанный скан'),
)

class CatalogDocuments(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование документа')
    description = models.CharField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name = 'Наименование документа'
        verbose_name_plural = 'Наименования документов'

class Document(models.Model):
    # Номер документа ?
    catalog_documents = models.OneToOneField(CatalogDocuments, related_name='catalog_documents',
                                             on_delete=models.PROTECT, verbose_name='Документ', blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS, default='НП', verbose_name='Статус')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
