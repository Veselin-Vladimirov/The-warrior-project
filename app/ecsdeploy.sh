#!/bin/bash
ecs-cli compose --project-name warrior  --file docker-compose.yaml \
--debug service up  \
--deployment-max-percent 200 --deployment-min-healthy-percent 100 \
--region eu-central-1 --ecs-profile warrior --cluster-config warrior
