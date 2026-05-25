# Agile Software Development: Modules 4, 5, and 6 Study Guide & Quiz

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
Agile gathers requirements iteratively through continuous feedback, unlike traditional "Big Upfront" documents.

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
A Liftoff is an intentional, collaborative event to align the team, sponsors, and stakeholders before work begins. 

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
***

# Agile Quiz: EASY SET

### Multiple Choice (15 Questions)

1. What is the typical duration of a Sprint in Scrum?
   a) 1-2 days
   b) 1-4 weeks
   c) 2-3 months
   d) 6 months
   **Answer:** b) 1-4 weeks

2. Which role manages the Product Backlog?
   a) Scrum Master
   b) Stakeholder
   c) Product Owner
   d) Development Team
   **Answer:** c) Product Owner

3. What is the primary purpose of the Daily Scrum?
   a) To assign new tasks
   b) To identify blockers and synchronize efforts
   c) To demonstrate completed work
   d) To write user stories
   **Answer:** b) To identify blockers and synchronize efforts

4. In the format "As an [Actor], I want [Action] so that [Value]", what does the Actor represent?
   a) The database architect
   b) The specific feature
   c) The person or role interacting with the system
   d) The business outcome
   **Answer:** c) The person or role interacting with the system

5. What does the "I" in INVEST stand for?
   a) Iterative
   b) Incremental
   c) Independent
   d) Immediate
   **Answer:** c) Independent

6. Which Agile sizing technique uses Small, Medium, Large, and Extra Large?
   a) Fibonacci sequence
   b) Planning Poker
   c) T-Shirt Sizing
   d) Spikes
   **Answer:** c) T-Shirt Sizing

7. What is a "Spike" in Agile?
   a) A major software bug
   b) A timeboxed research task to gather information
   c) A sudden increase in velocity
   d) A milestone deadline
   **Answer:** b) A timeboxed research task to gather information

8. What is a Team Liftoff?
   a) A celebration at the end of a project
   b) A formal process of launching a team with a shared mission
   c) A technical deployment to a server
   d) A daily meeting for the development team
   **Answer:** b) A formal process of launching a team with a shared mission

9. Which metric tracks "Code quality (e.g., number of bugs per release)"?
   a) Technical Metric
   b) Business Metric
   c) Operational Metric
   d) Financial Metric
   **Answer:** a) Technical Metric

10. What does a Burndown Chart visualize?
    a) Work completed vs. team satisfaction
    b) Work remaining vs. time left in the sprint
    c) Number of bugs over time
    d) Cumulative flow of all tasks
    **Answer:** b) Work remaining vs. time left in the sprint

11. Who facilitates the Sprint Retrospective?
    a) The Stakeholder
    b) The Product Owner
    c) The Scrum Master
    d) The end-user
    **Answer:** c) The Scrum Master

12. Which document is a team-defined checklist ensuring a product is technically sound and properly tested?
    a) Acceptance Criteria
    b) Definition of Done (DoD)
    c) Sprint Backlog
    d) Working Agreement
    **Answer:** b) Definition of Done (DoD)

13. What is a "Stub" in a User Story?
    a) The code implementation
    b) A short, paraphrased title for quick reference
    c) The final testing phase
    d) A blocked task
    **Answer:** b) A short, paraphrased title for quick reference

14. Which event bridges the gap between the team’s work and stakeholder expectations?
    a) Daily Scrum
    b) Sprint Planning
    c) Sprint Review
    d) Poker Planning
    **Answer:** c) Sprint Review

15. A company's "Purpose" answers which of the following questions?
    a) What is our current sprint goal?
    b) How many user stories can we finish?
    c) Why do we exist beyond making a profit?
    d) What is our deployment schedule?
    **Answer:** c) Why do we exist beyond making a profit?

### Multi-Select (10 Questions - Select all that apply)

16. Which of the following are Scrum Roles? 
    a) Project Manager
    b) Product Owner
    c) Scrum Master
    d) Development Team
    **Answer:** b, c, d

