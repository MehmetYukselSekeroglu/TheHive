#!/usr/bin/env bash


# TheHive cli controller version 1.0
# Developed By: Prime Security 2020 - 2024
 


# color codes 
red='\033[1;31m'
green='\033[1;32m'
yellow='\033[1;33m'
blue='\033[1;34m'
light_cyan='\033[1;96m'
reset='\033[0m'

#source "/etc/os-release"

# global const varables 
CONFIG_PATH="config/config.json"
DATABASE_SCHEMA_PATH="sql/postgresql_schema.sql"
CONTAINER_SCHEMA_PATH="/postgresql_schema.sql"
GET_TARGET=$1
SCRIPT_VERSION="1.0"
PIP_PACKAGET_FILE="requirements.txt"


# print functions 
p_error(){
    printf "$red[-]$reset $1 \n"
}

p_info(){
    printf "$green[+]$reset $1 \n"
}

# command checker 
check_command(){
    command -v $1 > /dev/null
    if [[ "$?" != "0" ]]; then
        p_error "$1 Not Found, install $1 and try run this script!"
        exit 1
    else
        p_info "$1 detected in system\tOK..."
    
    fi 

}

# check all commands 
check_reqiered_commands(){

    p_info "CHECKING REQUIRED PACKAGETS"
    printf "\n"
    
    check_command "docker"
    check_command "jq"
    check_command "docker"
    check_command "python3"
    check_command "pip3"
    check_command "cat"
    check_command "make"
    check_command "cmake"
    check_command "gcc"
    check_command "g++"
    check_command "sed"
    printf "\n"

}

# help menu printer 
print_help_exit(){
    printf "\n"
    
    printf "$blue<-[ Help Menu ]->\n$reset"  
    p_info "Script Version:\t$SCRIPT_VERSION"
    printf "\n"

    printf "COMMANDS:\n"
    
    printf "$0 --check-commands\t:Check the required commands status\n"
    printf "$0 --generate-docker\t:Create the docker container for PostgreSQL\n"
    printf "$0 --prepare-psql\t:Create database and execute database schema\n"
    printf "$0 --start-container\t:Start the container\n"
    printf "$0 --stop-container\t:Stop the running container\n"
    printf "$0 --remove-container\t:Remove container and database !DANGER!\n"
    printf "$0 --install-pip-packagets\t:Install Required pip packagets"
    printf "$0 --install-model\t:Install insightface model"
    printf "$0 --sql-shell\t\t:Connect PostgreSQL cli on \"$db_name\" database\n"
    printf "$0 --help/-h\t\t:Open this menu\n"
    printf "\n"
    exit 0

}

# reading conf file 
# conf file type    : json 
# bash json parser  : jq
p_info "Reading Config File:\t$CONFIG_PATH"
db_name=$(cat $CONFIG_PATH | jq ".database_config.database")
db_username=$(cat $CONFIG_PATH | jq ".database_config.user")
db_password=$(cat $CONFIG_PATH | jq ".database_config.password")
db_hostname=$(cat $CONFIG_PATH | jq ".database_config.host")
db_port=$(cat $CONFIG_PATH | jq ".database_config.port")


# parse json data with sed rmove " chars
db_name=$(echo $db_name | sed 's/"//g')
db_username=$(echo $db_username | sed 's/"//g')
db_password=$(echo $db_password | sed 's/"//g')
db_hostname=$(echo $db_hostname | sed 's/"//g')
db_port=$(echo $db_port | sed 's/"//g')

# set container name and max postgreSQL connection 
container_name="$db_name-postgresql-docker"
postgre_max_connections=200
container_package_name="postgres"   # container package name


# parse the argumant and execute the protocol 

# handle --generate-docker 
if [[ "$1" == "--generate-docker" ]] ;then
    printf "\n"
    printf "$blue<-[ Starting Docker Generator ]->\n$reset"    

    # call all command checker func 
    check_reqiered_commands

    # user feedback
    p_info "Printing your database config...\n"
    
    printf "[db_name]   -> \t$db_name \n"
    printf "[db_user]   -> \t$db_username \n"
    printf "[db_pass]   -> \t$db_password \n"
    printf "[db_host]   -> \t$db_hostname \n"
    printf "[db_port]   -> \t$db_port\n"
    printf "[max_conn]  -> \t$postgre_max_connections\n"
    printf "[container_name] -> \t$container_name\n"

    printf "\n"
    sleep 1

    # execute main docker command 
    docker run --name $container_name -d -p 5432:$db_port -e POSTGRES_PASSWORD=$db_password $container_package_name -N $postgre_max_connections

    # check command status 
    if [[ "$?" != "0" ]]; then
        p_error "PostgreSQL docker setup failed!"
        exit 1

    else
        p_info "PostgreSQL docker setup successfuly\tOK..."
    
    fi 

    # feedback and exit with code 0
    p_info "Docker generation successfuly !"
    exit 0


# handle --prepare-sql
# create database and execute .sql database schema 

