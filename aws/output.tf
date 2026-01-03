output "instance_ipv6_all" {
  value = aws_instance.app_server.ipv6_addresses
}
