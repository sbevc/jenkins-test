import os

from jenkins import Jenkins

jenkins_url = os.environ["JENKINS_URL"]
build_number = os.environ["BUILD_NUMBER"]
job_name = os.environ["JOB_NAME"]


server = Jenkins(jenkins_url, username="sbevc", password='+hs"ag1h"')

with open(f"{job_name}-{build_number}", "w") as f:
    build_output = server.get_build_console_output(job_name, build_number)
    f.write(build_output)
