

# Product Architecture

## Interview Details

The interviewer will focus on building a product or API at scale that supports an end user product or service. The focus is on holistic parts of building a software solution and less on the back end components required. Think APIs, data modeling, how the client and server interact, how a user may interact with it.

Let's say you're asked to build a video-only newsfeed interface, how would you build this? Would you use REST API or GraphQL for content? How would you fetch the video stream? How you THINK about the product and its users matters more here than how many server set you need to put on the backend system!

Example product architecture or design questions are:

- Design a service or product API
- Design a chat service or a feed API

The base expectation is that you consider the product needs and design the API to cater to the specific problem you're working on. You should be able to talk about enabling an efficient interaction between the product running on a client and the server. Do API calls require a single round trip between the client and the server or multiple round trips? If the product is latency sensitive, discuss caching and how that might help. What are the shortfalls of caching, for example, the client might need to store state on the device, which then needs to be secured and managed, or the server might need a good invalidation strategy in case the cache is inconsistent.



## Long Term Design

When designing a software system, you often face the challenge of balancing two important considerations: building a system that is capable of handling long-term changes and evolution, while also managing the inherent complexity that can arise as the system grows. Here's a breakdown of this concept:

**Designing for Long-Term:** Designing for the long-term means creating an architecture and structure that can accommodate future changes, updates, and additions to the system. This is essential because software systems rarely remain static; they need to evolve to meet new business requirements, technological advancements, and user expectations.

Key considerations when designing for the long-term include:

1. **Modularity:** Creating components that are modular and loosely coupled. This allows you to modify or replace parts of the system without affecting the entire system.
2. **Abstraction:** Using abstractions and interfaces to hide implementation details. This way, changes to the implementation won't impact other parts of the system.
3. **API Design:** Creating well-defined and versioned APIs that shield users from underlying changes, allowing for gradual updates without breaking compatibility.
4. **Separation of Concerns:** Dividing the system into distinct functional areas, each responsible for a specific aspect of functionality. This makes it easier to manage and update individual components.

**Designing for Complexity:** As a system grows, it can become increasingly complex. Complexity can lead to challenges in understanding, maintaining, and debugging the codebase. It's important to manage complexity to ensure that the system remains manageable by developers.

Strategies for managing complexity include:

1. **Clean Code:** Following best practices for writing clean, readable, and maintainable code. This includes using meaningful variable names, avoiding code duplication, and adhering to coding standards.
2. **Design Patterns:** Applying design patterns to organize code in a structured and consistent manner. Design patterns provide common solutions to recurring design problems.
3. **Documentation:** Creating thorough documentation that explains the system's architecture, components, and how they interact. This helps new developers understand the system more quickly.
4. **Code Reviews:** Implementing a code review process to ensure that code is of high quality and follows established guidelines.

**Balancing Long-Term and Complexity:** The challenge is finding the right balance between designing for long-term changes and managing complexity. It's possible to have a system that's highly modular and designed for future growth but also becomes overly complex due to excessive abstraction or an abundance of unnecessary features.

The key is to design with a clear understanding of the system's requirements, the anticipated future changes, and the trade-offs between flexibility and simplicity. Regularly reassess and refactor the codebase to ensure it aligns with the evolving needs of the application while maintaining readability and manageability.



## Anticipating Change

Explain strategies for designing your system to accommodate future changes and feature additions. Talk about using modular design, microservices architecture, versioned APIs, and maintaining loose coupling between components.

**1. Modular Architecture:** Design your system using a modular architecture where different components have well-defined responsibilities. This enables you to add, remove, or modify features without impacting the entire system. Using microservices or a component-based architecture can facilitate this modularity.

**2. Loose Coupling:** Maintain loose coupling between components. This means that changes to one component should not necessitate changes to others. Loose coupling makes it easier to replace or update individual parts of the system without causing a domino effect of changes.

