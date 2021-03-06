# NOTE: Generated By HttpRunner v3.1.3
# FROM: har/mubu.har
from httprunner import Parameters
import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from httprunner直播.demo.testcases.mubu_login_test import TestCaseMubuLogin as MubuLogin


class TestCaseMubuCreate(HttpRunner):
    # @pytest.mark.parametrize(
    #     "param",
    #     Parameters(
    #         {
    #             "title-node1text-node2text": [
    #                 ["demo1", "1abc", "1def"],
    #                 ["demo2", "2abc", "2def"],
    #             ],
    #         }
    #     ),
    # )
    # def test_start(self, param):
    #     super().test_start(param)

    config = Config("testcase description").verify(False).base_url("https://mubu.com") \
        .variables(
        **{
            "host": "mubu.com",
            "phone":"19945635122",
            "password":"123456",
            "title":"test1",
            "node1text":"node1",
            "node2text":"node2"


        }
    )
#export从login输出需要的变量值，实现跨脚本的变量传递
    teststeps = [
        Step(
            RunTestCase("login mubu").with_variables(phone="19945635122",password="123456").call(MubuLogin).export(*["unreadCount"])
        ),
        Step(
            RunRequest("/api/list/create_doc")
                .post("/api/list/create_doc")
                .with_headers(
                **{
                    "content-length": "17",
                    "unreadCount":"'$unreadCount'",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "x-requested-with": "XMLHttpRequest",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/list",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_cookies(
                **{
                    "_ga": "GA1.2.1509225228.1595645061",
                    "data_unique_id": "c4c1aa63-cc8a-40c1-bd5e-368b7c69464e",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1595654108",
                    "mubu_inner": "1",
                    "s_v_web_id": "kd17h9te_kcbr4MS4_S8N8_48iv_8agO_teIOtEdLmFsT",
                    "language": "en-US",
                    "country": "US",
                    "_gid": "GA1.2.2055068782.1595832349",
                    "reg_entrance": "https%3A%2F%2F${host}%2F",
                    "csrf_token": "496a39f8-6d42-4a89-bb66-4c35ad7b6b58",
                    "SESSION": "a436e48e-855e-4892-a203-54874e66a421",
                    "_gat": "1",
                    "reg_prepareId": "1738f30a169-1738f30a098-4e10-8111-7afa34f205b3",
                    "reg_focusId": "147b36a4-86a8-4e10-8111-1738f30a576",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "user_persistence": "e28a89d6-2288-4247-af6f-d8ac334c870f",
                    "SLARDAR_WEB_ID": "5f6ef0a9-6ff2-4847-ad5e-d378a0f25800",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1595835199",
                }
            )
                .with_data({"folderId": "0", "type": "0"})
                .extract()
                .with_jmespath("body.data.id", "docId")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/doc${docId}")
                .get("/doc${docId}")
                .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://${host}/list",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_cookies(
                **{
                    "_ga": "GA1.2.1509225228.1595645061",
                    "data_unique_id": "c4c1aa63-cc8a-40c1-bd5e-368b7c69464e",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1595654108",
                    "mubu_inner": "1",
                    "s_v_web_id": "kd17h9te_kcbr4MS4_S8N8_48iv_8agO_teIOtEdLmFsT",
                    "language": "en-US",
                    "country": "US",
                    "_gid": "GA1.2.2055068782.1595832349",
                    "reg_entrance": "https%3A%2F%2F${host}%2F",
                    "csrf_token": "496a39f8-6d42-4a89-bb66-4c35ad7b6b58",
                    "SESSION": "a436e48e-855e-4892-a203-54874e66a421",
                    "_gat": "1",
                    "reg_prepareId": "1738f30a169-1738f30a098-4e10-8111-7afa34f205b3",
                    "reg_focusId": "147b36a4-86a8-4e10-8111-1738f30a576",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "user_persistence": "e28a89d6-2288-4247-af6f-d8ac334c870f",
                    "SLARDAR_WEB_ID": "5f6ef0a9-6ff2-4847-ad5e-d378a0f25800",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1595835199",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/api/document/get")
                .post("https://api2.${host}/v3/api/document/get")
                .with_headers(
                **{
                    "content-length": "22",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "x-request-id": "bb365dab-6e95-47bc-b50f-d47a1f3e831e",
                    "content-type": "application/json;charset=UTF-8",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"docId": "${docId}"})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "Success")
        ),
        Step(
            RunRequest("/v3/api/user/current_level")
                .post("https://api2.${host}/v3/api/user/current_level")
                .with_headers(
                **{
                    "content-length": "28",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "x-request-id": "198feb33-536d-45a1-aace-110074e1cc85",
                    "content-type": "application/json;charset=UTF-8",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json({"document_id": "${docId}"})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "OK")
        ),
        Step(
            RunRequest("/v3/api/user/current_user")
                .post("https://api2.${host}/v3/api/user/current_user")
                .with_headers(
                **{
                    "content-length": "0",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "x-request-id": "8065ef70-a2f4-4d54-aace-14d719ec3cb2",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_data("")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "success")
        ),
        Step(
            RunRequest("/v3/api/user/get_user_params")
                .post("https://api2.${host}/v3/api/user/get_user_params")
                .with_headers(
                **{
                    "content-length": "0",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "x-request-id": "edc2ba06-6d9a-4136-ad98-c476f4f9efa8",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_data("")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "success")
        ),
        Step(
            RunRequest("/v3/api/user/get_invite_count")
                .get("https://api2.${host}/v3/api/user/get_invite_count")
                .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "x-request-id": "3a0d2884-6adf-4a3a-bd9d-52ed3164430c",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/register")
                .get("https://api2.${host}/v3/api/colla/register")
                .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "x-request-id": "533be322-21c5-4e77-b63b-67bfef87f696",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "Success")
        ),
        Step(
            RunRequest("/v3/api/colla/members")
                .options("https://api2.${host}/v3/api/colla/members")
                .with_params(**{"memberId": "${get_memberId()}", "documentId": "${docId}"})
                .with_headers(
                **{
                    "accept": "*/*",
                    "access-control-request-method": "GET",
                    "access-control-request-headers": "data-unique-id,jwt-token,request-id,x-request-id",
                    "origin": "https://${host}",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/api/colla/members")
                .get("https://api2.${host}/v3/api/colla/members")
                .with_params(**{"memberId": "${get_memberId()}", "documentId": "${docId}"})
                .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "request-id": "members:${get_memberId()}:1595835201908",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "x-request-id": "a34aad68-f2bb-43ff-ad39-52f0e4db5fc6",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "success")
        ),
        Step(
            RunRequest("/v3/api/colla/message")
                .post("https://api2.${host}/v3/api/colla/message")
                .with_headers(
                **{
                    "content-length": "456",
                    "member-id": "${get_memberId()}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "request-id": "MESSAGE:8362658:${get_memberId()}:3",
                    "x-request-id": "c53c6f11-ac45-449e-9eeb-063e21f25f74",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json(
                {
                    "engineType": "MUBU",
                    "messageType": "BROADCAST",
                    "reqId": 3,
                    "requestId": "MESSAGE:8362658:${get_memberId()}:3",
                    "token": "${docId}",
                    "data": {
                        "message": {
                            "type": "CHANGE",
                            "documentId": "${docId}",
                            "version": 0,
                            "content": [
                                {"name": "nameChanged", "title": "${title}", "original": "${title}"},
                                {"name": "nameChanged", "title": "${title}", "original": "${title}"},
                                {
                                    "name": "nameChanged",
                                    "title": "${title}",
                                    "original": "${title}",
                                },
                            ],
                        }
                    },
                    "context": {
                        "os": "macOS",
                        "osVersion": "10.15.6",
                        "appVersion": "1.0.0.268",
                        "platform": "web",
                    },
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "success")
        ),
        Step(
            RunRequest("/v3/api/colla/message")
                .with_variables(nodeId='91f054f94dbabd68d7924270bb47e837')
                .post("https://api2.${host}/v3/api/colla/message")
                .with_headers(
                **{
                    "content-length": "474",
                    "member-id": "${get_memberId()}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "request-id": "MESSAGE:8362658:${get_memberId()}:5",
                    "x-request-id": "8b133c45-ab30-401e-b9cc-68f599e2a9a5",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json(
                {
                    "engineType": "MUBU",
                    "messageType": "BROADCAST",
                    "reqId": 5,
                    "requestId": "MESSAGE:8362658:${get_memberId()}:5",
                    "token": "${docId}",
                    "data": {
                        "message": {
                            "type": "CHANGE",
                            "documentId": "${docId}",
                            "version": 1,
                            "content": [
                                {
                                    "name": "nameChanged",
                                    "title": "${title}",
                                    "original": "${title}",
                                },
                                {
                                    "name": "nameChanged",
                                    "title": "${title}",
                                    "original": "${title}",
                                },
                                {
                                    "name": "nameChanged",
                                    "title": "${title}",
                                    "original": "${title}",
                                },
                            ],
                        }
                    },
                    "context": {
                        "os": "macOS",
                        "osVersion": "10.15.6",
                        "appVersion": "1.0.0.268",
                        "platform": "web",
                    },
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "success")
        ),
        Step(
            RunRequest("/v3/api/colla/message")
                .post("https://api2.${host}/v3/api/colla/message")
                .with_headers(
                **{
                    "content-length": "364",
                    "member-id": "${get_memberId()}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "request-id": "MESSAGE:8362658:${get_memberId()}:7",
                    "x-request-id": "41836a15-3e9d-4ab1-b17c-920d4b6a7a58",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json(
                {
                    "engineType": "MUBU",
                    "messageType": "BROADCAST",
                    "reqId": 7,
                    "requestId": "MESSAGE:8362658:${get_memberId()}:7",
                    "token": "${docId}",
                    "data": {
                        "message": {
                            "type": "CHANGE",
                            "documentId": "${docId}",
                            "version": 2,
                            "content": [
                                {
                                    "name": "nameChanged",
                                    "title": "${title}",
                                    "original": "${title}",
                                }
                            ],
                        }
                    },
                    "context": {
                        "os": "macOS",
                        "osVersion": "10.15.6",
                        "appVersion": "1.0.0.268",
                        "platform": "web",
                    },
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "success")
        ),
        Step(
            RunRequest("/v3/api/colla/message")
                .post("https://api2.${host}/v3/api/colla/message")
                .with_headers(
                **{
                    "content-length": "478",
                    "member-id": "${get_memberId()}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "request-id": "MESSAGE:8362658:${get_memberId()}:8",
                    "x-request-id": "920462ef-16af-44ea-81cd-ea77a4f9a367",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json(
                {
                    "engineType": "MUBU",
                    "messageType": "BROADCAST",
                    "reqId": 8,
                    "requestId": "MESSAGE:8362658:${get_memberId()}:8",
                    "token": "${docId}",
                    "data": {
                        "message": {
                            "type": "CHANGE",
                            "documentId": "${docId}",
                            "version": 3,
                            "content": [
                                {
                                    "name": "create",
                                    "created": [
                                        {
                                            "index": 0,
                                            "parentId": None,
                                            "node": {
                                                "id": "91f054f94dbabd68d7924270bb47e837",
                                                "text": "",
                                                "modified": "${get_timetamp()}",
                                                "children": [],
                                            },
                                            "path": ["nodes", 0],
                                        }
                                    ],
                                }
                            ],
                        }
                    },
                    "context": {
                        "os": "macOS",
                        "osVersion": "10.15.6",
                        "appVersion": "1.0.0.268",
                        "platform": "web",
                    },
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "success")
        ),
        Step(
            RunRequest("/v3/api/colla/message")
                .post("https://api2.${host}/v3/api/colla/message")
                .with_headers(
                **{
                    "content-length": "545",
                    "member-id": "${get_memberId()}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "request-id": "MESSAGE:8362658:${get_memberId()}:10",
                    "x-request-id": "42b19fdb-9c85-4f2c-8713-6ef13ba6f709",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json(
                {
                    "engineType": "MUBU",
                    "messageType": "BROADCAST",
                    "reqId": 10,
                    "requestId": "MESSAGE:8362658:${get_memberId()}:10",
                    "token": "${docId}",
                    "data": {
                        "message": {
                            "type": "CHANGE",
                            "documentId": "${docId}",
                            "version": 4,
                            "content": [
                                {
                                    "name": "update",
                                    "updated": [
                                        {
                                            "updated": {
                                                "id": "91f054f94dbabd68d7924270bb47e837",
                                                "text": "<span>${node1text}</span>",
                                                "modified": 1595835205759,
                                            },
                                            "original": {
                                                "id": "91f054f94dbabd68d7924270bb47e837",
                                                "text": "",
                                                "modified": "${get_timetamp()}",
                                            },
                                            "path": ["nodes", 0],
                                        }
                                    ],
                                }
                            ],
                        }
                    },
                    "context": {
                        "os": "macOS",
                        "osVersion": "10.15.6",
                        "appVersion": "1.0.0.268",
                        "platform": "web",
                    },
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "success")
        ),
        Step(
            RunRequest("/v3/api/colla/message")
                .post("https://api2.${host}/v3/api/colla/message")
                .with_headers(
                **{
                    "content-length": "480",
                    "member-id": "${get_memberId()}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "request-id": "MESSAGE:8362658:${get_memberId()}:12",
                    "x-request-id": "5c2c9ae3-c322-4df3-b7eb-9433301e9976",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json(
                {
                    "engineType": "MUBU",
                    "messageType": "BROADCAST",
                    "reqId": 12,
                    "requestId": "MESSAGE:8362658:${get_memberId()}:12",
                    "token": "${docId}",
                    "data": {
                        "message": {
                            "type": "CHANGE",
                            "documentId": "${docId}",
                            "version": 5,
                            "content": [
                                {
                                    "name": "create",
                                    "created": [
                                        {
                                            "index": 1,
                                            "parentId": None,
                                            "node": {
                                                "id": "43211165dfaa1dc05bd9b0a3e4890849",
                                                "text": "",
                                                "modified": "${get_timetamp()}",
                                                "children": [],
                                            },
                                            "path": ["nodes", 1],
                                        }
                                    ],
                                }
                            ],
                        }
                    },
                    "context": {
                        "os": "macOS",
                        "osVersion": "10.15.6",
                        "appVersion": "1.0.0.268",
                        "platform": "web",
                    },
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "success")
        ),
        Step(
            RunRequest("/v3/api/colla/message")
                .post("https://api2.${host}/v3/api/colla/message")
                .with_headers(
                **{
                    "content-length": "545",
                    "member-id": "${get_memberId()}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "data-unique-id": "723e89b0-cfdb-11ea-9e64-e5c89e5bd0b5",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiODM2MjY1OCIsImV4cCI6MTU5ODQzNjYzMSwiaWF0IjoxNTk1ODQ0NjMxfQ.kUkcPuVPHByqKqaIVVgVFCtMJzIBLvxWSC7tR5TTNDSkJYb6QXIKyQ4lPRffLsrsXrN_NDdg_hjGzyR7jVZXQQ",
                    "request-id": "MESSAGE:8362658:${get_memberId()}:14",
                    "x-request-id": "7bbcd993-d53c-440f-9a8c-a8ac3c84fa36",
                    "origin": "https://${host}",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://${host}/doc${docId}",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
                .with_json(
                {
                    "engineType": "MUBU",
                    "messageType": "BROADCAST",
                    "reqId": 14,
                    "requestId": "MESSAGE:8362658:${get_memberId()}:14",
                    "token": "${docId}",
                    "data": {
                        "message": {
                            "type": "CHANGE",
                            "documentId": "${docId}",
                            "version": 6,
                            "content": [
                                {
                                    "name": "update",
                                    "updated": [
                                        {
                                            "updated": {
                                                "id": "43211165dfaa1dc05bd9b0a3e4890849",
                                                "text": "<span>${node2text}</span>",
                                                "modified": 1595835207953,
                                            },
                                            "original": {
                                                "id": "43211165dfaa1dc05bd9b0a3e4890849",
                                                "text": "",
                                                "modified": "${get_timetamp()}",
                                            },
                                            "path": ["nodes", 1],
                                        }
                                    ],
                                }
                            ],
                        }
                    },
                    "context": {
                        "os": "macOS",
                        "osVersion": "10.15.6",
                        "appVersion": "1.0.0.268",
                        "platform": "web",
                    },
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", "success")
        ),
    ]


if __name__ == "__main__":
    TestCaseMubuCreate().test_start()
