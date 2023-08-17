from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import VPC
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.security import Cognito, IAM, WAF




graph_attr = {
    "fontsize": "40"
}

with Diagram("Diagram", show=True, direction="LR", graph_attr=graph_attr):
    
    with Cluster("VPC"):
       vpc_ec2_instance = EC2("EC2 Instance")
 
    
    route = Route53("Route53") 
    firewall = WAF("AWS WAF")  
    lb = ELB("App_Load_Balancer")

    route >> firewall >> lb >> vpc_ec2_instance
    

     
    
    
