#! /bin/bash

NC='\033[0m'
G='\033[92m'

echo "----------UPDATING REPO----------"
git pull https://github.com/TheDucky/JoeBean.git
echo -e "${G}----------DONE----------${NC}\n"

echo "----------RUNNING BOT----------"
nohup python3 -u JoeBean.py >> data.log & 
raw=$(ps -ef |grep 'python3 -u JoeBean.py'| awk '{print $2}')
IFS=' '
read -ra ADDR <<< "$raw"   
for pid in "${ADDR[@]}"; do  
    echo -e "pid = ${G}\e[4m\e[1m$pid\e[0m\e[0m${NC}"
done
echo -e "\nKillSwitch: $pid" >> data.log
echo -e "${G}----------DONE----------${NC}\n"

echo -e "Please check 'data.log' file to view the logs"
echo -e "You can stop the bot by simply entering the command ${G}\e[4m\e[1mkill -9 $pid\e[0m\e[0m\t${NC}"