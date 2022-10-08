# mysql-selfmanaged
Part 1 – Installing MySQL on either Azure or GCP VM
Create a new public github repo called 'mysql-selfmanaged' in your github account. In this exercise, you will create a new VM and install MySQL onto that VM, configure it to allow external connections, and then upload via python a dummy dataset into a dummy database within MySQL. 

•	GCP cloud environment was used.

•	Set up GCP VM:
    -https://console.cloud.google.com/
    o	Under project Premvadee-HHA504, Compute Engine selected, VM Instances selected, create instance selected, Machine type: e2-medium; image: ubuntu-1804-bionic-   
      v20220901

•	Command used to setup the OS image:
    o	GCP: minimum hardware requirements: 2 CPU and 2 gigabyte of ram
    o	fresh up the OS by "sudo apt-get update"
    o	GCP environment: ubuntu OS version 18 which default to MySQL version older version 5.7 
    o	install MySQL to this OS that house all data:'sudo apt install MySQL-server MySQL-client'

•	Through GCP terminal:
    o	-type in “sudo MySQL”, we now log into SQL software.

•	To modify sql configuration mysql.cnf 
  o	Use terminal editor call nano to update configuration file and then restart sql server to update that piece.  
  o	sudo nano  /etc/mysql//mysql.conf.d/mysqld.cnf
  o	this is path where MySQL configuration file lives
  o	show complex configuration file that contain default options for MySQL server.
  o	Bind-address =   127.0.0.1  which is specific IP address that is equivalent to local host.  Mean you only have access that thing from that machine. Like flask    
    application, we change our IP address to within the flask application in order to take on the IP address of the VM. We do the same by change whatever IP address to 
    0.0.0.0 so it can take on IP address of VM or host machine. 
  o	To make it work -restart software
      	Sudo service mysql restart
      	/etc/init.d/mysql restart  (or type in sudo in front)
  o	To open up the port with MySQL uses which is port 3306 so we can access it via python or another VM.  Under firewall in GCP, we opened up firewall which is       
    security for this VM to enable access via port 80 or 443 but we need to open up port 3306 which is default port for MySQL.  
  o Within each GCP project, you need to go to different service called firewall. And under firewall service we then create new rule to enable that port to be open to      the WWW or for us to change permission. 
   	So under firewall that is set at a project setting, we can decide what services under project impact by firewall.  
    	Under firewall, we create firewall rule. And under firewall rule we will create a rule that will associate with that VM to open up that communication port.  we 
      will add port 3306. It will enable our VM to communicate via port 3306.
    o	Give name of firewall rule “mysql-allow”
    o	Description- this will enable incoming access to port 3306, which is the default port for MySQL 
    o	target all instances in the network (automatice this firewall rule to any VM that create now and future within this project.
    o	Source IPv4 ranges: 0.0.0.0/0 mean we will accept any connection from anywhere or set them from my IP addresses or take my own p address (which mean I would the      only person to access this) terminal type  “ifconfig en0”
    o	Specified specific port: 3306 which is default port
    o	Bottom next to create button there is command programmatically to copy to another project.
    o	Now you can rerun the code in Jupiter
    
    -Dataset
      brain_size_df = pd.read_csv("https://raw.githubusercontent.com/premdub/descriptives_scipy/main/data/brain_size.csv")
      

