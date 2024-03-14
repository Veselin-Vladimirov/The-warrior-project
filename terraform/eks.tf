provider "aws" {
  region = "eu-central-1"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "19.21.0"
  cluster_name    = "warrior-cluster"
  cluster_version = "1.28"
  vpc_id          = "vpc-09808750e4924c4b7"
  cluster_endpoint_public_access = true

  subnet_ids = ["subnet-0693c378eb2d859d2", "subnet-0cf0778b4532344bb", "subnet-09bf2b063afb3bb8d"]

  eks_managed_node_groups = {
    test = {
      desired_capacity = 1
      max_capacity     = 3
      min_capacity     = 1

      instance_type = ["t2.micro"]
    }
  }
}

