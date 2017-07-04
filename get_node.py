#!/usr/bin/env python3
''' Script to find out details of a node, given its name
- Looks for the node across all our stacks
- Shows Pods running on it, First the ones with problems

So far I just got the first, unrelated example, taken from
https://www.ianlewis.org/en/quick-look-kubernetes-python-client

TODO: Get this script to work fine
TODO: Do a similar one but for pods
'''

import os
from kubernetes import client, config
config.load_kube_config(
    os.path.join(os.environ["HOME"], '.kube/config.qa.eu'))

v1 = client.CoreV1Api()

pod_list = v1.list_namespaced_pod("default")
for pod in pod_list.items:
    print("%s\t%s\t%s" % (pod.metadata.name,
                          pod.status.phase,
                          pod.status.pod_ip))
