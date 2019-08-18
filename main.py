#!/usr/bin/env python3

# -- coding: utf-8 --


class HttpsResponse:
    def __init__(self, http_request_message):
        self.http_request_message = http_request_message

    def parse(self):
        """
        解析HTTP Request报文
        :return: 字典
        """
        pass

    def message(self):
        """
        根据Request报文，打印用户上传的参数
        :return:
        """
        info_dict = self.parse()

        # info_dict['body']['username']
        # info_dict['body']['password']
        response_message = ""

        return response_message

http_request_message = \
    "POST /index?arg=test HTTP/1.0\r\n" \
    "Host: www.example.com\r\n" \
    "Accept: */*\r\n" \
    "Content-Length: 12\r\n" \
    "Content-Type: application/x-www-form-urlencoded\r\n" \
    "\r\n" \
    "username=foo&password=bar"


response = HttpsResponse(http_request_message)

print(response.message())
