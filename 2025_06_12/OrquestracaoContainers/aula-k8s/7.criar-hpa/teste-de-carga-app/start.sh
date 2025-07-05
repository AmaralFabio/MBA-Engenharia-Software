#! /bin/sh -c "

locust -f src/tasks.py --host http://servidor-python-service.default.svc.cluster.local
# {NAME_OF_SERVICE}.{NAMESPACE}.svc.cluster.local