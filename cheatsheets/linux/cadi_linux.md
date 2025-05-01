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