#ifndef RESTCLIENT_H
#define RESTCLIENT_H

#include <string>
#include <curl/curl.h>

class RestClient {
public:
    std::string get(const std::string& url);
    
private:
    static size_t WriteCallback(void* contents, size_t size, size_t nmemb, std::string* response);
};

#endif // RESTCLIENT_H
