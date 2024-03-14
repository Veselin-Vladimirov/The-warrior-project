provider "aws" {
  region = "eu-central-1"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "19.21.0"
  cluster_name    = "warrior-cluster"
  cluster_version = "1.28"
  vpc_id          = "vpc-342c735c"
  cluster_endpoint_public_access = true

  subnet_ids = ["subnet-0495ea79", "subnet-de3f7293", "subnet-c96a6aa2"]

  eks_managed_node_groups = {
    test = {
      desired_capacity = 1
      max_capacity     = 3
      min_capacity     = 1

      instance_type = ["t2.micro"]
    }
  }
}

