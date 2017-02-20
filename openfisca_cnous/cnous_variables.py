# -*- coding: utf-8 -*-
from __future__ import division
from numpy import (maximum as max_, logical_not as not_, absolute as abs_, minimum as min_, select, where)
from openfisca_france.model.base import *  # noqa analysis:ignore

class distance_domicile_familial(Variable):
    column = FloatCol
    entity = Individu
    label = u"Distance en KM entre lieu d'inscription et domicile familiale d'origine."
