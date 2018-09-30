import factory.fuzzy
import factory

from document.models import CatalogDocuments, Document
from document.models import STATUS


class CatalogDocumentsFactory(factory.DjangoModelFactory):

    class Meta:
        model = CatalogDocuments

    name = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('sentence', nb_words=4)


class BuildCatalogDocumentsFactory(CatalogDocumentsFactory):
    class Meta:
        strategy = factory.BUILD_STRATEGY


STATUS_DOCUMENT = [x[0] for x in STATUS]


class DocumentFactory(factory.DjangoModelFactory):

    class Meta:
        model = Document

    catalog_documents = factory.SubFactory(CatalogDocumentsFactory)
    status = factory.fuzzy.FuzzyChoice(STATUS_DOCUMENT)
    created_date = factory.Faker('date_time')


class BuildDocumentFactory(DocumentFactory):
    class Meta:
        strategy = factory.BUILD_STRATEGY
