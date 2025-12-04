CC = clang
CXX = clang++
CFLAGS = -Wall -O2 -fPIC
CXXFLAGS = -Wall -O2 -fPIC -std=c++11
LDFLAGS = -shared

SRC_DIR = src/core
BUILD_DIR = build
BIN_DIR = bin

SOURCES = $(wildcard $(SRC_DIR)/**/*.c $(SRC_DIR)/**/*.cpp)
OBJECTS = $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.o,$(patsubst $(SRC_DIR)/%.cpp,$(BUILD_DIR)/%.o,$(SOURCES)))

all: dirs libfire

dirs:
	@mkdir -p $(BUILD_DIR)
	@mkdir -p $(BIN_DIR)

libfire: $(SRC_DIR)/libfire.c
	$(CC) $(CFLAGS) -o $(BUILD_DIR)/libfire.o -c $(SRC_DIR)/libfire.c
	$(CC) -o $(BUILD_DIR)/libfire.so $(BUILD_DIR)/libfire.o $(LDFLAGS)

clean:
	rm -rf $(BUILD_DIR)
	rm -f $(BIN_DIR)/fire-*

.PHONY: all clean dirs
