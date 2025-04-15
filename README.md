# Talos Escalations - CUA Injection Tool

The purpose of this tool is to take a list of URLs and inject\
telemetry data to CUA to assist with ticket automation.

# Release Notes
0.2\
take the url list and parse to remove hxxps or hxxp from the submissions

0.1\
initial release uses python requests\
tests connectivity and authentication to armory\
user inputs a xlsx file from ACE to extract all the entries (urls) and inject to ACE
take a hard coded list of urls or single url and posts to armory/cua for telemetry injection