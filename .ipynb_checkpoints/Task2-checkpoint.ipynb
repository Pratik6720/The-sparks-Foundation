{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The Sparks Foundation IOT and Computer Vision intern\n",
    "\n",
    "## Task -2 Color Identification in Images\n",
    "\n",
    "## By Pratik Jain"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Importing the Required Packages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Variable Declaration For Mouse Pointer Movement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "clicked = False\n",
    "r = g = b = xpos = ypos = 0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Reading the image "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = cv2.imread(\"colorpic.jpg\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Taking colors data as input using Pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "index = ['colors', 'color-names', 'hex-value', 'R-value', 'G-value', 'B-value'] \n",
    "df = pd.read_csv('colors.csv', names = index, header = None)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Function for selecting color of selected point by double clicking the left button of mouse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def selectColor(event, x, y , flags, param):\n",
    "    if event == cv2.EVENT_LBUTTONDBLCLK:\n",
    "        global b,g,r,xpos,ypos,clicked\n",
    "        clicked = True\n",
    "        xpos = x\n",
    "        ypos = y\n",
    "        b,g,r = img[y,x]\n",
    "        b = int(b)\n",
    "        g = int(g)\n",
    "        r = int(r)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Taking a window to display an Image and callback Function for Mouse Events"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "cv2.namedWindow('image')\n",
    "cv2.setMouseCallback('image',selectColor)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  Function for getting color name of selected area"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def getColorName(R,G,B):\n",
    "    minimum = 10000\n",
    "\n",
    "    #  calculate a distance(d) which tells us how close we are to color and choose the one having minimum distance.\n",
    "    for i in range(len(df)):\n",
    "        d = abs(R-int(df.loc[i,'R-value']))+abs(G-int(df.loc[i,'G-value']))+abs(B-int(df.loc[i,'B-value']))\n",
    "        if d<=minimum:\n",
    "            minimum = d\n",
    "            colorName = df.loc[i,\"color-names\"]\n",
    "    return colorName\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  Updates the color name whenever the double click occurs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "while(1):\n",
    "\n",
    "    # We shown the image window\n",
    "    cv2.imshow('image',img)\n",
    "    if(clicked):\n",
    "        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)\n",
    "        text = getColorName(r,g,b)\n",
    "        cv2.putText(img, text, (50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)\n",
    "\n",
    "        if(r+g+b>=600):\n",
    "            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)\n",
    "        \n",
    "        clicked = False\n",
    "\n",
    "    # Exits when the user presses the 'Esc' button\n",
    "    if cv2.waitKey(20) & 0xFF ==27:\n",
    "        break\n",
    "\n",
    "\n",
    "# Clears all the windows       \n",
    "cv2.destroyAllWindows()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