17. Which of the following are questions answered during the Daily Scrum?
    a) What did I complete yesterday?
    b) What am I working on today?
    c) How many story points is this task worth?
    d) What obstacles are blocking me?
    **Answer:** a, b, d

18. Which of the following are the 3 Cs of User Stories?
    a) Card
    b) Conversation
    c) Confirmation
    d) Collaboration
    **Answer:** a, b, c

19. Which numbers are typically part of the modified Fibonacci sequence used in Agile?
    a) 2
    b) 4
    c) 5
    d) 8
    **Answer:** a, c, d

20. Which items are typically included in a Team Charter?
    a) Definition of Done
    b) Working Agreements
    c) Individual salaries
    d) Team Calendar
    **Answer:** a, b, d

21. Which events are considered standard Scrum ceremonies?
    a) Sprint Planning
    b) Sprint Review
    c) Budget Approval
    d) Sprint Retrospective
    **Answer:** a, b, d

22. Which are examples of Business Metrics?
    a) Net Promoter Score
    b) Mean Time to Recovery (MTTR)
    c) Conversion rates
    d) Retention rates
    **Answer:** a, c, d

23. What issues are common with traditional Big Upfront Requirements?
    a) Prescriptive solutions limit creativity
    b) Highly adaptable to change
    c) Hard for non-technical stakeholders to understand
    d) Difficulty prioritizing individual requirements
    **Answer:** a, c, d

24. Story Points reflect which of the following elements?
    a) Complexity
    b) Risk
    c) Exact hours required
    d) Volume of work
    **Answer:** a, b, d

25. Which activities are part of the process for brainstorming user stories?
    a) Creating Story Stubs
    b) Identifying Overlaps & Gaps
    c) Writing Full User Stories
    d) Assigning tasks to specific developers
    **Answer:** a, b, c

### Short Written Answers (10 Questions)

26. Define the term "Sprint" in the context of Scrum.
    **Answer:** A time-boxed period (typically 1-4 weeks) where the team focuses on delivering a defined, usable set of work increments.

27. Write the standard template/format for a User Story.
    **Answer:** "As an [actor], I want [action] so that [value]."

28. What is the difference between a Product Backlog and a Sprint Backlog?
    **Answer:** The Product Backlog is the master, prioritized list of all features for the entire product. The Sprint Backlog is the specific subset of work pulled into the current sprint.

29. Briefly explain what the "Confirmation" step is in the 3 Cs of User Stories.
    **Answer:** Confirmation represents the Acceptance Criteria—validating that the story meets the agreed-upon, testable conditions for success.

30. List the three categories of Success Metrics discussed in Module 6.
    **Answer:** Technical Metrics, Business Metrics, and Operational Metrics.

31. What is the purpose of the Success Sliders activity?
    **Answer:** To visually prioritize different success metrics (like speed vs. quality) so the team knows what matters most when making project trade-offs.

32. What does it mean for a User Story to be "Independent" (the 'I' in INVEST)?
    **Answer:** It means the story can stand alone and be developed or prioritized without relying on the completion of other stories.

33. Briefly define "Water-Scrum-Fall".
    **Answer:** An anti-pattern where an organization uses Agile/Scrum for the middle development phase, but keeps rigid traditional planning at the start and slow release processes at the end.

34. Name three tools you can use for Task Management/Scrum Boards.
    **Answer:** Taiga, Jira, and Trello.

35. Who are the required participants in a Sprint Retrospective?
    **Answer:** The Scrum Master and the Development Team.

***
***

# Agile Quiz: MEDIUM SET

### Multiple Choice (15 Questions)

1. During Planning Poker, if there is a tight range of estimates (e.g., some vote 2, some vote 3), what is the recommended action?
   a) Go with the lowest estimate.
   b) Err on the side of the larger estimate.
   c) Average the two numbers to 2.5.
   d) Discard the story entirely.
   **Answer:** b) Err on the side of the larger estimate.

