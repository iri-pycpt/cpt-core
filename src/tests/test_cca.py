import cpttools as ct 
from .. import canonical_correlation_analysis

from pathlib import Path 

def test_cca(**kwargs):
    x = ct.open_cptdataset(Path( __file__ ).absolute().parents[0] / 'data/seasonal/SEASONAL_CANCM4I_PRCP_HCST_JUN-SEP_None_2021-05.tsv').prec
    y = ct.open_cptdataset( Path( __file__).absolute().parents[0] / 'data/seasonal/SEASONAL_CPCCMAPURD_PRCP_OBS_JUN-SEP_None_2021-05.tsv').prate
    f = x.isel(T=slice(-1, None))
    x = x.isel(T=slice(None,-1))
    hcsts, fcsts, skill, loadings = canonical_correlation_analysis(x, y, F=f, **kwargs)
    return hcsts, fcsts, skill, loadings