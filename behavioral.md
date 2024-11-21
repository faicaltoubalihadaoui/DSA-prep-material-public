# Tell me about yourself : 

I am an experienced software engineer with around 3 years in end-to-end software development, scalable system design, and real-time data analytics. My most recent experience is at Amadeus, the world pioneer for Travel Distribution and IT solutions for travel.
I led the full system dev life cycle for multiple european railway projects putting customer at the heart of my responsability and daily job.

I also co founded the monitoring and analytics team within our department driving a huge improvement in system performance.

# What excites you about the job 

What excites me about the software developement Engineer position at Amazon Security Platform is the opportunity to put my hands-on the thematic of cyber security in a world full of cyber threaths and security concerns is growing exponentially. So, the desire to put my software engineering skills from solution design, implementation, testing, automated deployments alongside the skills of AWS's engineers and security experts to maintain and protect Amazon's operations ensuring very high standards


# Why Amazon ?
Joining Amazon has been a very long standing aspiration and one of the biggest goals of mine. I am inspired by Amazon's culture and I truly find a huge match between my personality characters and amazon leadership principles, some of the principles I ve been applying then since a long time in my daily life.

My very first experience with Deployment and cloud infra was on AWS ...
- Learned my first knowledge of the Cloud 
- EC2 instance 
- Security Groups ( VPS )
- Load balancind auto scaling
- AWS RDS
- Controlling Billing


Make sure you refer to the learning for failing experiences, you ability to learn and apply that learning elsewhere
constructive learning, how you would change the process to improve it 
Satisfying whoever that customer is, diving into a situation to get more experience 

# Behavioral Questions ( STAR )


## <span style="color: #26B260">Story 1 -  Critical Deadline and Customer Trust - SBB Feature Delivery
## <span style="color: #26B260"> Customer Obsession / Ownership / Bias for Action / Deliver Results  : 

# Questions :

- Tell me about a time you delivered results despite a tight deadline.
- Describe a time when you had to deal with customer expectations and how you managed to meet them.
- Give me an example of a situation where you took ownership of an issue and successfully delivered.


Situation:

As a software engineer at Amadeus in the Rail Department, I was working on a critical feature for SBB railway clients. The feature aimed to include bike ancillaries and tickets within travelers’ bookings. The project was nearing its delivery deadline, with the MVP requiring an 80% success rate for shopping, booking, and ticketing tests. However, our booking tests were failing at a 60% success rate due to persistent issues with three key tests, putting the feature’s delivery—and the client relationship—at significant risk.

Task:

I needed to investigate and resolve the booking issues swiftly to meet the 80% success criterion within two working days. The resolution required a fix, a devops pipeline load, and UAT testing, all within the tight deadline to avoid delays, potential fines, and client dissatisfaction.

Action:

As the booking flow expert, I quickly identified the root cause of the issues causing test failures.
Recognizing the team’s growing pressure, I proposed a detailed plan to address the challenges.
    I prioritized resolving the issue immediately, staying late into the night to implement and test fixes.
    Coordinated with the DevOps team to expedite pipeline loading under exceptional measures.
    Encouraged the Scrum Master to document risks and inform stakeholders transparently about the mitigation plan.
I collaborated with teammates to review and validate the solution, ensuring its robustness for client presentation.

Result:

By morning, I resolved the booking flow issues, achieving the 80% success rate required for MVP. The fix was loaded successfully into UAT, and I presented the updated results in the client meeting. The timely resolution not only saved the project from missing its deadline but also avoided financial penalties and strengthened the client’s trust in our team’s ability to deliver under pressure.


## <span style="color: #26B260"> Centralized Monitoring Solution - Argos Suite with Prometheus
## <span style="color: #26B260"> Invent and Simplify - Learn and Be Curious - Think Big - Insist on the Highest Standards - Bias for Action

Questions:

- Tell me about a time when you created a solution that simplified a complex problem.
- Describe a situation where you had to innovate and think outside the box to improve a process.
- Share an example where you had to balance cost efficiency with quality in your work.
- Tell me a time when you disagreed with a teamate and it turned out that your solution was better 
- Tell me about a time when you had to convince team members of something you proposed.


