from diagrams import Cluster, Diagram
from diagrams.aws.compute import EKS, EC2
from diagrams.aws.network import InternetGateway, NLB
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet, StatefulSet
from diagrams.k8s.network import Ingress
from diagrams.onprem.client import User

with Diagram("EKS Cluster with Ingress, ALB, Services, and Pods", show=True):
    internet_gateway = InternetGateway("Internet Gateway")
    
    with Cluster("VPC"):
        with Cluster("Subnets"):
            public_subnet = EC2("Public Subnet")
            private_subnet = EC2("Private Subnet")

        vpc = EKS("EKS Cluster")
        internet_gateway >> public_subnet
        vpc >> [public_subnet, private_subnet]

    with Cluster("Load Balancer"):
        alb = NLB("ALB")
    
    with Cluster("Ingress"):
        ingress_controller = Ingress("Ingress Controller")

    alb >> ingress_controller
    
    with Cluster("Services"):
        with Cluster("Service 1"):
            service_1 = Deployment("Service 1 Deployment")
            pods_1 = [Pod("Pod 1"), Pod("Pod 2")]

        with Cluster("Service 2"):
            service_2 = StatefulSet("Service 2 StatefulSet")
            pods_2 = [Pod("Pod 3"), Pod("Pod 4")]

    ingress_controller >> [service_1, service_2]
    [service_1, service_2] >> alb

    with Cluster("Pods"):
        with Cluster("Replica Set"):
            replica_set = ReplicaSet("Replica Set")
            pods_3 = [Pod("Pod 5"), Pod("Pod 6")]

        pods_3 >> replica_set
        replica_set >> service_1

