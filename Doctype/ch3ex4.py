"""
  >>> whatsthis[2]
  42
  >>> type(whatsthis[4])
  <class 'list'>
  >>> whatsthis[6:8]
  [11, 'what is this?']
  >>> len(whatsthis)
  10
"""
whatsthis = [0,1,42,12,["apple", "grape"],"there",11,"what is this?",10,11]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
