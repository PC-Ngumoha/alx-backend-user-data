# Basic Authentication

## Useful Points

- REST APIs need to be able to authenticate clients that make requests to them in a way that the API can remain stateless. For this reason (i.e _Statelessness_), The regular _Session Storage_ is not really helpful as an authentication mechanism for REST APIs as it requires the client and server to be _Stateful_ and keep track of the state of their previous interactions.

- With that in mind, here are some of the mechanisms used for authentication in REST APIs:

  + **Basic Access Authentication:** This is the most simple of all the available mechanisms. In this, we are simply sending the _username_ and _password_ for the authenticating client every single time we try to access the server. However, there is a small nuance to this. Instead of sending this username and password in the body of out HTTP request as we would have, we send it in the request header. Before we can send it we first need to format the username and password in the following way:

    ```
    <username>:<password>
    ```
  and then, we encode it using Base64 encoding and then we send it using the `Authorization` HTTP header with the Base64 encoded username and password as a basic `Bearer` token that can then be accessed on the server where it accesses the `Authorization` header, decodes the Base64 encoded value and then checks to see if a user with said username and password already exists, if so, it authenticates the user. This mechanism is not a secure method as anyone can access this header and decode it, so we always need to use this over HTTPS.

    * The Advantages:
        - It's simple to implement
        - Enables a stateless server
        - Supported by all browsers

    * The Disadvantages:
        - Requires HTTPS to be secure enough for use
        - Subject to replay attacks (which is a type of attack in which an attacker gets hold of a request and sends it over and over to the server for the purpose of accessing the server. In this case, this will prove extremely effective because the username and password is being sent with every request to the server.)
        - Very tricky to implement a _LogOut_ mechanism.

  + **Digest Access Authentication:** Read more about it [here](https://en.wikipedia.org/wiki/Digest_access_authentication)

  + **Asymmetric Cryptography:** Read more about it [here](https://en.wikipedia.org/wiki/Public-key_cryptography)

  + **OAuth:** Read more about it [here](https://en.wikipedia.org/wiki/OAuth)

  + **JSON Web Tokens (JWT):** Read more about it [here](https://en.wikipedia.org/wiki/JSON_Web_Token)

## Useful Links

- [REST API Authentication Mechanisms (Youtube Video)](https://www.youtube.com/watch?v=501dpx2IjGY)

- [Python base64 package](https://docs.python.org/3.7/library/base64.html)

- [HTTP Header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)

- [Base64 (Wikipedia Article)](https://en.wikipedia.org/wiki/Base64)
