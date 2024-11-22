from django import forms
from django.utils.safestring import mark_safe

class CKEditor5Widget(forms.Textarea):
    class Media:
        js = (
            'https://cdn.ckeditor.com/ckeditor5/38.1.1/classic/ckeditor.js',
        )

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        ckeditor_script = f"""
        <script>
            ClassicEditor
                .create(document.querySelector('#id_{name}'))
                .catch(error => {{
                    console.error(error);
                }});
        </script>
        """
        return mark_safe(html + ckeditor_script)
