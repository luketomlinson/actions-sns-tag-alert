#!/usr/bin/env python
import json
import os
import re
import subprocess
import sys

import boto3


def get_recent_tags():
    """ Gets the last few tags in the repo; must be using SemVer or similar """

    return (
        subprocess.run(
            "git tag | sort --version-sort -r | head | tr '\n' ' '",
            shell=True,
            stdout=PIPE,
            stderr=STDOUT
        )
        .stdout.decode("utf-8")
    )


def guess_prev_tag(recent_tags, curr_tag):
    """ Try to guess which tag came before the current one """

    tag_form = re.compile(r"^v?\d+\.\d+\.\d+")
    for tag in recent_tags:
        if tag != curr_tag and tag_form.search(tag):
            return tag

    return "master"


def main():

    tag_prefix = "refs/tags/"
    git_tag = os.environ["GITHUB_REF"]
    if git_tag.startswith(tag_prefix):
        git_tag = git_tag[len(tag_prefix) :]

    recent_tags = get_recent_tags()
    print(recent_tags)

    prev_tag = "master"
    if recent_tags and len(recent_tags) > 1:
        prev_tag = guess_prev_tag(recent_tags, git_tag)


if __name__ == "__main__":
    main()
