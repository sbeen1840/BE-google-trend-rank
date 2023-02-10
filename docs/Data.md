# class `Data`

`__init__`

> a class named Data with a constructor method __ __init__ __() that sets the following variables:

- parameters: 

  `numb`: number of top keywords to extract (defaults to 2)
  
  `lang`: language to use with pytrends (defaults to 'ko')
  
  `time`: timezone to use with pytrends (defaults to 540)
  
  `geo`: location to use with pytrends (defaults to 'KR')
  
  `month`: number of months from the current time to retrieve data for (defaults to 3)
  
  `update`: frequency to update the data (defaults to 1 sec)
  
  `address`: file path to a CSV file that contains keywords
  
  `dicts`: a placeholder for the data (defaults to 7)
  
  

`read_csv`

  > reads the CSV file and creates two lists: lines and keys. 
  > lines is a list of lists containing similar keywords. 
  > keys is a list of representative keywords.



`py_trends`

  > uses the pytrends library to retrieve data for the keywords and computes the sum of the data for each keyword. 
  > The sums are stored in a list sums.



`to_json`

 >  converts the keys and sums lists into a JSON file.
