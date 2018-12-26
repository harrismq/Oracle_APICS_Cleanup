# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 12:06:20 2018

@author: harris.qureshi@oracle.com
"""

IDCS_Access_Token="eyJ4NXQjUzI1NiI6InMzb2UxSWw3VUh6YmwxTHJmNm5yYzlYbGo4NTV4SWlYa0dWOUFQVkJpd2ciLCJ4NXQiOiJmbmVlWWZmY1ZOeE1iQ3p4STJnU00yWDZLTjAiLCJraWQiOiJTSUdOSU5HX0tFWSIsImFsZyI6IlJTMjU2In0.eyJ1c2VyX3R6IjoiQW1lcmljYVwvQ2hpY2FnbyIsInN1YiI6ImhhcnJpcy5xdXJlc2hpQG9yYWNsZS5jb20iLCJ1c2VyX2xvY2FsZSI6ImVuIiwiaWRwX25hbWUiOiJsb2NhbElEUCIsInVzZXIudGVuYW50Lm5hbWUiOiJpZGNzLWIwOTg1ZTMzN2E4YjQ1ODJiMGE5NGUzMTIyNjIwOGY4IiwiaWRwX2d1aWQiOiJsb2NhbElEUCIsImFtciI6WyJVU0VSTkFNRV9QQVNTV09SRCJdLCJpc3MiOiJodHRwczpcL1wvaWRlbnRpdHkub3JhY2xlY2xvdWQuY29tXC8iLCJ1c2VyX3RlbmFudG5hbWUiOiJpZGNzLWIwOTg1ZTMzN2E4YjQ1ODJiMGE5NGUzMTIyNjIwOGY4IiwiY2xpZW50X2lkIjoiNEI2QUYyM0IzRTM3NEMxRThEMjg3RjE0RkQ5QjFDQUZfQVBQSUQiLCJzdWJfdHlwZSI6InVzZXIiLCJzY29wZSI6Ii5hcGlwbGF0Zm9ybSIsImNsaWVudF90ZW5hbnRuYW1lIjoiaWRjcy1iMDk4NWUzMzdhOGI0NTgyYjBhOTRlMzEyMjYyMDhmOCIsInVzZXJfbGFuZyI6ImVuIiwiZXhwIjoxNTQ1ODIyNDM4LCJpYXQiOjE1NDU4MTg4MzgsImNsaWVudF9ndWlkIjoiZTFkODZhMDM2NTM2NDQ2Mjk0MzkzMjc5ZjVhNzVlY2EiLCJjbGllbnRfbmFtZSI6IkFQSUNTQVVUT19hYXBpYWQyIiwiaWRwX3R5cGUiOiJMT0NBTCIsInRlbmFudCI6ImlkY3MtYjA5ODVlMzM3YThiNDU4MmIwYTk0ZTMxMjI2MjA4ZjgiLCJqdGkiOiJkZTQxZmQ5Yy1lODI3LTRmOWQtYWY3OS1iMDZjYjg4ZDBlYTIiLCJ1c2VyX2Rpc3BsYXluYW1lIjoiSGFycmlzIFF1cmVzaGkiLCJzdWJfbWFwcGluZ2F0dHIiOiJ1c2VyTmFtZSIsInRva190eXBlIjoiQVQiLCJhdWQiOlsidXJuOm9wYzpsYmFhczpsb2dpY2FsZ3VpZD00QjZBRjIzQjNFMzc0QzFFOEQyODdGMTRGRDlCMUNBRiIsImh0dHBzOlwvXC80QjZBRjIzQjNFMzc0QzFFOEQyODdGMTRGRDlCMUNBRi5hcGlwbGF0Zm9ybS5vY3Aub3JhY2xlY2xvdWQuY29tOjQ0MyJdLCJ1c2VyX2lkIjoiMzVlOWZjZjI3ZDk3NDkyNDhkNmM3NDFjODk2Mzk4MzAiLCJ0ZW5hbnRfaXNzIjoiaHR0cHM6XC9cL2lkY3MtYjA5ODVlMzM3YThiNDU4MmIwYTk0ZTMxMjI2MjA4ZjguaWRlbnRpdHkub3JhY2xlY2xvdWQuY29tIn0.NlIC9IyKuaqU9qzanKxMSj0z87GhnizpFEvn_wT-gT9r_pH-tJ1agCP3yRfRYX93IUWE-CDCgyD0p0rMxKKfGgSgeb0wONSCe2aTwXGeeXkMd-55wKFk8pOdu5QMla0-EWJxOcgZHq6grAcaFCiaK_4m_VkA9R8-qvbhitavxrBIz3FASMeTbstgkmkQ83iGGQs6VsIKT39-Yt1Zod-tOyEA7bnrG1McDV-uycCLUxOdtySpAakzKQx6m1tHFkDiWUm8LjEYsbOOmSuwlq_tAV592HGlA6pjQc4Wi0aRcPj9rP6E2JHo6kHX81FvzZjx3uXrXXCZ5ovDe_TuGFp5iQ"

API_URL="https://example.com/apiplatform/management/v1/apis"
PLAN_URL="https://example.com/apiplatform/management/v1/plans"

#filters used to select the API Name and Plan Name that you want to delete. 
#Any API's and Plans starting with these identifiers will be deleted

API_Name_Identifier="OrganizationDbi09"
PLAN_Name_Identifier="JAL-API"

#Constants
PUBLICATION_STATE_UNPUBLISHED = "UNPUBLISHED"
PUBLICATION_STATE_PUBLISHED = "PUBLISHED"
SUBSCRIPTION_STATE_SUBSCRIBED = "SUBSCRIBED"
SUBSCRIPTION_STATE_UNSUBSCRIBED = "UNSUBSCRIBED"
CONTENTTYPE_APP_JSON = "application/json"
