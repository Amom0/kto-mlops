import unittest

"""
Count names with more than seven letters
"""
def Compte_prenom_longueur(prenoms: list[str]) -> str:
    nombre_limite_lettres = 7
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > nombre_limite_lettres:
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    return more_than_seven

class TestNamesMethod(unittest.TestCase):
     def test_Compte_prenom_longueur(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = Compte_prenom_longueur(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()