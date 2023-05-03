#!/usr/bin/env python3

from requests import get, post
import json
import csv
import yaml

# import configuration from yaml
with open("config.yaml", "r") as file:
    try:
        configs = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)

gi_url = configs['gi-url']
api_key = configs['gi-api-key']
csv_path = configs['local-csv-file-path']


def get_connection_accounts():
    response = get(gi_url + '/api/v3/connections/accounts', headers={'accept': 'application/json',
                                                                     'authorization': api_key},
                   verify=False)

    return response


def lookup_account_id(account_name):
    account_configs = (get_connection_accounts().json())

    for account in account_configs['account_configs']:
        if account['account']['name'] == account_name:
            return account['account_id']


def import_connections_from_csv():
    connections_list = []

    with open(csv_path, newline='', encoding='utf-8-sig') as csv_file:
        reader = csv.DictReader(csv_file)  # import the csv file as a dictionary, use headers as key

        for row in reader:        # type: dict
            account_id = lookup_account_id(row['account_name'])
            imported_connection = {"type": "AZURE", "stream_connection": {"password": "", "start_monitor": "true",
                                                                          "account_id": account_id, "username": ""}}
            # add the content from the csv row to the connection
            imported_connection["stream_connection"].update(row)
            connections_list.append(imported_connection)     # add the full connection

    return connections_list


def create_connection_in_gi(connection_config):
    response = post(gi_url + '/api/v3/connections/configs',
                    headers={'accept': 'application/json',
                             'authorization': api_key,
                             'Content-Type': 'application/json'},
                    data=json.dumps(connection_config),        # json payload of the connection
                    verify=False)

    print("Creating connection...\n")
    print(json.dumps(connection))
    print(response.text)


# import the connections to be added from the CSV file
imported_connections = import_connections_from_csv()

# iterate through the list of connections and add them one by one
for connection in imported_connections:
    create_connection_in_gi(connection)

if __name__ == '__main__':    # code to execute if called from command-line
    pass    # do nothing - code deleted
