## Installation
### Setup
Step-1
install [Virtual box](https://www.virtualbox.org/wiki/Downloads) or VM-ware workstation

Step-2 
install [Mininet-VM](https://github.com/mininet/mininet/releases/)

Step-3
install [Ubuntu](https://ubuntu.com/download/desktop) in virtual box

Step-4
install [ryu-controller](https://ryu.readthedocs.io/en/latest/getting_started.html) in ubuntu vm

Step-5
Use git clone to install the code files
```bash
git clone https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation-using-Machine-Learning.git
```

### Go to Mininet-vm

```bash
# change working directory to mininet folder
cd mininet

# change controller ip address
nano topology.py

# run topology
sudo python topology.py
```

### Go to Ubuntu vm

```bash
# change working directory to controller folder
cd controller

# switch on the ryu-controller
ryu-manager controller.py
```

### hping commands 
```bash
# icmp flood
hping3 -1 -V -d 120 -w 64 -p 80 --rand-source --flood

# syn flood
hping3 -S -V -d 120 -w 64 -p 80 --rand-source --flood

# udp flood
hping3 -2 -V -d 120 -w 64 -p 80 --rand-source --flood


# You can try out the project using our vm too
## [Link to download our Mininet VM and Ryu Controller](shorturl.at/szH58)


