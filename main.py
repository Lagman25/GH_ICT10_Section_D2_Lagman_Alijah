# Working with Sets
from pyscript import display

wrestling = {'Euan', 'Harvey', 'Aaron', 'Marcus'}
valorant = {'Cad', 'Chris', 'Euan'}

display(wrestling | valorant, target='output')
display(wrestling & valorant, target='output')
display(wrestling - valorant, target='output')
display(valorant - wrestling, target='output')
display(wrestling ^ valorant, target='output')