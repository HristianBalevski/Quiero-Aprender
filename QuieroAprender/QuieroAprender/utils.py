from django.utils.text import slugify


def generate_unique_slug(model_class, title, slug_field_name="slug", max_length=80):
    base_slug = slugify(title)[:max_length]

    if len(base_slug) >= max_length - 10:
        base_slug = base_slug[:max_length - 10]

    slug = base_slug
    num = 1

    while model_class.objects.filter(**{slug_field_name: slug}).exists():
        slug = f"{base_slug}-{num}"
        num += 1
    return slug
