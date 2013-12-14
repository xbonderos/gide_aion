from django.db.models import F

from aion.pageviews.models import HitCount


class PageViewsMiddleware:
    def process_request(self, request, *args, **kwargs):
        hit, hit_created = HitCount.objects.get_or_create(url=request.path)
        hit.hits = F('hits') + 1
        hit.save()

        return None
