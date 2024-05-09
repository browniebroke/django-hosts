from urllib.parse import urlparse

from django.test import AsyncClient, Client


class HostClientMixin:
    """Test client to help work with django-hosts in tests."""
    def generic(self, method, path, *args, **kwargs):
        if path.startswith("http"):
            # Populate the host header from the URL host
            _scheme, host, *_others = urlparse(path)
            kwargs.setdefault("headers", {})
            kwargs["headers"]["host"] = host
        return super().generic(method, path, *args, **kwargs)


class HostsClient(HostClientMixin, Client):
    pass


class HostsAsyncClient(HostClientMixin, AsyncClient):
    pass
