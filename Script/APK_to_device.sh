#!/usr/bin/env bash

function main() {
  echo -ne "\033[36mEnter the APK you want to install: \033[0m"
  read Path

  if [[ -e ${Path} ]]; then
    if [[ -d ${Path} ]]; then
      UNDER_PATH=${Path}
      echo -e "\033[31mError: ${Path} is not a file.\033[0m\nPoint out the files and folders in ${UNDER_PATH}:"
      ls ${UNDER_PATH}
      echo
      main
    elif [[ -f ${Path} ]]; then
      if [[ 'apk' != $(echo "${Path}" | awk -F '[.]' '{print $NF}') ]]; then
        echo -e "\033[31mError: filename doesn't end .apk\033[0m"
        echo
        main
      else
        echo 'Install Task will start in 3s'
        sleep 3
        adb install ${Path}
        if [[ "$?" = "1" ]]; then
          echo -e "\033[31m:-( ERROR FOUND, NOW YOU CAN SAVE THE OUTPUT, AND PRESS ctrl + c TO EXIT.\033[0m"
          sleep 1d
        fi
      fi
    fi
  else
    N=$(echo "${Path}" | awk -F '[/]' '{print $NF}')
    UNDER_PATH=${Path/$N/}
    echo -e "\033[31mError: File ${Path} not found.\033[0m\nPoint out the files and folders in ${UNDER_PATH}:"
    ls $UNDER_PATH
    echo
    main
  fi
}

main
