In order to get the device working on another computer please ensure you have the following libraries avaliable and devices.
Make sure all appropriate tools that you may need are updated.

1.) Raspberry Pi for executing GPIO pin requests with Rasbian OS (may work on other OS but it may not be supported).

2.) You will also need bluepy for using bluetooth low energy devices and libglib2.0-dev.
  a.) in order for you to use bluepy ensure that you have the sudo, pip/pip3, and apt-get installed/updated.
  b.) you can install the required software using this command in the terminal: sudo apt-get install python-pip libglib2.0-dev this will some mandatory libraries.
  c.) Next you can install the blueby library using: sudo pip install bluepy (you can also use pip3 if you prefer python 3.X).
  d.) make sure python is updated and that you have either/both python 2.X or 3.X and check the version for issues (if there are any).
  
During our testing and implimentation of the product we used python 3.9 to run the program and ran it through the terminal using "python3 Dog_Attendant_PI.py"
You can test your bluetooth low energy devices using sudo hcitool lescan to scan for low energy blueetooth devices to check for a mac address
and change the mac address in the code to suit your needs for the product.
