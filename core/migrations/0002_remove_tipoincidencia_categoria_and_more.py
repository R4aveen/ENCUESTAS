"""
Este archivo de migración fue convertido en no-op manualmente porque el estado actual
del modelo `core` fue restablecido al esquema original (sin CategoriaIncidencia).
Dejar un stub evita que Django intente ejecutar operaciones que ya no aplican.

Si prefieres eliminar físicamente este archivo, puedes borrarlo del filesystem.
"""

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        # No-op: maneja la migración anterior que fue revertida manualmente en el código.
    ]
