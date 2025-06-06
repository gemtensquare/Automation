#!/bin/bash

echo -e "⏳ Check Disk Usage Started"

echo -e "\n🔍 Checking free -h Disk Usage..."
free -h

echo -e "\n🔍 Checking df -h Disk Usage..."
df -h

echo -e "\n🔍 Checking lsblk Disk Usage..."
lsblk


echo -e "\n⏳ Check Disk Usage Completed"