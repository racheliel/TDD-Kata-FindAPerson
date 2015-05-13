
import unittest
from Crowdmap import Crowdmap

class FindAPersonTests(unittest.TestCase):
    def setUp(self):
        self.crowdmap = Crowdmap(["I met Or A. at Chabad house Bangkok",
                                  "We found Or A. R.I.P at Langtang valley",
                                  "Missing Cowboy"])

    def test_getAllPostsForName(self):
        posts = self.crowdmap.get_all_posts_for("Or")
        self.assertEquals(["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"], posts)
        
    def test_getAllPostForMissingName(self):
        posts = self.crowdmap.get_all_posts_for("Racheli")
        self.assertEquals([], posts)

    def test_existingLocationInformationReturnsTrue(self):
        location_exist = self.crowdmap.is_location_for_name("Or")
        self.assertTrue(location_exist)

    def test_existingLocationInformissingName(self):
        location_exist = self.crowdmap.is_location_for_name("Or")
        self.assertTrue(location_exist)
		
    def test_existingLocationInformissingNameNotExist(self):
        location_exist = self.crowdmap.is_location_for_name("Racheli")
        self.assertFalse(location_exist)
		
    def test_if_there_are_map_inconsistencies(self):
        location_exist = self.crowdmap.if_there_are_map_inconsistencies("Or")
        self.assertFalse(location_exist)		
		
			
		
if __name__ == '__main__':
    unittest.main()