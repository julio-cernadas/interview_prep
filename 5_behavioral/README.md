# Behavioral

## Foundation

### Be Authentic

Tell the truth, be honest. Don’t think of the interview as an evaluation, approach the situation as a conversation with a colleague.

### Be Specific

You want to sound impressive but without being arrogant, to do this you must be specific in your responses by just giving the facts and letting the interviewer derive an interpretation.

### Limit Details

Stay light on details and just state the key points. When possible, try to translate it or at least explain the impact. You can always offer the interviewer the opportunity to drill in further.

### Think Before

Don't rush into the answer, think first and find a good story. It's ok to take a couple seconds.



## Responses

### Nugget First

This means starting your response with a "nugget" that succinctly describes what your response will be about.

This technique grabs your interviewer's attention and makes it very clear what your story will be about. It also helps you be more focused in your communication, since you've made it very clear to yourself what the gist of your response is.

```txt
IntervieweResult: "Tell me about a time you had to persuade a group of people to make a big change."

Candidate:"Sure, let me tell you about the time when I convinced my school to let undergraduates teach their own courses."
```

### Situation

Provide context, background, challenges, etc. Your interviewer generally does not need many details to understand what happened and, in fact, may be confused by them so keep this short!

### Action

Explain what you did and how you did it. In almost all cases, the "action" is the most important part of the story. Unfortunately, far too many people talk on and on about the situation, but then just breeze through the action. Instead, dive into the action. Where possible, break down the action into multiple parts, this will encourage sufficient depth. 

### Result

State benefits, outcomes, rewards. The tangible / quantifiable RESULTS of the situation: How did it help the team / company?

Without saying it, your story should display your key attributes.

# So Tell Me About Yourself

## Two Minute Pitch

**Headline:** I'm software engineer at a consulting firm that builds application solutions for hedge funds and trading firms.

**College:** I studied finance at the University of Maryland, where in my junior year I sparked interest in app development, so I joined a summer coding bootcamp in NYC focusing on Python and Fintech development. 

**Onward Situation:** From there I was able to break into the industry at a fintech firm called EZOPs (middle and back office automation) where I focused on extending features and ci/cd development. I became good friends with the CTO and when he left the firm he offered a position for me at his consulting firm.

**Current Role [Details]:** Which was what brought me to Ness where I provide app development, data engineering, and devops services. My latest contract was with MarketAxess where I was able to build up the Index and ETF business and successfully launched a publically listed ETF with State Street.

**Outside of Work**: Outside of work, I'm really into music production (house and hip hop) and fitness (training to run NYC marathon).

**Wrap Up:** Currently I'm looking for some change because although consulting is great, I build up connections and passion for the projects I work on but as a consultant you eventually always have to leave. And I'm looking for some where to stay. 



## Personal Values

**Make Impact** - Be all in, all the time.

**Move Fast** - Speed always wins. 

**Teamwork** - Communication and selflessness. The strength of the wolf is the pack, the strength of the pack is the wolf.

**Dynamic**- Embrace change and take risks. Building great things means taking risks.

**Tactical** - Always plan and seek to have an advantage. Always seek to have a tactical advantage, always have an unfair fight.

# Questions For You

## Challenges

**Tell me about a situation where you had to make a decision with incomplete information. How did you weigh the pros and cons and arrive at a conclusion?**

Situation: Build hedge fund analytics dashboard with minimal business requirements. 

Action:

- Communication with Project Manager. 
- Met with the targets users of the dashboard.
- Determined what questions they wanted answer and gathered intel on their research workflow. 
- Proposed KPIs, metrics, and features that would be useful for them; saught feedback; and adjusted accordingly. 
- The dynamic nature of the problem set led me to choose Tableau as a rapid prototyping tool.

Result: The dashboard was highly effective and useful to business users. 



**Can you provide an example of a time when you had to manage multiple priorities or deadlines simultaneously? How did you organize your work?**

Situation: One client had requested my services for a few weeks while I was still at another client. My firm assigned me to both.

Action: 

- Communication ~ I communicated with team members and managers on both sides. 
- Time allocation ~ I would attend all meetings but would split the week days for each client. 
- Documentation ~ I documented the details my work and shared with team so they could refer to the docs. 
- Task allocation ~ I re-allocated some easier tasks to teammates and chose tasks that could be accomplished independently. 

Result: The current client didn't even notice a difference, and the short term one requested I join them full time. 



**Tell me about a project that you're particularly proud of. What challenges did you face, and how did you overcome them?**

