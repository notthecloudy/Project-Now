import scratchattach as scratch3
import base64
from key import create_entry, read_database, update_value, delete_entry, check_validity, add_view, refresh_values

session = scratch3.login("Etherlastic", "Goldenboy12")
conn = session.connect_cloud(project_id="984352701")

client = scratch3.CloudRequests(conn, ignore_exceptions=True)

encoded_string = 'data:text/plain;base64,' + base64.b64encode(str("ggs").encode("utf-8")).decode('utf-8')
print(encoded_string)

@client.request
def create_asset(argument1):
    value = argument1
    key, stored_value = create_entry(value)
    print("Generated key:", key)
    print("Stored value:", stored_value)
    return key

@client.request
def asset_search(argument1):
    validity = check_validity(argument1)
    print("Key searched: " + argument1 + (" is " + (validity)))
    return validity

@client.request
def view_asset(argument1):
        add_view(argument1)
        print("Successfully incremented view.")
        return "Successfully incremented view."

@client.request
def get_values(argument1):
    values = refresh_values()
    print("Values successfully refreshed.")
    return ",".join(values)

@client.request
def base64(argument1):
    encoded_string = 'data:text/plain;base64,' + base64.b64encode(argument1.encode("utf-8"))
    return encoded_string

@client.event
def on_ready():
    print("Request handler is ready")

client.run()
