# -*- coding: utf-8 -*-



set1=set(map(int,input("enter element of first set(space-separated)").split()))
set2=set (map(int,input("enter element of second set(space-separated):").split()))
union_set=set1 | set2 #or set1.union(set2)
intersection_set=set1&set2 #or set1.intersection(set2) 
print("union of the sets:",union_set)
print("intersection of the sets:",intersection_set)                    