Situation: Just joined my firm, tasked to build POC application for FINRA CAT compliance, I had no background in this area.

Action: 

- Self Education ~ I read existing public documentation on the regulations.
- Research ~ Researched solutions to similar compliance challenges.
- Collaboration ~ met with business analyst to gather functional requirements, understand regulation and generate mock data.
- Drafted architecture and adjusted with senior engineers.

Result: Upper management liked the result, it was added to the suite of client offerings, and led to conversations with AWS.



**Discuss a time when you had to make a difficult decision in a project due to technical limitations or constraints. How did you troubleshoot and overcome the issue?**

Situation: We discovered that an upstream data source was occasionally late arriving and incrementally written.

Action: 

- Communication ~ We highlighted the situation to the owning team but they were very busy for weeks to come. 
- Temporary Solution ~ I couldn't touch their code base, so we needed a temporary solution.
- I setup retries and a polling mechanism that would wait up to 10 minutes for the full data set.

Result: Successfully delivered our service on time and handled inconsistencies without downstream users noticing. 



## Change 

**Describe a situation where a project's requirements changed midway through development. How did you adapt and ensure the project's success?**

Situation: When building indexes the client had a target strategy but quickly pivoted to another. 

Action:

- I learned that we needed a framework and not just individual ETL jobs. 
- I abstracted concepts like universes, instruments, and filters to create a meta data driven framework.
- Adding new indexes and strategies became a breeze.

Result: The client was able to test many strategies and make adjustments accordingly. 



**Discuss when you had to work on a project that required you to step outside your comfort zone and learn something new.**

Situation: There was a big initiative to embrace devops culture at EZOPs. 

Action:

- I had to learn what DevOps was.
- Learn new technologies like Docker, Terraform, Packer, Jenkins, Datadog. 
- Had to learn the AWS ecosystem.

Result: Successfully migrated a legacy deployment process into a modern CI/CD pipeline. Acquired my solutions architecture certificate. 



## Results

**Give an example of a time when you took the initiative to solve a problem without being asked. What was the outcome?**

Situation: The database class logic for a project was very messy. Developers has been complaining.

Action: 

- I refactored the design to support session management, unit of work, refresh connection, ORMs and the repository pattern.
- For each business service I swapped dependency from DB connection classes to Repository classes.
- Moved application boot strap logic to the root layer, allowing Devs to focus on the service layer.

Result: Developers were happier because they could use ORM data models and application start up became faster. 



**Tell me about a project where you took the lead in identifying a problem or inefficiency in the codebase and proposed a solution.** 

Situation: Our app was occasionally missing SLA. So I refactored the bootstrap process on an application.

Action: 

- I refactored the application entry point by adding a service registry which contained a recipe for each service and a reference to it's dependency container. 
- This allowed me to do 2 things: only call the required dependencies and orchestrate the dependency injection for each service.

Result: Application start up became faster and the application became easier to debug. 



**Give an example of a time when you identified an opportunity to improve a process or system. What steps did you take to implement your ideas?**

Situation: A project had many independent batch jobs, difficult to debug and lots of duplicated logic. 

Action: 

- I categorized each job and discovered that there was a trend, enough to create services (feeds, validations, etc)
- I modeled the behavior and stored metadata for how each job would be slightly different than others.
- I used design patterns like the Strategy pattern to create different styles of each service.   

Result: It decoupled the application and allowed for a seperation of domain logic from service logic. Higher productivity. 



**Do you take constructive criticism as an opportunity to improve? How have you approached improving your skills?**

Situation: Pandemic + start of WFH, I began working in silo. One of my colleagues pointed this out and referenced blue angels.

Action:

- Became more interactive with my fellow colleagues. 
- Started a watercooler tech topic channels where we could share news, comedy, and topics. 
- I began calling meetings with developers to review system / software design ideas. 
- I began calling meetings with project managers and business users to gather functional requirements.

Result: I developed a better connection with my colleagues and work became more fun.



**Have you ever had to roadmap or plan a project? Describe steps you take.**

Situation: A new data product service need to be launched. 

Action:

- Gather functional and non-functional requirements. 
- Understand the capacity estimations and SLAs.
- Breakdown the project - data producers/consumers, system design, software design, domain layer.
- Identify existing company resources and contact.
- Produce architecture and design diagrams, review with management and adjust accordingly.
- Prioritize, build the project in stages. End to end solution first. Refined optimized solution later.
- Allocate ownership - Agile / Project Management. 
- Provide an SOW with roadmap/timeline and delivery dates. Agreement with business.
- Execute and regularly review/share weekly progress to management.

