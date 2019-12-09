from copy import deepcopy
from .region import Region
from ..functions import Constant

def check_universe(regions):
		init = regions[0].init
		end = regions[0].end
		npoints = regions[0].npoints
		for region in regions:
			if not (region.init == init and region.end == end):
				raise ValueError('Error: Fuzzy regions are not in the same universe!')
			if not region.npoints == npoints:
				raise ValueError('Error: Fuzzy regions are not equaly discretized!')

def is_active(regions, x):
	result = []
	if type(regions) is Region:
		if regions.is_active(x):
			result.append(regions)

	if type(regions) is list:
		check_universe(regions)
		for region in regions:
			if region.is_active(x):
				result.append(region)
	return result

def union(regions, union_type='max'):
	check_universe(regions)

	result = Region('Região União', regions[0].npoints, regions[0].init, regions[0].end, Constant(0).function)
	for region in regions:
		for i, item in enumerate(region.fuzzy):
			if union_type == 'algebric_sum':
				result.fuzzy[i]['u'] = item['u'] + result.fuzzy[i]['u'] - item['u']*result.fuzzy[i]['u']
			else:
				result.fuzzy[i]['u'] = max(item['u'], result.fuzzy[i]['u'])
	result.update()
	result.region_type = 'union'
	return result

def implication(region, implication, treshold):
	if implication == 'mandani':
		region.mandani(treshold)
	elif implication == 'zadeh':
		region.zadeh(treshold)
	elif implication == 'larsen':
		region.larsen(treshold)

def agregation(regions, agregation):
	if agregation == 'max':
		return union(regions)
	if agregation == 'no_agregation':
		return regions

def inference_with_one_input(self, inputs, x, rules, implication, agregation):
	actives = is_active(inputs, x)
	outputs = []
	for active in actives:
		treshold = active.get_u(x)
		output = deepcopy(rules(active))
		implication(output, implication, treshold)
		outputs.append(output)
	return agregation(outputs, 'max')
	
# def inference_with_two_inputs(self, in_regions, x, rule_function, function_inputs=1, implication='mandani', agregation='max'):
# 	#Encontrando todas as regiões ativas nos dois inputs
# 	active_in_regions_a = self.is_active(in_regions[0], x[0])
# 	active_in_regions_b = self.is_active(in_regions[1], x[1])
# 	#criando lista de saida
# 	output_regions = []
# 	#Para cada combinação Possível de Entradas Ativas dos Inputs
# 	for active_in_a in active_in_regions_a:
# 		for active_in_b in active_in_regions_b:
# 			#encontra o treshold baseado na regra do min (E)
# 			treshold = min(active_in_a.get_u(x[0]), active_in_b.get_u(x[1]))
# 			#econtra região de saída a partir do set de regras
# 			output_region = deepcopy(rule_function(active_in_a, active_in_b))
# 			#Aplica função de implicação na região encontrada com o treshold definido
# 			if implication == 'mandani':
# 				output_region.mandani(treshold)
# 			elif implication == 'zadeh':
# 				output_region.zadeh(treshold)
# 			elif implication == 'larsen':
# 				output_region.larsen(treshold)
# 			#Adiciona a região de saída contabilizada à lista de regiões de saída ativas
# 			output_regions.append(output_region)
# 	if agregation == 'max':
# 		final_output = self.union(output_regions)
# 	if agregation == 'no_agregation':
# 		final_output = output_regions

# 	return final_output