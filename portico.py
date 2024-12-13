from no import node as nd

# Definição dos nós
nd.no(0, 0)
nd.no(0, 4)
nd.no(4, 4)
nd.no(4, 0)
nd.no(7, 0)

from apoio import apoio

# Definição dos apoios
apoio.engaste(1)
apoio.pino(4)
apoio.pino(5)

from elemento import element as el

# Definição dos elementos
el.elemento(1, 2)
el.elemento(2, 3)
el.elemento(3, 4)
el.elemento(3, 5)

from geometria import section

# Definição das seções
section.ret(0.4, 0.4, 1)
section.ret(0.3, 0.6, 2)
section.ret(0.4, 0.4, 3)
section.circ(0.02, 4)

from material import material

# Definição dos materiais
material.concreto(1)
material.concreto(2)
material.concreto(3)
material.aco(4)

from carga_centrada import point_load as pl
pl.forca_nod(2, -20, 0, 0)

from carregdist import q_load
q_load.carga_dist(2, 40)

from matrizrigidez import result

# Executa os cálculos
result.make()

from plot_estrutura_def import plot_elements_def as ped
ped.make( 10 )

from plot_results import plot_results
plot_results