2. How does the Definition of Done (DoD) differ from Acceptance Criteria?
   a) DoD applies to all stories; Acceptance Criteria are specific to one story.
   b) DoD is written by stakeholders; Acceptance Criteria are written by developers.
   c) DoD is used only in testing; Acceptance Criteria are used only in design.
   d) There is no difference; they are interchangeable terms.
   **Answer:** a) DoD applies to all stories; Acceptance Criteria are specific to one story.

3. If a User Story is estimated at 13 points using the Fibonacci sequence, what should the team likely do?
   a) Assign it to the most senior developer.
   b) Break it down into smaller, more manageable stories.
   c) Double the sprint length to accommodate it.
   d) Skip it and move to the next sprint.
   **Answer:** b) Break it down into smaller, more manageable stories.

4. During a Liftoff, who provides critical insights into the organizational priorities and business context?
   a) The Scrum Master
   b) The Core Team
   c) The Sponsors
   d) The End Users
   **Answer:** c) The Sponsors

5. In Scrum, who is responsible for maximizing the value of the product?
   a) Scrum Master
   b) Product Owner
   c) Development Team
   d) Project Manager
   **Answer:** b) Product Owner

6. Which tool helps teams spot inefficiencies by showing the status of all tasks over time?
   a) Burndown Chart
   b) Cumulative Flow Diagram
   c) Team Charter
   d) Success Slider
   **Answer:** b) Cumulative Flow Diagram

7. A team is building a predictive ensemble model. They aren't sure which algorithm (XGBoost or CatBoost) will yield the lowest error rate. What Agile tool should they use?
   a) A Sprint Review
   b) A Spike
   c) A Team Charter
   d) A Burndown Chart
   **Answer:** b) A Spike

8. What is the primary focus of the Sprint Retrospective?
   a) Demonstrating the product to stakeholders
   b) Planning the next sprint's backlog
   c) Reflecting on team processes and identifying improvements
   d) Re-estimating all user stories
   **Answer:** c) Reflecting on team processes and identifying improvements

9. Which of the following is the BEST example of an Acceptance Criterion?
   a) The system should be fast.
   b) The UI must look modern and clean.
   c) The user receives a confirmation email within 2 minutes of submitting the form.
   d) The database should use SQL.
   **Answer:** c) The user receives a confirmation email within 2 minutes of submitting the form.

10. What is the primary danger of the "Water-Scrum-Fall" approach?
    a) Teams deliver software too quickly.
    b) It requires too many Scrum Masters.
    c) Rigid upfront planning makes teams less responsive to change.
    d) Sprints become too short.
    **Answer:** c) Rigid upfront planning makes teams less responsive to change.

11. Which event is strictly time-boxed to 15 minutes?
    a) Sprint Planning
    b) Sprint Retrospective
    c) Daily Scrum
    d) Sprint Review
    **Answer:** c) Daily Scrum

12. Why do Agile teams prefer relative sizing over time-based estimates?
    a) It is mandated by the Scrum Guide.
    b) Humans are better at comparing relative complexity than predicting exact hours.
    c) It allows developers to work fewer hours.
    d) It eliminates the need for a Scrum Master.
    **Answer:** b) Humans are better at comparing relative complexity than predicting exact hours.

13. Which of the following defines how the team will handle meetings, provide feedback, and resolve conflicts?
    a) The Product Vision
    b) Working Agreements
    c) Acceptance Criteria
    d) Cumulative Flow Diagram
    **Answer:** b) Working Agreements

14. Which metric tracks "Lead time for changes" and "Team velocity"?
    a) Technical Metrics
    b) Business Metrics
    c) Operational Metrics
    d) Financial Metrics
    **Answer:** c) Operational Metrics

15. In the context of a liftoff, what is the purpose of reviewing the company's purpose?
    a) To determine individual bonuses
    b) To connect the team's work to the larger mission and make it feel meaningful
    c) To decide which coding language to use
    d) To write the Definition of Done
    **Answer:** b) To connect the team's work to the larger mission and make it feel meaningful

### Multi-Select (10 Questions - Select all that apply)

16. Which scenarios describe a good use of a "Spike"?
    a) Evaluating a new API integration before estimating a story.
    b) Completing a routine, well-understood bug fix.
    c) Researching a new architectural approach.
    d) Writing the final user documentation.
    **Answer:** a, c

