import factory.fuzzy
import factory
from document.models import *
from document.models import STATUS as document_status

class CatalogDocumentsFactory(factory.DjangoModelFactory):

	class Meta:
		model = CatalogDocuments

	name = factory.Faker('text', max_nb_chars=20)
	description = factory.Faker('text', max_nb_chars=200)

class BuildCatalogDocumentsFactory(CatalogDocumentsFactory):
	class Meta:
		strategy = factory.BUILD_STRATEGY

STATUS_DOCUMENT = [x[0] for x in document_status]

class DocumentFactory(factory.DjangoModelFactory):

	class Meta:
		model = Document

	catalog_documents = factory.SubFactory(CatalogDocumentsFactory)
	status = factory.fuzzy.FuzzyChoice(STATUS_DOCUMENT)
	created_date = factory.Faker('date_time')

class BuildDocumentFactory(DocumentFactory):
	class Meta:
		strategy = factory.BUILD_STRATEGY