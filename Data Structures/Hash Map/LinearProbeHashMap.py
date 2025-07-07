from HashMap import HashMapBase

class ProbeHashMap(HashMapBase):
    """Hashmap implemented with linear probing for collision resolution."""
    AVAIL = object() #sentinal marks locations of previous deletions

    def is_available(self, j):
        """Return True if index j is available in table."""
        return self.table[j] is None or self.table[j] is ProbeHashMap.AVAIL

    def findslot(self, j,k):
        """
            Search for key k in bucket at index j.

            Return(success, index)tuple,describedasfollows:
            If match was found, success is True and index denotes its location.
            If no match found,success is False and index denotes first available slot.
        """
        firstAvail=None
        while True:
            if self.is_available(j):
                if firstAvail is None:
                    firstAvail=j #mark this as first avail
                if self.table[j] is None:
                    return(False,firstAvail) #search has failed
            elif k==self. table[j].key:
                return(True, j) #found a match
            j=(j+1)%len(self. table) #keep looking(cyclically)
    
    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k,v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key