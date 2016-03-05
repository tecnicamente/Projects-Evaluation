# -*- coding: utf-8 -*-
"""
Created on Feb  29 2016

@author: Tecnicamente

Il modulo è una raccolta di funzioni personali per la gestione, lettura e informazioni sui file
"""

import sys, os


def ControlloParametriPassati (ParametriRigaComando,NumeroParametriRichiesti,MessaggioErrore):
#"""
# La funzione verifica che vengano passati dei parametri via riga di comando.
# ParametriRigaComando:		indica il risultato dell'istruzione "sys.argv"
# NumeroParametriRichiesti:	indica quanti parametri vogliamo siano passati al programma
# MessaggioErrore:			è una stringa con il messaggio da comunicare se il set parametri è scorretto
#"""
	if len(ParametriRigaComando) < NumeroParametriRichiesti:
		print"Uso: ", parametri[0], MessaggioErrore
		sys.exit(2)
	else:
		return

def CreaFileOutput (file):
# """
# Quando la funzione viene chiamata si deve passare "sys.argv[x]"
# """
	try:
		OutputFile = open(file,"w")
		print "Creato il file: ",file
	except:
		print "sono in CreaFileOutput dentro except"
		print "Errore nella creazione del file: ", file
		sys.exit(2)
	return OutputFile

def ApriFileInput(file):
#"""
#
#"""
	try:
		InputFile = open(file,"r")
		print "Letto il file: ",file
	except:
		print "Impossibile leggere il file: ",file
		sys.exit(2)
	return InputFile
