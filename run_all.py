from modules import Create_json, VariableTransformation, variableChecks, AtplanToScarModel, CVXPY_Optimization, CheckPenetrations
import logging

repo_path = './'

params = Create_json.main(repo_path)

logging.info('Beginning variable transformation script')
VariableTransformation.main(params)
logging.info('Variable transformation script complete')

logging.info('Beginning variable checks script')
variableChecks.main(params)
logging.info('Variable checks script complete')

logging.info('Beginning modeling script')
AtplanToScarModel.main(params)
logging.info('Modeling script complete')

logging.info('Beginning optimization script')
CVXPY_Optimization.main(params)
logging.info('Optimization script complete')

logging.info('Beginning final output script')
CheckPenetrations.main(params)
logging.info('Final output script complete')