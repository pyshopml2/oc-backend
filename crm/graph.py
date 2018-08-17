import os, django
import pytz

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')
django.setup()

os.system('./manage.py graph_models -a -I Client,ClientStatus,GroupClient,'
		  'CatalogDocuments,Document,GroupEmployee,Employee,ContactPerson,User,Position,Storage,Task -o my_project_subsystem.png')