**3. Versioned APIs:** If your system exposes APIs to external clients or internal modules, use versioning to ensure backward compatibility. This way, as you introduce changes to the API, existing clients can continue functioning with the older version until they are ready to upgrade.

**4. Dependency Management:** Manage dependencies carefully. Use dependency management tools and practices to keep track of third-party libraries and frameworks. Regularly update dependencies to leverage new features and security updates, but be cautious of breaking changes.

**5. CI/CD:** Implement CI/CD pipelines to automate testing, building, and deployment processes. This facilitates the rapid rollout of changes and helps catch issues early in the development cycle.

**6. Feature Flags:** Implement feature flags or toggles that allow you to enable or disable specific features without deploying new code. This can be especially useful when rolling out changes gradually or testing new functionality.

**7. Database Migration Strategies:** Plan for database schema changes by using database migration tools. This ensures that as you modify the database structure, you can easily apply those changes across different environments.

**8. Documentation:** Maintain comprehensive documentation that explains the architecture, design decisions, and the purpose of different components. This helps new team members understand the system and its evolution.

**9. Scalability Considerations:** Design for scalability from the beginning. This involves using scalable infrastructure components and designing for horizontal scaling, so your system can handle increased load as the user base grows.

**10. Agile Development:** Adopt agile practices that encourage iterative development and continuous feedback. This allows you to respond quickly to changing requirements and refine your design as you learn more about user needs.

**11. A/B Testing:** Implement A/B testing to test new features or changes with a subset of users before rolling them out to the entire user base. This mitigates the risk of deploying features that might not resonate well with users.

# Design Framework

## 1) Functional Reqs

**Gather functional requirements.**

Identify business - what part of the business service are we designing

Identify users - who are they, are they internal or external to the organization.

Identify features - focus on the interactions between peers and the system.



## 2) Non Functional Reqs

**Gather non-functional requirements.**

Identify scale

Expected payload size

Data Access Patterns (read write ratio)



## 3) High Level Design

**API design is UX but for developers so keep it simple. Provide what is necessary, no more, no less.** 

Identify entities and relationships

Identify resources and methods



## 4) Deep Dive Design

**Optimizations and improvements.** 

Data Ownership

Security

Scalability

# API Design:

## Client Server Architecture

### Background

Client-server architecture is a fundamental design pattern in software engineering where the functionality of a system is divided between two main components: the client and the server. 

The client is responsible for the user interface and user interactions, while the server manages data storage, processing, and business logic. It promotes a clear separation of concerns, enabling efficient communication, scalability, and maintainability.

### Interaction

The client and server communicate over a network. The client sends requests to the server, and the server responds with the necessary data. Common communication protocols include HTTP/HTTPS, WebSocket, and more. The client can be a web browser, a mobile app, a desktop application, or any other user-facing interface. 

### Benefits

**Scalability:** Separating client and server functionality allows for horizontal scalability. You can scale servers independently from clients, making it easier to handle increased user load by adding more server resources.

**Low Coupling:** The separation allows you to update the client or server components without affecting the other. This modularity simplifies maintenance and reduces the risk of introducing bugs in other parts of the system.

**Security:** Data security can be managed more effectively. Sensitive operations and data can be centralized on the server, reducing the risk of exposure on the client side.

**Performance:** Client-server architecture enables server-side processing, which can offload computation from client devices, leading to faster and more consistent performance.

**Consistency:** Centralized data management on the server ensures that all clients have access to the same data, reducing the risk of data inconsistencies.

**Cross-Platform Compatibility:** A well-defined API allows clients to be developed on various platforms while still communicating with the same server.



## Protocols

### REST APIs

Centered around resource-based interaction over HTTP, requiring statelessness and uniform interface.

### GraphQL

Offers flexible querying and efficient data retrieval. Reduces over-fetching and under-fetching.

### WebSocket

Provides persistent, bi-directional communication for real-time applications (using TCP connection).



## HTTP Methods

### **GET**

