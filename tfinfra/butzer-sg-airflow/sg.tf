###

# Private for CHS Security Group

##



###

# Private Security Group

##



resource "aws_security_group" "private" {

  name = "butzer-sg-airflow"

  description = "Private internet access"

  vpc_id = "vpc-0055752230db6161d"



  tags = {

    Name        = "butzer-sg-airflow"

    Role        = "Airflow Console etc."

    Project     = "ECCOE-IARPA"

    ManagedBy   = "terraform"

  }

}



resource "aws_security_group_rule" "private_out" {

  type        = "egress"

  from_port   = 0

  to_port     = 0

  protocol    = "-1"

  cidr_blocks = ["0.0.0.0/0"]



  security_group_id = aws_security_group.private.id

}



resource "aws_security_group_rule" "private_in" {

  type              = "ingress"

  from_port         = 8080

  to_port           = 8080

  protocol          = "-1"

  cidr_blocks = ["0.0.0.0/0"]



  security_group_id = aws_security_group.private.id

}
