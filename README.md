# gi-connections-from-csv
Add connections to Guardium Insights from a CSV file.
Notes:
- Currently, only Azure Event Hubs connections are supported
- Requires Python3

# Instructions
- Install python dependencies found in requirements.txt: `pip3 install -r requirements.txt`
- Edit `config.yaml` and add your configuration settings for your Guardium Insights instance (URL and API Key)
- Edit `connections_to_be_added.csv` and add the properties for each Azure Event Hub connection in a given row. Note: Each column must have an entry and do not rename or remove header names (you can change the order though if you want).

Example CSV connection entry:

| db_name | account_name | cluster_resource_id | consumer_group_name | db_dns_endpoint | db_type     | name         | port | provider | storage_connection_string |
| ------- | ------------ | ------------------- | ------------------- | --------------- | ----------- | ------------ | ---- | -------- | ------------------------- |
| db1     | azure1       | ccaf2485-dd45...    | giconsumethis       | gd.windows.net  | MSSQLServer | eventhubname | 1433 | Azure    | BlobEndpoint=https://...  |

- Run main.py to create the connections: `python3 main.py`
