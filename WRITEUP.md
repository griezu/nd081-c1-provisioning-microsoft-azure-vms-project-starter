# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

The price for both is relatively low since the CMS app does not need much processing. The appservice is a managed service and therefore the user does not have full control of the app itself. With the VM the user is able to set up all the services and connections to databases and other services. As well, the user can access to the files that are hosting the app and modify them directly(or from git). The VMs have been proved to be a bit more reliable since, with the app services, there are some downtime periods that recover themselves after a while. 

The CMS is a simple web app that is not critical and does not need a lot processing power. A managed service would simplify the deployment of the app and that is why I have chosen the Azure App Service to host the app. 

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

If the uptime was critical for the app or if I needed full access to assess the possible errors fast, I would probably consider changing to a VM. 