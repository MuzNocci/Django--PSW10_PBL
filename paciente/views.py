from django.shortcuts import render
from medico.models import DadosMedico, Especialidades



def home(request):

    if request.method == "GET":

        medico_filtrar = request.GET.get('medico')
        especialidades_filtrar = request.GET.getlist('especialidades')
        medicos = DadosMedico.objects.all()
        especialidades = Especialidades.objects.all()

        if medico_filtrar:
            medicos = medicos.filter(nome__icontains = medico_filtrar)

        if especialidades_filtrar:
            medicos = medicos.filter(especialidade_id__in=especialidades_filtrar)

        return render(request, 'home.html', {'medicos':medicos, 'especialidades':especialidades})