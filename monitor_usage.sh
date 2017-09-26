#!/bin/bash
echo "username,projects,scratch,total" > hitlist.csv
for user in $(ls -d /projects/*/); do
    username=$(basename ${user})
    proj_usage=$(du --block-size=1G -c /projects/${username} | grep total | xargs | cut -d ' ' -f 1)
    scth_usage=$(du --block-size=1G -c /scratch/${username} | grep total | xargs | cut -d ' ' -f 1)
    totl_usage=$(echo "${proj_usage} + ${scth_usage}" | bc)
    echo ${username///},${proj_usage},${scth_usage},${totl_usage}
    echo ${username///},${proj_usage},${scth_usage},${totl_usage} >> hitlist.csv;
done