Situation:

As part of the monitoring team in the Rail Department at Amadeus, we were tasked with replacing a legacy monitoring solution with the Argos suite using Prometheus for monitoring and alerting. The challenge was pushing metrics from dozens of components, each with unique logic and frameworks, to a central endpoint for Prometheus scraping. The initial proposed solution required implementing decentralized, component-specific monitoring logic—a time-intensive and fragmented approach that risked inconsistency and scalability issues.

Task:

I aimed to deliver a streamlined and scalable monitoring solution that avoided redundant development efforts and aligned with the highest standards of efficiency and maintainability.

Action:

I disagreed politely with the straightforward approach and was against the idea of dispatching it to the teams for implementation as I wanted the good for the team ( modulable solution efficient and not time consuming ) ( disagree and have backbone )

I took the initiative to dive deep into the architecture of all Python components, studying their unique frameworks and workflows to understand their complexities. This process helped me uncover opportunities to unify their monitoring logic. ( Learn and Be Curious )

I envisioned a centralized library that could handle the monitoring needs of all components, ensuring scalability and simplifying future maintenance. I recognized that a unified solution could serve as a long-term asset for the team, beyond just the current migration project. ( Think Big )

Using my understanding of the components, I developed a modular library leveraging context servers and configuration maps. This library identified common entry and exit points across components, enabling centralized metric handling ( Invent and Simplify )

I ensured that the library met rigorous quality standards by conducting thorough testing during its initial integration with one component. I worked closely with the team to validate its performance and scalability before rolling it out to the rest of the components.
Bias for Action: Despite the initial push for a decentralized approach, I acted quickly to implement the proof of concept, demonstrating the viability and efficiency of the centralized solution. ( Insist on the Highest Standards )

Result:

The centralized library eliminated the need for component-specific monitoring logic, saving substantial development time and ensuring consistent monitoring across the system. This solution significantly accelerated the project timeline, reduced complexity, and set a new standard for monitoring frameworks within the team. It also strengthened the system’s scalability and maintainability, proving valuable for future projects.



## <span style="color: #26B260"> Legacy Code Incident Resolution - Maintenance Rotation
## <span style="color: #26B260"> Dive Deep - Think Big - Frugality - Earn Trust  - Customer Obsession

Questions:

- Tell me about a time you had to dive deep into a complex issue to find a solution.
- Describe a situation where you had to solve a problem while maintaining a long-term vision.
- Give me an example of a time when you earned the trust of others through your actions.
- Tell me about a time when you had to make a decision based on data and were ultimately wrong.

Situation:

During a maintenance rotation in the Rail Department, I was assigned a high-urgency, medium-severity incident involving legacy C++ code. The issue prevented us from computing train itineraries in Northern Europe, specifically in Sweden, leading to missed shopping solutions and financial impact for the business.

Task:

My task was to investigate the issue and come up with a solution within a short timeframe to avoid further disruptions and potential financial losses.

Action:

Dive Deep: I thoroughly analyzed the legacy codebase, despite its size and complexity. I delved ( dove ) into both the technical and functional components to understand the root cause of the issue. This detailed investigation took a week, but I wanted to make sure I understood the full scope of the problem.

Think Big: While addressing the immediate issue, I recognized an opportunity to think beyond just fixing the problem. I envisioned a long-term solution that could be scaled and applied to similar issues in the future, ultimately reducing future incidents and improving the maintainability of legacy systems. I proposed this broader vision to my manager and worked towards creating a solution that aligned with the long-term goals of the department.

Frugality: I solved the problem efficiently by using existing resources and tools. Instead of creating an overly complex solution or requesting extra resources, I leveraged the current framework to build a simple, effective fix that required minimal investment, both in terms of time and resources.

Earn Trust: By taking ownership of the issue, diving deep to understand the problem, and proposing a scalable solution, I earned the trust of my manager and colleagues. The client even personally reached out to thank me, solidifying the trust between the team and the client. This proactive, results-driven approach showed that I could be relied upon for critical tasks.

Result:

