from django.utils import timezone
from urllib.parse import urlencode

from researchhub.settings import PRODUCTION
from utils.exceptions import GoogleAnalyticsError
from utils.http import http_request, POST

TRACKING_ID = 'UA-106669204-1'
USER_ID = 'django'
USER_AGENT = 'Django'


class GoogleAnalytics:

    def send_hit(self, hit):
        '''
        Returns an http response after constructing a urlencoded payload for
        `hit` and sending it to Google Analytics.
        '''
        data = self.build_hit_urlencoded(hit)
        self._send_hit_data(data)

    def send_batch_hits(self, hits):
        '''
        Args:
            hit_data (:list:`str`) -- List of urlencoded hit payloads. Max 20.

        Each hit payload in `hit_data` must be no more than 8K bytes. The total
        size of all payloads must be no more than 16K bytes.
        '''
        if len(hits) > 20:
            raise GoogleAnalyticsError(ValueError, 'Exceeds 20 hits')

        hit_data = []
        for hit in hits:
            payload = self.build_hit_urlencoded(hit)
            if len(payload.encode('utf-8')) > 8000:
                raise GoogleAnalyticsError(ValueError, 'Exceeds 8k bytes per hit')
            hit_data.append(self.build_hit_urlencoded(hit))

        data = '\n'.join(hit_data)
        if len(data.encode('utf-8')) > 16000:
            raise GoogleAnalyticsError(ValueError, 'Exceeds 16k bytes')

        self._send_hit_data(data, batch=True)

    def build_hit_urlencoded(self, hit):
        '''
        Returns urlencoded string of hit and GA fields.
        '''
        hit_fields = hit.fields
        optional_fields = {
            'npa': 1,  # Exclude from ad personalization
            'ds': 'django',  # Data source
            'qt': self.get_queue_time(hit.hit_datetime),  # Ms since hit occurred
            'ni': 0,  # Non-interactive
        }
        fields = {
            'v': 1,  # GA protocol version
            't': hit.hit_type,
            'tid': TRACKING_ID,
            'uid': USER_ID,
            'ua': USER_AGENT,
            **optional_fields,
            **hit_fields
        }
        return urlencode(fields)

    def get_queue_time(self, dt):
        if dt is None:
            return 0
        delta = timezone.now() - dt
        return delta.total_seconds() * 1000

    def _send_hit_data(self, data, batch=False):
        if not PRODUCTION:
            raise GoogleAnalyticsError('Not sending outside of production env')

        base_url = 'https://www.google-analytics.com/'

        url = base_url + 'collect'
        if batch:
            url = base_url + 'batch'

        return http_request(POST, url, data=data)


class Hit:
    '''
    Hit data for Google Analytics measurement protocol.

    See https://developers.google.com/analytics/devguides/collection/protocol/v1
    for more info.

    Args:
        hit_type (str)
        hit_datetime (obj) -- None converts to the time the hit is sent
        fields (dict)
    '''
    EVENT = 'event'

    def __init__(self, hit_type, hit_datetime, fields):
        self.hit_type = hit_type
        self.hit_datetime = hit_datetime
        self.fields = fields

    def build_event_fields(
        category=None,
        action=None,
        label=None,
        value=None
    ):
        '''
        Args:
            category (str)
            action (str)
            label (str)
            value (int)
        '''
        fields = {}
        fields['ec'] = category
        fields['ea'] = action
        fields['el'] = label
        fields['ev'] = value
        return fields

    def get_required_fields(self, hit_type):
        if hit_type == self.EVENT:
            return {
                'ec': None,  # Category
                'ea': None,  # Action
                'el': None,  # Label
                'ev': None,  # Value
            }