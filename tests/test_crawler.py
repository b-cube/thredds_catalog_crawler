import unittest

from thredds_crawler.crawl import Crawl


class CrawlerTest(unittest.TestCase):
    def test_root_finder(self):
        urls = [
            ('http://data.eol.ucar.edu/jedi/catalog/ucar.ncar.eol.dataset.106_224.thredds.xml',
                 'http://data.eol.ucar.edu/jedi/catalog/ucar.ncar.eol.thredds.xml', False),
            ('http://www.esrl.noaa.gov/psd/thredds/catalog/Datasets/noaa.oisst.v2.derived/catalog.xml',
                 'http://www.esrl.noaa.gov/psd/thredds/catalog.xml', True),
            ('https://rsg.pml.ac.uk/thredds/catalog/cnr/3b42-3h/1998/01/01/catalog.xml',
                 'https://rsg.pml.ac.uk/thredds/catalog.xml', True)
        ]

        for url, expected, output in urls:
            crawler = Crawl(url)
            found_url = crawler._find_root_url()

            assert (found_url == expected) == output


    # def test_single_dataset(self):
    #     c = Crawl("http://tds.maracoos.org/thredds/MODIS.xml", select=["MODIS-Agg"])
    #     assert len(c.datasets) == 1
    #     assert c.datasets[0].id == "MODIS-Agg"
    #     assert len(c.datasets[0].services) == 2
    #     service_names = sorted(map(lambda x: x.get('service'), c.datasets[0].services))
    #     assert service_names == ["ISO", "OPENDAP"]

    # def test_two_datasets(self):
    #     c = Crawl("http://tds.maracoos.org/thredds/MODIS.xml", select=["MODIS-Agg", "MODIS-2012-Agg"])
    #     assert len(c.datasets) == 2

    # def test_regex_selects(self):
    #     c = Crawl("http://tds.maracoos.org/thredds/MODIS.xml", select=[".*-Agg"])
    #     assert len(c.datasets) == 9

    #     # Get all DAP links:
    #     services = [s.get("url") for d in c.datasets for s in d.services if s.get("service").lower() == "opendap"]
    #     assert len(services) == 9

    # def test_regex_skips(self):
    #     # skip everything
    #     c = Crawl("http://tds.maracoos.org/thredds/MODIS.xml", skip=[".*"])
    #     assert len(c.datasets) == 0

    # def test_iso_links(self):
    #     c = Crawl("http://thredds.axiomalaska.com/thredds/catalogs/global.html", debug=True)
    #     isos = [s.get("url") for d in c.datasets for s in d.services if s.get("service").lower() == "iso"]
    #     assert "?dataset=" in isos[0]
    #     assert "&catalog=" in isos[0]

    # def test_dataset_size_using_xml(self):
    #     c = Crawl("http://tds.maracoos.org/thredds/catalog/MODIS/2014/catalog.xml", debug=True)
    #     assert c.datasets[0].size == 77.56

    # def test_dataset_size_using_dap(self):
    #     c = Crawl("http://tds.maracoos.org/thredds/MODIS.xml", select=["MODIS-One-Agg"], debug=True)
    #     assert c.datasets[0].size == 14678820.092728