This method is used to retrieve data from the server. It's a read-only operation and does not modify any data on the server. It is the method used when you visit a webpage in your browser.

### **POST**

POST is used to send data to the server to create a new resource. It's often used when submitting forms or uploading files. Unlike GET, the data sent through POST is not directly visible in the URI.

### **PUT**

PUT is used to update or create a resource on the server. It's idempotent, meaning if you make the same request multiple times, the result will be the same as making it once.

### **PATCH**

Similar to PUT, PATCH is used to update a resource on the server. However, while PUT updates the entire resource, PATCH is used to apply a partial update, modifying only specific fields.

### **DELETE**

This method is used to request the removal of a resource from the server. It's used to delete the resource specified in the URI.



## About REST APIs

### Key Terms

- **API:** a contract between developer and client.
- **Resource:** an object which that has some associated data to it and as well as a set of methods
    to operate on it. Ex: Posts, users, animals are resources and CRUD operations can be performed on them.
- **Collections:** are a set of resources. Ex: Companies is the collection of a Company resource.
- **Endpoints/URI:** the path through which a resource can be located and some action performed on it.
- **Payload:** refers to data that has been transferred through the REST API
- **Idempotent Methods:** method yields the same response, regardless of how many times a request is sent.
- **Safe Methods:** method that does not change a resource, READs not WRITE. Think GET methods!



### Resource vs Collection 

You would use a **resource** endpoint when you want to perform actions on a specific individual entity, like retrieving, updating, or deleting a single user or article.

You would use a **collection** endpoint when you want to perform actions that involve multiple entities of the same type, like retrieving a list of all users or creating new articles in bulk.



### Key Features

- **Client-Server Interaction:** there will exists a client communicating with a server.
- **Stateless:** Designed on the principle that client should not depend on previous API calls. 
- **Resources:** REST APIs expose resources, which are entities that can be identified by a unique URI (Uniform Resource Locator). Resources can represent real-world objects or abstract concepts.
- **Uniform Interface:** REST APIs maintain a consistent interface for interactions. Each resource is accessed using a unique URI, and the HTTP methods map to an action performed on a resource. There are 4 constrains:
    - Resource Identification: a given resource can be identified by a URI.
        - `GET /employees/1234 => ouputs a resource representation`
    - Resource Manipulation through Representation.
        - `PUT /employees/1234 + a JSON body => resource representations can be used to change data`
    - Self-Descriptive: server tells the client what kind of content is being sent back.
        - Is that resource cacheable?
        - How to process the response? Ex. 'Content-Type: application/json'.
        - How to request the next resource?
    - HATEOS: hypermedia as the engine of application state.
        - Provides a reference as to the next actions available in the resource hierarchy.
- **Cacheable:** a response from a server can define itself as cacheable or not.
    - GET, PUT and DELETE are considered safe, so they can be cached. POST on the other hand can't be cached.
    - Use eTags as they are built for cache signaling.
- **Layered:** the response to a request can come from a web server, load balancer, cache server, cdn, etc.
    - The client doesn't care where it gets its data from, as long as it gets what it asks for.



### HTTP Request

- Method - verb

- URI - used to identify the resource

- HTTP version - 1.1 or 2.0

- Request Header - metadata like message format, cache settings, content format, etc

- Request Body - content (optional)

    

### HTTP Response

- Status Code:
    - Success - 200s
    - Client Side Error - 400s
    - Server Side Error - 500s
- HTTP version - 1.1 or 2.0
- Response Header - metadata like content length, content type, date, etc
- Response Body - content (required)



## Writing REST APIs

### Identify Resources

Understand the resources the application will need. For example:

- Items Resouce: List items, View items, Search items, Add/Edit items, Remove items.
- Orders Resource: List orders, Obtain order status, Cancel orders.



### Identify Activities

Map activities to HTTP nouns and verbs. Determine resource relationships:

