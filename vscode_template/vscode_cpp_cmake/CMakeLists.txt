# 工程名称 HW2
project(HW2)

# 规定需要的cmake最低版本
cmake_minimum_required(VERSION 3.0)

# 创建debug版本
set(CMAKE_BUILD_TYPE "Debug")

# 向工程添加存放源文件的子目录 src
# 子文件夹可以有CMakeLists.txt
add_subdirectory(src)
