provider "aws" {
  profile = "default"
  region  = var.region_aws_favorite
}

resource "aws_instance" "app_server" {
  ami           = var.instance_ami
  instance_type = var.instance_type
  tags = {
    "Name" = var.instance_name
  }

  subnet_id     = module.vpc.public_subnets[0]

  enable_primary_ipv6 = true

  ipv6_address_count = 1

  associate_public_ip_address = false

  vpc_security_group_ids = [
    aws_security_group.ssh_ipv6_only.id
  ]

  key_name = var.key_name

}

resource "aws_security_group" "ssh_ipv6_only" {
  name        = var.aws_security_group_name
  description = "Allow SSH only from my IPv6"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description      = "SSH from my phone IPv6"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    ipv6_cidr_blocks = [var.ipv6_ssh_connection]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    ipv6_cidr_blocks = ["::/0"]
  }
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "6.5.1"

  name = var.vpc_name
  cidr = "10.0.0.0/16"

  azs             = [var.subnet_aws_favorite]
  public_subnets  = ["10.0.1.0/24"]

  enable_ipv6 = true

  public_subnet_ipv6_prefixes = [0]
}