* Independent - resources may exists regardless of each other, but they may reference each other.
* Dependent - one resource cannot exists without the other.
* Associative - independent but the relationship contains additional properties to describe it.



### Identify Hierarchy

Using URI hierarchy to represent the relationship of resources. If resources contain sub-resources, make sure to depict this in the API to make it more clear and explicit in relation to the logic.

```
GET /movies/:id/actors
GET /movies/:id/characters
GET /movies/:id/characters/:id
GET /actors/:id/characters/
GET /actors/:id/characters/:id

GET /companies/3/employees - get the list of all employees from company 3
GET /companies/3/employees/45 - get the details of employee 45 from company 3
```

https://developer.twitter.com/en/docs/api-reference-index#twitter-api-v2

https://developers.tiktok.com/doc/tiktok-api-v2-get-user-info/



## Best Practices

### Documentation

Write documentation or leverage OpenAPI / Swagger



### Versioning

Version your APIs `/api/v2/cars`

Can also uses headers for this rather than stating in the URI.



### Data Formats

JSON - lightweight, text-based data interchange format. It's highly readable for both humans and machines and is widely supported in various programming languages. 

Protocol Buffers - a binary serialization format that is highly efficient in terms of both size and speed.



### Headers

Most important headers for your API are:

- Status: the response code of what you are trying to accomplish.
- Content-Type: identifies the type of payload being passed back by the server
- Media-Type: describes the actual structure of the payload and how things work together.



### Responses

Return Representation. Applies to POST, PUT, PATCH methods:

- Always return the updated resource as a response, including its URI in the Location header.
- Also send the appropriate status code (i.e status code 201 if resource is created after using a POST method).

Avoid Nesting. Make your responses flat not nested. Flatter structures are easier to parse and consume.



### Status Codes

Send HTTP status codes:

- 1xx Info
- 2xx Success
- 3xx Redirection
- 4xx Client Errors
- 5xx Server Errors



### Exception Handling

Ensure that you are handling errors with their appropriate code. Add personalized app-specific error messages.



### Idepotency

Idempotent operations (repeated requests producing the same result) allows you to handle repeated requests.



### Filtering

Accept searching, sorting, filtering params for your GET requests!

- Searching:  `GET /companies?search=Facebook`
- Sorting:  `GET /companies?sort=rank_asc`
- Filtering:  `GET /companies?category=banking&location=india`



### Pagination

Implement pagination for large datasets. Instead of sending the entire dataset in a single response, break it into smaller chunks (pages) and allow clients to request subsequent pages as needed. It helps in improving the performance and is easier to handle the response:

- Limit/Offset:  `GET /articles?offset=20&limit=10`
- Page-Based: `GET /companies?page=23&pageSize=100`
- Ranged: `GET /orders?start_date=2023-01-01&end_date=2023-03-31`
- Cursor: `GET /comments?after=comment_12345`



### Validation

Assume all data you're receiving is bad, until it's been validated! Separate validation logic from your route objects. Removes the chance of an SQL Injection.



## Authentication

### API Keys

API keys are unique identifiers (usually alphanumeric strings) that clients include in their requests to authenticate themselves. The server checks the validity of the key to allow or deny access. API keys are simple to implement but may lack fine-grained control and security.

### Token-Based

Tokens, like JSON Web Tokens (JWT), are encrypted strings issued by an authentication server after successful login. The client includes the token in subsequent requests' headers. Token-based authentication is widely used due to its flexibility, statelessness, and ability to store user claims in the token. Among those are bearer tokens

### OAuth

OAuth 2.0 provides a standardized framework for authorization. It enables third-party applications to access a user's data without exposing their credentials. OAuth 2.0 involves a flow where the user grants access, and the app receives an access token to make authorized API requests.



## Authorization

### Role-Based Access Control

RBAC involves assigning specific roles (e.g., admin, user, manager) to users or groups. Each role has associated permissions that dictate what actions they can perform. Access control is then managed by checking a user's role against the required permissions for a resource.

