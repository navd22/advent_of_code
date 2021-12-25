{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "\n",
    "import rich\n",
    "import rich.text\n",
    "import numpy as np\n",
    "\n",
    "STATS = {'start': time.perf_counter(), 'times': []}\n",
    "\n",
    "def print_board(array, highlight=None, length=1, lookup=None, type='d'):\n",
    "    if highlight is None:\n",
    "        highlight = np.zeros_like(array, dtype=bool)\n",
    "    for i, row in enumerate(array):\n",
    "        for j, value in enumerate(row):\n",
    "            if lookup:\n",
    "                v = lookup[value]\n",
    "            else:\n",
    "                v = value\n",
    "            text = rich.text.Text(f'{v:{length}{type}}')\n",
    "            if highlight[i, j]:\n",
    "                text.stylize(style='bold magenta')\n",
    "            rich.print(text, end='')\n",
    "        rich.print()\n",
    "\n",
    "\n",
    "def solution(value):\n",
    "    start = STATS['start']\n",
    "    elapsed = time.perf_counter() - start\n",
    "    STATS['times'].append(elapsed)\n",
    "    part = len(STATS['times'])\n",
    "    print(f\"Part {part} ({elapsed:.02f}: s)\", value)"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
