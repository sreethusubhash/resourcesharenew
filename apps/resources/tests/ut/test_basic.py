from django.test import TestCase

# Create your tests here.
#Test Case:#Test<Logic-name> or <Logic-name>Test
class TestBaseCalculation(TestCase):
    #Unit Test
    def test_basic_sum(self):#test_<unit-test-name>
        #Arrange
        x=1
        y=4
        expected_output=5
        
        #Act
        result=x+y
        
        #Assert
        #assert result==expected_output
        self.assertEqual(result, expected_output)
        
        
