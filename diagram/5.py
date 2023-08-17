from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import VPC
from diagrams import Diagram, Cluster, Edge


graph_attr = {
    "fontsize": "40"
}


with Diagram("EC2 Instance Inside VPC", show=True, graph_attr=graph_attr):

     with Cluster("VPC"):
       vpc_ec2_instance = EC2("EC2 Instance")
    
