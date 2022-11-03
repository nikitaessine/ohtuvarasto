import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)



    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
        

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_addataa_negatiivinen(self):
        
       varasto = Varasto(-56565)

       self.assertAlmostEqual(varasto.tilavuus,0)

    def test_negatiivinen_ottaminen(self):
        saatu_maara = self.varasto.ota_varastosta(-56)

        self.assertAlmostEqual(saatu_maara,0.0)
    
    def test_lisataan_enemma_ku_mahtuu(self):

        self.varasto.lisaa_varastoon(15)
        
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)
    
    def test_tulostaa_oikein(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
    
    def test_alku_saldo(self):
        varasto = Varasto(10,-3.5)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)
    
    def test_alku_otetaan_liikaa(self):
        self.varasto.lisaa_varastoon(5)

        self.assertAlmostEqual(self.varasto.ota_varastosta(8),5)
    
    def test_negatiivisen_lisaaminen(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0.0)