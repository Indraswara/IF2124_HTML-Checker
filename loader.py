from cnf import *

#allowable = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/<>")
allowable = list("Aa")
allowableRule = list(map(lambda v: [v], allowable))

loaderCNF = CNF(
['*S', '*H', '*T', '*A', '*W'], 
allowable + list("-|> \n"),
{
    '*S': [['*W', '*H', '*W', '-', '>', '*W', '*T', '*W'], ["*S", "\n", "*S"]],
    '*H': [['*A']],
    '*T': [['*A'], ['*A', '*W', '|', '*W', '*T']],
    '*A': allowableRule + [['*A', '*A']],
    '*W': [[], [' '], ['*W', '*W']]
}, '*S')

loaderCNF.eliminateEpsilon()
loaderCNF.eliminateUnitProductionPair()
loaderCNF.eliminateUselessSymbol()
loaderCNF.eliminateMultipleRecursion()
loaderCNF.printProductionRule()

loaderCNF.simplify()