### Attribute-Based Access Control

ABAC considers a wide range of attributes (user attributes, resource attributes, environmental attributes) to determine access. Policies are defined based on these attributes, allowing for dynamic and context-aware access control.

### Permission-Based Access Control

Instead of predefined roles, permission-based access control assigns fine-grained permissions directly to users or groups. Permissions specify what actions are allowed for specific resources (e.g., read, write, delete). This approach offers more flexibility in defining access control.



## Optimization & Scalability 

### Asynchronous

Offload time-consuming tasks to background processing queues or workers. This can help free up API server resources to handle incoming requests more efficiently.



### Server Side Caching 

A client requests the same data multiple times, if we cache the response then less bandwidth is needed and the client may retrieve data faster. Each REST API contains specific metadata related to the caching of response. For example the header of cache control and expires specify what response may be cached, by whom and for how long. 



### Client Side Caching

Storing and reusing web content on the user's device (client) to improve the performance and reduce the need to repeatedly fetch the same content from the server. 



### Reduce Payload Size 

Compression of the response content (gZip, brotli).

Content minification of JSON and assets to reduce response sizes. Use image formats that support efficient compression while maintaining quality.



### Content Delivery Networks

Serve static assets and content through CDNs to reduce the load on your API servers. CDNs distribute content to geographically distributed edge servers, improving content delivery speed.



## API Gateway

### Background

An API Gateway is a server or service that acts as an intermediary between various microservices, applications, or clients and a collection of APIs (Application Programming Interfaces). Its primary purpose is to manage, optimize, secure, and distribute incoming requests to the appropriate backend services or APIs.



### Rate Limiting

API Gateways can control the rate at which requests are allowed to be made to APIs. This prevents abuse and helps maintain the stability and availability of backend services.



### Monitoring

API Gateways often offer analytics and reporting features to provide insights into API usage patterns, performance metrics, and error rates.



### Request Routing

API Gateways can route incoming API requests to the appropriate backend services based on predefined rules. This allows for a unified entry point for multiple APIs, even if they are hosted on different servers or locations.



## Security 

### Guarding Against Spammers or Bad Actors

Discuss strategies like CAPTCHA challenges, IP rate limiting, behavior analysis (e.g., detecting unusual patterns), user reputation systems, and manual review processes. Explain how you would balance security measures with user experience to avoid false positives.



## Personalization

### User Preferences

Allow users to set preferences that affect their experience (themes, notifications, or display options):

- Create endpoints for managing user preferences.
- Use HTTP methods like GET, PUT, or PATCH to retrieve, update, or partially modify preferences.
- Store preferences in a user profile or preferences database table.

Request:

```shell
GET /v1/users/{user_id}/preferences
```

Response:

```json
{
  "theme": "dark",
  "notifications": true,
  "language": "en",
  "location": "us"
}
```



## Localization

### Language

Support multiple languages and localized content for users:

- Use the `Accept-Language` header to determine the user's preferred language.
- Implement language-specific endpoints, e.g., `/articles/{article_id}?lang=en` for English content.
- Store translated content in a way that makes it easy to retrieve based on language codes.

### Location

- Personalize content based on the user's location:
- Use the user's IP address or GPS coordinates to determine their location.
- Have endpoints that serve location-specific content, such as `/events?location={location_id}`.
- Store location data in a structured way, linking it to relevant content.

# Client Design

How you handle user interactions like scrolling, page refreshes etc. You will also want talk about how you can improve user experience by masking latency for server interactions by tweaking the client.

Improving user experience by masking latency for server interactions involves optimizing the perception of speed and responsiveness in your application, even when actual network and server delays are present.

**1. Preemptive Actions and Feedback:** Implement actions that provide immediate visual or interactive feedback to user actions. For example, when a user clicks a button, show a loading animation or feedback indicating that the system has acknowledged the action. This reduces the perceived waiting time and keeps users engaged.