17. What are the key objectives of the Sprint Review?
    a) Demonstrate completed work to stakeholders.
    b) Discuss interpersonal conflicts within the team.
    c) Ensure deliverables align with the Sprint Goal.
    d) Collect stakeholder feedback to update the backlog.
    **Answer:** a, c, d

18. Which attributes belong to the INVEST criteria for good user stories?
    a) Estimable
    b) Extensive
    c) Small
    d) Testable
    **Answer:** a, c, d

19. Which of the following would typically be found in a Team Calendar?
    a) Daily Standup times
    b) Code repositories
    c) Sprint Planning sessions
    d) Milestone checkpoints
    **Answer:** a, c, d

20. What characterizes an effective Sprint Goal?
    a) It answers "What problem are we solving?"
    b) It lists every single technical task required.
    c) It answers "Why does it matter?"
    d) It is updated daily during the standup.
    **Answer:** a, c

21. Which are examples of Technical Metrics?
    a) Mean Time to Recovery (MTTR)
    b) Code quality (bugs per release)
    c) Customer satisfaction score
    d) Deployment frequency
    **Answer:** a, b, d

22. During Planning Poker, what steps should be taken if there is a wide variation in estimates (e.g., 2 vs. 13)?
    a) The Scrum Master chooses the average.
    b) The lowest estimator explains their reasoning.
    c) The highest estimator explains their reasoning.
    d) The team revotes after the discussion.
    **Answer:** b, c, d

23. Which elements make up a complete User Story Card?
    a) The Stub
    b) Acceptance Criteria
    c) Detailed UML diagrams
    d) Story Size
    **Answer:** a, b, d

24. Which of the following are true about the Product Owner role?
    a) They manage the Product Backlog.
    b) They facilitate the Daily Scrum.
    c) They ensure the team works on tasks delivering the most value.
    d) They represent the customer’s perspective.
    **Answer:** a, c, d

25. When prioritizing the Product Backlog, how might tasks be categorized?
    a) Must Be Done
    b) Can Be Done
    c) Postponed
    d) Already Done
    **Answer:** a, b, c

### Short Written Answers (10 Questions)

26. Write a proper User Story for a data analyst who needs to export predictive modeling results to a CSV file to share with stakeholders.
    **Answer:** "As a data analyst, I want to export my predictive modeling results to a CSV file so that I can easily share the insights with stakeholders."

27. Provide two examples of what might be included in a team's "Working Agreements".
    **Answer:** 1) All team members will update progress daily in the tracking tool. 2) Peer code review is mandatory before deployment.

28. Explain the difference between a company's "Purpose" and its "Mission".
    **Answer:** Purpose is *why* the company exists (the big picture/reason for being). Mission reflects the *current* objectives and where the organization is heading right now.

29. Describe the specific scenario in Planning Poker where a team should simply "err on the side of the larger estimate" without extensive debate.
    **Answer:** When there is a very tight range of small differences between team members' votes (e.g., half the team votes 2, the other half votes 3).

30. What is the purpose of creating "Personas" when writing User Stories?
    **Answer:** Personas provide context about the specific needs, goals, and pain points of the target user to ensure the team is building features that deliver actual value to that type of person.

31. How does the Scrum Master assist the Development Team during the execution of a Sprint?
    **Answer:** By proactively removing impediments or blockers that are slowing the team down, and by facilitating Scrum events to keep them focused.

32. What is the difference between an Epic and a Task?
    **Answer:** An Epic is a large, vague body of work that must be broken down. A task is a small, actionable item that forms a piece of a refined User Story.

33. Why are traditional Big Upfront Requirements difficult to manage when business needs change?
    **Answer:** They lock down highly prescriptive technical solutions early on, requiring rigid, formal approvals to change, which causes massive delays when new information emerges.

34. List three things team members must answer during the Daily Scrum.
    **Answer:** 1) What did I complete yesterday? 2) What am I working on today? 3) What obstacles are blocking me?

