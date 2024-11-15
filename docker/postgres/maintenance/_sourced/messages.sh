#! usr/bin/env/ bash

# Just blank(empty) line 
message_newline(){
    echo 
}

# @ means all passed params to the function
message_debug(){
    echo -e "DEBUG: ${@}"
}

message_welcome(){
    echo -e "\e[1m${@}\e[0m"
}
# "\e[1m${TEXT}\e[0m" - ascii code to make our text BOLD!

message_warning(){
    echo -e "\e[33mWARNING\e[0m: ${@}"
    # e[33m means changing color to YELLOW, and e[0m] changing back 
}

message_error(){
     echo -e "\e[31mWARNING\e[0m: ${@}"
         # e[33m means changing color to RED, and e[0m] changing back 
}

message_info(){
     echo -e "\e[37mINFO\e[0m: ${@}"
         # e[33m means changing color to LIGHT GRAY, and e[0m] changing back 
}

message_suggestion(){
     echo -e "\e[33mSUGGESTION\e[0m: ${@}"
         # e[33m means changing color to YELLOW, and e[0m] changing back 
}

message_success(){
     echo -e "\e[32mSUCCESS\e[0m: ${@}"
         # e[33m means changing color to GREEN, and e[0m] changing back 
}