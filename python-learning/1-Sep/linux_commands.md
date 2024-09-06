# Basic Linux Commands

This guide provides an overview of essential Linux commands, complete with explanations and examples. These commands are fundamental for navigating and managing a Linux system.

## Table of Contents

- [Print Working Directory (`pwd`)](#print-working-directory-pwd)
- [List Directory Contents (`ls`)](#list-directory-contents-ls)
- [Change Directory (`cd`)](#change-directory-cd)
- [Make Directory (`mkdir`)](#make-directory-mkdir)
- [Remove Directory (`rmdir`)](#remove-directory-rmdir)
- [Remove Files or Directories (`rm`)](#remove-files-or-directories-rm)
- [Create an Empty File (`touch`)](#create-an-empty-file-touch)
- [Copy Files or Directories (`cp`)](#copy-files-or-directories-cp)
- [Move or Rename Files or Directories (`mv`)](#move-or-rename-files-or-directories-mv)
- [Concatenate and Display Files (`cat`)](#concatenate-and-display-files-cat)
- [Text Editors (`nano` or `vim`)](#text-editors-nano-or-vim)
- [Print Text to the Screen (`echo`)](#print-text-to-the-screen-echo)
- [Change File Permissions (`chmod`)](#change-file-permissions-chmod)
- [Change File Owner (`chown`)](#change-file-owner-chown)
- [Disk Space Usage (`df`)](#disk-space-usage-df)
- [Disk Usage (`du`)](#disk-usage-du)
- [Process Status (`ps`)](#process-status-ps)
- [Terminate Processes (`kill`)](#terminate-processes-kill)
- [Search Text (`grep`)](#search-text-grep)
- [Search for Files (`find`)](#search-for-files-find)
- [Archive Files (`tar`)](#archive-files-tar)
- [Download Files from the Internet (`wget`)](#download-files-from-the-internet-wget)
- [Transfer Data from or to a Server (`curl`)](#transfer-data-from-or-to-a-server-curl)
- [Secure Shell (`ssh`)](#secure-shell-ssh)
- [Secure Copy (`scp`)](#secure-copy-scp)
- [Package Management (`apt-get` or `yum`)](#package-management-apt-get-or-yum)
- [Manual Pages (`man`)](#manual-pages-man)
- [Command History (`history`)](#command-history-history)
- [Create Shortcuts for Commands (`alias`)](#create-shortcuts-for-commands-alias)
- [Close Terminal Session (`exit`)](#close-terminal-session-exit)

---

## Print Working Directory (`pwd`)

- **Explanation**: Displays the current directory you are in.
- **Example**:
  ```bash
  pwd
  ```
  Output: `/home/user`

## List Directory Contents (`ls`)

- **Explanation**: Lists all files and directories in the current directory.
- **Example**:
  ```bash
  ls
  ```
  Use `ls -a` to include hidden files in the list.

## Change Directory (`cd`)

- **Explanation**: Changes the current directory to another directory.
- **Example**:
  ```bash
  cd /home/user/Documents
  ```

## Make Directory (`mkdir`)

- **Explanation**: Creates a new directory.
- **Example**:
  ```bash
  mkdir new_folder
  ```

## Remove Directory (`rmdir`)

- **Explanation**: Removes an empty directory.
- **Example**:
  ```bash
  rmdir old_folder
  ```

## Remove Files or Directories (`rm`)

- **Explanation**: Deletes files or directories.
- **Example**:
  ```bash
  rm file.txt
  ```
  Use `rm -r directory_name` to delete a directory and its contents.

## Create an Empty File (`touch`)

- **Explanation**: Creates a new empty file or updates the timestamp of an existing file.
- **Example**:
  ```bash
  touch newfile.txt
  ```

## Copy Files or Directories (`cp`)

- **Explanation**: Copies files or directories from one location to another.
- **Example**:
  ```bash
  cp original.txt copy.txt
  ```
  Use `cp -r dir1 dir2` to copy a directory and its contents.

## Move or Rename Files or Directories (`mv`)

- **Explanation**: Moves or renames files or directories.
- **Example**:
  ```bash
  mv oldname.txt newname.txt
  ```
  Use `mv file.txt /home/user/Documents/` to move a file to a different directory.

## Concatenate and Display Files (`cat`)

- **Explanation**: Displays the contents of a file.
- **Example**:
  ```bash
  cat file.txt
  ```

## Text Editors (`nano` or `vim`)

- **Explanation**: Opens a text editor within the terminal.
- **Example**:
  ```bash
  nano file.txt
  ```
  Alternatively, use `vim file.txt` for the `vim` editor.

## Print Text to the Screen (`echo`)

- **Explanation**: Displays a line of text or variables.
- **Example**:
  ```bash
  echo "Hello, World!"
  ```

## Change File Permissions (`chmod`)

- **Explanation**: Modifies the read, write, and execute permissions of a file or directory.
- **Example**:
  ```bash
  chmod 755 script.sh
  ```

## Change File Owner (`chown`)

- **Explanation**: Changes the owner and/or group of a file or directory.
- **Example**:
  ```bash
  chown user:user file.txt
  ```

## Disk Space Usage (`df`)

- **Explanation**: Shows the amount of disk space used and available on the filesystem.
- **Example**:
  ```bash
  df -h
  ```

## Disk Usage (`du`)

- **Explanation**: Estimates file space usage.
- **Example**:
  ```bash
  du -sh foldername
  ```

## Process Status (`ps`)

- **Explanation**: Lists the currently running processes.
- **Example**:
  ```bash
  ps aux
  ```

## Terminate Processes (`kill`)

- **Explanation**: Sends a signal to terminate a process.
- **Example**:
  ```bash
  kill 1234
  ```

## Search Text (`grep`)

- **Explanation**: Searches for a specified pattern in files.
- **Example**:
  ```bash
  grep "hello" file.txt
  ```

## Search for Files (`find`)

- **Explanation**: Searches for files and directories in a directory hierarchy.
- **Example**:
  ```bash
  find /home/user -name "*.txt"
  ```

## Archive Files (`tar`)

- **Explanation**: Archives multiple files into a single file.
- **Example**:
  ```bash
  tar -cvf archive.tar file1.txt file2.txt
  ```

## Download Files from the Internet (`wget`)

- **Explanation**: Downloads files from the internet using HTTP, HTTPS, or FTP.
- **Example**:
  ```bash
  wget https://example.com/file.zip
  ```

## Transfer Data from or to a Server (`curl`)

- **Explanation**: Transfers data from or to a server, often used for interacting with web APIs.
- **Example**:
  ```bash
  curl https://example.com
  ```

## Secure Shell (`ssh`)

- **Explanation**: Connects to a remote machine securely over a network.
- **Example**:
  ```bash
  ssh user@hostname
  ```

## Secure Copy (`scp`)

- **Explanation**: Copies files between hosts on a network.
- **Example**:
  ```bash
  scp file.txt user@remote_host:/home/user/
  ```

## Package Management (`apt-get` or `yum`)

- **Explanation**: Installs, updates, and removes software packages.
- **Example**:
  ```bash
  sudo apt-get update
  sudo apt-get install package_name
  ```
  For CentOS/RHEL, use `yum`:
  ```bash
  sudo yum install package_name
  ```

## Manual Pages (`man`)

- **Explanation**: Displays the manual pages for a command, providing detailed information about how to use it.
- **Example**:
  ```bash
  man ls
  ```

## Command History (`history`)

- **Explanation**: Displays the list of previously executed commands.
- **Example**:
  ```bash
  history
  ```

## Create Shortcuts for Commands (`alias`)

- **Explanation**: Creates an alias (shortcut) for a longer command.
- **Example**:
  ```bash
  alias ll='ls -la'
  ```

## Close Terminal Session (`exit`)

- **Explanation**: Closes the terminal or SSH session.
- **Example**:
  ```bash
  exit
  ```

---

This file provides a comprehensive reference for basic Linux commands. It's intended to help new users become more comfortable with using the command line to navigate and manage a Linux system.