35. How does a well-crafted Sprint Goal help the team during Sprint execution?
    **Answer:** It acts as a guiding compass, keeping them aligned on a unified objective and helping them decide what work is essential versus non-essential if time runs short.

***
***

# Agile Quiz: HARD SET

### Multiple Choice (15 Questions)

1. A team member consistently pulls tasks into "In Progress" but fails to move them to "Done" because they skip unit testing. Which artifact or agreement is the team failing to enforce?
   a) The Sprint Goal
   b) The Definition of Done (DoD)
   c) The Success Slider
   d) The Burndown Chart
   **Answer:** b) The Definition of Done (DoD)

2. During a Sprint Retrospective, the team realizes they underestimated several stories due to hidden database complexities. What should the Scrum Master suggest for future sprints?
   a) Stop using relative estimation.
   b) Utilize timeboxed Spikes before estimating complex database stories.
   c) Assign all database tasks to the Product Owner.
   d) Extend the sprint length to 6 weeks.
   **Answer:** b) Utilize timeboxed Spikes before estimating complex database stories.

3. A stakeholder wants to add a new "Must Have" feature in the middle of an active Sprint. Who is responsible for protecting the team from this scope creep and managing the stakeholder's request?
   a) The Lead Developer
   b) The Scrum Master
   c) The Product Owner
   d) The Agile Coach
   **Answer:** c) The Product Owner

4. In the 3 Cs model, what does "Conversation" specifically replace from traditional project management?
   a) The project budget
   b) Lengthy, prescriptive requirement documents
   c) The final delivery phase
   d) The quality assurance testing
   **Answer:** b) Lengthy, prescriptive requirement documents

5. If a team uses Success Sliders and pushes "Timely Delivery" to the maximum, while lowering "Technical Quality", what is the most likely outcome they are accepting?
   a) Higher customer retention
   b) Accumulating technical debt to meet a deadline
   c) Zero bugs in the production environment
   d) An increase in automated test coverage
   **Answer:** b) Accumulating technical debt to meet a deadline

6. A User Story reads: *"As a system, I want to process spatial data faster so that the database doesn't crash."* Why does this violate the principles of a good User Story?
   a) It does not include acceptance criteria.
   b) The "Actor" is a system, not a user deriving value.
   c) It is not estimable.
   d) It uses the Fibonacci sequence incorrectly.
   **Answer:** b) The "Actor" is a system, not a user deriving value.

7. Which of the following best demonstrates the "N" (Negotiable) in the INVEST criteria?
   a) The story's acceptance criteria are permanently locked during the liftoff.
   b) The developer and PO collaborate during the sprint to tweak the UI layout for better UX.
   c) The team negotiates their salaries based on completed story points.
   d) The PO refuses to change the backlog order.
   **Answer:** b) The developer and PO collaborate during the sprint to tweak the UI layout for better UX.

8. How does a Cumulative Flow Diagram help identify workflow bottlenecks?
   a) By showing the exact hour a developer stopped working.
   b) By displaying a widening band in the "In Progress" or "Testing" columns over time.
   c) By tracking the financial burn rate of the project.
   d) By highlighting which team member is the slowest.
   **Answer:** b) By displaying a widening band in the "In Progress" or "Testing" columns over time.

9. During a Team Liftoff, the team defines its "Current Mission". How does this differ from the Product Vision?
   a) The mission is immediate and actionable (e.g., "Increase onboarding by 20% in 3 months"), while the vision is the overarching "why".
   b) The mission is permanent, while the vision changes every sprint.
   c) The mission is written by developers, while the vision is written by stakeholders.
   d) They are identical concepts.
   **Answer:** a) The mission is immediate and actionable, while the vision is the overarching "why".

10. What is the core physiological/psychological reason the modified Fibonacci sequence is effective for estimation?
    a) It mathematically guarantees project completion on time.
    b) The growing gaps between numbers force critical thinking about escalating complexity and uncertainty.
    c) It is easier to translate directly into hours.
    d) It was created specifically by the founders of Scrum.
    **Answer:** b) The growing gaps between numbers force critical thinking about escalating complexity and uncertainty.

