resource "aws_security_group" "admin" {
  name        = "billing-admin"
  description = "admin access"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
