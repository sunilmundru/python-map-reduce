s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0
count=0.0


for line in s:
  data = line.strip().split('\t')
  paymentType, amount = data

  if paymentType != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(count)+'\n')

    # start over when changing keys
    thisKey = paymentType
    thisValue = 0.0
    count=0.0
    
  
  # apply the aggregation function
  
  count+=1

# output the final entry when done
r.write(thisKey + '\t' + str(count)+'\n')

s.close()
r.close()