from diagrams import Diagram, Cluster
from diagrams.aws.compute import EKS
from diagrams.aws.network import ALB, InternetGateway, PrivateSubnet, PublicSubnet, VPC
from diagrams.onprem.client import User

with Diagram("EKS Cluster with Ingress and ALB", show=True):
    with Cluster("VPC"):
        vpc = VPC("VPC")

    with Cluster("Subnets"):
        with Cluster("Public Subnets"):
            public_subnet = PublicSubnet("Public Subnet 1")
            igw = InternetGateway("Internet Gateway")
            igw >> public_subnet

        with Cluster("Private Subnets"):
            private_subnet = PrivateSubnet("Private Subnet 1")

    with Cluster("EKS"):
        eks_cluster = EKS("EKS Cluster")

    with Cluster("Ingress"):
        ingress_controller = User("Ingress Controller")

    with Cluster("Load Balancer"):
        alb = ALB("ALB")

    vpc >> [public_subnet, private_subnet]
    eks_cluster >> ingress_controller
    ingress_controller >> alb
    alb >> private_subnet

