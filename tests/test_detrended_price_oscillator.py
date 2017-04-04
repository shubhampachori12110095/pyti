import unittest
import numpy as np

from tests.sample_data import SampleData
from py_ti import detrended_price_oscillator


class TestDetrendedPriceOscillator(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.dop_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        1.6849999999999454, 2.2975000000001273, 3.9800000000000182,
        0.10500000000001819, -2.5950000000000273, 2.3524999999999636,
        3.9199999999999591, 0.65999999999996817, -6.2950000000000728,
        -3.1949999999999363, -11.795000000000073, -9.5274999999999181,
        -16.887500000000045, -7.0399999999999636, -13.122499999999945,
        -6.4674999999999727, 5.1574999999999136, 15.912500000000023,
        6.92999999999995, -2.6275000000000546, -4.6075000000000728,
        2.5025000000000546, 2.5499999999999545, -5.2225000000000819,
        3.1775000000000091, -1.7474999999999454, -4.1575000000000273,
        -20.409999999999854, 1.7225000000000819, 10.184999999999945,
        27.877499999999941, 19.577499999999986, 2.0574999999998909,
        -19.075000000000045, -12.134999999999991, -0.015000000000100044,
        16.182500000000005, 13.402499999999918, 13.719999999999914,
        4.2775000000000318, 4.8725000000000591, 6.6600000000000819,
        9.8050000000000637, -3.5525000000001228, -5.8650000000000091,
        -0.03999999999996362, -2.0775000000001, -12.422500000000014,
        -10.404999999999973, -5.1724999999999, 4.9474999999999909,
        2.0650000000000546, 4.2724999999999227, -8.3450000000000273,
        -3.8024999999998954, -3.5674999999999955, 0.83749999999997726,
        -1.4900000000000091, 1.9449999999999363, 0.17250000000001364,
        5.7749999999999773, 3.8575000000000728, -3.8700000000000045,
        5.3600000000000136, 4.8775000000000546, -4.6175000000000637,
        -9.1500000000000909, -8.6475000000000364, -1.5724999999999909,
        2.6374999999999318, -5.8025000000000091, -5.875, 4.0125000000000455,
        -3.1399999999999864, 8.125, 8.4574999999999818, 6.1874999999998863,
        -7.0599999999999454, -9.6700000000000728, -6.6849999999999454,
        -0.59000000000003183, 3.5724999999999909, 0.51749999999992724,
        -1.7650000000001, 0.11500000000000909, 2.9125000000000227,
        2.3399999999999181, 2.9524999999998727, 3.7649999999999864,
        4.2274999999999636, -1.0625, 2.1299999999999955, 2.1449999999999818,
        2.6000000000001364, 1.0650000000000546, -0.32499999999993179,
        -2.1200000000000045, -0.10249999999996362, -6.9724999999999682,
        -3.1625000000000227, -0.68499999999994543, 1.63250000000005,
        -6.4900000000000091, -23.720000000000027, -18.052500000000009,
        -11.550000000000068, -3.2250000000000227, 0.17499999999995453,
        -2.80499999999995, 0.0075000000000500222, -2.6349999999999909,
        -1.3250000000000455, -14.200000000000045, -8.7100000000000364,
        -9.0475000000000136, -0.84500000000002728, -4.0474999999999,
        -8.9625000000000909, -13.927500000000009, -6.3324999999999818,
        -4.8350000000000364, 2.4075000000000273]

        self.dop_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, 4.2380000000001701, 1.0240000000000009,
        -2.0439999999999827, 2.571999999999889, 3.6739999999999782,
        1.0960000000000036, -5.4240000000000919, -3.7960000000000491,
        -13.980000000000018, -12.395999999999958, -19.853999999999928,
        -11.877999999999929, -16.639999999999986, -10.601999999999975,
        4.0659999999999172, 14.973999999999933, 9.8099999999999454,
        1.0720000000000027, -3.0620000000001255, 1.1139999999999191,
        1.8419999999999845, -5.0240000000000009, 3.9739999999999327,
        -2.40199999999993, -5.2540000000000191, -20.877999999999929,
        -1.5039999999999054, 8.2100000000000364, 28.388000000000034,
        27.413999999999987, 7.7019999999998845, -15.09800000000007,
        -14.388000000000034, -4.7240000000000464, 13.635999999999967,
        16.481999999999971, 18.449999999999932, 9.20799999999997,
        7.2220000000000937, 9.0579999999999927, 11.080000000000155,
        -1.4999999999998863, -4.7859999999999445, -0.32399999999995543,
        -4.5120000000000573, -13.382000000000062, -11.730000000000018,
        -8.7399999999998954, 2.01400000000001, 2.1979999999999791,
        5.3319999999999936, -7.3500000000000227, -4.7799999999999727,
        -4.5219999999999345, -1.6059999999999945, -1.2580000000000382,
        1.7519999999999527, 0.41999999999995907, 6.0739999999999554,
        5.1560000000000628, -3.3780000000000427, 6.7520000000000664,
        5.0799999999999272, -4.8339999999999463, -7.8940000000000055,
        -10.831999999999994, -4.8539999999999281, 1.3500000000000227,
        -6.5060000000000855, -6.0340000000001055, 3.3799999999999955,
        -5.0620000000000118, 8.9759999999999991, 10.619999999999891,
        6.7899999999999636, -3.9700000000000273, -10.024000000000001,
        -8.9759999999999991, -3.6920000000000073, 2.6480000000000246,
        0.77800000000002001, -1.1220000000001846, 0.42799999999999727,
        2.4840000000000373, 2.6180000000000518, 4.0319999999998117,
        4.8419999999998709, 5.1479999999999109, -0.0019999999999527063,
        2.9660000000000082, 2.5760000000000218, 2.6360000000000809,
        2.3120000000001255, 0.044000000000096406, -2.0599999999999454,
        -0.33600000000001273, -7.8259999999999081, -4.2420000000000755,
        -1.5699999999999363, 0.10800000000006094, -6.3740000000000236,
        -25.591999999999985, -22.072000000000003, -17.898000000000025,
        -9.3440000000000509, -1.1720000000000255, -3.7559999999999718,
        -0.10799999999983356, -2.92999999999995, -2.2759999999999536,
        -15.116000000000099, -11.224000000000046, -12.024000000000001,
        -4.8139999999999645, -4.9239999999999782, -10.773999999999887,
        -15.586000000000126, -9.7740000000000009, -8.3300000000000409,
        0.41999999999995907]

        self.dop_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, -1.3633333333333439, 3.1383333333333212,
        4.0099999999998772, 0.93666666666672427, -5.2866666666666333,
        -3.228333333333353, -15.063333333333503, -14.733333333333348,
        -23.071666666666715, -14.844999999999914, -21.364999999999895,
        -13.974999999999909, 0.78999999999996362, 14.688333333333389,
        9.4366666666664969, 3.5166666666666515, -0.10666666666668334,
        2.4483333333332666, 0.76166666666654237, -5.8233333333333803,
        4.30499999999995, -1.838333333333253, -6.0183333333333167,
        -22.661666666666633, -1.9566666666665924, 5.8633333333333439,
        27.925000000000068, 28.981666666666683, 14.553333333333171,
        -11.023333333333426, -11.673333333333289, -6.7983333333334031,
        10.279999999999859, 15.046666666666624, 21.784999999999968,
        13.533333333333303, 11.631666666666661, 11.393333333333317,
        13.540000000000077, -0.49999999999988631, -3.2749999999998636,
        0.56166666666672427, -4.9366666666666106, -15.968333333333362,
        -13.01833333333343, -10.208333333333371, -0.875, -0.15499999999985903,
        5.6649999999999636, -6.7733333333331984, -4.1499999999999773,
        -5.5250000000000909, -2.4683333333332484, -3.3466666666665787,
        2.0183333333333167, 0.27666666666664241, 6.533333333333303,
        5.6200000000000045, -2.4366666666666106, 7.4433333333332712,
        6.4516666666667106, -4.8666666666666742, -8.4033333333333076,
        -10.236666666666679, -6.8766666666666652, -1.3283333333333758,
        -7.8500000000000227, -6.8716666666666697, 3.3883333333333212,
        -5.8000000000000682, 7.7483333333333348, 11.771666666666647,
        8.8749999999998863, -3.6333333333334394, -7.8666666666667879,
        -9.6449999999999818, -5.7550000000001091, 0.17333333333340306,
        0.040000000000077307, -0.95166666666671063, 0.98166666666656965,
        2.8483333333333576, 2.3700000000000045, 4.4316666666667288,
        5.9433333333332712, 6.2599999999999909, 0.76499999999998636,
        3.9733333333333576, 3.3799999999998818, 3.1050000000001319,
        2.4383333333333894, 1.0850000000001501, -1.838333333333253,
        -0.30000000000006821, -8.3466666666666924, -5.1299999999998818,
        -2.5350000000000819, -0.62499999999988631, -7.9099999999999682,
        -26.561666666666611, -24.55166666666662, -21.993333333333339,
        -15.023333333333426, -6.32000000000005, -5.0350000000000819,
        -0.90499999999997272, -3.1483333333333121, -2.6166666666665606,
        -16.538333333333412, -12.455000000000155, -14.620000000000005,
        -7.4950000000000045, -8.4366666666666106, -11.953333333333262,
        -17.745000000000005, -11.563333333333389, -11.545000000000073,
        -2.4750000000000227]

    def test_dop_period_6(self):
        period = 6
        dop = detrended_price_oscillator.detrended_price_oscillator(self.data, period)
        np.testing.assert_array_equal(dop, self.dop_period_6_expected)

    def test_dop_period_8(self):
        period = 8
        dop = detrended_price_oscillator.detrended_price_oscillator(self.data, period)
        np.testing.assert_array_equal(dop, self.dop_period_8_expected)

    def test_dop_period_10(self):
        period = 10
        dop = detrended_price_oscillator.detrended_price_oscillator(self.data, period)
        np.testing.assert_array_equal(dop, self.dop_period_10_expected)

    def test_dop_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            detrended_price_oscillator.detrended_price_oscillator(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
