# VCC-Assignment-3
# Auto-Scaling from Local VM to GCP

This project demonstrates how to create a local virtual machine (VM), monitor resource usage, and automatically scale to Google Cloud Platform (GCP) when CPU usage exceeds 75%. A sample web application is deployed to demonstrate the process.

---

## **Files Included**
1. **`app.py`**: The main Flask application that runs on the local VM. It handles user requests, monitors CPU usage, and migrates tasks to GCP when necessary.
2. **`app.log`**: A log file that records system events, such as CPU usage and migration triggers.
3. **`stress_cpu.py`**: A Python script to simulate high CPU usage for testing the auto-scaling functionality.

---

## **Project Overview**
The system consists of the following components:
1. **Local VM**: Hosts the Flask application and monitors CPU usage.
2. **GCP VM**: Handles resource-intensive tasks when CPU usage on the local VM exceeds 75%.
3. **Resource Monitor**: Tracks CPU usage and triggers auto-scaling.
4. **Auto-Scaling Logic**: Migrates tasks to GCP when CPU usage exceeds 75%.
5. **Sample Application**: A web-based calculator that performs mathematical operations.

---

## **Setup Instructions**

### **1. Set Up the Local VM**
1. Install VirtualBox or VMware.
2. Create a new VM with Ubuntu.
3. Install Python and Flask.

### **2. Set Up the GCP VM**
1. Create a GCP account and set up a project.
2. Go to **Compute Engine → VM Instances → Create**.
3. Install Python and Flask on the GCP VM.

### **3. Deploy the GCP Application**
1. Copy the `gcp_app.py` file to the GCP VM.
2. Run the GCP application.

### **4. Run the Local Application**
1. Copy the `app.py` and `stress_cpu.py` files to the local VM.
2. Run the local application.

---

## **Usage Instructions**

### **1. Access the Web Application**
1. Open your browser and go to the local VM's IP address on port 5000.
2. Enter a number and click **Calculate**.
3. The application will display the results of the calculations.

### **2. Simulate High CPU Usage**
1. Run the `stress_cpu.py` script to simulate high CPU usage.
2. Monitor CPU usage using a system monitoring tool like `htop`.

### **3. Verify Auto-Scaling**
1. When CPU usage exceeds 75%, the application will migrate tasks to the GCP VM.
2. Check the `app.log` file for details about the migration.

---

## **File Descriptions**

### **`app.py`**
- The main Flask application that runs on the local VM.
- Monitors CPU usage and migrates tasks to GCP when necessary.
- Logs system events to `app.log`.

### **`app.log`**
- A log file that records system events, such as CPU usage and migration triggers.
- Useful for debugging and monitoring system behavior.

### **`stress_cpu.py`**
- A Python script to simulate high CPU usage.
- Used to test the auto-scaling functionality.

---

## **Architecture Design**
The system architecture includes:
1. **User Browser**: Interacts with the web application.
2. **Local VM**: Hosts the main application and monitors CPU usage.
3. **GCP VM**: Handles migrated tasks when CPU usage exceeds 75%.
4. **Resource Monitor**: Tracks CPU usage and triggers auto-scaling.
5. **Load Balancer**: Distributes requests between the local VM and GCP VM.

---

## **Conclusion**
This project demonstrates how to create a local VM, implement resource monitoring, configure auto-scaling policies, and deploy a sample application. By monitoring CPU usage and migrating tasks to the cloud when necessary, the system ensures that it can handle high loads without degrading performance.

---

## **Plagiarism Clause**
I declare that no part of this implementation or documentation has been copied from other sources. All work is original and created for the purpose of this assignment.

---

