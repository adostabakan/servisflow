"""Ortam doğrulama testi: paket ve katmanlar içe aktarılabiliyor mu?"""

import servisflow
from servisflow import repository, services, ui


def test_paket_surumu_tanimli():
    assert servisflow.__version__


def test_katmanlar_ice_aktarilabilir():
    assert services is not None
    assert repository is not None
    assert ui is not None
