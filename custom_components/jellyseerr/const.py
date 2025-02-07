"""Support for Jellyseer."""
ATTR_NAME = "name"
ATTR_SEASON = "season"
ATTR_ID = "request_id"
ATTR_STATUS = "new_status"

CONF_URLBASE = "urlbase"

DEFAULT_NAME = DOMAIN = "jellyseer"
DEFAULT_PORT = 5055
DEFAULT_SEASON = "latest"
DEFAULT_SSL = False
DEFAULT_URLBASE = ""

SERVICE_MOVIE_REQUEST = "submit_movie_request"
SERVICE_MUSIC_REQUEST = "submit_music_request"
SERVICE_TV_REQUEST = "submit_tv_request"
SERVICE_UPDATE_REQUEST = "update_request"

SENSOR_TYPES = {
    "movies": {"type": "Movie requests", "icon": "mdi:movie"},
    "tv": {"type": "TV Show requests", "icon": "mdi:television-classic"},
    # "music": {"type": "Music album requests", "icon": "mdi:album"},
    "pending": {"type": "Pending requests", "icon": "mdi:clock-alert-outline"},
    # "approved": {"type": "Approved requests", "icon": "mdi:check"},
    # "available": {"type": "Available requests", "icon": "mdi:download"},
    "total": {"type": "Total requests", "icon": "mdi:movie"},
    "issues": {"type":"Issues", "icon": "mdi:movie"},
}
