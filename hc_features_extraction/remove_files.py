import os

#directory = r"E:\Coding\Jupyter_files\ECG_2\Data_saves\Final_data"
directory = r'E:\Coding\Jupyter_files\ECG_2\Data_saves\Selected_data'


files_to_remove = [
'A1002.mat',
'A3927.mat',
'A5438.mat',
'A5897.mat',
'A5904.mat',
'HR03584.mat',
'HR09295.mat',
'HR10446.mat',
'HR13378.mat',
'HR13429.mat',
'HR15164.mat',
'HR15632.mat',
'HR16273.mat',
'HR16711.mat',
'HR17091.mat',
'HR17626.mat',
'HR18827.mat',
'HR19054.mat',
'HR19140.mat',
'Q0400.mat',
'Q2961.mat',


'A0009.mat',
'A0017.mat',
'A0121.mat',
'A0145.mat',
'A0180.mat',
'A0184.mat',
'A0215.mat',
'A0260.mat',
'A0272.mat',
'A0274.mat',
'A0294.mat',
'A0298.mat',
'A0308.mat',
'A0314.mat',
'A0317.mat',
'A0374.mat',
'A0406.mat',
'A0421.mat',
'A0451.mat',
'A0456.mat',
'A0525.mat',
'A0537.mat',
'A0545.mat',
'A0551.mat',
'A0607.mat',
'A0646.mat',
'A0649.mat',
'A0658.mat',
'A0674.mat',
'A0689.mat',
'A0706.mat',
'A0719.mat',
'A0737.mat',
'A0747.mat',
'A0769.mat',
'A0773.mat',
'A0796.mat',
'A0799.mat',
'A0835.mat',
'A0840.mat',
'A0857.mat',
'A0862.mat',
'A0884.mat',
'A0886.mat',
'A0890.mat',
'A0907.mat',
'A0931.mat',
'A0963.mat',
'A1010.mat',
'A1041.mat',
'A1053.mat',
'A1061.mat',
'A1098.mat',
'A1180.mat',
'A1183.mat',
'A1196.mat',
'A1232.mat',
'A1266.mat',
'A1299.mat',
'A1318.mat',
'A1324.mat',
'A1329.mat',
'A1366.mat',
'A1392.mat',
'A1432.mat',
'A1461.mat',
'A1462.mat',
'A1468.mat',
'A1485.mat',
'A1504.mat',
'A1528.mat',
'A1602.mat',
'A1605.mat',
'A1606.mat',
'A1612.mat',
'A1620.mat',
'A1635.mat',
'A1661.mat',
'A1670.mat',
'A1683.mat',
'A1686.mat',
'A1725.mat',
'A1762.mat',
'A1772.mat',
'A1780.mat',
'A1781.mat',
'A1789.mat',
'A1841.mat',
'A1852.mat',
'A1867.mat',
'A1927.mat',
'A1948.mat',
'A1953.mat',
'A1973.mat',
'A2000.mat',
'A2011.mat',
'A2027.mat',
'A2085.mat',
'A2093.mat',
'A2113.mat',
'A2115.mat',
'A2154.mat',
'A2159.mat',
'A2170.mat',
'A2176.mat',
'A2193.mat',
'A2244.mat',
'A2272.mat',
'A2274.mat',
'A2286.mat',
'A2300.mat',
'A2336.mat',
'A2368.mat',
'A2375.mat',
'A2385.mat',
'A2448.mat',
'A2459.mat',
'A2529.mat',
'A2539.mat',
'A2563.mat',
'A2573.mat',
'A2595.mat',
'A2607.mat',
'A2612.mat',
'A2613.mat',
'A2626.mat',
'A2642.mat',
'A2647.mat',
'A2653.mat',
'A2659.mat',
'A2682.mat',
'A2699.mat',
'A2749.mat',
'A2750.mat',
'A2753.mat',
'A2757.mat',
'A2772.mat',
'A2800.mat',
'A2821.mat',
'A2845.mat',
'A2959.mat',
'A2975.mat',
'A2977.mat',
'A3001.mat',
'A3039.mat',
'A3048.mat',
'A3079.mat',
'A3094.mat',
'A3112.mat',
'A3131.mat',
'A3140.mat',
'A3148.mat',
'A3158.mat',
'A3171.mat',
'A3230.mat',
'A3254.mat',
'A3277.mat',
'A3294.mat',
'A3308.mat',
'A3372.mat',
'A3398.mat',
'A3401.mat',
'A3402.mat',
'A3428.mat',
'A3456.mat',
'A3460.mat',
'A3510.mat',
'A3543.mat',
'A3545.mat',
'A3559.mat',
'A3570.mat',
'A3597.mat',
'A3622.mat',
'A3627.mat',
'A3641.mat',
'A3659.mat',
'A3669.mat',
'A3677.mat',
'A3679.mat',
'A3719.mat',
'A3734.mat',
'A3764.mat',
'A3773.mat',
'A3798.mat',
'A3812.mat',
'A3837.mat',
'A3876.mat',
'A3881.mat',
'A3887.mat',
'A3916.mat',
'A3969.mat',
'A3985.mat',
'A4004.mat',
'A4012.mat',
'A4058.mat',
'A4073.mat',
'A4080.mat',
'A4106.mat',
'A4112.mat',
'A4160.mat',
'A4171.mat',
'A4178.mat',
'A4226.mat',
'A4254.mat',
'A4281.mat',
'A4301.mat',
'A4344.mat',
'A4347.mat',
'A4353.mat',
'A4361.mat',
'A4365.mat',
'A4367.mat',
'A4431.mat',
'A4458.mat',
'A4461.mat',
'A4471.mat',
'A4496.mat',
'A4510.mat',
'A4515.mat',
'A4531.mat',
'A4537.mat',
'A4559.mat',
'A4574.mat',
'A4584.mat',
'A4587.mat',
'A4594.mat',
'A4632.mat',
'A4636.mat',
'A4642.mat',
'A4685.mat',
'A4696.mat',
'A4706.mat',
'A4709.mat',
'A4713.mat',
'A4720.mat',
'A4727.mat',
'A4753.mat',
'A4760.mat',
'A4788.mat',
'A4817.mat',
'A4836.mat',
'A4838.mat',
'A4889.mat',
'A4928.mat',
'A4953.mat',
'A4981.mat',
'A4990.mat',
'A4992.mat',
'A4996.mat',
'A5000.mat',
'A5008.mat',
'A5020.mat',
'A5078.mat',
'A5085.mat',
'A5093.mat',
'A5098.mat',
'A5101.mat',
'A5129.mat',
'A5148.mat',
'A5208.mat',
'A5220.mat',
'A5273.mat',
'A5275.mat',
'A5325.mat',
'A5329.mat',
'A5333.mat',
'A5382.mat',
'A5404.mat',
'A5416.mat',
'A5421.mat',
'A5423.mat',
'A5521.mat',
'A5531.mat',
'A5534.mat',
'A5538.mat',
'A5557.mat',
'A5559.mat',
'A5570.mat',
'A5571.mat',
'A5595.mat',
'A5613.mat',
'A5627.mat',
'A5648.mat',
'A5674.mat',
'A5692.mat',
'A5699.mat',
'A5718.mat',
'A5820.mat',
'A5834.mat',
'A5915.mat',
'A5967.mat',
'A5978.mat',
'A5989.mat',
'A6022.mat',
'A6043.mat',
'A6092.mat',
'A6176.mat',
'A6185.mat',
'A6186.mat',
'A6194.mat',
'A6236.mat',
'A6243.mat',
'A6244.mat',
'A6245.mat',
'A6250.mat',
'A6282.mat',
'A6290.mat',
'A6292.mat',
'A6294.mat',
'A6296.mat',
'A6300.mat',
'A6335.mat',
'A6352.mat',
'A6368.mat',
'A6369.mat',
'A6372.mat',
'A6422.mat',
'A6428.mat',
'A6444.mat',
'A6450.mat',
'A6469.mat',
'A6485.mat',
'A6503.mat',
'A6544.mat',
'A6551.mat',
'A6567.mat',
'A6626.mat',
'A6629.mat',
'A6649.mat',
'A6662.mat',
'A6685.mat',
'A6710.mat',
'A6721.mat',
'A6733.mat',
'A6738.mat',
'A6755.mat',
'A6768.mat',
'A6781.mat',
'A6790.mat',
'A6803.mat',
'A6807.mat',
'A6815.mat',
'A6862.mat',
'A6872.mat',
'E00028.mat',
'E00053.mat',
'E00054.mat',
'E00083.mat',
'E00152.mat',
'E00263.mat',
'E00344.mat',
'E00381.mat',
'E00426.mat',
'E00474.mat',
'E00482.mat',
'E00581.mat',
'E00591.mat',
'E00593.mat',
'E00682.mat',
'E00688.mat',
'E00712.mat',
'E00762.mat',
'E01044.mat',
'E01084.mat',
'E01140.mat',
'E01190.mat',
'E01216.mat',
'E01246.mat',
'E01261.mat',
'E01262.mat',
'E01288.mat',
'E01388.mat',
'E01409.mat',
'E01430.mat',
'E01438.mat',
'E01475.mat',
'E01477.mat',
'E01502.mat',
'E01509.mat',
'E01525.mat',
'E01624.mat',
'E01662.mat',
'E01757.mat',
'E01803.mat',
'E01875.mat',
'E01908.mat',
'E02074.mat',
'E02158.mat',
'E02170.mat',
'E02184.mat',
'E02210.mat',
'E02211.mat',
'E02305.mat',
'E02315.mat',
'E02317.mat',
'E02424.mat',
'E02457.mat',
'E02523.mat',
'E02534.mat',
'E02551.mat',
'E02629.mat',
'E02637.mat',
'E02640.mat',
'E02643.mat',
'E02736.mat',
'E02810.mat',
'E02860.mat',
'E02863.mat',
'E02879.mat',
'E03035.mat',
'E03073.mat',
'E03076.mat',
'E03086.mat',
'E03111.mat',
'E03145.mat',
'E03148.mat',
'E03155.mat',
'E03158.mat',
'E03195.mat',
'E03208.mat',
'E03279.mat',
'E03312.mat',
'E03328.mat',
'E03376.mat',
'E03418.mat',
'E03438.mat',
'E03449.mat',
'E03473.mat',
'E03492.mat',
'E03532.mat',
'E03544.mat',
'E03575.mat',
'E03576.mat',
'E03658.mat',
'E03706.mat',
'E03794.mat',
'E03810.mat',
'E03815.mat',
'E03816.mat',
'E03854.mat',
'E03857.mat',
'E03924.mat',
'E03935.mat',
'E03985.mat',
'E03990.mat',
'E04020.mat',
'E04035.mat',
'E04084.mat',
'E04133.mat',
'E04146.mat',
'E04153.mat',
'E04156.mat',
'E04198.mat',
'E04299.mat',
'E04305.mat',
'E04416.mat',
'E04444.mat',
'E04481.mat',
'E04503.mat',
'E04507.mat',
'E04523.mat',
'E04539.mat',
'E04601.mat',
'E04621.mat',
'E04630.mat',
'E04632.mat',
'E04697.mat',
'E04703.mat',
'E04729.mat',
'E04749.mat',
'E04791.mat',
'E04799.mat',
'E04943.mat',
'E04947.mat',
'E04962.mat',
'E05021.mat',
'E05044.mat',
'E05086.mat',
'E05095.mat',
'E05158.mat',
'E05165.mat',
'E05210.mat',
'E05305.mat',
'E05306.mat',
'E05331.mat',
'E05352.mat',
'E05383.mat',
'E05431.mat',
'E05440.mat',
'E05497.mat',
'E05524.mat',
'E05558.mat',
'E05591.mat',
'E05592.mat',
'E05626.mat',
'E05630.mat',
'E05708.mat',
'E05743.mat',
'E05764.mat',
'E05902.mat',
'E05924.mat',
'E05957.mat',
'E05999.mat',
'E06005.mat',
'E06019.mat',
'E06032.mat',
'E06056.mat',
'E06181.mat',
'E06291.mat',
'E06295.mat',
'E06324.mat',
'E06354.mat',
'E06459.mat',
'E06682.mat',
'E06697.mat',
'E06771.mat',
'E06802.mat',
'E06803.mat',
'E06819.mat',
'E06823.mat',
'E06858.mat',
'E06875.mat',
'E06955.mat',
'E06993.mat',
'E07035.mat',
'E07063.mat',
'E07068.mat',
'E07089.mat',
'E07093.mat',
'E07131.mat',
'E07193.mat',
'E07204.mat',
'E07248.mat',
'E07336.mat',
'E07367.mat',
'E07493.mat',
'E07509.mat',
'E07510.mat',
'E07549.mat',
'E07567.mat',
'E07595.mat',
'E07620.mat',
'E07651.mat',
'E07671.mat',
'E07698.mat',
'E07767.mat',
'E07903.mat',
'E07968.mat',
'E07982.mat',
'E08009.mat',
'E08173.mat',
'E08175.mat',
'E08219.mat',
'E08314.mat',
'E08436.mat',
'E08488.mat',
'E08500.mat',
'E08560.mat',
'E08562.mat',
'E08597.mat',
'E08599.mat',
'E08611.mat',
'E08694.mat',
'E08786.mat',
'E08815.mat',
'E08946.mat',
'E08989.mat',
'E08994.mat',
'E09055.mat',
'E09063.mat',
'E09065.mat',
'E09099.mat',
'E09179.mat',
'E09191.mat',
'E09303.mat',
'E09344.mat',
'E09353.mat',
'E09377.mat',
'E09413.mat',
'E09421.mat',
'E09441.mat',
'E09476.mat',
'E09481.mat',
'E09490.mat',
'E09491.mat',
'E09569.mat',
'E09629.mat',
'E09657.mat',
'E09675.mat',
'E09704.mat',
'E09753.mat',
'E09793.mat',
'E09920.mat',
'E09943.mat',
'E10105.mat',
'E10141.mat',
'E10161.mat',
'E10199.mat',
'E10233.mat',
'E10251.mat',
'E10257.mat',
'E10278.mat',
'E10295.mat',
'E10299.mat',
'E10309.mat',
'E10330.mat',
'HR00145.mat',
'HR00150.mat',
'HR00196.mat',
'HR00240.mat',
'HR00244.mat',
'HR00258.mat',
'HR00284.mat',
'HR00307.mat',
'HR00322.mat',
'HR00337.mat',
'HR00372.mat',
'HR00383.mat',
'HR00445.mat',
'HR00452.mat',
'HR00461.mat',
'HR00463.mat',
'HR00500.mat',
'HR00510.mat',
'HR00512.mat',
'HR00544.mat',
'HR00547.mat',
'HR00567.mat',
'HR00579.mat',
'HR00581.mat',
'HR00624.mat',
'HR00702.mat',
'HR00704.mat',
'HR00722.mat',
'HR00751.mat',
'HR00765.mat',
'HR00771.mat',
'HR00825.mat',
'HR00828.mat',
'HR00835.mat',
'HR00846.mat',
'HR00963.mat',
'HR00966.mat',
'HR01006.mat',
'HR01065.mat',
'HR01075.mat',
'HR01077.mat',
'HR01134.mat',
'HR01157.mat',
'HR01186.mat',
'HR01200.mat',
'HR01202.mat',
'HR01203.mat',
'HR01216.mat',
'HR01294.mat',
'HR01337.mat',
'HR01345.mat',
'HR01379.mat',
'HR01433.mat',
'HR01439.mat',
'HR01456.mat',
'HR01524.mat',
'HR01578.mat',
'HR01658.mat',
'HR01798.mat',
'HR01799.mat',
'HR01805.mat',
'HR01810.mat',
'HR01815.mat',
'HR01889.mat',
'HR01914.mat',
'HR01930.mat',
'HR01941.mat',
'HR01948.mat',
'HR01956.mat',
'HR01965.mat',
'HR02029.mat',
'HR02062.mat',
'HR02073.mat',
'HR02132.mat',
'HR02200.mat',
'HR02219.mat',
'HR02244.mat',
'HR02263.mat',
'HR02267.mat',
'HR02292.mat',
'HR02304.mat',
'HR02314.mat',
'HR02317.mat',
'HR02359.mat',
'HR02382.mat',
'HR02433.mat',
'HR02446.mat',
'HR02463.mat',
'HR02525.mat',
'HR02527.mat',
'HR02557.mat',
'HR02560.mat',
'HR02580.mat',
'HR02600.mat',
'HR02601.mat',
'HR02609.mat',
'HR02657.mat',
'HR02699.mat',
'HR02722.mat',
'HR02735.mat',
'HR02817.mat',
'HR02823.mat',
'HR02916.mat',
'HR02964.mat',
'HR03057.mat',
'HR03060.mat',
'HR03087.mat',
'HR03103.mat',
'HR03109.mat',
'HR03111.mat',
'HR03214.mat',
'HR03223.mat',
'HR03238.mat',
'HR03290.mat',
'HR03312.mat',
'HR03423.mat',
'HR03429.mat',
'HR03431.mat',
'HR03433.mat',
'HR03484.mat',
'HR03528.mat',
'HR03659.mat',
'HR03675.mat',
'HR03748.mat',
'HR03764.mat',
'HR03772.mat',
'HR03800.mat',
'HR03801.mat',
'HR03802.mat',
'HR03805.mat',
'HR03834.mat',
'HR03835.mat',
'HR03867.mat',
'HR03869.mat',
'HR03883.mat',
'HR03905.mat',
'HR03923.mat',
'HR03984.mat',
'HR03994.mat',
'HR04102.mat',
'HR04106.mat',
'HR04114.mat',
'HR04117.mat',
'HR04137.mat',
'HR04154.mat',
'HR04177.mat',
'HR04310.mat',
'HR04333.mat',
'HR04412.mat',
'HR04438.mat',
'HR04442.mat',
'HR04461.mat',
'HR04467.mat',
'HR04495.mat',
'HR04502.mat',
'HR04604.mat',
'HR04616.mat',
'HR04632.mat',
'HR04653.mat',
'HR04654.mat',
'HR04659.mat',
'HR04660.mat',
'HR04700.mat',
'HR04712.mat',
'HR04749.mat',
'HR04823.mat',
'HR04824.mat',
'HR04827.mat',
'HR04830.mat',
'HR04838.mat',
'HR04878.mat',
'HR04920.mat',
'HR04939.mat',
'HR04981.mat',
'HR05022.mat',
'HR05077.mat',
'HR05168.mat',
'HR05188.mat',
'HR05242.mat',
'HR05258.mat',
'HR05293.mat',
'HR05419.mat',
'HR05466.mat',
'HR05481.mat',
'HR05528.mat',
'HR05594.mat',
'HR05603.mat',
'HR05616.mat',
'HR05631.mat',
'HR05670.mat',
'HR05724.mat',
'HR05761.mat',
'HR05767.mat',
'HR05814.mat',
'HR05827.mat',
'HR05842.mat',
'HR05852.mat',
'HR05859.mat',
'HR05875.mat',
'HR05878.mat',
'HR05879.mat',
'HR05885.mat',
'HR05887.mat',
'HR05903.mat',
'HR05906.mat',
'HR05939.mat',
'HR06048.mat',
'HR06064.mat',
'HR06065.mat',
'HR06151.mat',
'HR06160.mat',
'HR06167.mat',
'HR06214.mat',
'HR06352.mat',
'HR06460.mat',
'HR06663.mat',
'HR06693.mat',
'HR06704.mat',
'HR06718.mat',
'HR06817.mat',
'HR06892.mat',
'HR06908.mat',
'HR06931.mat',
'HR06934.mat',
'HR06945.mat',
'HR06956.mat',
'HR07018.mat',
'HR07020.mat',
'HR07035.mat',
'HR07055.mat',
'HR07057.mat',
'HR07068.mat',
'HR07102.mat',
'HR07105.mat',
'HR07118.mat',
'HR07145.mat',
'HR07149.mat',
'HR07194.mat',
'HR07218.mat',
'HR07336.mat',
'HR07358.mat',
'HR07387.mat',
'HR07406.mat',
'HR07427.mat',
'HR07489.mat',
'HR07491.mat',
'HR07556.mat',
'HR07588.mat',
'HR07590.mat',
'HR07658.mat',
'HR07665.mat',
'HR07685.mat',
'HR07688.mat',
'HR07690.mat',
'HR07742.mat',
'HR07751.mat',
'HR07806.mat',
'HR07822.mat',
'HR07847.mat',
'HR07903.mat',
'HR07977.mat',
'HR08021.mat',
'HR08031.mat',
'HR08044.mat',
'HR08092.mat',
'HR08139.mat',
'HR08230.mat',
'HR08276.mat',
'HR08329.mat',
'HR08354.mat',
'HR08368.mat',
'HR08372.mat',
'HR08392.mat',
'HR08408.mat',
'HR08452.mat',
'HR08455.mat',
'HR08475.mat',
'HR08547.mat',
'HR08562.mat',
'HR08602.mat',
'HR08605.mat',
'HR08653.mat',
'HR08687.mat',
'HR08720.mat',
'HR08721.mat',
'HR08726.mat',
'HR08793.mat',
'HR08811.mat',
'HR08830.mat',
'HR08861.mat',
'HR08909.mat',
'HR08913.mat',
'HR08937.mat',
'HR08973.mat',
'HR09010.mat',
'HR09016.mat',
'HR09068.mat',
'HR09098.mat',
'HR09100.mat',
'HR09118.mat',
'HR09123.mat',
'HR09145.mat',
'HR09211.mat',
'HR09223.mat',
'HR09234.mat',
'HR09253.mat',
'HR09283.mat',
'HR09316.mat',
'HR09322.mat',
'HR09327.mat',
'HR09371.mat',
'HR09395.mat',
'HR09424.mat',
'HR09425.mat',
'HR09467.mat',
'HR09485.mat',
'HR09530.mat',
'HR09536.mat',
'HR09561.mat',
'HR09564.mat',
'HR09578.mat',
'HR09592.mat',
'HR09594.mat',
'HR09630.mat',
'HR09713.mat',
'HR09728.mat',
'HR09769.mat',
'HR09770.mat',
'HR09823.mat',
'HR09836.mat',
'HR09846.mat',
'HR09857.mat',
'HR09861.mat',
'HR09987.mat',
'HR09988.mat',
'HR10051.mat',
'HR10053.mat',
'HR10059.mat',
'HR10063.mat',
'HR10115.mat',
'HR10135.mat',
'HR10154.mat',
'HR10201.mat',
'HR10227.mat',
'HR10233.mat',
'HR10284.mat',
'HR10304.mat',
'HR10322.mat',
'HR10328.mat',
'HR10344.mat',
'HR10357.mat',
'HR10399.mat',
'HR10463.mat',
'HR10477.mat',
'HR10491.mat',
'HR10657.mat',
'HR10704.mat',
'HR10721.mat',
'HR10723.mat',
'HR10725.mat',
'HR10779.mat',
'HR10802.mat',
'HR10850.mat',
'HR10871.mat',
'HR10926.mat',
'HR10927.mat',
'HR10929.mat',
'HR10932.mat',
'HR10976.mat',
'HR10991.mat',
'HR11031.mat',
'HR11033.mat',
'HR11084.mat',
'HR11090.mat',
'HR11106.mat',
'HR11110.mat',
'HR11161.mat',
'HR11244.mat',
'HR11259.mat',
'HR11269.mat',
'HR11288.mat',
'HR11320.mat',
'HR11330.mat',
'HR11342.mat',
'HR11358.mat',
'HR11488.mat',
'HR11490.mat',
'HR11493.mat',
'HR11547.mat',
'HR11691.mat',
'HR11704.mat',
'HR11805.mat',
'HR11844.mat',
'HR11877.mat',
'HR11889.mat',
'HR11970.mat',
'HR11997.mat',
'HR12048.mat',
'HR12062.mat',
'HR12263.mat',
'HR12299.mat',
'HR12318.mat',
'HR12324.mat',
'HR12334.mat',
'HR12348.mat',
'HR12374.mat',
'HR12384.mat',
'HR12421.mat',
'HR12436.mat',
'HR12453.mat',
'HR12507.mat',
'HR12526.mat',
'HR12626.mat',
'HR12634.mat',
'HR12646.mat',
'HR12725.mat',
'HR12780.mat',
'HR12791.mat',
'HR12843.mat',
'HR12871.mat',
'HR12878.mat',
'HR12892.mat',
'HR12908.mat',
'HR12911.mat',
'HR12961.mat',
'HR12963.mat',
'HR12988.mat',
'HR12989.mat',
'HR12993.mat',
'HR12994.mat',
'HR12998.mat',
'HR13019.mat',
'HR13079.mat',
'HR13080.mat',
'HR13116.mat',
'HR13168.mat',
'HR13261.mat',
'HR13298.mat',
'HR13309.mat',
'HR13362.mat',
'HR13389.mat',
'HR13458.mat',
'HR13520.mat',
'HR13556.mat',
'HR13584.mat',
'HR13694.mat',
'HR13747.mat',
'HR13787.mat',
'HR13823.mat',
'HR13875.mat',
'HR13885.mat',
'HR13903.mat',
'HR13949.mat',
'HR14002.mat',
'HR14019.mat',
'HR14026.mat',
'HR14087.mat',
'HR14216.mat',
'HR14289.mat',
'HR14334.mat',
'HR14343.mat',
'HR14361.mat',
'HR14369.mat',
'HR14380.mat',
'HR14389.mat',
'HR14412.mat',
'HR14527.mat',
'HR14601.mat',
'HR14610.mat',
'HR14612.mat',
'HR14653.mat',
'HR14706.mat',
'HR14752.mat',
'HR14783.mat',
'HR14798.mat',
'HR14804.mat',
'HR14848.mat',
'HR14872.mat',
'HR14887.mat',
'HR14924.mat',
'HR14936.mat',
'HR14959.mat',
'HR14983.mat',
'HR15089.mat',
'HR15125.mat',
'HR15167.mat',
'HR15199.mat',
'HR15254.mat',
'HR15283.mat',
'HR15341.mat',
'HR15398.mat',
'HR15416.mat',
'HR15433.mat',
'HR15448.mat',
'HR15483.mat',
'HR15509.mat',
'HR15529.mat',
'HR15535.mat',
'HR15659.mat',
'HR15745.mat',
'HR15756.mat',
'HR15771.mat',
'HR15774.mat',
'HR15784.mat',
'HR15806.mat',
'HR15807.mat',
'HR15809.mat',
'HR15814.mat',
'HR15825.mat',
'HR15853.mat',
'HR15854.mat',
'HR15899.mat',
'HR15935.mat',
'HR15949.mat',
'HR15973.mat',
'HR15985.mat',
'HR16016.mat',
'HR16061.mat',
'HR16073.mat',
'HR16079.mat',
'HR16138.mat',
'HR16168.mat',
'HR16171.mat',
'HR16176.mat',
'HR16235.mat',
'HR16259.mat',
'HR16268.mat',
'HR16381.mat',
'HR16403.mat',
'HR16404.mat',
'HR16414.mat',
'HR16423.mat',
'HR16470.mat',
'HR16481.mat',
'HR16487.mat',
'HR16490.mat',
'HR16497.mat',
'HR16591.mat',
'HR16606.mat',
'HR16616.mat',
'HR16641.mat',
'HR16677.mat',
'HR16713.mat',
'HR16731.mat',
'HR16758.mat',
'HR16762.mat',
'HR16797.mat',
'HR16818.mat',
'HR16838.mat',
'HR16843.mat',
'HR16845.mat',
'HR16851.mat',
'HR16852.mat',
'HR16891.mat',
'HR16926.mat',
'HR16940.mat',
'HR16945.mat',
'HR16949.mat',
'HR16959.mat',
'HR16972.mat',
'HR16983.mat',
'HR16990.mat',
'HR16999.mat',
'HR17009.mat',
'HR17034.mat',
'HR17035.mat',
'HR17050.mat',
'HR17073.mat',
'HR17076.mat',
'HR17095.mat',
'HR17103.mat',
'HR17104.mat',
'HR17154.mat',
'HR17164.mat',
'HR17190.mat',
'HR17237.mat',
'HR17288.mat',
'HR17302.mat',
'HR17312.mat',
'HR17354.mat',
'HR17360.mat',
'HR17365.mat',
'HR17367.mat',
'HR17383.mat',
'HR17387.mat',
'HR17456.mat',
'HR17515.mat',
'HR17595.mat',
'HR17657.mat',
'HR17696.mat',
'HR17716.mat',
'HR17721.mat',
'HR17809.mat',
'HR17817.mat',
'HR17852.mat',
'HR17855.mat',
'HR17862.mat',
'HR17866.mat',
'HR17867.mat',
'HR17891.mat',
'HR17903.mat',
'HR17914.mat',
'HR17924.mat',
'HR18012.mat',
'HR18099.mat',
'HR18110.mat',
'HR18128.mat',
'HR18211.mat',
'HR18230.mat',
'HR18301.mat',
'HR18343.mat',
'HR18469.mat',
'HR18478.mat',
'HR18489.mat',
'HR18528.mat',
'HR18547.mat',
'HR18596.mat',
'HR18602.mat',
'HR18653.mat',
'HR18690.mat',
'HR18696.mat',
'HR18734.mat',
'HR18798.mat',
'HR18803.mat',
'HR18812.mat',
'HR18838.mat',
'HR18876.mat',
'HR18882.mat',
'HR18886.mat',
'HR18925.mat',
'HR18945.mat',
'HR18960.mat',
'HR18996.mat',
'HR19043.mat',
'HR19051.mat',
'HR19101.mat',
'HR19187.mat',
'HR19188.mat',
'HR19300.mat',
'HR19303.mat',
'HR19327.mat',
'HR19351.mat',
'HR19356.mat',
'HR19394.mat',
'HR19485.mat',
'HR19504.mat',
'HR19511.mat',
'HR19519.mat',
'HR19528.mat',
'HR19544.mat',
'HR19589.mat',
'HR19606.mat',
'HR19628.mat',
'HR19715.mat',
'HR19721.mat',
'HR19736.mat',
'HR19743.mat',
'HR19750.mat',
'HR19793.mat',
'HR19811.mat',
'HR19824.mat',
'HR19837.mat',
'HR19872.mat',
'HR19902.mat',
'HR19904.mat',
'HR19906.mat',
'HR19925.mat',
'HR19935.mat',
'HR19941.mat',
'HR19952.mat',
'HR19966.mat',
'HR19968.mat',
'HR19973.mat',
'HR19997.mat',
'HR19998.mat',
'HR20019.mat',
'HR20073.mat',
'HR20089.mat',
'HR20137.mat',
'HR20142.mat',
'HR20195.mat',
'HR20216.mat',
'HR20233.mat',
'HR20272.mat',
'HR20334.mat',
'HR20354.mat',
'HR20366.mat',
'HR20368.mat',
'HR20375.mat',
'HR20376.mat',
'HR20392.mat',
'HR20395.mat',
'HR20459.mat',
'HR20471.mat',
'HR20483.mat',
'HR20516.mat',
'HR20540.mat',
'HR20575.mat',
'HR20651.mat',
'HR20656.mat',
'HR20683.mat',
'HR20701.mat',
'HR20702.mat',
'HR20711.mat',
'HR20793.mat',
'HR20821.mat',
'HR20832.mat',
'HR20851.mat',
'HR20865.mat',
'HR20874.mat',
'HR20877.mat',
'HR20913.mat',
'HR20966.mat',
'HR21096.mat',
'HR21123.mat',
'HR21130.mat',
'HR21250.mat',
'HR21260.mat',
'HR21275.mat',
'HR21288.mat',
'HR21319.mat',
'HR21371.mat',
'HR21400.mat',
'HR21431.mat',
'HR21461.mat',
'HR21511.mat',
'HR21530.mat',
'HR21533.mat',
'HR21535.mat',
'HR21543.mat',
'HR21553.mat',
'HR21563.mat',
'HR21577.mat',
'HR21601.mat',
'HR21621.mat',
'HR21671.mat',
'HR21675.mat',
'HR21761.mat',
'HR21804.mat',
'Q0090.mat',
'Q0173.mat',
'Q0241.mat',
'Q0315.mat',
'Q0409.mat',
'Q0516.mat',
'Q0543.mat',
'Q0631.mat',
'Q0960.mat',
'Q1022.mat',
'Q1028.mat',
'Q1054.mat',
'Q1073.mat',
'Q1194.mat',
'Q1251.mat',
'Q1268.mat',
'Q1287.mat',
'Q1559.mat',
'Q1568.mat',
'Q1576.mat',
'Q1581.mat',
'Q1712.mat',
'Q1774.mat',
'Q1785.mat',
'Q1926.mat',
'Q1985.mat',
'Q2032.mat',
'Q2064.mat',
'Q2344.mat',
'Q2615.mat',
'Q2661.mat',
'Q2699.mat',
'Q2880.mat',
'Q2970.mat',
'Q3016.mat',
'Q3020.mat',
'Q3055.mat',
'Q3191.mat',
'Q3393.mat',
'Q3422.mat',
'Q3453.mat',
'Q3505.mat',
'S0019.mat',
'S0074.mat',
'S0077.mat',
'S0081.mat',
'S0082.mat',
'S0086.mat',
'S0095.mat',
'S0098.mat',
'S0142.mat',
'S0152.mat',
'S0171.mat',
'S0224.mat',
'S0228.mat',
'S0229.mat',
'S0237.mat',
'S0242.mat',
'S0253.mat',
'S0254.mat',
'S0270.mat',
'S0272.mat',
'S0274.mat',
'S0299.mat',
'S0313.mat',
'S0371.mat',
'S0384.mat',
'S0414.mat',
'S0423.mat',
'S0473.mat',
'S0482.mat',
'S0483.mat',
'S0498.mat',
'S0499.mat',
'S0518.mat',
'S0522.mat',
'S0526.mat',
'S0527.mat',
'S0528.mat',
'S0529.mat',
'S0538.mat',
'S0545.mat',
'S0546.mat'
]

# Add .hea extensions to the same files
files_to_remove += [file.replace('.mat', '.hea') for file in files_to_remove if file.endswith('.mat')]

for root, dirs, files in os.walk(directory):
    for file_name in files:
        if file_name in files_to_remove or file_name[:-4] + '.hea' in files_to_remove:
            file_path = os.path.join(root, file_name)
            try:
                os.remove(file_path)
                print(f"Removed: {file_path}")
            except Exception as e:
                print(f"Error removing {file_path}: {e}")
