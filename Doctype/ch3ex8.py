"""
  >>> b_list[1:]
  ['Stills', 'Nash']
  >>> group = b_list + c_list
  >>> group[-1]
  'Young'
"""
b_list = [1, "Stills", "Nash"]
c_list = ["Love", "Young"]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
