/*
 * Firelib Core Library
 * Minimal C implementation for performance-critical operations
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <dirent.h>

#define FIRELIB_VERSION "0.1.0"

/* Get Firelib version */
const char* fire_version() {
    return FIRELIB_VERSION;
}

/* Fast directory size calculation */
long long fire_dir_size(const char* path) {
    DIR *dir;
    struct dirent *entry;
    struct stat statbuf;
    long long total = 0;
    char filepath[1024];
    
    dir = opendir(path);
    if (!dir) return -1;
    
    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;
        
        snprintf(filepath, sizeof(filepath), "%s/%s", path, entry->d_name);
        
        if (lstat(filepath, &statbuf) == 0) {
            if (S_ISDIR(statbuf.st_mode)) {
                total += fire_dir_size(filepath);
            } else {
                total += statbuf.st_size;
            }
        }
    }
    
    closedir(dir);
    return total;
}

/* Check if path exists */
int fire_exists(const char* path) {
    return access(path, F_OK) == 0 ? 1 : 0;
}

/* Create directory recursively */
int fire_mkdir_p(const char* path) {
    char tmp[1024];
    char *p = NULL;
    size_t len;
    
    snprintf(tmp, sizeof(tmp), "%s", path);
    len = strlen(tmp);
    
    if (tmp[len - 1] == '/')
        tmp[len - 1] = 0;
    
    for (p = tmp + 1; *p; p++) {
        if (*p == '/') {
            *p = 0;
            mkdir(tmp, 0755);
            *p = '/';
        }
    }
    
    return mkdir(tmp, 0755);
}