Result: A well implemented project with transparency and agreed upon requirements.



## Conflict

**Tell me about a time when you had to work on a challenging team project. How did you handle the conflict?**

Situation: Lead developers left a project due to conflicts with a manager. 

Action:

- Communicated with manager I would need to focus all my time on KT with them.
- Requested to know their exact day to day responsiblities + their vision of the project's future.
- Collaborated with them to write extensive documentation on the software design and future system design.
- Generated a high level integration test to ensure future functionality.
- Applied git tags to the functional version they handed over.

Result: The project was successfully handed over, I became the lead developer for the project and led all tech deliverables. 



**Tell me about a time when you faced a setback or failure. How did you handle it, and what did you learn from the experience?**

Situation: Holidays, calendar logic breaks

Action:

- Short term resolution: I added a force run feature that would handle anamolies. 
- Met with business to understand all possible combinations of calendar date types and expected deliveries.
- Refactored the calendar class this logic and ensured consistent behavior across all services.

Result: We made it through christmas/new years without a single issue. I learned to have foresight of upcoming events and plan accordingly. 



**Describe a situation where you had to work with a difficult colleague or team member. How did you approach the situation and resolve any conflicts?**

Situation: Senior developer onboards project, he became difficult to work and wanted to radically change the design. 

Action:

- There's usually a reason for the action, so I wanted to understand his perspective.
- I scheduled a one on one meeting where I respectfully review what his ideas were and we abstracted them.
- As we conversed, I realized his background was from DevOps and he was intimidated by how the code base alone was able to accomplish a lot without using heavy weight infrastructure like Kakfa or Flink. Especially didn't understand the design patterns.
- I scheduled meetings to deep dive into the codebase and create software design diagrams of the application. 

Result: He was impressed by the approach the application and provided suggestions specifically on what tools existed that we could leverage. We factored in his ideas and the application became even more robust and scalable. 



## Communication

**Describe a situation where you had to give constructive feedback to a colleague or team member. How did you approach the conversation?**

Situation: Tej feedback

Action: 

- Met privately and had a respectful conversation
- Mentioned 3 things: what we should start doing, keep doing, and stop doing
- We promised to check in on each other in a few months to see how we progressed.

Result: The transparency between us grew our relationship and we stay in touch. 



**Give an example of a project where you collaborated effectively with colleagues from different disciplines, such as design or product management.**

Situation: Analytics dashboard, Tableau dev onboarded (George)

Action:

- First formed good rapport with the dev, I recommended a virtual happy hour with the team.
- I studied Tableau vigorously over the weekend and gained as much steam on the project while he was onboarding.
- I gained his respect by demonstrating my quick ability to learn a new technology and show some results.

Result: We worked very well together and business users loved our dashboard.



**Tell me about a time when you faced conflicting priorities from different stakeholders. How did you manage to satisfy everyone's needs?**

Situation: Deployment of a service of to AWS, my consulting manager (deploy it) vs client manager conflict (optimize it).

Action: 

- The business requirement was to deploy the application to AWS, but the client requested a favor to identify where there was a latency bottleneck. 
- I first accomplished the SOW requirements. Then I delegated some complement tasks to other developers and I focused on the clients request.
- I used AWS X-Ray to run monitoring on the software design itself and found the bottleneck. 

Result: Both managers were happy with the result and I formed a stronger personal relationship with the client too.



## Weakness

**Tell me about your weaknesses?**

Perfectionism - spend too much time on insignifcant details, whiles it's good for code quality it does have deminishing returns, which is why I'm finding a balance between deadlines and code quality. 

Overcommitting - sometimes I sign up for too many tasks since I'm ethusiastic for contributing. You're learning to manage your commitments better and communicate more effectively about what you can realistically handle.

# Questions For Them

## Interviewer

- What's your favorite part about working for XYZ?
- Can you describe your experience on latest project you've worked on?



## Business

- Can you walk me through the typical software development lifecycle here, from idea to committed feature?
- Centralized vs decentralized devops model?



## Team

- How do engineers collaborate or communicate across different teams, like to be aware of existing datasets or tooling?
- What style of project management do you guys use: Agile, Waterfall, etc?



## Opportunities

- How does the company encourage innovation and the exploration of new technologies in software development?
- How does the company support and encourage professional development for engineers? Are there opportunities for attending conferences or training courses?