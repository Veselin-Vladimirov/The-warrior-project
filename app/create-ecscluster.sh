#!/bin/bash
KEY_PAIR=warrior-cluster
    ecs-cli up \
      --keypair $KEY_PAIR  \
      --capability-iam \
      --size 2 \
      --instance-type t3.medium \
      --tags project=warrior-cluster \
      --cluster-config warrior \
      --ecs-profile warrior
