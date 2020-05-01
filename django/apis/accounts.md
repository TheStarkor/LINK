---
description: User APIs.
---

# Accounts

{% api-method method="get" host="http://127.0.0.1:8000" path="/accounts/api/user" %}
{% api-method-summary %}
User List
{% endapi-method-summary %}

{% api-method-description %}
User List를 반환한다.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
User List successfully retrieved.
{% endapi-method-response-example-description %}

```
[
    {
        "id": 1,
        "email": "ab@a.com",
        "portal_id": "aaa",
        "name": null,
        "dept_major": null,
        "username": "hoho",
        "reputation": 0
    },
    {
        "id": 2,
        "email": "adwdaw@dw.com",
        "portal_id": "bbb",
        "name": null,
        "dept_major": null,
        "username": "gglgg",
        "reputation": 0
    }
]
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="http://127.0.0.1:8000" path="/accounts/api/login" %}
{% api-method-summary %}
Login
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="username" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="password" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-path-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
User successfully login.
{% endapi-method-response-example-description %}

```
{
    "username": "thestar",
    "id": 1
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="http://127.0.0.1:8000" path="/accounts/api/signup" %}
{% api-method-summary %}
Signup
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-body-parameters %}
{% api-method-parameter name="portal\_id" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="username" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="email" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="password" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-body-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
User successfully signup.
{% endapi-method-response-example-description %}

```
{
    "portal_id": "kaist",
    "username": "thestar",
    "email": "sk_and_mc@kaist.ac.kr"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="http://127.0.0.1:8000" path="/accounts/api/findaccount" %}
{% api-method-summary %}
Find Account
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-body-parameters %}
{% api-method-parameter name="portal\_id" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="password" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-body-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
User successfully find own account.
{% endapi-method-response-example-description %}

```
{
    "portal_id": "kaist",
    "email": "sk_and_mc@kaist.ac.kr"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="post" host="http://127.0.0.1:8000" path="/accounts/api/passwordreset/<int:pk>" %}
{% api-method-summary %}
Password Reset
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="pk" type="integer" required=true %}
User's primary key
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}

{% api-method-body-parameters %}
{% api-method-parameter name="username" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="password" type="string" required=true %}

{% endapi-method-parameter %}

{% api-method-parameter name="new\_password" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-body-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
User successfully reset password
{% endapi-method-response-example-description %}

```
{
    "username": "thestar"
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

