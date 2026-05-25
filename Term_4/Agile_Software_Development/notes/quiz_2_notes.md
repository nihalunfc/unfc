# Agile Software Development: Modules 4, 5, and 6 Study Guide

## Module 4: Implementing Scrum in Your Team
Scrum is a lightweight, adaptable Agile framework focusing on short, repeatable cycles called Sprints (typically 1-4 weeks). 

### Key Scrum Concepts
* **Incremental Delivery:** Delivering small, usable pieces of work rather than a big-bang launch.
* **Empirical Process:** Decisions are based on observation, experience, and experimentation.
* **Water-Scrum-Fall:** An anti-pattern where teams use Agile for development but retain traditional big upfront planning and long release processes.

### Scrum Roles
1.  **Product Owner (PO):** Manages the Product Backlog, prioritizes tasks based on value, and represents the customer.
2.  **Scrum Master (SM):** Guides the team on Scrum principles, facilitates events, and removes blockers.
3.  **Development Team:** Self-organizing group that completes the work (design, coding, testing, etc.).

### Scrum Events (Ceremonies)
* **Sprint Planning:** Defines the Sprint Goal, selects backlog items, and breaks them into tasks.
* **Daily Scrum (Standup):** 15-minute daily sync answering: *What did I do yesterday? What am I doing today? What are my blockers?*
* **Sprint Review:** End-of-sprint demonstration of completed work to stakeholders to gather feedback and update the backlog.
* **Sprint Retrospective:** Internal team reflection on successes, challenges, and process improvements for the next sprint.

### Tools & Tracking
* **Scrum Board:** Visual workflow (e.g., To Do, In Progress, Done). Tools include Taiga, Jira, Trello.
* **Burndown Chart:** Tracks remaining work vs. time left in the sprint.
* **Cumulative Flow Diagrams:** Shows the status of all tasks over time to spot bottlenecks.

---

## Module 5: Agile User Requirements & User Stories
Agile gathers requirements iteratively through continuous feedback, unlike traditional "Big Upfront" documents (which limit creativity and are inflexible).

### User Story Essentials
A simple description of a feature from the user's perspective. It sparks conversation rather than dictating technical implementation.
* **Format:** "As an [Actor], I want [Action] so that [Value]."
* **Card Elements:** * **Stub:** Short title (e.g., "Log Daily Workouts").
    * **Acceptance Criteria:** Specific, testable conditions defining success for *that specific story*.
    * **Story Size:** Estimated effort.
    * **Notes:** Context, constraints, or technical rules.

### Attributes of a Good Story
* **INVEST:** **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, **T**estable.
* **The 3 Cs:** **C**ard (the stub/statement), **C**onversation (team discussion), **C**onfirmation (acceptance criteria).

### Estimation & Sizing
Agile prefers *relative sizing* over exact time estimates to account for complexity, risk, and volume.
* **T-Shirt Sizing:** High-level grouping (S, M, L, XL).
* **Modified Fibonacci (1, 2, 3, 5, 8, 13):** Reflects non-linear complexity. 
* **Planning Poker:** Team votes simultaneously.
    * *Consensus:* Move forward.
    * *Tight range (e.g., 2s and 3s):* Use the higher estimate.
    * *Wide variation (e.g., 2 and 13):* Discuss extremes, identify hidden risks, and revote.
* **Spikes:** Timeboxed research stories to investigate unknowns and close knowledge gaps.

### Acceptance Criteria vs. Definition of Done (DoD)
* **Acceptance Criteria:** Specific to an individual User Story (e.g., "User can filter by date").
* **DoD:** A universal team checklist applied to *all* stories (e.g., "Code reviewed, tests passed, deployed to staging").

---

## Module 6: Team Setup with Liftoffs
A Liftoff is an intentional, collaborative event to align the team, sponsors, and stakeholders before work begins. It is more comprehensive than a simple kickoff meeting.

### Alignment Elements
* **Purpose:** Why the company exists beyond profit (the big picture).
* **Mission:** Current objectives and where the team is heading.
* **Product Vision:** What the team is building and how it serves the organization's goals.

### Success Metrics
* **Technical:** Code quality, MTTR, deployment frequency.
* **Business:** Net Promoter Score (NPS), conversion rates.
* **Operational:** Lead time, velocity, DoD compliance.
* **Success Sliders:** A visual activity where the team agrees on the relative priority of different metrics (e.g., choosing quality over speed).

### Team Charter
A "team contract" establishing how members collaborate. Includes:
* **Definition of Done (DoD):** Shared quality standards.
* **Working Agreements:** Rules for communication, code reviews, standup attendance, and conflict resolution.
* **Team Calendar:** Schedule for sprints, daily standups, reviews, and retrospectives.

***

# Agile Quiz: EASY SET

