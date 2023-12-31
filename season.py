import pandas as pd

num = [100, 101, 283, 284, 272, 273, 274, 270, 268, 265, 264,
       281, 261, 256, 252, 251, 253, 249, 246, 237, 231, 233,
       254, 236, 276, 262, 238, 219, 218, 217, 216, 214, 213,
       210, 207, 206, 202, 201, 278, 279, 258, 259, 240, 241,
       220, 222, 211, 212, 287, 267, 250, 230, 215, 280, 260,
       242, 221, 225, 234, 293, 294, 295, 298, 297, 247, 512,
       510, 507, 504, 277, 257, 239, 511, 508, 506, 503, 502,
       501, 500, 300, 321, 320, 319, 318, 317]
season = ['ICON The Moment',
          'ICON',
          'HG',
          'RTN',
          'BWC',
          'WC22',
          'RM',
          'SPL',
          'LN',
          'LOL',
          'FA',
          '23HR',
          '22HR',
          'BTB',
          'CAP',
          'EBS',
          'E21',
          'NTG',
          'UP',
          'MC',
          'VTR',
          'MOG',
          'CHELSEA Ambassador',
          'LIVERPOOL Ambassador',
          '22NG',
          '21NG',
          '20NG',
          '19NG',
          'OTW',
          'COC',
          'HOT',
          'TC',
          'MCT ICON',
          'GR',
          'TT',
          'TB',
          'KOREA',
          'NHD',
          '23TY',
          '23NO',
          '22TY',
          '22NO',
          '21TY',
          '21NO',
          '20TY',
          '20NO',
          '19TY',
          '18TY',
          '23TS',
          '22TS',
          '21TS',
          '20TS',
          '19TS',
          '22C',
          '21C',
          '20C',
          '19C',
          'LH',
          'TKL',
          'K22',
          'K21',
          'K19',
          'K18',
          'MCT',
          '12KH',
          '23KL',
          '22KL',
          '21KL',
          '20KL',
          '22KB',
          '21KB',
          '20KB',
          '22PL',
          '21PL',
          '20A',
          '19S',
          '19A',
          '18S',
          '18A',
          '22',
          '21',
          '20',
          '19',
          '18',
          '17',
          ]
data = { 
        "num" : num,
        "season" : season
        }
df = pd.DataFrame(data)
df.to_csv("season_info.csv")

print(df)
