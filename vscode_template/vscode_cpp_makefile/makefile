# target ... : prerequisites ...
#             command

hw2 : hw2.o solution.o
	g++ -o hw2 hw2.o solution.o #注意前面必须是tab，不能是空格
hw2.o : hw2.cpp solution.h
	g++ -g -c hw2.cpp
solution.o : solution.h solution.cpp
	g++ -g -c solution.cpp
clean :
	-rm hw2.o solution.o hw2

# 更稳健的写法：  
# .PHONY : clean	# ‘.PHONY’——伪目标 
# clean :
# 	-rm edit $(objects)		# ‘-’——出错则跳过