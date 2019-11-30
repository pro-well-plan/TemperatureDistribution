from unittest import TestCase
from pwptemp import wellpath
from pwptemp.drilling import input, analysis


class TestAnalysis(TestCase):
    def test_temp_time(self):
        tdata = input.data()
        depths = wellpath.get(3000, 50)
        well = input.set_well(tdata, depths)
        eff = analysis.hs_effect(well)
        total = eff.ds_rot1 + eff.fric1 + eff.ds_rot2 + eff.fric2
        self.assertEqual(total, 100)
        self.assertIsInstance(eff.ds_rot1, float)
        self.assertIsInstance(eff.fric1, float)
        self.assertIsInstance(eff.ds_rot2, float)
        self.assertIsInstance(eff.fric2, float)
        self.assertIsInstance(eff.hsr, float)
