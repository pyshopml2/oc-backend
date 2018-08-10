import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')
django.setup()

import factory.fuzzy
import factory
from document.models import STATUS as document_status
from document.models import CatalogDocuments, Document
from user.models import STATUS as user_status
from user.models import EmployeePosition, User, Employee, ContactPerson, GroupEmployee

STATUS_DOC = [x[0] for x in document_status]
STATUS_USER = [x[0] for x in user_status]

class CatalogDocumentsFactory(factory.Factory):
    class Meta:
        model = CatalogDocuments

    name = factory.Faker('text')
    description = factory.Faker('text')

catalog_document = CatalogDocumentsFactory()

class DocumentFactory(factory.Factory):
    class Meta:
        model = Document

    document = factory.SubFactory(CatalogDocumentsFactory)
    status = factory.fuzzy.FuzzyChoice(STATUS_DOC)
    created_date = factory.Faker('iso8601')

documents = DocumentFactory()

class EmployeePositionFactory(factory.Factory):
    class Meta:
        model = EmployeePosition

    name = factory.Faker('text')
    description = factory.Faker('text')