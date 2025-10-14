from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.utils import solo_admin
from core.models import CategoriaIncidencia, TipoIncidencia
from .forms_clasificacion import CategoriaIncidenciaForm, TipoIncidenciaForm

# ----------------- CRUD Categorías -----------------
@login_required
@solo_admin
def categoria_lista(request):
    categorias = CategoriaIncidencia.objects.all()
    return render(request, 'categoria/categoria_lista.html', {'categorias': categorias})

@login_required
@solo_admin
def categoria_crear(request):
    if request.method == "POST":
        form = CategoriaIncidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría creada correctamente.")
            return redirect('incidencias:categoria_lista')
    else:
        form = CategoriaIncidenciaForm()
    return render(request, 'categoria/categoria_form.html', {'form': form})

@login_required
@solo_admin
def categoria_editar(request, pk):
    categoria = get_object_or_404(CategoriaIncidencia, pk=pk)
    if request.method == "POST":
        form = CategoriaIncidenciaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría actualizada correctamente.")
            return redirect('incidencias:categoria_lista')
    else:
        form = CategoriaIncidenciaForm(instance=categoria)
    return render(request, 'categoria/categoria_form.html', {'form': form})

@login_required
@solo_admin
def categoria_toggle(request, pk):
    categoria = get_object_or_404(CategoriaIncidencia, pk=pk)
    categoria.estado = not categoria.estado
    categoria.save()
    estado = "activada" if categoria.estado else "desactivada"
    messages.success(request, f"Categoría {estado} correctamente.")
    return redirect('incidencias:categoria_lista')

@login_required
@solo_admin
@login_required
@solo_admin
def categoria_eliminar(request, pk):
    categoria = get_object_or_404(CategoriaIncidencia, pk=pk)
    if request.method == "POST":
        try:
            categoria.delete()
            messages.success(request, "Categoría eliminada correctamente.")
            return redirect('incidencias:categoria_lista')
        except Exception as e:
            messages.error(request, "No se puede eliminar la categoría porque tiene elementos asociados.")
            return redirect('incidencias:categoria_lista')
    return render(request, 'categoria/categoria_eliminar.html', {'obj': categoria})

# ----------------- CRUD Tipos de Incidencia -----------------
@login_required
@solo_admin
def tipo_lista(request):
    tipos = TipoIncidencia.objects.all()
    return render(request, 'tipo/tipo_lista.html', {'tipos': tipos})

@login_required
@solo_admin
def tipo_crear(request):
    if request.method == "POST":
        form = TipoIncidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de incidencia creado correctamente.")
            return redirect('incidencias:tipo_lista')
    else:
        form = TipoIncidenciaForm()
    return render(request, 'tipo/tipo_form.html', {'form': form})

@login_required
@solo_admin
def tipo_editar(request, pk):
    tipo = get_object_or_404(TipoIncidencia, pk=pk)
    if request.method == "POST":
        form = TipoIncidenciaForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de incidencia actualizado correctamente.")
            return redirect('incidencias:tipo_lista')
    else:
        form = TipoIncidenciaForm(instance=tipo)
    return render(request, 'incidencias/tipo_form.html', {'form': form})

@login_required
@solo_admin
def tipo_toggle(request, pk):
    tipo = get_object_or_404(TipoIncidencia, pk=pk)
    tipo.estado = not tipo.estado
    tipo.save()
    estado = "activado" if tipo.estado else "desactivado"
    messages.success(request, f"Tipo de incidencia {estado} correctamente.")
    return redirect('incidencias:tipo_lista')

@login_required
@solo_admin
def tipo_eliminar(request, pk):
    tipo = get_object_or_404(TipoIncidencia, pk=pk)
    if request.method == "POST":
        try:
            tipo.delete()
            messages.success(request, "Tipo de incidencia eliminado correctamente.")
            return redirect('incidencias:tipo_lista')
        except Exception as e:
            messages.error(request, "No se puede eliminar el tipo porque tiene incidencias asociadas.")
            return redirect('incidencias:tipo_lista')
    return render(request, 'incidencias/tipo_eliminar.html', {'obj': tipo})