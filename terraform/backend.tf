terraform {
  backend "s3" {
    bucket         = "warrior-bucket"
    key            = "test/warrior-statefile/terraform.tfstate"
    region         = "eu-central-1"
    dynamodb_table = "warrior-table"
    encrypt        = true
  }
}

