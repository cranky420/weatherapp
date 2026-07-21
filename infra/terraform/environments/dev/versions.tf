terraform {

  required_version = ">= 1.8.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  backend "s3" {

    bucket = "weather-app-tfstate-bijayrajsinghdeo"

    key = "dev/terraform.tfstate"

    region = "ap-south-1"

    dynamodb_table = "weather-app-tf-locks"

    encrypt = true
  }
}