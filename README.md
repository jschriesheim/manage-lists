# Manage Lists - webhook implementation to support API.AI voice actions

This webhook implementation that gets Api.ai classification JSON (i.e. a JSON output of Api.ai /query endpoint), modifies or reads list data, and returns a fulfillment response.

More info about Api.ai webhooks could be found here:
[Api.ai Webhook](https://docs.api.ai/docs/webhook)

# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?
It's a fulfillment service that maintains lists for shopping. Each operation provides an item name and a list name.
Supported actions include "add item to list", "delete item from list", "create list", "delete list" and "read list".

The service packs the result in the Api.ai webhook-compatible response JSON and returns it.

