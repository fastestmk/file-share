from django.shortcuts import render,redirect
from django.views.generic import TemplateView, View
from .models import *   
from django.http import HttpResponse
import json
from django.conf import settings
from django.contrib import messages
import os
from datetime import datetime,timedelta,date
from django.utils import timezone


class SampleTest(TemplateView):
	template = 'uploader/index.html'
	def get(self, request):
		return render(request, self.template, locals())

class UploadFile(TemplateView):
	template = 'uploader/index.html'
	def get(self, request):
		return render(request, self.template, locals())

	def post(self, request):
		context = {}
		file = request.FILES.get("myfile")
		file_name = str(file)
		description = request.POST.get("description") 
		uploaded_at = datetime.now(tz=timezone.utc)
		expired_at = uploaded_at + timedelta(minutes=5)

		print(file, "---------")  
		print(description, "---------")  

		file_obj = FileUpload(
			file=file,
			file_name=file_name,
			description=description,
			uploaded_at=uploaded_at,
			expired_at=expired_at
		)
		file_obj.save()
		context['status'] = True
		context['message'] = "file uploaded"
		link = settings.BASE_URL+'download/'+str(file_obj.id)
		messages.info(request, "{}".format(link))
		return redirect('download-file')
		# return HttpResponse(json.dumps(context),content_type="application/json")

class DownloadView(TemplateView):
	template = 'uploader/download.html'
	def get(self, request):
		return render(request, self.template, locals())


class DownloadFile(View):
	def get(self, request, *args, **kwargs):
		print("In download view ---------------------")
		file_id = kwargs['id']
		print("File id -", file_id)
		file_obj = FileUpload.objects.get(id=file_id)

		print(str(file_obj.description))
		file_name =  file_obj.file #get the filename of desired excel file
		path_to_file = settings.MEDIA_ROOT+'/'+str(file_name)
		print(path_to_file)
		if path_to_file:
			with open(path_to_file, 'rb') as fh:
				response = HttpResponse(fh.read(), content_type='application/force-download')
				# response = HttpResponse(content_type='text/plain')
				response['Content-Disposition'] = 'attachment; filename=%s' %file_obj.file_name
				response['X-Sendfile'] = path_to_file
				return response 

class DeleteView(View):
	def get(self, request, *args, **kwargs):
		file_id=kwargs['id']
		file_obj = FileUpload.objects.get(id=file_id)
		if file_obj:
			file = file_obj.file
			file_path = settings.MEDIA_ROOT+'/'+str(file)
			if os.path.isfile(file_path):
				file_obj.delete()
				os.remove(file_path)
				return redirect('file-upload')	
