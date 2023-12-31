import pytest
from lecture14.pages.page_yt_music_player import PageYTMusicPlayer

media_list = (('Антитіла', 'Люди як кораблі'), ('Океан Ельзи', 'Човен'))
data_names = ['Antityla--Lyudy yak korabli', 'OE--Choven']

class TestYtMusic:

    @pytest.mark.parametrize('band, song', media_list, ids=data_names)
    def test_get_songs_for_band(self, yt_music_page, band, song):
        # band_locator = f'//a[text() = "{band}"]'
        # song_locator = '//ancestor::ytmusic-responsive-list-item-renderer//a[contains(@href, "watch")]'
        # all_songs_locator = f'{band_locator}{song_locator}'
        # elements = yt_music_page.find_elements(By.XPATH, all_songs_locator)
        # song_names = [el.text for el in elements]
        # assert song in song_names

        page = PageYTMusicPlayer(yt_music_page)
        page.any()

