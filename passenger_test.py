from passenger import *
l=PassengerRepo([])
def tests():
    def test_add_passenger():
        l.add_passenger("Vlad", "Morosanu", "2309x")
        assert l==[Passenger("Vlad", "Morosanu", "2309x")]
        l.add_passenger("Mishu", "Samurai", "999t")
        assert l==[Passenger("Vlad", "Morosanu", "2309x"),Passenger("Mishu", "Samurai", "999t")]
        try:
            l.add_passenger("Florin", "Salam", "999t")
            assert False
        except:
            assert True
    def test_remove_passenger():
        l.remove_passenger("2309x")
        assert l==[Passenger("Mishu", "Samurai", "999t")]
        try:
            l.remove_passenger("000x")
            assert False
        except:
            assert True
    def test_update_passenger():
        l.update_passenger("Alex", "PLM", "999t")
        assert l==[Passenger("Alex", "PLM", "999t")]






tests()