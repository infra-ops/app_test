from diagrams import Diagram, Cluster
from diagrams.aws.compute import EKS
from diagrams.aws.network import ALB, InternetGateway, PrivateSubnet, PublicSubnet, VPC
from diagrams.onprem.client import User
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EKS, EC2
from diagrams.aws.network import InternetGateway, NLB
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet, StatefulSet
from diagrams.k8s.network import Ingress
from diagrams.onprem.client import User





with Diagram("EKS Cluster with Ingress and ALB", show=True, direction="TB"):

    with Cluster("EKS"):
        eks_cluster = EKS("EKS Cluster")

    with Cluster("Ingress"):
        ingress_controller = User("Ingress Controller")

    with Cluster("Load Balancer"):
        alb = ALB("ALB")

#    vpc >> [public_subnet, private_subnet]
#    eks_cluster >> ingress_controller >> alb
    
    with Cluster("Services"):
        with Cluster("Service 1"):
            service_1 = Deployment("Service 1 Deployment")
            pods_1 = [Pod("Pod 1"), Pod("Pod 2")]

  
     
    eks_cluster >> ingress_controller >> alb >> service_1 >> pods_1
