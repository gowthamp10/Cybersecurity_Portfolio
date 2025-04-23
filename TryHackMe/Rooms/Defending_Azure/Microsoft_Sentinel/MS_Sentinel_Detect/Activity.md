# Activity performed as part of "MS Sentinal: Detect" Room

- **Lab-04: Enable an Analytics Rule** :

Step 1: Enable an Analytics Rule
1.1 Log in to the Azure portal using your lab credentials
1.2 Go to your Microsoft Sentinel dashboard and select the available workspace
1.3 Under Content management, select Content hub
1.4 Search for Azure Activity and install it
1.5 Under Configuration, select Analytics
1.6 Switch to the Rule templates tab
1.7 Search for the "rare subscription-level operations" rule
1.8 Select the rule template and click "Create rule"
1.9 Read the rule description for some background context
1.10 Expand the MITRE ATT&CK drop-down to see how to map the rule to the different MITRE Tactics and Techniques
1.11 On the Set rule logic tab, read through the Rule query
        Note the SensitiveOperationList array values
        Also, note that you can easily customize the rule query to your needs by simply modifying the SensitiveOperationList array values here
1.12 The test with current data shows you a graphical simulation of the rule
1.13 Update the Query scheduling to the following:
        Run query every 1 hour
        Lookup data from the last 7 days
1.14 On the Incident settings tab:
        Leave defaults so that incidents are created from alerts triggered by this rule.
        Alert grouping can also be done here to reduce the noise from single alert
Note: Because you might encounter an error on the Automated response tab, we will skip it for now.
1.15 Select Review + create to save the rule
1.16 Then, go back to the Active Rules tab, search for the newly created rule, select it, and click Edit on the sidebar
1.17 Select the Automated response tab:
        Add a new automation rule:
            Rule Name: Tag Rule
            Trigger: When incident is created
            Actions: Add tags
                Tag: subscription
            Rule expiration: Leave as default
        Click Apply
1.18 Finally, Review and Create the rule

Step 2: Review the Enabled Analytics Rule
2.1 Go back to the Analytics page of your Sentinel workspace
2.2 Switch to the Active rules tab
2.3 Select the recently saved rule - Rare subscription-level operations in Azure
2.4 On the right pane, review the rule details, and scroll down to see your settings for:
    Rule frequency
    Rule period
2.6 Click Compare with template to see the differences between your settings and the rule template in YAML representation

After completing this task, user should be able to:
1. Create a new analytics rule from an existing rule template
2. Review the rule properties, run schedule, and the differences from the rule template
