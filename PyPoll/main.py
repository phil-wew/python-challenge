{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import csv file\n",
    "path = '/Users/philipwewiora/iCloud Drive (Archive)/Desktop/Data/PythonStuff/python-challenge/PyPoll/Resources'\n",
    "csvreader = csv.reader(open(path, 'r'), delimiter = ',')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#inititate vote count\n",
    "votetotal = []\n",
    "\n",
    "#count votes for total\n",
    "for i in csvreader:\n",
    "    print (i)\n",
    "    if len(i) > 0:\n",
    "        if i[0] != 'Voter ID':\n",
    "            votetotal.append(i) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3521001"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#vote total\n",
    "len(votetotal)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#count votes per candidate. Establish candidate name as key in dictionary and +1 vote for every occurence, otherwise start new key for unique candidate name.\n",
    "candidates = {}\n",
    "for i in votetotal:\n",
    "    if i[2] in candidates.keys():\n",
    "        candidates[i[2]] = candidates[i[2]] + 1\n",
    "\n",
    "    else: \n",
    "        candidates[i[2]] = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-----------------\n",
      "Total Votes: 3521001\n",
      "-----------------\n",
      "Khan : 63.000%  (2218231)\n",
      "Correy : 20.000%  (704200)\n",
      "Li : 14.000%  (492940)\n",
      "O'Tooley : 3.000%  (105630)\n",
      "-----------------\n",
      "Winner : Khan\n"
     ]
    }
   ],
   "source": [
    "#Output for terminal and create txt file with results\n",
    "print(\"Election Results\")\n",
    "obj = open('/Users/philipwewiora/iCloud Drive (Archive)/Desktop/Data/PythonStuff/python-challenge/PyPoll/analysis/election_results.txt','w')\n",
    "obj.write(\"Election Results \\n\")\n",
    "\n",
    "print(\"-----------------\")\n",
    "obj.write(\"-----------------\\n\")\n",
    "\n",
    "#total votes equal to length of vote counter\n",
    "print('Total Votes: ' + str(len(votetotal)))\n",
    "obj.write('Total Votes: ' + str(len(votetotal)) + \"\\n\")\n",
    "\n",
    "\n",
    "print(\"-----------------\")\n",
    "obj.write(\"-----------------\\n\")\n",
    "\n",
    "   \n",
    "#using dictionary values and keys show results with candidate, % of votes and raw vote total.\n",
    "for candidate in candidates.keys():\n",
    "   \n",
    "    #find the % of votes a candidate recieved\n",
    "    percent_vote = candidates[candidate] / sum(candidates.values())\n",
    "    \n",
    "    # Candidate name (key) --- percent of vote total they received (*100 to display as a % and limit to three decimal points) --- display raw vote total\n",
    "    print(candidate + \" : \" + \"%.3f\" %(percent_vote*100) + \"%\" + '  (' + str(candidates[candidate])  + ')')\n",
    "    obj.write(candidate + \" : \" + \"%.3f\" %(percent_vote*100) + \"%\" + '  (' + str(candidates[candidate])  + ')' + '\\n')\n",
    "\n",
    "    \n",
    "\n",
    "print(\"-----------------\")\n",
    "obj.write(\"-----------------\\n\")\n",
    "\n",
    "#name of winning candidate\n",
    "print(f\"Winner : \" + max(candidates, key=candidates.get))\n",
    "obj.write (f\"Winner : \" + max(candidates, key=candidates.get) + '\\n')\n",
    "obj.close()"
   ]
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
