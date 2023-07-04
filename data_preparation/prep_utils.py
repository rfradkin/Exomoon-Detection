import os
import numpy as np
from ephesos import ephesos
import copy
import utils


def return_sector_paths(sector_number):
    '''
    Returns a set of paths containing sectors of fits data from
    specified sector
    '''
    file_names = set()
    for file in os.listdir(f'../assets/fits_data/sector-{sector_number}'):
        # check if file already includes full path
        # don't remmeber, not sure
        file_names.add(f'../assets/fits_data/sector-{sector_number}/{file}')
    return file_names

def create_curves(path):
    '''
    Import a light curve from a fits file.
    '''

    body_attributes = {
        'amplitude': None,
        'density': None,
        'eccentricity': None,
        'epoch': None,
        'inclination': None,
        'mass': None,
        'period': None,
        'radius': None,
        'sin_w': None,
        'signal': None,
        'signal_time': None,
        'snr': None,
        'transit_duration': None,
        'magnitude': None,
        'effective_temperature': None
    }

    cut_attributes = {
        'times': None,
        'transit': None,
        'number': None,
        'start_index': None
    }

    curve = {
        'injection_type': None, 
        'cut': cut_attributes,
        'data': None,
        'file_name': None,
        'injection_times': None,
        'interpolation_type': None,
        'initial_padding': None,
        'linear_limb_darkening_coefficient': None,
        'model_file': None,

        'planet': copy.deepcopy(body_attributes),
        'moon': copy.deepcopy(body_attributes),
        'star': copy.deepcopy(body_attributes),

        'planet_cut_injected': None,
        'planet_moon_cut_injected': None,

        'prediction': None,
        'quadratic_limb_darkening_coefficent': None,
        'ratio_moon_planet_radius': None,
        'ratio_moon_star_radius': None,
        'ratio_planet_star_radius': None,
        'raw_curve_length': None,
        'rms': None,
        'signal': None,
        'snr': None,

        'tic_id': None,
        'toi': None,
    }

    curve['data'] = ephesos.read_tesskplr_file(path)
    curve['file_name'] = path.split('/')[-1]
    curve['tic_id'] = utils.return_TIC_id(path)
        
    return curve
