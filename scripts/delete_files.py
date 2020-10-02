import os
import psycopg2
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler

# DATABASE_URL = "postgres://vapqwtuddvoocu:dc4fa7072cd240cba13b93e4e92ecff470e3bf075eab0b47b33232658417f0aa@ec2-107-22-7-9.compute-1.amazonaws.com:5432/dbu95qaiu69bq4"
conn = psycopg2.connect(database = "file_uploader", user = "fileuploader321", password = "si@f#$tc27VTH34")
print("Opened database successfully")
cursor = conn.cursor()

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=5)
def deleteFiles():
	sql = "SELECT * from uploader_fileupload"
	cursor = conn.cursor()
	cursor.execute(sql)

	# file_objlist = 
	now = datetime.now(tz=timezone.utc)
	try:
		for obj in cursor.fetchall():
			expired_at = obj[5]
			print(now)
			print(expired_at)
			if obj and now > expired_at:
				file = obj[1]
				root_dir = os.path.dirname(os.getcwd())
				file_path = root_dir+'/media/'+str(file)
				print(file_path)
				if os.path.isfile(file_path):
					os.remove(file_path)
				# del(obj)
				cursor = conn.cursor()
				cursor.execute("DELETE FROM uploader_fileupload WHERE   '"+str(expired_at)+"' < now() ;")
				conn.commit()
					# return redirect('file-upload')	
	except Exception as e:
		raise e				

if __name__ == '__main__':
	sched.start()
	# deleteFiles()			