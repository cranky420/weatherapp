terraform {
  backend "s3" {
    bucket         = "weather-app-tfstate-bijayrajsinghdeo"
    key            = "dev/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "weather-app-tf-locks"
    encrypt        = true
  }
}