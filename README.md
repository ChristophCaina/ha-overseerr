## What is this?
This project is a fork of @vaparr's ha-overseer custom integration.  
The reason for the fork is the inactivity of the project and the adaption to jellyseerr

---
title: Jellyseer
description: Instructions on how to set up the Jellyseer integration in Home Assistant.
ha_category:
  - Sensor
ha_domain: jellyseer
---

needs to be modified
---
The `Jellyseer` integration monitors data from your Jellyseer instance.

## Setup
Install of this component should be done via HACS
* Go into HACS -> Intregrations
* 3 Dots -> Custom Repositories
* Add Custom Repository URL: https://github.com/ChristophCaina/ha-jellyseerr
* Category: Integration

Restart HA

---

This component needs to authenticate to your Jellyseer instance using your `api_key`.

To find your `api_key` open the Jellyseer web interface. Navigate to **Settings**, you should then be able to see your `api_key`.


## Configuration

If you want to enable this sensor, add the following lines to your `configuration.yaml`:  
__this is still based on the overseer integration, but will be changed in the near future__

```yaml
# Example configuration.yaml entry
overseerr:
  host: OVERSEERR_HOST
  port: OVERSEERR_PORT
  api_key: OVERSEERR_API_KEY
  scan_interval: 600
```
```
{% configuration %}
host:
  description: The hostname or IP Address Overseerr is running on.
  required: true
  type: string
api_key:
  description: Your Overseerr API key. 
  required: true
  type: string
port:
  description: The port Overseerr is running on.
  required: false
  default: 5055
  type: integer
ssl:
  description: Whether or not to use SSL when connecting to Overseerr.
  required: false
  default: false
  type: boolean
scan_interval:
  description: Polling interval for Overseerr in seconds
  required: false
  default: 60
  type: integer
{% endconfiguration %}
```
## Full example for the configuration

```yaml
# Example configuration.yaml entry
overseerr:
  host: 192.168.1.62
  port: 5055
  api_key: MTYwODIpppppppppppppppYzLTI0OqqqqqqqqqqqqzIwLeeeeeee==
```

## Services

### Submit request services

Available services: `submit_movie_request`, `submit_tv_request`

#### Service `submit_movie_request`

Searches and requests the closest matching movie.

| Service data attribute | Optional | Description                                      |
| ---------------------- | -------- | ------------------------------------------------ |
| `name`                 |      no  | Search parameter.                                |                          |

#### Service `submit_tv_request`

Searches and requests the closest matching TV show.

| Service data attribute | Optional | Description                                                                                   |
|------------------------|----------|-----------------------------------------------------------------------------------------------|
| `name`                 |       no | Search parameter.                                                                             |
| `season`               |      yes | Which season(s) to request. Must be one of `first`, `latest` or `all`. Defaults to latest.    |

## WebHook support

You can enable Webhook support in Overseerr to enable faster pending sensor updates.

In Jellyseer, navigate to Settings -> Notifications > Webhook

Check Enable Agent

for the Webhook URL use:

{{HA SERVER URL}}/api/webhook/{{JELLYSEER API KEY}}

http://homassist.local:8123/api/webhook/MTYwODIpppppppppppppppYzLTI0OqqqqqqqqqqqqzIwLeeeeeee==

Select only the boxes "Media Requested", "Media Approved"

* You will also want to have 'Enable Notifications for Auto-Approved Requests' checked in the global notifications area

* payload can be left as default

Authorization Header will most likley need to be left blank.

With webhooks enabled, you dont really need to poll overseerr anymore, so we suggest setting the scan_interval to a large value like 600 or more


