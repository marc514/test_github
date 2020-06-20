# 规定需要的cmake最低版本
cmake_minimum_required(VERSION 3.0)

# 工程名称 HW2
project(main_proj)

FIND_PATH(LIBDB_CXX_INCLUDE_DIR
        ./inc)

# 根目录/代码路径
aux_source_directory(. DIR_MAIN)

SET(SRC_LIST main.cpp
        inc/solution.cpp
        src/hello.cpp)

# 创建debug版本
set(CMAKE_BUILD_TYPE "Debug")

# 编译成可执行文件
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/build)
add_executable(main.out ${SRC_LIST})
