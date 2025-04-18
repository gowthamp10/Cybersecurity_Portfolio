# Activity performed as part of "MS Sentinel: Ingest Data" Room

- **Lab-02: Install Content Hub Solutions** :

Lab scenario: Following the initial deployment of Microsoft Sentinel, you are tasked with installing a Content hub solution.
1. First, make sure Sentinel is enabled for the workspace
2. Then, you will install a Content hub solution
3. Finally, you will review the results

Solution steps:
Step 1: Install a Content hub solution
1.1 Log in to Azure portal using your lab credentials
1.2 Go to Microsoft Sentinel and open the available workspace
1.3 Under Content management, select Content hub
(Note that currently, no standalone contents or packaged solutions are installed)
1.4 Search for solution: Microsoft Entra ID, select it and click Install
1.5 Wait for the content hub installation to complete

Step 2: Review the results
2.1 Select the recently installed Content hub solution
2.2 Review the Content hub solution details on the right pane
2.3 Note that various content types are deployed by this Content hub solution:
    63 Analytics Rules
    1 Data Connector
    11 Playbooks
    2 Workbooks (dashboards)
2.4 Click Manage to see the package details for the Content hub solution
2.5 Under Content name, click on Microsoft Entra ID
2.6 Review the data connector status
2.7 Note that the data connector is installed. However, it is still not connected yet. We will do this later on
2.8 After completing this lab, now you should be able to:
    Install a Content hub solution
    Review an installed Content hub solution and it's connector status


- **Lab-03: Connect and Configure a Data Connector** :

Lab scenario: Following the installation of the Content hub solution, you are tasked with configuring data connectors.
1. First, you will install another Content hub solution: Threat Intelligence
2. Then, you will connect the data connector
3. Finally, you will review the ingested Threat Intelligence data

Step 1: Install the Threat Intelligence Content hub solution
1.1 Log in to Azure portal using your lab credentials
1.2 Go to Microsoft Sentinel and open the available workspace
1.3 Under Content Management, Select Content hub
1.4 Search for Threat Intelligence and select it
1.5 Install the Threat Intelligence Content hub solution

Step 2: Connect the Threat Intelligence data connector
2.1 After the installation is complete, select Manage to review the deployed Threat Intelligence (TI) connectors
2.2 Select the Microsoft Defender Threat Intelligence data connector and open the connector page
2.3 Notice the Prerequisites and Configuration sections:
    Prerequisites will show the required permissions to configure the data connector.
(For this data connector, only workspace-scoped permissions are needed, which you already have
Other data connectors might have different permission requirements on various scopes depending on the integration nature of that data connector)
2.4 Click Connect to import Indicators of Compromise (IOCs) from Microsoft Defender Threat Intelligence (MDTI) into Microsoft Sentinel
2.5 Review the data connector's status to ensure it is connected
(When the log data starts to flow, the Last Log Received will be updated (this might take 10-15min, but it's not required to wait for it))
2.6 Once the connection is established, the data type icon will turn to green, indicating that the corresponding log table is populated and now contains data in the Log Analytics workspace.
2.7 Clicking on the table name will take you to the ThreatIntelligenceIndicator log table in the Log Analytics workspace.
