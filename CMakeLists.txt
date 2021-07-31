set(PROJECT_NAME CppProject)
PROJECT(${PROJECT_NAME})
SET(CMAKE_C_COMPILER "clang")
SET(CMAKE_CXX_COMPILER "clang++")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

message("project name: " ${PROJECT_NAME})
message("project directory: " ${PROJECT_SOURCE_DIR})

cmake_minimum_required(VERSION 3.11)

add_definitions(-std=c++17)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)

include_directories(
    ${PROJECT_SOURCE_DIR}/include

    /usr/local/include
    /usr/include
)

link_directories(
    ${PROJECT_BINARY_DIR}/target/lib

    /usr/local/lib
    /usr/lib
)

add_subdirectory(lib)

enable_testing()
add_subdirectory(ut)
