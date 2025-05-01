# Cheatsheet for CADI Ubuntu Linux Desktop 

## How to get an account?

Contact Quentin or David. They will create a user for you.

## How do I log in?


### 1. Remote Desktop / GUI

- from the DFO Software Center, look for and download `ThinLinc`

![img_2.png](static/img_2.png)

- Open the client and simply enter your credentials:

![img_9.png](static/img_9.png)

- You can use the `F8` key to play around with the display settings, e.g. full screen mode
- If you close the window without logging out first, your user will still be logged in. In other words, closing the terminal on the Windows side does not log you out. 



### 1. Command Line Interface (CLI)

####  Windows Command Prompt / Powershell
- Open a terminal with Windows `Command Prompt` or `Powershell`
- type the following command `ssh myusername@glf-science-cadi.ent.dfo-mpo.ca` followed by `yes` and then your password.

#### SSH with MobaXterm (this tool is great)

- Download MobaXterm: [https://mobaxterm.mobatek.net/](https://mobaxterm.mobatek.net/)

- Create a new session

![img_8.png](static/img_8.png)

- Enter the following information

![img_10.png](static/img_10.png)

- The new session will be saved and can be accessed by the sessions sidebar
- MobaXterm supports X11 forwarding so you can do neat things such as typing in `rstudio` in the command line and the program will open up for you in Windows


## Who else is currently logged into the linux box?

Open up a terminal (`Ctrl` + `Alt` + `T`) and type the following: `w`

![img_6.png](static/img_6.png)

## How can I copy files from my DFO computer to the linux computer

Your user profile should come with the DFO Gulf Science network share pre-mounted in your home directory:

![img_12.png](static/img_12.png)

You can use this as a way to move files back and forth.

It is also possible to access your NAS shares from this environment. 
Unlike the DFO Windows computers, these can be mapped without any issue. 

## Using local storage

Your user profile should come pre-mounted with a folder called `my_hot_storage` in your home directory:

![img11.png](static/img11.png)


## Installing a Specific R Version (SUDO privileges required)
from [here](https://docs.posit.co/resources/install-r/#specify-r-version)

```bash
R_VERSION=4.2.3
curl -O https://cdn.rstudio.com/r/ubuntu-2204/pkgs/r-${R_VERSION}_1_amd64.deb
sudo gdebi r-${R_VERSION}_1_amd64.deb
sudo ln -s /opt/R/${R_VERSION}/bin/R /usr/local/bin/R${R_VERSION}
sudo ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/local/bin/Rscript${R_VERSION}
```

From a terminal, you can open up a console by typing `R${R_VERSION}`, (e.g. `R4.3.2`) followed by `enter`.

## How to point R Studio to a different R Version

In linux when r studio opens up, it will load the version of R that is pointed to by the environmental variable called `RSTUDIO_WHICH_R` or to the path as specified by `which R`.
If both of these are empty, R studio will not load.

To point your profile's R Studio to a different version of R, do the following:

- Make sure the version you want to use is actually installed (see above)
- Open up a terminal (`Ctrl` + `Alt` + `T`) and type the following: `nano ~/.profile`
- Update the following line: `export RSTUDIO_WHICH_R=/opt/R/x.x.x/bin/R` where `x.x.x` is the version you want to be using e.g., `4.4.3`
- Log out and log back in.


**Note to the geeks**: There is a complication when accessing ubuntu desktop via windows remote connection. The .profile file is not sourced / re-sourced.  


## ADMB

- We installed ADMB 13.1 at the system level under the `opt` directory
- There is a symlink to the admb executable which was placed in `/usr/local/bin` and therefore the `admb` command should be available from anywhere in the terminal. 
- If in the future we need to install different versions of ADMB, we should reassign the symlink to contain the version, e.g. `admb13.1`



# ADMIN: Bash cmds to run when creating a new account:

```bash

USER=lastnamef
PASS=123456
USER_HOME="/home/$USER"
sudo useradd -m -p "$(openssl passwd -6 $PASS)" -s /bin/bash $USER
R_PATH="/opt/R/4.4.3/bin/R"
# ll $R_PATH
echo "export RSTUDIO_WHICH_R=$R_PATH" | sudo tee -a /home/$USER/.profile 
echo "export GIT_SSL_NO_VERIFY=1" | sudo tee -a /home/$USER/.profile 
mkdir /hot_stuff/$USER
sudo chown -R $USER:$USER /hot_stuff/$USER
sudo chmod -R 770 /hot_stuff/$USER
sudo ln -s /hot_stuff/$USER /home/$USER/my_hot_storage
echo "# YOUR HOT STORAGE FOLDER

### GENERAL:

- This folder is situated on a locally installed solid state drive (SSD). 
- It is an optimal location for storing data and data products associated with analyses conducted on this workstation.
- Using this folder, as opposed to a remote location, can help limit bottlenecks in your analyses.   

### PERMISSIONS

- Only the user **$USER** has permission to read/write/execute from this folder.

### DISCLAIMER

- **THIS DRIVE IS NOT BACKED UP**
- Please ensure that all files placed in this location are backed up else where." | sudo tee -a /home/$USER/my_hot_storage/README.md

# prime the fstab for user entries:
FSTAB_ENTRY="
# $USER"
echo $FSTAB_ENTRY | sudo tee -a /etc/fstab

# Create the smb credential file, if not already present
touch "$USER_HOME/.smbcredentials"
echo "user=$USER" | sudo tee -a $USER_HOME/.smbcredentials
echo "password=...." | sudo tee -a $USER_HOME/.smbcredentials

# Create the root folder for the shares in the users home dir
SHARES_HOME="$USER_HOME/shares"
sudo mkdir $SHARES_HOME

# do this for every share they care about
SHARE=my_fav_share
SHARE_DIR=$SHARES_HOME/$SHARE
sudo mkdir $SHARE_DIR
FSTAB_ENTRY="//glfscidm002/$SHARE $SHARE_DIR cifs credentials=$USER_HOME/.smbcredentials,_netdev,x-systemd.after=network-online.target,uid=$USER 0 0"
echo $FSTAB_ENTRY | sudo tee -a /etc/fstab

# Add a user writeable folder from the aquarescommon share
AQUA_NETWORK_SHARE="//ENT.dfo-mpo.ca/dfo-mpo/GROUP/GLF/Regional_Shares/AquaRes_Common/CadiBox/$USER"
AQUA_LOCAL_SHARE=$SHARES_HOME/AquaRes_$USER
sudo mkdir $AQUA_LOCAL_SHARE
FSTAB_ENTRY="$AQUA_NETWORK_SHARE $AQUA_LOCAL_SHARE cifs credentials=/home/fishmand/.dfosmbcredentials,_netdev,x-systemd.after=network-online.target,uid=$USER 0 0"
echo $FSTAB_ENTRY | sudo tee -a /etc/fstab

# then finally
sudo systemctl daemon-reload; sudo mount -a

# add a README to the network share
echo "### GENERAL:

- This folder has been mounted in order to facilitate the transfer of files between your DFO computer and this workstation. 
- The full network path to this folder is: **$AQUA_NETWORK_SHARE**. 

### PERMISSIONS

- From within this workstation, only the user **$USER** has permission to read/write/execute from this folder. 
- From the DFO Network, anybody who can access the **AquaRes_Common** share can access this folder.

### DISCLAIMER

- DFO Network shares fall outside of the purview of CADI.
- Backups and recoveries are handled via IT Service Desk / Shared Service Canada." | sudo tee -a $AQUA_LOCAL_SHARE/README.md

 

# READ ONLY DRIVES as symlinks
sudo ln -s /mnt/AquaRes_Common /home/$USER/shares/AquaRes_Common_ReadOnly 
sudo ln -s /mnt/HD2 /home/$USER/shares/HD2_ReadOnly 



```

### R snipet for dealing with filepaths

```r
if(.Platform$OS.type == "unix") {
  # assumes share is mounted by system administrator
  aqua_res_path <- "/mnt/AquaRes_Common"
} else {
  aqua_res_path <- "//ENT.dfo-mpo.ca/dfo-mpo/GROUP/GLF/Regional_Shares/AquaRes_Common"
}
fish_fram_path <- paste(aqua_res_path,"FishFramSci", sep="/")
list.files(fish_fram_path)
```