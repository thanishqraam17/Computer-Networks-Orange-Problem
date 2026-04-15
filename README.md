# Computer-Networks-Orange-Problem


**Student Name:** Thanishq Raam Paatil  
**Student SRN:** PES1UG24CS502  

---

## Problem Statement (Topic 14)
The goal of this project is to build a network that can survive a link failure. We use an SDN controller to monitor the network. If a link between switches breaks, the controller finds a new path to send data so the hosts can still communicate with each other.

---

## Requirements
To run this project, you need:
- Linux system  
- Mininet  
- POX controller  

If you do not have POX, follow these steps:

```bash
cd ~/Desktop
git clone https://github.com/noxrepo/pox
```

This will create a folder named `pox` on your Desktop.

---

## Files in this Repository
- `topo.py` – Defines the triangle topology with redundant links  
- `controller.py` – Handles failure detection and rerouting  

---

## How to Run the Project

### Step 1: Copy files to POX
```bash
cp topo.py controller.py ~/Desktop/pox/ext/
```

### Step 2: Start controller
```bash
cd ~/Desktop/pox
python3 pox.py controller
```

### Step 3: Start Mininet (new terminal)
```bash
sudo mn -c
sudo mn --custom ext/topo.py --topo recovery --controller remote
```

---

## Proof of Execution

### 1. Normal Connectivity
Before the failure, the network is stable and hosts can ping each other.

![Normal Connectivity](CN%201.png)

---

### 2. Simulating Link Failure
We break the primary link using the Mininet command:

```bash
link s1 s2 down
```

![Breaking the Link](CN%202.png)

---

### 3. Recovery Verification
After the failure, the ping shows temporary packet loss before the controller restores connectivity via an alternate path.

![Recovery Results](CN%203.jpg)

---

## Test Case Commands

### Initial Connectivity Test
```bash
h1 ping -c 5 h2
```

---

### Simulate Link Failure
```bash
link s1 s2 down
```

---

### Verify Recovery
```bash
h1 ping -c 5 h2
```

---

### Check Flow Rules
```bash
sh ovs-ofctl dump-flows s1
```

---

## References
- POX Official Documentation: https://noxrepo.github.io/pox-doc/html/  
- Mininet Walkthrough: http://mininet.org/walkthrough/  

---

## Conclusion
This project demonstrates:
- Detection of link failure using an SDN controller  
- Dynamic recovery using alternate paths  
- Improved network reliability and fault tolerance  
