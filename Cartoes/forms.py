# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from .models import Cartao
__author__ = 'hermogenes'

class FormCartao(forms.ModelForm):

    class Meta:
        model = Cartao
        fields = '__all__'