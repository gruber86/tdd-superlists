from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # wejscie  na strone glowna aplikacji
        self.browser.get('http://localhost:8000')

        # tytul 'Listy' w naglowku strony
        self.assertIn('Listy', self.browser.title)
        self.fail('Zakonczenie testu!')
        # "Tytul okna przegladarki: " + browser.title

        # Od razu zostaje zachęcona, aby wpisać rzecz do zrobienia.

# W polu tekstowym wpisała "Kupić pawie pióra" (hobby Edyty # polega na tworzeniu ozdobnych przynęt).

# Po naciśnięciu klawisza Enter strona została uaktualniona i wyświetla # "1: Kupić pawie pióra" jako element listy rzeczy do zrobienia.

# Na stronie nadal znajduje się pole tekstowe zachęcające do podania kolejnego zadania.
# Edyta wpisała "Użyć pawich piór do zrobienia przynęty" (Edyta jest niezwykle skrupulatna).

# Strona została ponownie uaktualniona i teraz wyświetla dwa elementy na liście rzeczy do zrobienia.

# Edyta była ciekawa, czy witryna zapamięta jej listę. Zwróciła uwagę na wygenerowany dla niej # unikatowy adres URL, obok którego znajduje się pewien tekst z wyjaśnieniem


# Przechodzi pod podany adres URL i widzi wyświetloną swoją listę rzeczy do zrobienia. # Usatysfakcjonowana kładzie się spać.

#browser.quit()
if __name__ == '__main__':
    unittest.main(warnings='ignore')