### Multiple Choice (15 Questions)
1. What is the typical duration of a Sprint in Scrum?
   a) 1-2 days
   b) 1-4 weeks
   c) 2-3 months
   d) 6 months
2. Which role manages the Product Backlog?
   a) Scrum Master
   b) Stakeholder
   c) Product Owner
   d) Development Team
3. What is the primary purpose of the Daily Scrum?
   a) To assign new tasks
   b) To identify blockers and synchronize efforts
   c) To demonstrate completed work
   d) To write user stories
4. In the format "As an [Actor], I want [Action] so that [Value]", what does the Actor represent?
   a) The database architect
   b) The specific feature
   c) The person or role interacting with the system
   d) The business outcome
5. What does the "I" in INVEST stand for?
   a) Iterative
   b) Incremental
   c) Independent
   d) Immediate
6. Which Agile sizing technique uses Small, Medium, Large, and Extra Large?
   a) Fibonacci sequence
   b) Planning Poker
   c) T-Shirt Sizing
   d) Spikes
7. What is a "Spike" in Agile?
   a) A major software bug
   b) A timeboxed research task to gather information
   c) A sudden increase in velocity
   d) A milestone deadline
8. What is a Team Liftoff?
   a) A celebration at the end of a project
   b) A formal process of launching a team with a shared mission
   c) A technical deployment to a server
   d) A daily meeting for the development team
9. Which metric tracks "Code quality (e.g., number of bugs per release)"?
   a) Technical Metric
   b) Business Metric
   c) Operational Metric
   d) Financial Metric
10. What does a Burndown Chart visualize?
    a) Work completed vs. team satisfaction
    b) Work remaining vs. time left in the sprint
    c) Number of bugs over time
    d) Cumulative flow of all tasks
11. Who facilitates the Sprint Retrospective?
    a) The Stakeholder
    b) The Product Owner
    c) The Scrum Master
    d) The end-user
12. Which document is a team-defined checklist ensuring a product is technically sound and properly tested?
    a) Acceptance Criteria
    b) Definition of Done (DoD)
    c) Sprint Backlog
    d) Working Agreement
13. What is a "Stub" in a User Story?
    a) The code implementation
    b) A short, paraphrased title for quick reference
    c) The final testing phase
    d) A blocked task
14. Which event bridges the gap between the team’s work and stakeholder expectations?
    a) Daily Scrum
    b) Sprint Planning
    c) Sprint Review
    d) Poker Planning
15. A company's "Purpose" answers which of the following questions?
    a) What is our current sprint goal?
    b) How many user stories can we finish?
    c) Why do we exist beyond making a profit?
    d) What is our deployment schedule?

### Multi-Select (10 Questions - Select all that apply)
16. Which of the following are Scrum Roles? 
    a) Project Manager
    b) Product Owner
    c) Scrum Master
    d) Development Team
17. Which of the following are questions answered during the Daily Scrum?
    a) What did I complete yesterday?
    b) What am I working on today?
    c) How many story points is this task worth?
    d) What obstacles are blocking me?
18. Which of the following are the 3 Cs of User Stories?
    a) Card
    b) Conversation
    c) Confirmation
    d) Collaboration
19. Which numbers are typically part of the modified Fibonacci sequence used in Agile?
    a) 2
    b) 4
    c) 5
    d) 8
20. Which items are typically included in a Team Charter?
    a) Definition of Done
    b) Working Agreements
    c) Individual salaries
    d) Team Calendar
21. Which events are considered standard Scrum ceremonies?
    a) Sprint Planning
    b) Sprint Review
    c) Budget Approval
    d) Sprint Retrospective
22. Which are examples of Business Metrics?
    a) Net Promoter Score
    b) Mean Time to Recovery (MTTR)
    c) Conversion rates
    d) Retention rates
23. What issues are common with traditional Big Upfront Requirements?
    a) Prescriptive solutions limit creativity
    b) Highly adaptable to change
    c) Hard for non-technical stakeholders to understand
    d) Difficulty prioritizing individual requirements
24. Story Points reflect which of the following elements?
    a) Complexity
    b) Risk
    c) Exact hours required
    d) Volume of work
25. Which activities are part of the process for brainstorming user stories?
    a) Creating Story Stubs
    b) Identifying Overlaps & Gaps
    c) Writing Full User Stories
    d) Assigning tasks to specific developers

### Short Written Answers (10 Questions)
26. Define the term "Sprint" in the context of Scrum.
27. Write the standard template/format for a User Story.
28. What is the difference between a Product Backlog and a Sprint Backlog?
29. Briefly explain what the "Confirmation" step is in the 3 Cs of User Stories.
30. List the three categories of Success Metrics discussed in Module 6.
31. What is the purpose of the Success Sliders activity?
32. What does it mean for a User Story to be "Independent" (the 'I' in INVEST)?
33. Briefly define "Water-Scrum-Fall".
34. Name three tools you can use for Task Management/Scrum Boards.
35. Who are the required participants in a Sprint Retrospective?

