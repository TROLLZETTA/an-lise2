from elemento import element as el

class Material:

    def __init__( self , mat = { } ) :
      self.mat = mat

    def concreto( self , n_elem ) :
      self.mat[ n_elem ] = 25000000

    def concreto( self , n_elem ) :
      self.mat[ n_elem ] = 20000000

    def aco( self , n_elem ):
      self.mat[ n_elem ] = 200000000

    def generic( self , modulo_elasticidade , n_elem ):
      self.mat[ n_elem ] = modulo_elasticidade


material = Material()