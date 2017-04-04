import unittest
import numpy as np

from tests.sample_data import SampleData
from py_ti import money_flow


class TestAccumulationDistribution(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.close_data = SampleData().get_sample_close_data()
        self.high_data = SampleData().get_sample_high_data()
        self.low_data = SampleData().get_sample_low_data()
        self.volume = SampleData().get_sample_volume()

        self.mf_expected = [1203861240.8599999, 1553716404.8666668,
        1694259812.96, 2662913259.9299998, 1103809271.55, 2054975406.8199999,
        1252707685.0466664, 1522731247.6133335, 897474013.69333339,
        1079485789.7, 866177879.22666669, 954220671.06666672,
        1090016254.4833333, 1088561820.8399999, 833822262.0, 825998757.75999987,
        829289393.70666659, 781406052.61333323, 973755157.96000004,
        1390664966.8599999, 1057136293.2866668, 784041982.43666673,
        1062708520.3800001, 1089529128.51, 955801301.51666665,
        982531236.06000018, 1146923211.8, 788836827.12, 1053134844.4499999,
        1071889105.8999999, 1010837958.1466668, 1097007225.5999999,
        899531907.94666684, 1004931373.25, 1300262999.5999999, 1088440513.75,
        1240619581.3, 1354530117.7133334, 1758135238.4100001,
        1579976044.0666666, 2773031331.8400002, 3023099141.4633331,
        2828683285.5900002, 1362235555.3733335, 1379509305.4166667,
        2019980276.5133333, 1082089890.5766666, 894367885.18000007,
        846860834.25999987, 1184169350.1166668, 1067126734.6266667,
        1109440058.9599998, 1069389730.9200001, 963469816.14666665,
        1132770199.5866666, 1637795356.4633331, 1085315009.8, 1233339463.23,
        1568715265.0799997, 1393974485.8966668, 847397473.43999994,
        975104887.13333333, 780912741.09333336, 615466230.10000002,
        908691541.62, 1182337603.4133334, 1030839973.4499999,
        1014268044.8266666, 2118621551.8600001, 1444090704.0,
        1448859443.4733334, 1702113981.8666663, 1295547462.3266666,
        1519551983.0699999, 1291809334.3066666, 1604462263.7166667,
        1367822609.2200003, 1348448307.26, 1354954842.8266668,
        2301419413.6266665, 1840989433.813333, 1262096267.8099997,
        2052241573.9733334, 485425652.6566667, 1036961757.5766666,
        1103874442.4733334, 1297856545.8166668, 1432535936.6399999,
        1213620641.7533331, 1427130539.7333331, 2344130494.0299997,
        2939222433.3399997, 2872064994.6299996, 4744647777.8299999,
        2495715536.2333331, 1417667030.7366667, 1605626189.8000002,
        1590079560.7, 1757610781.6000001, 1900954009.5466666,
        1902051350.4000001, 1805887362.3633335, 3513534927.48, 2370363923.0,
        1433884147.8399999, 1512777578.3199999, 1159366702.0800002,
        1278857534.4866664, 1067430292.2333332, 1142958189.8,
        1734217438.9833336, 800257863.29666674, 844187705.69333327,
        1032845968.5299999, 687174370.65333331, 1297206762.5, 1126704258.3,
        856233938.33999991, 809474362.18666673, 885615210.20000005,
        922039906.18000007, 1083024462.9599998, 1191653539.7766666,
        954953607.9466666, 1042492232.1333334, 963866806.58999991,
        1046194449.0533333]

    def test_money_flow(self):
        mf = money_flow.money_flow(self.close_data, self.high_data, self.low_data, self.volume)
        np.testing.assert_array_equal(mf, self.mf_expected)

    def test_money_flow_invalid_data(self):
        self.close_data.append(1)
        with self.assertRaises(Exception) as cm:
            money_flow.money_flow(self.close_data, self.high_data, self.low_data, self.volume)
        expected = ("Error: mismatched data lengths, check to ensure that all input data is the same length and valid")
        self.assertEqual(str(cm.exception), expected)
