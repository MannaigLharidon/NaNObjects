# -*- coding: utf-8 -*-
"""
Created on Wed May 30 14:19:44 2018

@author: Mannaig
"""

from skimage import io
import skimage as ski
import numpy as np
#import scipy.misc as sm

#############################################################################
#                                                                           #
#       Vérification présence ou non de NAN dans images fusionnées          #
#                                                                           #
#############################################################################

# Chargement d'une image fusionnée
image = io.imread('IMG_PHR1A_P_201704081107243_SEN_2262927101-001.tif')

# Détection de la présence de nan
nanObject = np.isnan(image)
cpt_nan = np.count_nonzero((nanObject))

if cpt_nan==0 : 
    print (" Pas de NaN dans l'image")
else :

    # Recuperer coordonnees des nan
    nan_px = np.where(nanObject)   #Attention il s'agit d'un tuple !

    # Nombre de NaN et liste des lignes sur lesquelles ils se situent
    cpt = 0
    list_val = []
    for i in range(nan_px[0].shape[0]):
        if nan_px[0][i] not in list_val :
            list_val.append(nan_px[0][i])
            cpt+=1

    # Remplacer dans ces coordonnées les nan par moyenne des pixels entourant
    for n in range(nan_px[0].shape[0]):
        image[nan_px[0][n]][nan_px[1][n]] = 0
    
    # Détection de la présence de nan dans l'image modifiée
    nanObject_bis = np.isnan(image)
    cpt_nan_bis = np.count_nonzero((nanObject_bis))


    io.imsave('IMG_PHR1A_P_201704081107243_SEN_2262927101-001_noNan.png',image)