elif [[ "$1" == "--prepare-psql" ]]; then
    printf "\n"
    printf "$blue<-[ Generating PostgreSQL databse and executing schema ]->\n$reset"    

    check_reqiered_commands



    p_info "Printing your database config...\n"
    
    printf "[db_name]   -> \t$db_name \n"
    printf "[db_user]   -> \t$db_username \n"
    printf "[db_pass]   -> \t$db_password \n"
    printf "[db_host]   -> \t$db_hostname \n"
    printf "[db_port]   -> \t$db_port\n"
    printf "[max_conn]  -> \t$postgre_max_connections\n"
    printf "[container_name] -> \t$container_name\n"

    printf "\n"
    sleep 1
    printf "\n"
    p_info "Creating database:\t$db_name"
    docker exec -t $container_name psql -p $db_port -h $db_hostname -U $db_username -c "CREATE DATABASE \"$db_name\";"
    if [[ "$?" != "0" ]]; then
        p_error "Failed to create database: $db_name !"
        exit 1

    else
        p_info "$db_name successfuly created"
    
    fi 
    
    p_info "Copy $DATABASE_SCHEMA_PATH -> $container_name"
    docker cp $DATABASE_SCHEMA_PATH $container_name:$CONTAINER_SCHEMA_PATH
    if [[ "$?" != "0" ]]; then
        p_error "Failed to copy database schema!"
        exit 1

    else
        p_info "OK..."
    
    fi 

    printf "\n"
    p_info "Executing database schema:\t$DATABASE_SCHEMA_PATH"
    docker exec -t $container_name psql -p $db_port -h $db_hostname -U $db_username -d "$db_name" -f $CONTAINER_SCHEMA_PATH
    if [[ "$?" != "0" ]]; then
        p_error "Failed to execute database schema !"
        exit 1

    else
        p_info "Database schema successfuly executed"
    
    fi 
    
    printf "\n"
    p_info "PostgreSQL server is readdy!"
    exit 0



# stop container for user 
elif [[ "$1" == "--stop-container" ]]; then
    printf "\n"
    printf "$blue<-[ Stopping Docker Container ]->\n$reset"  
    printf "\n"
    sleep 1

    docker stop $container_name

    if [[ "$?" != "0" ]]; then
        p_error "Failed to stop docker container:\t$container_name !"
        exit 1

    else
        p_info "OK..."
    
    fi 
    
    printf "\n"
    p_info "Container Successfully stopped:\t$container_name!"
    exit 0

# stop container for user 
elif [[ "$1" == "--start-container" ]]; then
    printf "\n"
    printf "$blue<-[ Starting Docker Container ]->\n$reset"  
    printf "\n"
    sleep 1

    docker start $container_name

    if [[ "$?" != "0" ]]; then
        p_error "Failed to start docker container:\t$container_name !"
        exit 1

    else
        p_info "OK..."
    
    fi 
    
    printf "\n"
    p_info "Container Successfully start:\t$container_name!"
    exit 0


# stop container for user 
elif [[ "$1" == "--start-hive" ]]; then
    printf "\n"
    printf "$blue<-[ Starting TheHive ]->\n$reset"  
    printf "\n"
    sleep 1

    python3 main.py

elif [[ "$1" == "--install-model" ]]; then
    printf "\n"
    printf "$blue<-[ Installing Insightface Model ]->\n$reset"  
    printf "\n"
    sleep 1

    python3 hivelibrary/install_insightface_model.py
    if [[ "$?" != "0" ]]; then
        p_error "Failed to install insightface model..."
        exit 1

    else
        p_info "OK..."
    
    fi 

# romove/delete container 
# for uninstall or reinstall
elif [[ "$1" == "--remove-container" ]]; then
    printf "\n"
    printf "$blue<-[ Removing Docker Container ]->\n$reset"  
    printf "\n"
    sleep 1

    p_info "Stopping container..."
    docker stop $container_name
    if [[ "$?" != "0" ]]; then
        p_error "Failed to stop docker container:\t$container_name !"
        exit 1

    else
        p_info "OK..."
    
    fi 
    
    p_info "Removing container..."
    docker rm $container_name
    if [[ "$?" != "0" ]]; then
        p_error "Failed to delete docker container:\t$container_name !"
        exit 1

    else
        p_info "OK..."
    
    fi 
    

    printf "\n"
    p_info "Container Successfully removed:\t$container_name!"
    exit 0


# quick sql shell with psql
elif [[ "$1" == "--sql-shell" ]]; then
    printf "\n"
    printf "$blue<-[ Starting SQL shell on PostgreSQL container ]->\n$reset"  
    printf "\n"
    docker exec -it $container_name psql -p $db_port -h $db_hostname -U $db_username -d "$db_name" 
    p_info "OK.."
    exit 0


elif [[ "$1" == "--install-pip-packagets" ]]; then
    printf "\n"
    printf "$blue<-[ Starting pip package installing ]->\n$reset"  
    printf "\n"
    sleep 1
    p_info "Using file:\t$PIP_PACKAGET_FILE"

    while read current_packaget
    do
        p_info "Installing packaget:\t$current_packaget"
        python3 -m pip install $current_packaget
    done < $PIP_PACKAGET_FILE

    exit 0


# manuel command check for user 
elif [[ "$1" == "--check-commands" ]]; then
    check_reqiered_commands

# handle --help 
elif [[ "$1" == "--help" || "$1" == "-h" ]]; then
    print_help_exit
    

# invalid arg handler 
else

    p_error "Invalid args!"
    print_help_exit

fi
