module "networking" {
  source = "../../modules/networking"

  project_name = var.project_name
  environment  = var.environment

  vpc_cidr = "10.0.0.0/16"

  public_subnets = [
    "10.0.1.0/24",
    "10.0.2.0/24"
  ]

  private_subnets = [
    "10.0.11.0/24",
    "10.0.12.0/24"
  ]

  availability_zones = [
    "ap-south-1a",
    "ap-south-1b"
  ]
}
module "security" {
  source = "../../modules/security"

  project_name = var.project_name
  environment  = var.environment

  vpc_id = module.networking.vpc_id
}
module "iam" {

  source = "../../modules/iam"

  project_name = var.project_name
  environment  = var.environment
}
module "ecr" {

  source = "../../modules/ecr"

  project_name = var.project_name
  environment  = var.environment
}
module "cloudwatch" {

  source = "../../modules/cloudwatch"

  project_name = var.project_name
  environment  = var.environment

  log_retention_days = 30
}
module "alb" {

  source = "../../modules/alb"

  project_name = var.project_name
  environment  = var.environment

  vpc_id = module.networking.vpc_id

  public_subnet_ids = module.networking.public_subnet_ids

  alb_security_group_id = module.security.alb_security_group_id
}
module "ecs" {

  source = "../../modules/ecs"

  project_name = var.project_name
  environment  = var.environment

  aws_region = var.aws_region

  private_subnet_ids = module.networking.private_subnet_ids

  frontend_security_group_id = module.security.frontend_security_group_id
  backend_security_group_id  = module.security.backend_security_group_id

  execution_role_arn = module.iam.execution_role_arn
  task_role_arn      = module.iam.task_role_arn

  frontend_repository_url = module.ecr.frontend_repository_url
  backend_repository_url  = module.ecr.backend_repository_url

  frontend_log_group_name = module.cloudwatch.frontend_log_group_name
  backend_log_group_name  = module.cloudwatch.backend_log_group_name

  frontend_target_group_arn = module.alb.frontend_target_group_arn
  backend_target_group_arn  = module.alb.backend_target_group_arn
}