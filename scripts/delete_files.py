import os
import psycopg2
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler

DATABASE_URL = "postgres://wtupribqqpvbua:567e751a041b375875d895a60f941b4b585f7fde41929861ad74a4b75d821a43@ec2-3-210-178-167.compute-1.amazonaws.com:5432/d6pcsub86jqpjt"
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
print("Opened database successfully")
cursor = conn.cursor()

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=2)
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
				print(os.getcwd)
				root_dir = os.path.dirname(os.getcwd())
				file_path = root_dir+'/media/'+str(file)
				print(file_path)
				if os.path.isfile(file_path):
					print("files deleted from media")
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