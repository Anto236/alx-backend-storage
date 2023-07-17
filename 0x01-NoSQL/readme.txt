MongoDB installation.

Let's proceed with reinstalling MongoDB using the MongoDB repository:

Step 1: Remove MongoDB packages and data (if they were installed before)

bash
Copy code
sudo apt purge mongodb-org*
sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongodb
Save to grepper
Step 2: Clear MongoDB configuration files (optional)

bash
Copy code
sudo rm /etc/mongod.conf
Save to grepper
Step 3: Add the MongoDB repository key to the new trusted GPG keyring

bash
Copy code
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo gpg --dearmor --output /etc/apt/trusted.gpg.d/mongodb-server-5.0.gpg
Save to grepper
Step 4: Add the MongoDB repository to the sources list

bash
Copy code
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
Save to grepper
Step 5: Update package lists and clean the cache

bash
Copy code
sudo apt update
sudo apt clean
Save to grepper
Step 6: Install MongoDB

bash
Copy code
sudo apt install -y mongodb-org
Save to grepper
Step 7: Start and enable the MongoDB service

bash
Copy code
sudo systemctl start mongod
sudo systemctl enable mongod
Save to grepper
Check the status of MongoDB to ensure it's running correctly:

bash
Copy code
sudo systemctl status mongod
Save to grepper
If the installation is successful, MongoDB should be up and running without any "core-dump" issues. If you encounter any errors during this process, please share the error messages, and we can further investigate the problem.
