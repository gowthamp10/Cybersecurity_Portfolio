# Activity performed as part of "MS Sentinal: Deploy" Room

- **Lab-01: Deploy Microsoft Sentinel** :

Lab scenario: A SIEM product needs to be utilized as part of organizational security policies. Your initial assignment is to onboard Microsoft Sentinel for the organization. 
You will:
1. First, create a Log Analytics workspace.
2. Then, enable/onboard Microsoft Sentinel to that workspace.


Step 1: Create a Log Analytics Workspace (LAW)
1.1 Click on Cloud Deatils button, Join the lab.
1.2 Log into the Azure portal using your lab credentials.
1.3 Using the top search bar, search for "Sentinel" and select "Microsoft Sentinel" in the dropdown.
1.4 Click Create Microsoft Sentinel.
1.5 On the Add Microsoft Sentinel to a workspace page, click Create a new workspace.
1.6 Create a Log Analytics workspace (LAW) instance with the following values (your values might differ from the below screenshot):
    Subscription: Az-Subs-B2C-1
    Resource Group: rg-04184635
    Name: law-04184635
    Region: East US
1.7 Click Review + Create followed by Create again.
1.8 Wait for the LAW deployment.
1.9 Confirm that the new LAW is listed on the Add Microsoft Sentinel to a workspace page (you might need to refresh).

Step 2: Add Microsoft Sentinel to the workspace
2.1 Select recently created LAW, and click Add.
2.2 Wait for Microsoft Sentinel to be added to the LAW.
2.3 Click OK after the Microsoft Sentinel free trial activated message.
2.4 Browse through the Get Started page to get an idea of what's to come next.
2.5 Go to General -> Overview on the left hand side to see the tiles - Incidents, Data, Automation and Analytics.
2.6 Confirm that no data connectors or incidents have been found yet, as this is a brand-new deployment.

