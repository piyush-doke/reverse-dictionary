# Import the required modules -------------------------------------------------
from __future__ import print_function
import json
import time
import gensim
# -----------------------------------------------------------------------------


# Create a priority queue class -----------------------------------------------
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.maxLen = 20

    def __str__(self):
        result = 'Top ' + str(len(self.queue)) + ' results\n\n'
        for i, item in enumerate(self.queue):
            result += str(i + 1) + ' ' + item[0] + ' - ' + str(item[1]) + '\n'
        return result

    def isEmpty(self):
        return len(self.queue) == []

    def push(self, data):
        self.queue.append(data)
        self.queue = sorted(self.queue, key = lambda x: x[1])
        if len(self.queue) > self.maxLen: del self.queue[self.maxLen]

    def pop(self):
        if len(self.queue) > 0:
            smallestElement = self.queue[0]
            del self.queue[0]
        else:
            smallestElement = None
        return smallestElement
# -----------------------------------------------------------------------------


# Load the dictionary ---------------------------------------------------------
print('\nLoading Dictionary...', end=' ')
with open('dictionary.json') as dictFileHandle:
    data = dictFileHandle.read().strip()
fullEngDict = json.loads(data)
print('Done!')
# -----------------------------------------------------------------------------


# Load the word2vec model -----------------------------------------------------
print('Loading Word2Vec Model...', end=' ')
model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
print('Done!\n')
# -----------------------------------------------------------------------------


# Search for the word ---------------------------------------------------------
while True:
    query = raw_input('Enter the phrase to search (press x to exit): ')
    if query == 'x': break
    alpha = set(raw_input('Enter the first letter of the expected result (press 0 to search in full dictionary): ').lower())

    # Restrict the size of the dictionary -------------------------------------
    engDict = dict()
    print('Restricting the size of the Dictionary...', end=' ')
    if alpha == set('0'):
        print('Zero given')
        alpha = range(ord('a'), ord('z')+1)
        alpha = set(map(chr, alpha))
    for key in fullEngDict.keys():
        if key.lower()[0] in alpha:
            engDict[key] = fullEngDict[key]
    print('Done!')

    # Search in the dictionary ------------------------------------------------
    a = time.time()
    resultBuffer = PriorityQueue()
    print('Searching from', len(engDict),'different keys, please wait')
    for key, valueList in engDict.items():
        wmDist = 0
        for value in valueList:
            wmDist = model.wmdistance(query, value)
            resultBuffer.push((key, wmDist))
    b = time.time()
    print('Time taken:', b-a)
    print(resultBuffer)
# -----------------------------------------------------------------------------