The fix resolved the issue, allowing the affected shopping offers to work properly and preventing financial losses. Additionally, the solution I proposed was scalable and could be applied to similar situations in the future, resulting in increased efficiency and reduced dependency on legacy systems. My actions earned the trust of both internal and external stakeholders, and the client acknowledged my direct involvement and ownership of the issue.


## <span style="color: #26B260"> Splitting logic 
- Tell me about a time when you had a dispute with someone 
- Tell me about a time when you had to change the course or direction of a project when you were almost 70% through.

Situation:

While working as a software engineer at Amadeus, I was part of a team tasked with integrating a new feature for a client. During the project, a disagreement arose between me and a colleague regarding the implementation approach. I advocated for a solution that I believed would be more efficient and scalable, while my colleague preferred a different method.

Task:

Our objective was to resolve the disagreement constructively to ensure the project's success and maintain a collaborative team environment.

Action:

I initiated a one-on-one discussion with my colleague to understand their perspective fully. I listened actively to their concerns and explained my viewpoint, providing data and examples to support my approach. Recognizing the importance of collaboration, I proposed a compromise that incorporated elements from both our suggestions, aiming to leverage the strengths of each. I also suggested involving our manager to gain additional insights and ensure alignment with the project's goals.

Result:

The open dialogue and collaborative approach led to a consensus on the implementation strategy. By combining our ideas, we developed a solution that was both efficient and met the project's requirements. This experience strengthened our professional relationship and demonstrated our ability to resolve conflicts constructively.


## <span style="color: #26B260"> Night Trains :
- A time when you fail.
- A time when you had to balance short term delivery and long term quality.
- Tell me about a time when you received critical feedback on your code or design. How did you respond, and what changes did you implement?
- Tell me about a time when you had to make a trade-off between shipping a feature quickly and ensuring high quality. How did you decide on the best course of action?”

Situation : 
While working as a software engineer at Amadeus, I was part of a team tasked with integrating a new feature for a client ( night trains for SBB clients ). offer night trains tickets in Europe.

Task : 
- Booking flow Implementation 
- Understand how ancillaries work ( first time we will include this kind of feature for our client )
- Complexities in regards to dealing with multiple clients at the same time ( each client has own set of rules and messages constraints )

Action : 
- Learn from other XML flows ( SOAP messages ) and try to mimic the behavior of other flows 
- Team was stuck on how to represent the ancilalries in a way that won't break the flow for other clients
- I suddenly had this idea that will successfully create the ancillary => developed the fix and it worked => suddenly a hero of the time 
- In the morning, we had some incidents in TST systems that the booking component crashes for some 
- a problem in the way the quotes / product elements are created which works for some providers but not others
- No longer a Hero, Step back and went it quickly to take immediate actions to recover
- Request fallback ( talk with DevOps Teams)
- made a fix for the scenario
- Informed the impacted teams of what happened ( debriefing )
- I documented this case within the specs for visiblity for upcomming features 
- Tst system was unblocked ( config for that specific provider ) bias for action, making solution design that will cover all the providers at once

Result:
- I wouldn't call it a failing experience, but a constructive one that helped us uncover the complex behaviour of orchestration layer in his relation 
with multiple clients API at once, it taught me how to act quickly under stress without panicking, what s done is done, do whatever you can 
to mitigate the problem, the issue, debrief about it, make others know about the sitatuino ( post mortem / ad hoc sessions ...)


# Functional Questions 

# Why Amazon ?

Culture  LP : Customer Obssession  e-commerce services

Functionnal Part : Functionnal Curiosity to express the willingess to join the team that are developing the product
you candidated for 




# Never do's

