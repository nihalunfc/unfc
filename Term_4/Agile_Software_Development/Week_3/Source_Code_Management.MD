# Source Code Management (SCM)

**Source Code Management (SCM)** is a subset of software configuration management that tracks every modification to the code in a special kind of database. If a mistake is made, developers can turn back the clock and compare earlier versions of the code to help fix the mistake while minimizing disruption to all team members.

---

## Why Use SCM?

In the "old days," developers shared code by emailing files or using FTP. This was a nightmare for collaboration. SCM solves this by providing:

* **Version Control:** Keep a complete history of every change made to the project.
* **Branching & Merging:** Multiple people can work on the same file at the same time without overwriting each other.
* **Traceability:** Know exactly **who** changed **what** and **why** (via commit messages).
* **Experimentation:** Create a "branch" to try a new feature; if it fails, delete it. If it works, merge it back.

---

## The SCM Workflow

Most modern SCMs (specifically Git) operate using a three-tier architecture that allows you to manage changes locally before sharing them with the world.



1.  **Working Directory:** Your actual files on your computer.
2.  **Staging Area (Index):** A "prep" area where you group changes you want to include in your next snapshot.
3.  **Repository:** Where the permanent snapshots (commits) are stored.

---

## Key Concepts

| Term | Definition |
| :--- | :--- |
| **Repository (Repo)** | The project folder being tracked by the SCM. |
| **Commit** | A snapshot of your code at a specific point in time. |
| **Branch** | A parallel version of your repository (e.g., `feature-login`). |
| **Merge** | Combining changes from one branch into another (e.g., merging a feature into `main`). |
| **Clone** | Creating a local copy of a remote repository. |

---

## Centralized vs. Distributed

There are two main types of SCM systems:

### 1. Centralized (CVCS)
There is a single central server that contains all the versioned files. Developers "check out" files from that server.
* **Pros:** Easier to manage permissions.
* **Cons:** Single point of failure (if the server goes down, nobody can save history).
* **Example:** Subversion (SVN).

### 2. Distributed (DVCS)
Every developer has a full copy of the entire history of the project on their own machine.
* **Pros:** Fast, works offline, and highly reliable.
* **Cons:** Can be more complex to learn initially.
* **Example:** Git (used by GitHub, GitLab, and Bitbucket).



---

## Common Tools

* **Git:** The most popular open-source distributed SCM.
* **GitHub/GitLab:** Cloud-based platforms that host Git repositories and add collaboration tools.
* **Bitbucket:** Another Git hosting service, often used in corporate environments.
* **Perforce (Helix Core):** Often used in the gaming industry for handling very large binary files.

---

> **Pro Tip:** Always write clear, concise commit messages. Future you (and your teammates) will thank you when you're trying to figure out why a specific line of code was changed six months ago!
