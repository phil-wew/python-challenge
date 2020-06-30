{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import csv file\n",
    "path = '/Users/philipwewiora/iCloud Drive (Archive)/Desktop/Data/bootcamp/uofa-phx-data-pt-06-2020-u-c/03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv'\n",
    "csvreader = csv.reader(open(path, 'r'), delimiter = ',')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Date', 'Profit/Losses']\n",
      "['Jan-2010', '867884']\n",
      "['Feb-2010', '984655']\n",
      "['Mar-2010', '322013']\n",
      "['Apr-2010', '-69417']\n",
      "['May-2010', '310503']\n",
      "['Jun-2010', '522857']\n",
      "['Jul-2010', '1033096']\n",
      "['Aug-2010', '604885']\n",
      "['Sep-2010', '-216386']\n",
      "['Oct-2010', '477532']\n",
      "['Nov-2010', '893810']\n",
      "['Dec-2010', '-80353']\n",
      "['Jan-2011', '779806']\n",
      "['Feb-2011', '-335203']\n",
      "['Mar-2011', '697845']\n",
      "['Apr-2011', '793163']\n",
      "['May-2011', '485070']\n",
      "['Jun-2011', '584122']\n",
      "['Jul-2011', '62729']\n",
      "['Aug-2011', '668179']\n",
      "['Sep-2011', '899906']\n",
      "['Oct-2011', '834719']\n",
      "['Nov-2011', '132003']\n",
      "['Dec-2011', '309978']\n",
      "['Jan-2012', '-755566']\n",
      "['Feb-2012', '1170593']\n",
      "['Mar-2012', '252788']\n",
      "['Apr-2012', '1151518']\n",
      "['May-2012', '817256']\n",
      "['Jun-2012', '570757']\n",
      "['Jul-2012', '506702']\n",
      "['Aug-2012', '-1022534']\n",
      "['Sep-2012', '475062']\n",
      "['Oct-2012', '779976']\n",
      "['Nov-2012', '144175']\n",
      "['Dec-2012', '542494']\n",
      "['Jan-2013', '359333']\n",
      "['Feb-2013', '321469']\n",
      "['Mar-2013', '67780']\n",
      "['Apr-2013', '471435']\n",
      "['May-2013', '565603']\n",
      "['Jun-2013', '872480']\n",
      "['Jul-2013', '789480']\n",
      "['Aug-2013', '999942']\n",
      "['Sep-2013', '-1196225']\n",
      "['Oct-2013', '268997']\n",
      "['Nov-2013', '-687986']\n",
      "['Dec-2013', '1150461']\n",
      "['Jan-2014', '682458']\n",
      "['Feb-2014', '617856']\n",
      "['Mar-2014', '824098']\n",
      "['Apr-2014', '581943']\n",
      "['May-2014', '132864']\n",
      "['Jun-2014', '448062']\n",
      "['Jul-2014', '689161']\n",
      "['Aug-2014', '800701']\n",
      "['Sep-2014', '1166643']\n",
      "['Oct-2014', '947333']\n",
      "['Nov-2014', '578668']\n",
      "['Dec-2014', '988505']\n",
      "['Jan-2015', '1139715']\n",
      "['Feb-2015', '1029471']\n",
      "['Mar-2015', '687533']\n",
      "['Apr-2015', '-524626']\n",
      "['May-2015', '158620']\n",
      "['Jun-2015', '87795']\n",
      "['Jul-2015', '423389']\n",
      "['Aug-2015', '840723']\n",
      "['Sep-2015', '568529']\n",
      "['Oct-2015', '332067']\n",
      "['Nov-2015', '989499']\n",
      "['Dec-2015', '778237']\n",
      "['Jan-2016', '650000']\n",
      "['Feb-2016', '-1100387']\n",
      "['Mar-2016', '-174946']\n",
      "['Apr-2016', '757143']\n",
      "['May-2016', '445709']\n",
      "['Jun-2016', '712961']\n",
      "['Jul-2016', '-1163797']\n",
      "['Aug-2016', '569899']\n",
      "['Sep-2016', '768450']\n",
      "['Oct-2016', '102685']\n",
      "['Nov-2016', '795914']\n",
      "['Dec-2016', '60988']\n",
      "['Jan-2017', '138230']\n",
      "['Feb-2017', '671099']\n"
     ]
    }
   ],
   "source": [
    "#initiate counters for months and profits\n",
    "totalprofits = []\n",
    "totalmonths = []\n",
    "\n",
    "#only count rows that aren't empty and without header \n",
    "for i in csvreader:\n",
    "    print(i)\n",
    "    if len(i) > 0:\n",
    "        if i[1] != \"Profit/Losses\":\n",
    "            \n",
    "            #counter for profits and months\n",
    "            totalprofits.append(float(i[1]))\n",
    "            totalmonths.append(i[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "86"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#count length of rows \n",
    "len(totalprofits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "38382578.0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#sum of profits\n",
    "sum(totalprofits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# deltas for differences in profit month to month\n",
    "deltas = []\n",
    "\n",
    "# subtract current months profit from previous to determine the change month-to-month\n",
    "for i in range(1, len(totalprofits)):\n",
    "    lastMonth = totalprofits[i - 1]\n",
    "    thisMonth = totalprofits[i]\n",
    "    deltas.append(thisMonth - lastMonth)\n",
    "    \n",
    "    #determine largest change month-to-month\n",
    "    if (thisMonth - lastMonth) == max(deltas):\n",
    "        maxDifference = thisMonth - lastMonth\n",
    "        maxMonth = totalmonths[i]\n",
    "        \n",
    "    #determine least change month-to-month\n",
    "    if (thisMonth - lastMonth) == min(deltas):\n",
    "        minDifference = thisMonth - lastMonth\n",
    "        minMonth = totalmonths[i]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Feb-2012'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "maxMonth"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Sep-2013'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "minMonth"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-2196167.0"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "minDifference"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1926159.0"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "maxDifference"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-2315.1176470588234"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find average change month-to-month\n",
    "\n",
    "sum(deltas) / len(deltas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "------------------------\n",
      "Total Months : 86\n",
      "Total Profit : 38382578.0\n",
      "Average Change : -2315.1176470588234\n",
      "Greatest Increase in Profits : Feb-2012  1926159.0\n",
      "Greatest Decrease in Profits : Sep-2013 -2196167.0\n"
     ]
    }
   ],
   "source": [
    "#print analysis\n",
    "\n",
    "print(\"Financial Analysis\")\n",
    "obj = open('/Users/philipwewiora/iCloud Drive (Archive)/Desktop/Data/PythonStuff/python-challenge/PyBank/analysis/financial_analysis.txt','w')\n",
    "obj.write(\"Financial Analysis \\n\")\n",
    "\n",
    "print(\"------------------------\")\n",
    "obj.write(\"------------------------ \\n\")\n",
    "\n",
    "print(f\"Total Months : {len(totalmonths)}\")\n",
    "obj.write(f\"Total Months : {len(totalmonths)} \\n\")\n",
    "\n",
    "print(f\"Total Profit : {sum(totalprofits)}\")\n",
    "obj.write(f'Total Profit : {sum(totalprofits)} \\n')\n",
    "\n",
    "print(f\"Average Change : {sum(deltas) / len(deltas)}\")\n",
    "obj.write(f'Average Change : {sum(deltas) / len(deltas)} \\n')\n",
    "\n",
    "print(f'Greatest Increase in Profits : {(maxMonth)}  {(maxDifference)}')\n",
    "obj.write(f'Greatest Increase in Profits : {(maxMonth)}  {(maxDifference)} \\n')\n",
    "\n",
    "\n",
    "print(f'Greatest Decrease in Profits : {minMonth} {minDifference}')\n",
    "obj.write(f'Greatest Decrease in Profits : {minMonth}  {minDifference} \\n')\n",
    "obj.close()\n",
    "\n",
    "\n",
    "      "
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
