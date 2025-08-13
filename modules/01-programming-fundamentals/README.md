# Module 1: The Blazingly Fast Tech Stack (from The Coding Sloth)

## Overview

This module mirrors the YouTube video "The BLAZINGLY FAST Tech Stack To Build A Million Dollar App" by The Coding Sloth and focuses only on the tools shown there: shadcn/ui (UI components), Clerk (authentication and billing), and Convex (data/backend).

Video: [The BLAZINGLY FAST Tech Stack To Build A Million Dollar App](https://www.youtube.com/watch?v=gFWZM0saGGI)

Scope guard: This module intentionally excludes topics not presented in the video.

## Learning objectives

By the end, you will be able to:

- Install and configure shadcn/ui for a modern component-based UI
- Add authentication using Clerk (Sign in/Sign up, session handling, route protection)
- Connect a Convex backend for data storage, queries, and mutations
- Set up basic billing flows using Clerk Billing
- Stitch these parts into a minimal working app that mirrors the video demo

Assumptions: The video uses a React-based app (commonly Next.js) with Tailwind via shadcn/ui, plus official integrations for Clerk and Convex. If your app differs, adapt the steps to your chosen React framework.

## Sprint plan (mirrors the video)

### Part 0 — Prerequisites

- Node.js LTS and a package manager (npm, pnpm, or yarn)
- Accounts: Clerk and Convex (free tiers)
- A React app scaffold as in the video (e.g., Next.js)

### Part 1 — UI foundation with shadcn/ui

- Install shadcn/ui and run its init steps
- Add a small set of components (e.g., button, card, input) to build the shell shown in the video
- Verify Tailwind/styles are applied correctly

Deliverable: A basic shell UI that matches the video’s starting point.

### Part 2 — Authentication with Clerk

- Create an application in the Clerk dashboard
- Configure environment variables/keys locally
- Drop in Clerk SignIn/SignUp components and session provider
- Protect routes/components so only signed-in users can access the app body

Deliverable: Authenticated access flow per the video.

### Part 3 — Data/backend with Convex

- Initialize Convex in the project
- Define a simple schema/collections and write one query and one mutation
- Call Convex from the UI to create/read data

Deliverable: A working client ↔ Convex data loop as demonstrated.

### Part 4 — Billing with Clerk Billing

- Enable Billing in Clerk and connect the required settings
- Expose pricing/portal links per the video’s approach
- Gate premium features based on billing status

Deliverable: Basic billing integration per the video.

### Wrap-up

- Ensure shadcn/ui + Clerk + Convex + Billing work together end-to-end
- Save a minimal demo recording or screenshots for your portfolio

## Assessment

- Recreate the app demonstrated in the video using only shadcn/ui, Clerk, and Convex
- Show a successful sign-in, a Convex-backed data action, and a billing screen/flow

## Resources (from the video description)

- [shadcn/ui](https://ui.shadcn.com/)
- [Clerk](https://go.clerk.com/sloth-fs)
- [Convex](https://www.convex.dev/)
- [Clerk + Convex docs](https://clerk.com/docs/integrations/databases/convex)
- [Clerk Billing docs](https://clerk.com/docs/billing/overview)

## Support and help

- Use the official docs linked above (they match the video)
- Discuss blockers with peers; keep changes within the video’s toolset

## Completion requirements

1. Working UI shell using shadcn/ui
2. Clerk-authenticated routes with session state
3. Convex data wired into the UI (one read + one write)
4. Billing flow accessible via Clerk Billing
5. A short walkthrough (screenshots or a 1–2 min capture) of the app in action

---

Module duration: short sprint (adjust to your pace)

Prerequisites: basic JavaScript/React familiarity

Difficulty: beginner–intermediate (focused on integration)

Primary tools: shadcn/ui, Clerk, Convex (as in the video)
