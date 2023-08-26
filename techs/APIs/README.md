# Web APIs

A **web API** is an API that can be accessed using the HTTP protocol.

## API Types


### API types by audience

1. Public APIs

Public APIs may also be called external or open APIs. These APIs are available for anyone to use with little to no restriction, though many require registration and authentication, often via an easy-to-grab API key. Public APIs are generally easy to access because they are intended for the public to use and designed to encourage new use cases and integrations. Public APIs may require agreeing to a terms of use or impose rate-limiting on requests by free accounts, but they make access open to anyone who complies, without extensive verification of the user’s identity or use case.


2. OpenAPI standard

Many public APIs follow the OpenAPI standard. Previously known as Swagger, the OpenAPI standard is a specification for writing a public API, with guidelines for details like endpoint naming conventions, data formats, and error messaging. The standards required by OpenAPI and its automation of some tasks make it easier for a developer to start working with an API without needing to read through a complex code base. For API producers, the OpenAPI standard offers access to a wide variety of tools based on the standard. API teams can use these tools to quickly up mock servers and create high-quality documentation, among other tasks.

3. Private / internals APIs

Meanwhile, private or internal APIs are designed for use within a closed group of API consumers, usually a private company or institution. To interact with the data in a private API, a developer typically needs to be actively granted permission to access it, because the data and functionality available through the API are proprietary to the company. Private APIs are often set up with extensive logging and load-balancing capabilities because they must have greater fault tolerance and security than public APIs. They also do not follow the OpenAPI standard as consistently as public APIs. Since private API producers and consumers typically work together closely, data formats can be negotiated based on specific use cases.

4. Partner APIs

Partner APIs exist somewhere between public and private APIs. They often function to share data between two companies or organizations for a specific business purpose, while still ensuring strict privacy protection. For example, your company’s HR team might access a partner API from a payroll provider that serves many other businesses and needs to ensure each customer can only access data about their own employees. Perhaps you’ve used personal finance tools that allow you to share access to your checking account with your retirement planning application. You would not be able to connect your personal website to your bank’s API because you have not met their audit standards for an approved institutional partner, but you can authorize the two companies to share information about your accounts via their partner APIs.


### API types by architecture

1. Monolithic APIs

Most public APIs are monolithic APIs, meaning they are architected as a single, coherent codebase providing access to a complex data source. Monolithic APIs are familiar to most web developers, and they often closely follow the architecture of a relational database or MVC (model-view-controller) application. They provide predictable functionality across a range of resources, and they generally remain fairly stable over time because they serve so many different use cases for so many different users.

However, as the name implies, monolithic APIs can be difficult to scale or refactor, because so much data is interconnected within them. When developers worry about releasing “breaking changes,” they are often working with monolithic architectures, where changing even minor details can have unpredictable consequences.

2. Microservices APIs

The main alternative to a monolith is a microservices API architecture, in which each API serves a narrow and specific purpose. This architecture is more common for internal and partner APIs, though public APIs may also be part of an organization’s overall microservices architecture. Most development teams using a CI/CD (continuous integration/continuous deployment) process make use of many microservices as part of their code lifecycle, each serving a discrete, independent purpose. An e-commerce company, for example, might have an internal microservice that provides inventory data, and another to validate employee geolocation on changes to inventory data, while software developers pushing code automatically call microservices for testing and governance. As workflows change, individual microservices can be swapped out, updated, or sunsetted without affecting other parts of the system.

3. Composite APIs

Microservices come with an obvious drawback, which is that they generate an enormous number of individual API calls. Two additional API architecture types offer solutions to that problem. A composite API is a special API type that lets you hit multiple API endpoints on a single call. It’s not uncommon for APIs to include some overlapping data at different endpoints, and a composite API can streamline API calls by identifying the most efficient set of calls to deliver the necessary data. Additionally, composite APIs can be used to bundle calls for common use cases, like creating a new user account. By sending a single payload to multiple endpoints, a composite API can deliver greater data fidelity and reduce the volume of data being sent. Composite APIs often coordinate authentication and data formats through an API gateway.

4. Unified APIs

A unified API is similar to a composite API, but instead of bundling calls to multiple endpoints on a single API, it bundles related calls to multiple different APIs. Unified APIs are common among partner APIs. Personal finance applications are a good example to illustrate how they work: Imagine that you are looking at a financial planning application, where you have several different accounts linked. Each of the companies holding those accounts may have a different authentication protocol and data format requirement. The application could send a separate API request to each custodian to get current account balances, but this could create a lot of duplicate code and potential threading complications, and it would potentially expose more sensitive data in the browser. A unified API works as a clearinghouse, allowing your financial planning application to send a single HTTP request to a single endpoint. Then, secure servers handle mapping the data from that request to the required formats for each financial institution and return data to the client-side application in a predictable and controlled way.


### API Protocols

Understanding what protocol an API uses is just as important as knowing what type it is. The protocol defines how your API connects to the internet and how it communicates information. The protocol you choose will determine how you design and build your API, as well as what’s required to maintain it, so it’s important to understand the advantages and drawbacks of each choice.

1. REST APIs

The Representational State Transfer (REST or RESTful) protocol is probably the best-known API protocol. The REST protocol defines routes with a URL … and that’s it. That simplicity is a big advantage compared to other protocols that require the developer to wrap routes with XML. The drawback is that REST APIs can only transmit information through the HTTP protocol, which means they are limited to sending text and not much else.

