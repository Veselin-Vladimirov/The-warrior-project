#!/bin/bash
set -e
PROFILE_NAME=warrior
AWS_ACCESS_KEY_ID=AKIAW3MECICGIXXUCQVK
AWS_SECRET_ACCESS_KEY=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
CLUSTER_NAME=warrior-cluster
REGION=eu-central-1
LAUNCH_TYPE=EC2
ecs-cli configure profile --profile-name "$PROFILE_NAME" --access-key "$AWS_ACCESS_KEY_ID" --secret-key "$AWS_SECRET_ACCESS_KEY"
ecs-cli configure --cluster "$CLUSTER_NAME" --default-launch-type "$LAUNCH_TYPE" --region "$REGION" --config-name "$PROFILE_NAME"
