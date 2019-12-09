from copy import deepcopy
from .region import Region
from ..functions.constant import Constant
from itertools import product

def check_universe(regions):
	init = regions[0].init
	end = regions[0].end
	npoints = regions[0].npoints
	for region in regions:
		if not (region.init == init and region.end == end):
			raise ValueError('Error: Fuzzy regions are not in the same universe!')
		if not region.npoints == npoints:
			raise ValueError('Error: Fuzzy regions are not equaly discretized!')
	return npoints, init, end

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

def union(regions, union_type):
	npoints, init, end = check_universe(regions)
	result = Region('Região União', npoints, init, end, Constant(0).function)
	union = deepcopy(result.fuzzy)
	
	for region in regions:
		for i, item in enumerate(region.fuzzy):
			if union_type == 'algebric_sum':
				union[i]['u'] = item['u'] + union[i]['u'] - item['u']*union[i]['u']
			if union_type == 'max':
				union[i]['u'] = max(item['u'], union[i]['u'])
	
	result.fuzzy = union
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
		return union(regions, 'max')
	if agregation == 'no_agregation':
		return regions

def get_treshold(active_regions, x):
	if not len(active_regions) == len(x):
		raise ValueError('Error: Number of value inputs and active regions are not the same.')
	treshold = 999
	for i in range(len(active_regions)):
		treshold = min(treshold, active_regions[i].get_u(x[i]))
	return treshold

def mono_inference(self, inputs, x, rules, implication, agregation):
	actives = is_active(inputs, x)
	outputs = []
	for active in actives:
		treshold = active.get_u(x)
		output = deepcopy(rules(active))
		implication(output, implication, treshold)
		outputs.append(output)
	return agregation(outputs, agregation)

def inference(self, inputs, x, rules, implication, agregation):
	active = []
	outputs = []
	for i in range(len(inputs)):
		active.append(is_active(inputs[i], x[i]))
	
	active_rules = product(*active)
	for active_rule in active_rules:
		treshold = get_treshold(active_rule, x)
		output = deepcopy(rules(*active_rule))
		implication(output, implication, treshold)
		outputs.append(output)
	return agregation(outputs, agregation)