#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

f = cgi.FieldStorage()
clients = f.getvalue("x")

if "get" in clients and "pod" in clients:
   comm="sudo kubectl get pod --kubeconfig admin.conf"

elif "get" in clients and "deployment" in clients:
   comm="sudo kubectl get deployments --kubeconfig admin.conf"

command = clients.split()
if command[0] == "a":
    deploy_namw = command[2]
    image_name = command[1]
    cmd = "kubectl create deployment " + (deploy_name) + " --image=" + (image_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif command[0] == "b":
    pod_name = command[2]
    image_name = command[1]
    cmd = "kubectl run " + (pod_name) + " --image=" + (image_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif command[0] == "c":
    pod_name = command[1]
    cmd = "kubectl delete pod " + (pod_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif command[0] == "d":
    deployment_name = command[1]
    cmd = "kubectl delete deployment " + (deploy_name)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif command[0] == "e":
    deployment_name = command[1]
    port_no = command[2]
    Expose_type =  command[3]
    cmd = "kubectl expose deployment " + (deploy_name) + " --port=" + (port_no) + " --type=" + (Expose_type)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif command[0] == "f":
    deployment_name = command[1]
    replica = command[2]
    cmd = "kubectl scale deployment " + (deploy_name) + " --replicas=" + (replica)
    output = subprocess.getoutput("sudo " + cmd + " --kubeconfig admin.conf")
    print(output)
elif command[0] == "g":
    cmd = "kubectl get svc --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print(output)
elif command[0] == "h":
    cmd = "kubectl delete all --all --kubeconfig admin.conf"
    output = subprocess.getoutput("sudo " + cmd)
    print(output)
elif command[0] == "err":
    print("command not found")

#out=subprocess.getoutput(comm)
#print(out)