**2. Caching:** Leverage client-side caching to store frequently used data or resources. This minimizes the need for repeated server requests. Consider using browser storage mechanisms like localStorage or sessionStorage to temporarily store data that can be retrieved instantly.

**3. Skeleton Screens:** Instead of showing a blank screen while waiting for content to load, use skeleton screens. These are lightweight representations of the content's layout that give users a visual indication of what's coming. This creates a perception of progress and reduces the feeling of waiting.

**4. Progressive Loading:** Load content progressively, starting with the most crucial elements. For instance, load the main text of an article first and then gradually load images and other non-essential components. This creates a sense of continuous progress.

**5. Lazy Loading:** Implement lazy loading for images, videos, and other media. Load only the visible content initially, and load additional content as the user scrolls down. This reduces initial page load times and provides a smoother experience.

**6. Predictive Fetching:** Anticipate user actions and start fetching required data before the user explicitly requests it. For instance, preload content when hovering over links or buttons, so the content is ready when the user clicks.

**7. Minimize Round-Trips:** Reduce the number of server requests by bundling multiple requests into a single request or utilizing batch processing. Fewer round-trips mean less waiting time for the user.

**8. PWA Techniques:** Utilize Progressive Web App (PWA) techniques such as service workers to cache assets and enable offline access. This provides a seamless experience even when the network connection is slow or unstable.

**9. Visual Effects:** Incorporate subtle animations or transitions to distract users from the actual loading time. Animations can give users the feeling of continuous activity, reducing perceived waiting time.

**10. Quality Content Loading:** Load high-priority content first, ensuring that users see meaningful content before less critical elements. This can apply to text, images, or interactive elements.

# DB Design

## Relational vs NonRelational

Structured data can be easily stored in SQL databases via values for rows and columns. It is highly organized information that uploads neatly into a relational database, they must have a relational key and can be easily mapped into fields.

Unstructured data may have its own internal structure but does not conform neatly into a spreadsheet or database. Most data are unstructured, but it is also where many key insights lay. A NoSQL database lends itself to unstructured data.

## Data Normalization

Data normalization is the process of structuring a relational database to reduce data redundancy and ensure data integrity. It involves breaking down data into smaller, related tables and eliminating duplicate information. This is typically achieved by organizing data into separate tables based on their logical relationships and minimizing data duplication.

The normalization process is divided into several normal forms, each with specific rules for structuring data:

- **First Normal Form (1NF):** Ensures that each column contains atomic (indivisible) values, and each row is uniquely identifiable by a primary key.
- **Second Normal Form (2NF):** Builds upon 1NF by eliminating partial dependencies. In other words, no non-key column should be dependent on only a portion of the primary key.
- **Third Normal Form (3NF):** Further eliminates transitive dependencies, where non-key attributes depend on other non-key attributes.



## Data Denormalization

While normalization improves data integrity and reduces redundancy, it can lead to complex joins and slower query performance, especially for complex queries or large datasets. Denormalization is the process of intentionally introducing redundancy by combining related data into fewer tables to optimize query performance.

Denormalization strategies include:

- **Flattening:** Combining data from multiple normalized tables into a single table. This reduces the need for joins, speeding up queries.
- **Adding Redundant Data:** Storing calculated or frequently accessed data redundantly, reducing the need for expensive calculations or joins.
- **Caching:** Precomputing and storing the results of complex queries to avoid recomputation.



## Normalize vs Denormalize

The decision to normalize or denormalize depends on your application's specific needs:

- **Normalize:** Prioritize data integrity, minimize redundancy, and when the application is more read-heavy with complex updates.
- **Denormalize:** Optimize read-heavy applications with complex queries, reporting, and analytical workloads, where query performance is crucial.

It's important to strike a balance between normalization and denormalization based on your application's usage patterns. Modern databases also offer features like indexing, materialized views, and query optimization that can help mitigate the performance impact of normalization.