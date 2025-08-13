# Project Setup Guide (Video-Aligned)

## 1) Install tools

- Node.js LTS (with npm)
- Git
- Visual Studio Code (with ESLint and Prettier)

## 2) Create the app (as in the video)

- Scaffold a React app (e.g., Next.js)
- Initialize a Git repository (optional)

## 3) Add shadcn/ui

- Follow: [shadcn/ui](https://ui.shadcn.com/)
- Run init steps and add core components (button, card, input)

## 4) Add Clerk (authentication)

- Create an app in Clerk dashboard
- Add environment keys locally
- Wrap app with Clerk provider and add SignIn/SignUp components
- Protect routes per the video

Docs: [Clerk quick start](https://go.clerk.com/sloth-fs)

## 5) Add Convex (backend/data)

- Initialize Convex in the project
- Define a simple schema, one query, one mutation
- Call them from the UI

Docs: [Convex docs](https://www.convex.dev/)

## 6) Enable Clerk Billing

- Turn on Billing in Clerk
- Expose pricing/portal links and gate premium features

Docs: [Clerk Billing overview](https://clerk.com/docs/billing/overview)

## 7) Verify end-to-end

- Sign in works (Clerk)
- Data read/write works (Convex)
- Billing screen accessible (Clerk Billing)

Tip: Keep changes within shadcn/ui + Clerk + Convex to match the video.
