#!/usr/bin/python
import argparse
import pprint
import pandas
import numpy

from decisionengine.framework.modules import Source
from decisionengine.modules.htcondor import htcondor_query
from decisionengine.framework.modules import de_logger



PRODUCES = ['job_manifests']


class FakeCondorSource(Source.Source):

    def __init__ (self, *args, **kwargs):
        if args:
            config = args[0]
        else:
            config = {}

	self.logger = de_logger.get_logger()
	self.logger.info('__init__ completed')


    def produces(self):
        """
        Return list of items produced
        """
	self.logger.debug('>>> starting produces()')
        return PRODUCES


    def acquire(self):
        """
        Acquire jobs from the HTCondor Schedd
        :rtype: :obj:`~pd.DataFrame`
        """

	self.logger.debug('>>> starting acquire()')
        #dataframe = pandas.DataFrame()

        # fake output of condor_q
        job_l = [
                 {'clusterid':1, 'procid':0, 'jobstatus':1},
                 {'clusterid':1, 'procid':1, 'jobstatus':2},
                ]
        
        dataframe = pandas.DataFrame()
        df = pandas.DataFrame(job_l)
	dataframe = dataframe.append(df, ignore_index=True)

	self.logger.debug('>>> finishing acquire(). Returning %s' %dataframe)
        return {'job_manifests': dataframe}


#def module_config_template():
#    """
#    Print template for this module configuration
#    """
#    self.logger.debug('>>> starting module_config_template()')
#
#    template = {
#        'job_manifests': {
#            'module': 'modules.htcondor.s_job_q',
#            'name': 'JobQ',
#            'parameters': {
#                'collector_host': 'factory_collector.com',
#                'schedds': ['job_schedd1', 'job_schedd2'],
#                'condor_config': '/path/to/condor_config',
#                'constraints': 'HTCondor job query constraints',
#                'classad_attrs': '[]',
#            }
#        }
#    }
#    print('Entry in channel configuration')
#    pprint.pprint(template)
#
#
#def module_config_info():
#    """
#    Print module information
#    """
#    print('produces %s' % PRODUCES)
#    module_config_template()
#
#
#def main():
#
#    parser = argparse.ArgumentParser()
#    parser.add_argument(
#        '--configtemplate',
#        action='store_true',
#        help='prints the expected module configuration')
#
#    parser.add_argument(
#        '--configinfo',
#        action='store_true',
#        help='prints config template along with produces and consumes info')
#    args = parser.parse_args()
#
#    if args.configtemplate:
#        module_config_template()
#    elif args.configinfo:
#        module_config_info()
#    else:
#        pass
#
#
#if __name__ == '__main__':
#    main()

