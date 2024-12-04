from django.utils.text import slugify


def generate_unique_slug(model_class, title, slug_field_name="slug"):

    base_slug = slugify(title)
    slug = base_slug
    num = 1

    while model_class.objects.filter(**{slug_field_name: slug}).exists():
        slug = f"{base_slug}-{num}"
        num += 1
    return slug