- Don't talk bad about the company you worked for ( obvious, looking for greater opportunity, the company was super great )
- I will do anything, don't show a level of desperation. You should talk about the value you can bring and how excited you are to add them to the company
- Bring examples, put in context your achievements and values ( don't say you are detail oriented but show it instead through an example )
- Don't say I don't know how to do this 
- You should do research on the company, the project, the team ... 


############### AMAZON PREP ##################################################

# Technical 

# Leadership principles 
( Actions - Results )
Add 2 or 3 more 
-----------------------------------------------------------------------------

4 areas :
1 - code form maintainable, formatted, minor edit, works as intended, logical approach 
2 - coding from a problem solving problem ( define the problem by asking clarifying questions, Identify the requirments, demonstrate why one solution is better than the other ) - build a workable solution
3 - Logical approaches
4 -

No bar raiser (  )
confident technical ability 

- Cameron : he does want to be confident in your technical abilities ( he will be inj the us )
if you were to join his team in dublin, you wouldn't be at a loss if he is in the US
supported and okay in dublin, he is fair and open to supporting candidates 
he won't put candidates in position in which they can't succeed 
he wants everybody to succeed, plans for dublin 
solve challenging technical problems quickly
lifelong learner constantly 


Paragraph :
I know what you might be looking for cameron, I am not gonna tell you that I am the best top notch software programmer in the world, but I have all the skills and foundational basis in terms of DSA and system design, scalable architecture to succeed in the job, also an active learner taking learnings of any experience that comes along the way ( both suceeding and failing one )

Worked with business consultant advisors with expertise for +30 years and mentored by a friend of mine who worked
at NASA and now Senior level software engineer at Google Gemini. From them, I learned what it takes to be playing at the highest sphere, top tier big tech companies managers are not only looking for solid technical skills, they are looking for highly reliable people to join their team, someone they can trust to do whatever it takes to make the job done with the available resources and to deliver no matter what the circustances are and I ve been constructively building and shaping myself to be the kind of an engineer 

For me, being a professional isn’t just about individual excellence—it’s about making those around me feel confident and secure, knowing I will do whatever it takes to help the team succeed.  engineers work together to build to reinveit the normal
Saying this, I know you are based in the US, I can guarantee to you that you are going to put someone who is extremely autonomous and reliable to the edge, someone who is going to earn fully your trust to achieve the goals that you aspire from the team you're gathering adn driving your team, our team forward.

Sometimes in life, all you need is someone to take a shot on you and believe in your abilities, and beautiful extremely successful stories and experience come out of this trust you ve been given for the good of yourself, the person who trust you, your team, communiity and even the world. and I need you to be that person for me Cameron,I will make sure that your trust in me is worth every tiny bit of it, I will make it my daily goal in my journey with you, future manager.

############################### Criteo ######################################

Criteo is a tech company specialized in digital advertising solutions. Founded in Paris 2005.
The company servers more than 18 000 customers 
it delivers about 5 billion ads per day

Mission 
=> enables marketers, media owners and retailers to achieve better commerce outcomes through its commerce media platform.
It has the largest open commerce dataset to activate and monetize audiences accross multiple channels.

The goal :
bring rich experience to every consumer by empowering marketers and media owners with trusted and impactful advertising.

# Why Criteo ? 
Joining Criteo has been a very long standing aspiration and one of the biggest goals of mine. I am inspired by Criteo's culture and I truly find a huge match between my personality characters.

I am looking for a tier 1 company that has a huge impact on the world, shapes the world even through its actions and work. 

Commerce media is advertising that connects shoppers with products and services throughout the buying journey across both physical and digital touchpoints

The key to commerce media is having large-scale commerce data (purchase and intent data), applying it to enrich audiences and add relevancy, and connecting it to media to deliver the right ads in the right place.

It’s also about delivering relevant ads at all stages while driving measurable commerce outcomes at each stage.

marketers, media owners, and consumers all mutually benefit.


Culture : Open - Together - Impactful 

At Criteo, we welcome open minds with open arms. So, the first thing you will notice is how genuinely open and authentic people are.

Criteos are assets, gathered with diversity and inclusion -> building rich experiences 
Beyond the job, there is a community, open and free place to speak your mind 
you care to hire personalities and ppl with values that you share and resonates within them 



Leadership principles: 

The six leadership principles and values of Criteo resonates with me :
Ownership : employees own their impact, hold themselves accountable and grow together as own while supporting each other.
Recognition : contributions are recognized, grow together as a team 
Trust :  valorisez the culture of the company and increases its authenticity.

Execution 
Innovation 
Client Centricity 