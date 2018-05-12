from gcloud import storage
import datetime
import os


import gcloud

client = storage.Client.from_service_account_json(os.environ["GOOGLE_APPLICATION_CREDENTIAL"])
time = datetime.datetime.now().isoformat()

print(f"creating file {time}")

kd = client.get_bucket("testkubedata")

b = kd.blob(time)

b.upload_from_string(time)

print(f"created file {time}")
b2 = kd.get_blob(time)
dl_str = b2.download_as_string()


print(f"downloaded file with contents {dl_str}")