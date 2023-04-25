# DevOps Accelerator

The repository contains several Accelerators developed to introduce and expand on DevOps concepts- using Microsoft tools.

Each Accelerator has a corresponding branch to demonstrate a set of examples, so ensure the fork you create maintains all branches.

## On startup, navigate to to the startup-branch:
- Ensure you have an Azure subscription, create a Resource Group and add your credentials as secrets into the GitHub repository. [https://github.com/marketplace/actions/azure-load-testing#azure-service-principal-for-rbac (steps 1-3)]
- Create a Resource Group in Azure for a webapp.
- Set RESOURCE_GROUP and WEBAPP_NAME as repository variables.
- Once you've made the above changes to the startup-branch, push the changes- this will trigger a GitHub Action workflow.
- This workflow has 2 jobs, with the first creating the resources in Azure. Once the resources are created in Azure, head to the webapp created, and save the "Publish" profile of the production and staging slot as GitHub secrets.
- Once you have saved this, review the workflow triggered against your changes, and approve the validateEnvs job.
