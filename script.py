import json
import os

from jenkins import Jenkins

jenkins_url = os.environ["JENKINS_URL"]
build_number = int(os.environ["BUILD_NUMBER"])
job_name = os.environ["JOB_NAME"]


server = Jenkins(jenkins_url, username="sbevc", password='+hs"ag1h')
build_console_output = server.get_build_console_output(job_name, build_number)
build_info = server.get_build_info(job_name, build_number)

print()
print("BUILD CONSOLE OUTPUT")
print(build_console_output)


print()
print("BUILD INFO")
print(json.dumps(build_info, indent=2))


print()
print("ENV VARS")
print(json.dumps(dict(os.environ), indent=2))
