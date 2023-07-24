from selenium.webdriver.common.by import By


class TestYtMusic:

    band = 'Океан Ельзи'
    def test_get_songs_for_band(self, yt_music_page):
        band_locator = f'//a[text() = "{self.band}"]'
        sond_locator = '//ancestor::ytmusic-responsive-list-item-renderer//a[contains(@href, "watch")]'
        all_songs_locator = f'{band_locator}{sond_locator}'
        elements = yt_music_page.find_elements(By.XPATH, all_songs_locator)
        for el in elements:
            print(el.text)
        pass