***

# Agile Quiz: MEDIUM SET

### Multiple Choice (15 Questions)
1. During Planning Poker, if there is a tight range of estimates (e.g., some vote 2, some vote 3), what is the recommended action?
   a) Go with the lowest estimate.
   b) Err on the side of the larger estimate.
   c) Average the two numbers to 2.5.
   d) Discard the story entirely.
2. How does the Definition of Done (DoD) differ from Acceptance Criteria?
   a) DoD applies to all stories; Acceptance Criteria are specific to one story.
   b) DoD is written by stakeholders; Acceptance Criteria are written by developers.
   c) DoD is used only in testing; Acceptance Criteria are used only in design.
   d) There is no difference; they are interchangeable terms.
3. If a User Story is estimated at 13 points using the Fibonacci sequence, what should the team likely do?
   a) Assign it to the most senior developer.
   b) Break it down into smaller, more manageable stories.
   c) Double the sprint length to accommodate it.
   d) Skip it and move to the next sprint.
4. During a Liftoff, who provides critical insights into the organizational priorities and business context?
   a) The Scrum Master
   b) The Core Team
   c) The Sponsors
   d) The End Users
5. In Scrum, who is responsible for maximizing the value of the product?
   a) Scrum Master
   b) Product Owner
   c) Development Team
   d) Project Manager
6. Which tool helps teams spot inefficiencies by showing the status of all tasks over time?
   a) Burndown Chart
   b) Cumulative Flow Diagram
   c) Team Charter
   d) Success Slider
7. A team is building a predictive ensemble model. They aren't sure which algorithm (XGBoost or CatBoost) will yield the lowest error rate. What Agile tool should they use?
   a) A Sprint Review
   b) A Spike
   c) A Team Charter
   d) A Burndown Chart
8. What is the primary focus of the Sprint Retrospective?
   a) Demonstrating the product to stakeholders
   b) Planning the next sprint's backlog
   c) Reflecting on team processes and identifying improvements
   d) Re-estimating all user stories
9. Which of the following is the BEST example of an Acceptance Criterion?
   a) The system should be fast.
   b) The UI must look modern and clean.
   c) The user receives a confirmation email within 2 minutes of submitting the form.
   d) The database should use SQL.
10. What is the primary danger of the "Water-Scrum-Fall" approach?
    a) Teams deliver software too quickly.
    b) It requires too many Scrum Masters.
    c) Rigid upfront planning makes teams less responsive to change.
    d) Sprints become too short.
11. Which event is strictly time-boxed to 15 minutes?
    a) Sprint Planning
    b) Sprint Retrospective
    c) Daily Scrum
    d) Sprint Review
12. Why do Agile teams prefer relative sizing over time-based estimates?
    a) It is mandated by the Scrum Guide.
    b) Humans are better at comparing relative complexity than predicting exact hours.
    c) It allows developers to work fewer hours.
    d) It eliminates the need for a Scrum Master.
13. Which of the following defines how the team will handle meetings, provide feedback, and resolve conflicts?
    a) The Product Vision
    b) Working Agreements
    c) Acceptance Criteria
    d) Cumulative Flow Diagram
14. Which metric tracks "Lead time for changes" and "Team velocity"?
    a) Technical Metrics
    b) Business Metrics
    c) Operational Metrics
    d) Financial Metrics
15. In the context of a liftoff, what is the purpose of reviewing the company's purpose?
    a) To determine individual bonuses
    b) To connect the team's work to the larger mission and make it feel meaningful
    c) To decide which coding language to use
    d) To write the Definition of Done

### Multi-Select (10 Questions - Select all that apply)
16. Which scenarios describe a good use of a "Spike"?
    a) Evaluating a new API integration before estimating a story.
    b) Completing a routine, well-understood bug fix.
    c) Researching a new architectural approach.
    d) Writing the final user documentation.
17. What are the key objectives of the Sprint Review?
    a) Demonstrate completed work to stakeholders.
    b) Discuss interpersonal conflicts within the team.
    c) Ensure deliverables align with the Sprint Goal.
    d) Collect stakeholder feedback to update the backlog.
18. Which attributes belong to the INVEST criteria for good user stories?
    a) Estimable
    b) Extensive
    c) Small
    d) Testable
19. Which of the following would typically be found in a Team Calendar?
    a) Daily Standup times
    b) Code repositories
    c) Sprint Planning sessions
    d) Milestone checkpoints
20. What characterizes an effective Sprint Goal?
    a) It answers "What problem are we solving?"
    b) It lists every single technical task required.
    c) It answers "Why does it matter?"
    d) It is updated daily during the standup.
21.