API developers can use formatting parameters to make text transmissions usable in more complex ways, such as by specifying a content type in the header to transmit images or audio files, but those files will still be encoded as text, generally in either JSON or XML format. REST APIs are still used for an incredible range of functions, but it takes some creativity to work within the constraints of REST and HTTP.

Additionally, while REST protocol makes lots of suggestions about how HTTP transmissions should be formatted, there is no enforcement mechanism. That makes this type of API less reliable in some scenarios, because both the API producer and consumer must make their applications resilient to bad requests and unexpected data payloads. The lack of enforcement also means that web APIs can deliver data in a truly platform-agnostic format, which enables API consumers to be more flexible in how they use the data they receive.

Once you have decided to use the REST protocol, it’s important to understand the architectural requirements for a REST API. Those requirements include:

- **Client-server architecture**: The API interface remains on the client and is separated from the data kept on the server.
- **Statelessness**: Each request made with the API is independent of all others and calls are made independently of one other.
- **Cacheable**: A REST API response may be able to retrieve cached data, but you need to specify whether or not your responses can be cached.
- **Layered**: The API works the same whether it interacts directly with the server or if there are other layers, like a load balancer or proxy service, between the client and the server.


2. SOAP APIs

The Simple Object Access Protocol (SOAP) is another major API protocol. A SOAP API can communicate over other major internet communication protocols, such as TCP and SMTP, in addition to HTTP. In that regard, it is more flexible than REST, but in most ways, SOAP is more restrictive. SOAP APIs can only work with XML data and have much more rigid requirements for requests. SOAP requests also generally require more bandwidth than REST, and building and maintaining SOAP code is more complex.

One major advantage of SOAP is that it requires metadata files describing requests, which makes exchanges more predictable. It also enables stateful requests, unlike REST, which is stateless. Having a more standardized protocol allows SOAP APIs to communicate more complex data reliably, and to deliver it over more channels than just HTTP. SOAP’s use of service interfaces instead of simple URL-based organization can also lead to greater discoverability for knowledgeable users. In general, SOAP is a better fit for more sophisticated applications, where reliability is more important than speed or usability by a public audience. As a result, it’s widely used in financial services and in large enterprise applications like Salesforce.

3. RPC APIs

The Remote Procedure Call (RPC) protocol can return XML or JSON responses. It differs from SOAP and REST APIs in a few key ways. As the name suggests, this protocol calls a method rather than a data resource. While a RESTful API returns a document, the response from an RPC server is confirmation that the function was triggered, or an error indicating why it failed to run. In other words, a REST API works with resources, while an RPC API works with actions.

Another key difference is that a REST API shows the server and the query parameters in its routes, while an RPC’s URI identifies only the server. RPC APIs are rarely public APIs; triggering methods on remote servers is not something most companies want to allow for the general public. Calling an RPC server actually changes the state of the server, so it goes beyond the stateless/stateful distinction between REST and SOAP. As a result, RPC APIs must have a high level of security and trust between producers and consumers, which is why they are most often private APIs. Discoverability and predictability are thus less important for RPC APIs than they are for REST or SOAP APIs, while reliability and performance are more important.

One of the most common use cases for RPC APIs is distributed client-server applications. Payloads are light and limited to parameters for the methods being called, and front-end developers can access server methods without worrying about details like opening and closing connections or parsing inputs. Methods can be called from remote locations, meaning client applications can be hosted entirely separately from the remote backend server that hosts the functions and data. Task threading is also simplified, compared to calling methods locally, because a multi-threaded process can run on the remote server without impacting the client application.

In 2015, Google introduced a type of RPC called gRPC, which uses [Protocol Buffers](https://protobuf.dev/) to serialize and parse data. The advantage of a Protocol Buffer is that the response can be parsed much faster than with the JSON encoding used in REST, and with greater control than XML. gRPC is built on HTTP/2, an update to HTTP that was introduced in 2015. While most browsers are now capable of handling HTTP/2 transparently, gRPC makes use of parts of the protocol that are not exposed in the browser. That means that if you want to work with gRPC in the browser, you will need a proxy service like [envoy](https://www.envoyproxy.io/docs/envoy/latest/start/sandboxes/grpc_bridge), which may make it less useful for websites or browser-based apps.

4. GraphQL APIs

While GraphQL isn’t really a separate protocol, it is a distinct query language, with best practices for its use. GraphQL uses HTTP, similar to a REST API, transmitting text data in the payload of each request, but its approach is different.

A REST API has multiple endpoints, each representing a different data schema. To get the information you need, you must map your requirements to the existing schema and call the appropriate endpoints. GraphQL APIs typically have a single endpoint, but effectively unlimited data schemas available at that endpoint. The API user must know what data fields are available, but they can write a query that combines those fields in whatever order they want. Queries are sent in the payload of an HTTP POST request, and data is returned in the shape of the schema specified by the query.

GraphQL provides users a lot of flexibility within a single query, compared to a REST API’s strict routing requirements. It can also make caching data a challenge and makes the API consumer responsible for maintaining consistent query syntax to get comparable data. Additionally, to use a GraphQL API, the user must know what fields exist in order to write a query. For users to get the most out of a GraphQL API, you will have to provide more extensive custom documentation than for a comparable REST API, and there are fewer tools available to automate the process. If speed is a priority, either for deployment or integration, it may make sense to stick with a more formulaic protocol like REST.