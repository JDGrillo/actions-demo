# DevOps Accelerator

The repository contains several Accelerators developed to introduce and expand on DevOps concepts- using Microsoft tools.

Each Accelerator has a corresponding branch to demonstrate a set of examples, so ensure the fork you create maintains all branches.

## On startup, navigate to to the startup-branch:
- If using VS Code, suggested Extensions include: Black Formatter, GitHub Copilot, GitLens, Prettier, Python.
- Ensure you have an Azure subscription, create a Resource Group, Service Principal, and add your sp credentials as secrets into the GitHub repository. [https://github.com/marketplace/actions/azure-load-testing#azure-service-principal-for-rbac (steps 1-3)]
- Create two environments in GitHub named Development and Production which require manual approval.
- Set RESOURCE_GROUP and WEBAPP_NAME (your choice, use a unique name) as repository variables.
- The first time you run a GitHub Action, there must be a trigger- we'll acheive this by uncommenting lines 4 and 5 of .github\workflows\startup-workflow.yml 
- Once you've made the above changes to these lines while in the startup-branch, push the changes- this will trigger a GitHub Action workflow.
- There will be required approval between the jobs in the Workflow. Make sure the resources are created in Azure before approving. Wait ~5 minutes before approving.
- Once the Workflow is complete, navigate to the webapp url and ensure the application is running.