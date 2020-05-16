list1=[179,2358,5197,867,163,4418,3135,5049,187,166,4682,5080,5541,172,4294,1397]
list2=[2637,136,3222,591,2593,1982,4506,195,4396,3741,2373,157,4533,3864,4159,142]
list3=[1049,1163,1128,193,1008,142,169,168,165,310,1054,104,1100,761,406,173]
list4=[200,53,222,227,218,51,188,45,98,194,189,42,50,105,46,176]
list5=[299,2521,216,2080,2068,2681,2376,220,1339,244,605,1598,2161,822,387,268]
list6=[1043,1409,637,1560,970,69,832,87,78,1391,1558,75,1643,655,1398,1193]
list7=[90,649,858,2496,1555,2618,2302,119,2675,131,1816,2356,2480,603,65,128]
list8=[2461,5099,168,4468,5371,2076,223,1178,194,5639,890,5575,1258,5591,6125,226]
list9=[204,205,2797,2452,2568,2777,1542,1586,241,836,3202,2495,197,2960,240,2880]
list10=[560,96,336,627,546,241,191,94,368,528,298,78,76,123,240,563]
list11=[818,973,1422,244,1263,200,1220,208,1143,627,609,274,130,961,685,1318]
list12=[1680,1174,1803,169,450,134,3799,161,2101,3675,133,4117,3574,4328,3630,4186]
list13=[1870,3494,837,115,1864,3626,24,116,2548,1225,3545,676,128,1869,3161,109]
list14=[890,53,778,68,65,784,261,682,563,781,360,382,790,313,785,71]
list15=[125,454,110,103,615,141,562,199,340,80,500,473,221,573,108,536]
list16=[1311,64,77,1328,1344,1248,1522,51,978,1535,1142,390,81,409,68,352]

total=0
list1.sort()
total=total+list1[len(list1)-1]-list1[0]

list2.sort()
total=total+list2[len(list2)-1]-list2[0]

list3.sort()
total=total+list3[len(list3)-1]-list3[0]

list4.sort()
total=total+list4[len(list4)-1]-list4[0]

list5.sort()
total=total+list5[len(list5)-1]-list5[0]

list6.sort()
total=total+list6[len(list6)-1]-list6[0]

list7.sort()
total=total+list7[len(list7)-1]-list7[0]

list8.sort()
total=total+list8[len(list8)-1]-list8[0]

list9.sort()
total=total+list9[len(list9)-1]-list9[0]

list10.sort()
total=total+list10[len(list10)-1]-list10[0]

list11.sort()
total=total+list11[len(list11)-1]-list11[0]

list12.sort()
total=total+list12[len(list12)-1]-list12[0]

list13.sort()
total=total+list13[len(list13)-1]-list13[0]

list14.sort()
total=total+list14[len(list14)-1]-list14[0]

list15.sort()
total=total+list15[len(list15)-1]-list15[0]

list16.sort()
total=total+list16[len(list16)-1]-list16[0]

print(total)

test=[125,454,110,103,615,141,562,199,340,80,500,473,221,573,108,536]
for digit in test:
  for num in test:
    res1=(digit/num).round()
    res2=num/digit
    
    for digit in res1:
      if digit==".":
        print(numb)
        print(digit)
        print(digit/num)
    for digit in res2:
      if digit==".":
        print(numb)
        print(digit)
        print(num/digit)


