from .config import sample_data
from .context import pandas_ta

from unittest import TestCase
from pandas import DataFrame



class TestVolatilityExtension(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = sample_data

    @classmethod
    def tearDownClass(cls):
        del cls.data


    def setUp(self): pass
    def tearDown(self): pass


    def test_aberration_ext(self):
        self.data.ta.aberration(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-4:]), ["ABER_ZG_5_15", "ABER_SG_5_15", "ABER_XG_5_15", "ABER_ATR_5_15"])

    def test_accbands_ext(self):
        self.data.ta.accbands(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-3:]), ["ACCBL_20", "ACCBM_20", "ACCBU_20"])

    def test_atr_ext(self):
        self.data.ta.atr(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "ATR_14")

    def test_bbands_ext(self):
        self.data.ta.bbands(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-3:]), ["BBL_5_2.0", "BBM_5_2.0", "BBU_5_2.0"])

    def test_donchian_ext(self):
        self.data.ta.donchian(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-3:]), ["DCL_20_20", "DCM_20_20", "DCU_20_20"])

    def test_kc_ext(self):
        self.data.ta.kc(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-3:]), ["KCL_20", "KCB_20", "KCU_20"])

    def test_massi_ext(self):
        self.data.ta.massi(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "MASSI_9_25")

    def test_natr_ext(self):
        self.data.ta.natr(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "NATR_14")

    def test_pdist_ext(self):
        self.data.ta.pdist(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "PDIST")

    def test_rvi_ext(self):
        self.data.ta.rvi(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "RVI_14")

    def test_rvi_refined_ext(self):
        self.data.ta.rvi(refined=True, append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "RVIr_14")

    def test_rvi_thirds_ext(self):
        self.data.ta.rvi(thirds=True, append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "RVIt_14")

    def test_true_range_ext(self):
        self.data.ta.true_range(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "TRUERANGE_1")