11. A team finishes all their Sprint tasks with 3 days left in the Sprint. What should they do?
    a) End the sprint early and start the next one.
    b) Consult the Product Owner to pull the next highest-priority stories from the Product Backlog.
    c) Take time off until the Sprint Review.
    d) Rewrite their Definition of Done to be harder.
    **Answer:** b) Consult the Product Owner to pull the next highest-priority stories from the Product Backlog.

12. Why is "Water-Scrum-Fall" considered an anti-pattern?
    a) It relies too heavily on Kanban boards.
    b) It isolates the Agile development phase between rigid upfront planning and delayed release phases, neutralizing Agile's adaptability.
    c) It forces teams to release software too frequently.
    d) It skips the Sprint Retrospective.
    **Answer:** b) It isolates the Agile development phase between rigid upfront planning and delayed release phases, neutralizing Agile's adaptability.

13. Which scenario represents an empirical process control in Scrum?
    a) Following a strict 2-year project plan without deviation.
    b) Adjusting the next sprint's capacity based on the observed velocity of the previous sprint.
    c) Forcing developers to work overtime to meet an initial estimate.
    d) Writing all acceptance criteria at the beginning of the year.
    **Answer:** b) Adjusting the next sprint's capacity based on the observed velocity of the previous sprint.

14. What happens to incomplete User Stories at the end of a Sprint?
    a) They are marked as Done anyway to keep velocity high.
    b) They are deleted.
    c) They are returned to the Product Backlog to be re-prioritized by the Product Owner.
    d) The sprint is extended until they are finished.
    **Answer:** c) They are returned to the Product Backlog to be re-prioritized by the Product Owner.

15. When defining "Done" for a data analytics model, which of the following is the most appropriate criterion?
    a) "The code looks good to the original author."
    b) "A privacy check confirms data processing complies with governance policies."
    c) "The model was completed before lunch."
    d) "The stakeholder thinks the graphs are pretty."
    **Answer:** b) "A privacy check confirms data processing complies with governance policies."

### Multi-Select (10 Questions - Select all that apply)

16. Which of the following are consequences of lacking a clear Definition of Done?
    a) Increased technical debt.
    b) Stakeholders rejecting the increment during the Sprint Review.
    c) Faster delivery of high-quality software.
    d) Work being revisited or reworked in later sprints.
    **Answer:** a, b, d

17. What are the facilitator's responsibilities during a Team Liftoff?
    a) Dictating the technical architecture.
    b) Keeping discussions on track.
    c) Ensuring all voices are heard.
    d) Helping the team make agreements without endless debate.
    **Answer:** b, c, d

18. Which actions occur during backlog refinement (grooming)?
    a) Breaking down Epics into smaller User Stories.
    b) Writing code for the upcoming sprint.
    c) Categorizing tasks into Must Be Done vs. Postponed.
    d) Demonstrating the product to the client.
    **Answer:** a, c

19. Which statements accurately describe the Sprint Review?
    a) It is an internal meeting just for the Development Team.
    b) It is not merely a status update; it requires demonstrating tangible progress.
    c) It provides an opportunity to adapt the Product Backlog.
    d) It focuses exclusively on how the team communicated.
    **Answer:** b, c

20. What steps should a team take during the Sprint Retrospective?
    a) Review successes from the sprint.
    b) Assign blame for missed deadlines.
    c) Identify workflow inefficiencies.
    d) Commit to actionable changes for the next sprint.
    **Answer:** a, c, d

21. Which attributes describe a good Sprint Goal?
    a) It answers what problem is being solved.
    b) It lists every minor bug fix in the sprint.
    c) It helps the team decide what work is essential.
    d) It keeps the team focused on a unified objective.
    **Answer:** a, c, d

22. Which are valid techniques for managing "Spikes"?
    a) They must be timeboxed.
    b) They are allowed to run indefinitely until the research is done.
    c) They result in findings that help refine related User Stories.
    d) They are used when there are significant unknowns.
    **Answer:** a, c, d

