from django.forms import ModelForm
<<<<<<< HEAD
from .models import Pessoa, Veiculo
=======
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)

>>>>>>> HOMEOFFICE

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
<<<<<<< HEAD
        
class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
=======


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class MovRotativoForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'


class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'


class MovmensalistaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'
>>>>>>> HOMEOFFICE
