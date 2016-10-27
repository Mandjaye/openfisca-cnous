# -*- coding: utf-8 -*-
from __future__ import division

from numpy import (maximum as max_, logical_not as not_, absolute as abs_, minimum as min_, select, where)

from openfisca_france.model.base import *  # noqa analysis:ignore

from openfisca_cnous.plafonds import get_plafond    
import ipdb
#       ipdb.set_trace()
import numpy as np


class bourse(Variable): 
    column = FloatCol
    entity = Individus
    label = u"Aide financière accordée à un écycle_suptudiant en fonction de(s revenus d'imposition/ des freres et soeurs/ de la distance par rapoort au foyer."

    def function(individu, period, legislation):
        period = period.this_month
        ## nbr d'enfants enseignements supétrieur
        nbr_siblings_cycle_sup = individu.foyer_fiscal('f7ef', period)

        # cast foyer fiscal -> individu
        nbr_siblings_cycle_sup = individu.foyer_fiscal.project(nbr_siblings_cycle_sup)

        ## total de personne
        nbr_siblings = individu.foyer_fiscal.nb_persons(role=PERSONNE_A_CHARGE)

        # cast foyer fiscal -> individu
        nbr_siblings = individu.foyer_fiscal.project(nbr_siblings)

        nbr_siblings_non_cycle_sup = nbr_siblings - nbr_siblings_cycle_sup 
        #montant_par_enfant = legislation(period).ma_collectivite.mon_aide.montant
        distance = individu('distance_domicile_familial', period)
        cond_dist_0 = distance >250 
        cond_dist_1 = distance > 30
        cond_dist_2 = distance < 30

        # revenu global du foyer
        avis_imposition_required = individu.foyer_fiscal('rbg', period.n_2)

        # calcul du point de charge
        pc = nbr_siblings_non_cycle_sup*2 + (nbr_siblings_cycle_sup-1)*4 #+ select([cond_dist_0, cond_dist_1, cond_dist_2], [2,1,0])

        list_plafond = get_plafond(pc)
        list_plafond = list_plafond[::-1]
        conditions = [avis_imposition_required <= plafond for plafond in list_plafond]



        echelon = select(
          conditions,
          range(7,-1,-1),
          -1
          )
        # liste des montants alloues aux etudiants en fonctions des criteres .
        list_montants_aides = np.asarray([1009, 1669, 2513, 3218, 3924, 4505, 4778, 5551])

        return (period,list_montants_aides[echelon])