from rest_framework import serializers

from hotelaria.models import Funcionario, tipoFuncionario, Servico, tipoQuarto, Quarto

class quartoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model=Quarto
        fields="__all__"

class tipoQuartoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model=tipoQuarto
        fields="__all__"

class tipoFuncionarioSerializer(serializers.ModelSerializer): 
    class Meta: 
        model=tipoFuncionario
        fields="__all__"

class funcionarioSerializer(serializers.ModelSerializer): 
    class Meta: 
        model=Funcionario
        fields="__all__"

class servicoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model=Servico
        fields="__all__"

class tipoQuartoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model=tipoQuarto
        fields="__all__"