23. When evaluating Success Metrics, what are potential risks of choosing poor metrics?
    a) Focusing too much on velocity at the expense of quality.
    b) Encouraging behavior that undermines the product vision.
    c) Ensuring 100% customer satisfaction.
    d) Ignoring technical debt to hit numerical targets.
    **Answer:** a, b, d

24. What are the benefits of organizing a workspace with high visibility (e.g., a shared Scrum Board)?
    a) It clarifies responsibility and who is working on what.
    b) It hides bottlenecks so management doesn't panic.
    c) It fosters accountability.
    d) It serves as a single source of truth.
    **Answer:** a, c, d

25. What actions should occur during the Brainstorming phase of User Stories?
    a) Creating short story stubs (approx. 15 minutes).
    b) Identifying dependencies and overlaps.
    c) Writing complex backend server logic.
    d) Expanding stubs into full stories with acceptance criteria.
    **Answer:** a, b, d

### Short Written Answers (10 Questions)

26. Draft a 3-point snippet of a Team Charter specifically addressing "Working Agreements" for a remote data annotation team.
    **Answer:** 1) Core hours overlap between 10 AM - 2 PM EST for syncs. 
    2) All annotation queries must be logged in the #blockers Slack channel. 
    3) Video cameras must be on during Sprint Planning.

27. Analyze the following User Story and rewrite it to fit the proper Agile format: *"The pipeline needs to be faster because right now the model training takes too long for the data team."*
    **Answer:** "As a data team member, I want the model training pipeline optimized so that I can train models faster and increase my iteration speed."

28. Explain how the "Card, Conversation, Confirmation" (3 Cs) model prevents the problems associated with traditional "Big Upfront Requirements".
    **Answer:** It replaces rigid, prescriptive documents with a short stub (Card) that forces real-time collaboration (Conversation) to figure out the best technical solution, which is then validated by mutually agreed criteria (Confirmation).

29. Describe a scenario where a team should use a "Spike" rather than assigning a Fibonacci number to a story immediately. 
    **Answer:** The team needs to implement a new API but nobody has used it before. They cannot estimate effort accurately due to the unknown variables, so they run a time-boxed Spike to research the API first.

30. How does setting a "Sprint Goal" help a development team handle ad-hoc requests that arise during the Sprint?
    **Answer:** It provides a filter: if the ad-hoc request does not align with or actively help achieve the Sprint Goal, the Product Owner moves it to the Product Backlog for a future sprint rather than derailing current progress.

31. In the context of a liftoff, contrast the role of a "Sponsor" with the role of a "Facilitator".
    **Answer:** A Sponsor provides the product vision, business context, and overarching organizational support. A Facilitator guides the meeting mechanics, ensuring equal participation and driving the team toward consensus without dictating the outcome.

32. What is the specific danger of treating a Sprint Review merely as a "status update" PowerPoint presentation?
    **Answer:** It fails to show tangible, working software (the Increment) to stakeholders, missing the core Agile opportunity to gather actual empirical feedback on the product itself.

33. Write three robust Acceptance Criteria for the following User Story: *"As a data analyst, I want to filter the dashboard by date range so that I can analyze seasonal sales trends."*
    **Answer:** 1) The user can select a start date and an end date from a calendar UI. 
    2) The dashboard visuals update within 3 seconds to reflect only the chosen range. 
    3) An error message appears if the end date selected is chronologically before the start date.

34. Why is it recommended that the gaps between numbers in the modified Fibonacci sequence (5, 8, 13, 21) get larger as the numbers increase?
    **Answer:** To reflect that as tasks get larger, the uncertainty and complexity escalate exponentially. The large gaps force the team to acknowledge this risk and break down massive tasks rather than falsely predicting them with a precise number.

35. If a team consistently fails to complete their Sprint Backlog, what process adjustments should the Scrum Master suggest during the Sprint Retrospective?
    **Answer:** The Scrum Master should suggest evaluating their estimation accuracy, reviewing if their stories are truly "Small" (the S in INVEST) before pulling them in, and ensuring they aren't over-committing their velocity during Sprint Planning.
