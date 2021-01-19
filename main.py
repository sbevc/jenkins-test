import json
import os

from jenkins import Jenkins


def get_info(jenkins_url, job_name, build_number):
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

    print()
    print("READING TEST FILE")
    try:
        with open("tests.xml", "r") as f:
            f.read()
        print("SUCCESSFULLY READ tests.xml")
    except FileExistsError as e:
        print(e)


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument("--jenkins-url", required=True)
    parser.add_argument("--job-name", required=True)
    parser.add_argument("--build-number", required=True, type=int)

    args = parser.parse_args()

    sys.exit(get_info(parser.jenkins_url, parser.job_name, parser.build_number))
