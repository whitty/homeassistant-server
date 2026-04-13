"""Test we can parse the dicts returned by helpers into Music Assistant models."""

from unittest.mock import Mock, AsyncMock
import pytest

from music_assistant.providers.ytmusic import YoutubeMusicProvider

from music_assistant_models.enums import (
    AlbumType,
)
from music_assistant_models.media_items import (
    Album,
)


@pytest.fixture
def mass_mock() -> Mock:
    """Return a mock MusicAssistant instance."""
    mass = Mock()
    mass.http_session = AsyncMock()
    mass.metadata.locale = "en_US"
    mass.cache.get = AsyncMock(return_value=None)
    mass.cache.set = AsyncMock()
    mass.cache.delete = AsyncMock()
    return mass


@pytest.fixture
def manifest_mock() -> Mock:
    """Return a mock provider manifest."""
    manifest = Mock()
    manifest.domain = "ytmusic"
    return manifest


@pytest.fixture
def config_mock() -> Mock:
    """Return a mock provider config."""
    config = Mock()
    config.name = "Youtube Music Test"
    config.instance_id = "ytmusic_test"
    config.enabled = True
    config.get_value.side_effect = lambda key: {
        "cookie": "cookie",
        "log_level": "INFO",
    }.get(key, "INFO" if "log" in key else None)
    return config


@pytest.fixture
def provider(
    mass_mock: Mock, manifest_mock: Mock, config_mock: Mock
) -> YoutubeMusicProvider:
    """Return a Provider instance."""
    return YoutubeMusicProvider(mass_mock, manifest_mock, config_mock)


# data from ytm.get_album
library_album_dict = {
    "artists": [{"id": "UCixP1MOaomAQY-9Aozsz2Uw", "name": "Serj Tankian"}],
    "audioPlaylistId": "OLAK5uy_kWEdcjeKDJmb3nsKUciPvYms2jlwHQrzM",
    "description": "Elasticity is the third EP by American metal singer Serj "
    "Tankian, released on 19 March 2021 by Alchemy Recordings and "
    "BMG.\n"
    "\n"
    "From Wikipedia (",
    "duration": "20 minutes",
    "duration_seconds": 1253,
    "isExplicit": False,
    "likeStatus": "INDIFFERENT",
    "other_versions": [
        {
            "artists": [{"id": "UCixP1MOaomAQY-9Aozsz2Uw", "name": "Serj Tankian"}],
            "audioPlaylistId": "OLAK5uy_k3YdCzBqqD3ytHa-JgVo1Q82OYQWUplqk",
            "browseId": "MPREb_temXbe4prc7",
            "isExplicit": True,
            "thumbnails": [
                {
                    "height": 226,
                    "url": "https://lh3.googleusercontent.com/9qyEm8vPDBDVD3o-GY-M_S_D6O_mF0frGTug4QVwdcaVBTITw9MHLoBSk0uqNboK0oMLne5QoKhaMLaj=w226-h226-l90-rj",
                    "width": 226,
                },
                {
                    "height": 544,
                    "url": "https://lh3.googleusercontent.com/9qyEm8vPDBDVD3o-GY-M_S_D6O_mF0frGTug4QVwdcaVBTITw9MHLoBSk0uqNboK0oMLne5QoKhaMLaj=w544-h544-l90-rj",
                    "width": 544,
                },
            ],
            "title": "Elasticity",
            "type": "Single",
        }
    ],
    "related_recommendations": [
        {
            "artists": [{"id": "UCvp1Agf5a75ig9qrzWIfmOg", "name": "GWAR"}],
            "audioPlaylistId": "OLAK5uy_kssyy0AreaNtcW20eUcH0qcHvoHwMPkS0",
            "browseId": "MPREb_tayClqYH9JA",
            "isExplicit": True,
            "thumbnails": [
                {
                    "height": 226,
                    "url": "https://yt3.googleusercontent.com/Cq3L4y6NYDIsjrWVeTPtz_OT7cDSfNi7A8Gqg1X3if4bsUtK-ssFOTkl6WDTNlkqlDwktaQBu5zHBR2y=w226-h226-l90-rj",
                    "width": 226,
                },
                {
                    "height": 544,
                    "url": "https://yt3.googleusercontent.com/Cq3L4y6NYDIsjrWVeTPtz_OT7cDSfNi7A8Gqg1X3if4bsUtK-ssFOTkl6WDTNlkqlDwktaQBu5zHBR2y=w544-h544-l90-rj",
                    "width": 544,
                },
            ],
            "title": "The New Dark Ages",
            "type": "Album",
        },
        {
            "artists": [
                {"id": "UCQkyDVuHnSX1DV_YK2hUZXg", "name": "American Head Charge"}
            ],
            "audioPlaylistId": "OLAK5uy_nYIbWEmaYAwDCCQIENjujg6zphphudID4",
            "browseId": "MPREb_VJBVOpSwiYQ",
            "isExplicit": True,
            "thumbnails": [
                {
                    "height": 226,
                    "url": "https://yt3.googleusercontent.com/oM8aWvBl7L9X8CNX_2tSo2MOe1033d3Tqi7PvsGftwoDVitaEREkuBDxBNKQmksb9wMyeOJWugavDGg=w226-h226-s-l90-rj",
                    "width": 226,
                },
                {
                    "height": 544,
                    "url": "https://yt3.googleusercontent.com/oM8aWvBl7L9X8CNX_2tSo2MOe1033d3Tqi7PvsGftwoDVitaEREkuBDxBNKQmksb9wMyeOJWugavDGg=w544-h544-s-l90-rj",
                    "width": 544,
                },
            ],
            "title": "The War Of Art",
            "type": "Album",
        },
        {
            "artists": [{"id": "UCGexNm_Kw4rdQjLxmpb2EKw", "name": "Metallica"}],
            "audioPlaylistId": "OLAK5uy_lLZbgZsZ40ofzOWIN2c3vqKMlhD3FcTxQ",
            "browseId": "MPREb_6m0nHsUQhPk",
            "isExplicit": True,
            "thumbnails": [
                {
                    "height": 226,
                    "url": "https://lh3.googleusercontent.com/Wk5CVl_OtLfuMptLcgQoktLQp6Dpfasb_lko5LWwU3yCC3_VTSJh5B3ZjRPhyr8owSjgMDJ8TFG_xbI=w226-h226-l90-rj",
                    "width": 226,
                },
                {
                    "height": 544,
                    "url": "https://lh3.googleusercontent.com/Wk5CVl_OtLfuMptLcgQoktLQp6Dpfasb_lko5LWwU3yCC3_VTSJh5B3ZjRPhyr8owSjgMDJ8TFG_xbI=w544-h544-l90-rj",
                    "width": 544,
                },
            ],
            "title": "St. Anger",
            "type": "Album",
        },
        {
            "artists": [{"id": "UC1OKR9fkIEm_QqxJuGCDrJQ", "name": "Marilyn Manson"}],
            "audioPlaylistId": "OLAK5uy_lSrobM1P7b2VjTnrC_7bPfO94zJQGLr9A",
            "browseId": "MPREb_bkeIJMN0Gdu",
            "isExplicit": True,
            "thumbnails": [
                {
                    "height": 226,
                    "url": "https://yt3.googleusercontent.com/67kcQa3ewEWo1-wZn1su4xLo8XXPgP_pgXu_JTID5gDyxEUkwdL1x0zrPWRmOoEfhCeUqeDeygEBwHd6=w226-h226-s-l90-rj",
                    "width": 226,
                },
                {
                    "height": 544,
                    "url": "https://yt3.googleusercontent.com/67kcQa3ewEWo1-wZn1su4xLo8XXPgP_pgXu_JTID5gDyxEUkwdL1x0zrPWRmOoEfhCeUqeDeygEBwHd6=w544-h544-s-l90-rj",
                    "width": 544,
                },
            ],
            "title": "EAT ME, DRINK ME",
            "type": "Album",
        },
        {
            "artists": [
                {"id": "UCCi7NcB61ZJNNUEyfdiG4mQ", "name": "Black Light Burns"}
            ],
            "audioPlaylistId": "OLAK5uy_lkPYXSC1Fp8MaA-GM4Hxc4WCFGpWqL-SI",
            "browseId": "MPREb_nPrm3B8j1OU",
            "isExplicit": True,
            "thumbnails": [
                {
                    "height": 226,
                    "url": "https://yt3.googleusercontent.com/-cyBlLgpk37wtbCZqXlzagYLM3mDyYmAhuNo-ElMpTOtHT3Rd6zbM_0ejc0u3ksQOs8iQCoAGSX2VXu3=w226-h226-l90-rj",
                    "width": 226,
                },
                {
                    "height": 544,
                    "url": "https://yt3.googleusercontent.com/-cyBlLgpk37wtbCZqXlzagYLM3mDyYmAhuNo-ElMpTOtHT3Rd6zbM_0ejc0u3ksQOs8iQCoAGSX2VXu3=w544-h544-l90-rj",
                    "width": 544,
                },
            ],
            "title": "Cruel Melody",
            "type": "Album",
        },
        {
            "artists": [
                {"id": "UCsuErkHQ1ix25ZoBwqGyjHQ", "name": "Metalocalypse: Dethklok"}
            ],
            "audioPlaylistId": "OLAK5uy_mtB7sZQlzkaPgkHr-UJWxWXrueeiIJJbA",
            "browseId": "MPREb_C7ZmFqZAPPR",
            "isExplicit": True,
            "thumbnails": [
                {
                    "height": 226,
                    "url": "https://lh3.googleusercontent.com/Q_TPgNJcQWr9jRKfyQNOy4z7fhAhiwfhYm9D4iHBVf5hcBz08mKg4-xba0mBmX8IxDiNMn3HY_IIaCw6=w226-h226-l90-rj",
                    "width": 226,
                },
                {
                    "height": 544,
                    "url": "https://lh3.googleusercontent.com/Q_TPgNJcQWr9jRKfyQNOy4z7fhAhiwfhYm9D4iHBVf5hcBz08mKg4-xba0mBmX8IxDiNMn3HY_IIaCw6=w544-h544-l90-rj",
                    "width": 544,
                },
            ],
            "title": "The Dethalbum (Expanded Edition)",
            "type": "Album",
        },
        {
            "artists": [{"id": "UCTxnbvh5hLYx9L1Qcy3TCsw", "name": "Helloween"}],
            "audioPlaylistId": "OLAK5uy_mPtliO3hiPCpRhWvWxQfIyE-HqOjD4vRk",
            "browseId": "MPREb_MeqD6lODJSv",
            "isExplicit": False,
            "thumbnails": [
                {
                    "height": 226,
                    "url": "https://yt3.googleusercontent.com/AZ2SsykAfmeblAQfdXhbRby9HXlWqOjFFG9J-G4NCyzYG7qRHT4JqlqnSPz_s1UGwY7WMqU374bhTUkc=w226-h226-l90-rj",
                    "width": 226,
                },
                {
                    "height": 544,
                    "url": "https://yt3.googleusercontent.com/AZ2SsykAfmeblAQfdXhbRby9HXlWqOjFFG9J-G4NCyzYG7qRHT4JqlqnSPz_s1UGwY7WMqU374bhTUkc=w544-h544-l90-rj",
                    "width": 544,
                },
            ],
            "title": "Metal Jukebox",
            "type": "Album",
        },
        {
            "artists": [{"id": "UCIxhwCa4CY-etSc7Y2f8nCg", "name": "Skindred"}],
            "audioPlaylistId": "OLAK5uy_lKPM4oTkUU8vYoGMmXxjL5u7x0T1O3EVk",
            "browseId": "MPREb_RA1KD9cXTpc",
            "isExplicit": False,
            "thumbnails": [
                {
                    "height": 226,
                    "url": "https://lh3.googleusercontent.com/uWaDFW41mPLkkojHYZUpDYdMGlCGH_bSsknQ3v8PoxRXEh8_C-zIo1dnauxyfmWe-vgG0YH3UP-qEEMu=w226-h226-l90-rj",
                    "width": 226,
                },
                {
                    "height": 512,
                    "url": "https://lh3.googleusercontent.com/uWaDFW41mPLkkojHYZUpDYdMGlCGH_bSsknQ3v8PoxRXEh8_C-zIo1dnauxyfmWe-vgG0YH3UP-qEEMu=w512-h512-l90-rj",
                    "width": 512,
                },
            ],
            "title": "Babylon (U.S. Version)",
            "type": "Album",
        },
        {
            "artists": [{"id": "UCP2HiJh3Uus1s4hNza08NRA", "name": "Mushroomhead"}],
            "audioPlaylistId": "OLAK5uy_nc9VtO3rtfb_I8irvt7qAb8wCSH36oIEg",
            "browseId": "MPREb_abHvFcHo7tj",
            "isExplicit": False,
            "thumbnails": [
                {
                    "height": 226,
                    "url": "https://yt3.googleusercontent.com/uU1NfZoUyKZrkRfQW9Q5xprjFYJ3KpTLOmHPhQbIVs1BUwibmOlrQK9kvyaFJ3jH3cbQiIf4EnSm-N-_Jw=w226-h226-l90-rj",
                    "width": 226,
                },
                {
                    "height": 544,
                    "url": "https://yt3.googleusercontent.com/uU1NfZoUyKZrkRfQW9Q5xprjFYJ3KpTLOmHPhQbIVs1BUwibmOlrQK9kvyaFJ3jH3cbQiIf4EnSm-N-_Jw=w544-h544-l90-rj",
                    "width": 544,
                },
            ],
            "title": "Beautiful Stories for Ugly Children",
            "type": "Album",
        },
        {
            "artists": [{"id": "UCGexNm_Kw4rdQjLxmpb2EKw", "name": "Metallica"}],
            "audioPlaylistId": "OLAK5uy_ncBemsUmZKL1xGBRJkY7YsF3oQZx6Rbak",
            "browseId": "MPREb_L51hlbVRrVO",
            "isExplicit": False,
            "thumbnails": [
                {
                    "height": 226,
                    "url": "https://lh3.googleusercontent.com/ub0s9Ke6h42OHCX2ybn5G3gFo0Q7YsBFeW_Mm_bL-OZLL8kkALpmGAo2R_08RL0w58HIhBbQTn5noSlB=w226-h226-l90-rj",
                    "width": 226,
                },
                {
                    "height": 544,
                    "url": "https://lh3.googleusercontent.com/ub0s9Ke6h42OHCX2ybn5G3gFo0Q7YsBFeW_Mm_bL-OZLL8kkALpmGAo2R_08RL0w58HIhBbQTn5noSlB=w544-h544-l90-rj",
                    "width": 544,
                },
            ],
            "title": "Beyond Magnetic",
            "type": "EP",
        },
    ],
    "thumbnails": [
        {
            "height": 60,
            "url": "https://yt3.googleusercontent.com/BDohYZ5B7FfkKZhGTFm_qzZf4DD7W6xpLh6Q80oS_MMuwAvg0uh9IjDKblAfpkxGnYNWeS4Z4mZhvpc_=w60-h60-l90-rj",
            "width": 60,
        },
        {
            "height": 120,
            "url": "https://yt3.googleusercontent.com/BDohYZ5B7FfkKZhGTFm_qzZf4DD7W6xpLh6Q80oS_MMuwAvg0uh9IjDKblAfpkxGnYNWeS4Z4mZhvpc_=w120-h120-l90-rj",
            "width": 120,
        },
        {
            "height": 226,
            "url": "https://yt3.googleusercontent.com/BDohYZ5B7FfkKZhGTFm_qzZf4DD7W6xpLh6Q80oS_MMuwAvg0uh9IjDKblAfpkxGnYNWeS4Z4mZhvpc_=w226-h226-l90-rj",
            "width": 226,
        },
        {
            "height": 544,
            "url": "https://yt3.googleusercontent.com/BDohYZ5B7FfkKZhGTFm_qzZf4DD7W6xpLh6Q80oS_MMuwAvg0uh9IjDKblAfpkxGnYNWeS4Z4mZhvpc_=w544-h544-l90-rj",
            "width": 544,
        },
    ],
    "title": "Elasticity",
    "trackCount": 5,
    "tracks": [
        {
            "album": "Elasticity",
            "artists": [{"id": "UCixP1MOaomAQY-9Aozsz2Uw", "name": "Serj Tankian"}],
            "duration": "4:02",
            "duration_seconds": 242,
            "feedbackTokens": {
                "add": None,
                "remove": "AB9zfpKz9b9vhbeBM_3QtyromGx5o66H_BcQmZmViyx1NEQvRBf_f1xsXEA0j3az-cE4pnXQsJvbbwK1HHAsJZjq4V6n_I-N0A",
            },
            "inLibrary": False,
            "isAvailable": True,
            "isExplicit": False,
            "likeStatus": "INDIFFERENT",
            "pinnedToListenAgain": False,
            "thumbnails": None,
            "title": "Elasticity",
            "trackNumber": 1,
            "videoId": "5oMDAfUpWyQ",
            "videoType": "MUSIC_VIDEO_TYPE_OMV",
            "views": "3.5M plays",
        },
        {
            "album": "Elasticity",
            "artists": [{"id": "UCixP1MOaomAQY-9Aozsz2Uw", "name": "Serj Tankian"}],
            "duration": "3:19",
            "duration_seconds": 199,
            "feedbackTokens": {
                "add": None,
                "remove": "AB9zfpKFMQdR8uVCdutLcTTF3BDBOjqqqbwr-bDANWE--9HXr9tADOQYfnW81FW6QXLX-R6cMtCvdsgPKuMT8XjniP-LQ_Pw6g",
            },
            "inLibrary": False,
            "isAvailable": True,
            "isExplicit": True,
            "likeStatus": "INDIFFERENT",
            "pinnedToListenAgain": False,
            "thumbnails": None,
            "title": "Your Mom",
            "trackNumber": 2,
            "videoId": "wgG10tsBBOE",
            "videoType": "MUSIC_VIDEO_TYPE_OMV",
            "views": "1.4M plays",
        },
        {
            "album": "Elasticity",
            "artists": [{"id": "UCixP1MOaomAQY-9Aozsz2Uw", "name": "Serj Tankian"}],
            "duration": "4:17",
            "duration_seconds": 257,
            "feedbackTokens": {
                "add": None,
                "remove": "AB9zfpJbWFPVXXvTsAlcQy9sp6gBs30JkaZtdjZuWCQ-Hx3NHMZ-uLkPnZ-7dLqHfj8tuMoqcSHwBg2t_QRuCZrHsH47n_PoLg",
            },
            "inLibrary": False,
            "isAvailable": True,
            "isExplicit": False,
            "likeStatus": "INDIFFERENT",
            "pinnedToListenAgain": False,
            "thumbnails": None,
            "title": "How Many Times?",
            "trackNumber": 3,
            "videoId": "lLYkjQr3s5c",
            "videoType": "MUSIC_VIDEO_TYPE_OMV",
            "views": "1.3M plays",
        },
        {
            "album": "Elasticity",
            "artists": [{"id": "UCixP1MOaomAQY-9Aozsz2Uw", "name": "Serj Tankian"}],
            "duration": "5:28",
            "duration_seconds": 328,
            "feedbackTokens": {
                "add": None,
                "remove": "AB9zfpKk_MM2e2ZqEtkfkdI-lCm6Y9wRzhojFIAhstKwmlnx81h0yjMaVNRfrlVjuqtvFLo9qqsxkl801-tKLvEihCRk5-p5RQ",
            },
            "inLibrary": False,
            "isAvailable": True,
            "isExplicit": False,
            "likeStatus": "INDIFFERENT",
            "pinnedToListenAgain": False,
            "thumbnails": None,
            "title": "Rumi",
            "trackNumber": 4,
            "videoId": "usOpQ0ex4yQ",
            "videoType": "MUSIC_VIDEO_TYPE_OMV",
            "views": "2.5M plays",
        },
        {
            "album": "Elasticity",
            "artists": [{"id": "UCixP1MOaomAQY-9Aozsz2Uw", "name": "Serj Tankian"}],
            "duration": "3:47",
            "duration_seconds": 227,
            "feedbackTokens": {
                "add": None,
                "remove": "AB9zfpL81xM0DZOyozozULUOcSP5MT_eDfu5np-uIcHMzOR52bF2SrB7LY5vC_GBg1ak6SSJOHigg8rZNh9RgzDQPl7z0PlYBQ",
            },
            "inLibrary": False,
            "isAvailable": True,
            "isExplicit": False,
            "likeStatus": "INDIFFERENT",
            "pinnedToListenAgain": False,
            "thumbnails": None,
            "title": "Electric Yerevan",
            "trackNumber": 5,
            "videoId": "BGilNMeIR70",
            "videoType": "MUSIC_VIDEO_TYPE_OMV",
            "views": "838K plays",
        },
    ],
    "type": "Single",
    "year": "2021",
}


def test_parse_library_album(provider: YoutubeMusicProvider) -> None:
    """Check parsing of regular album is sane."""
    album: Album = provider._parse_album(library_album_dict, "SomeID")
    assert album.album_type == AlbumType.SINGLE
    assert album.metadata.description.startswith("Elasticity is the third EP")
    assert album.name == "Elasticity"
    assert album.year == '2021'
    assert album.artists[0].name == 'Serj Tankian'


# data from ytm.get_library_upload_album()
upload_album_dict = {
    "artists": [
        {
            "id": "FEmusic_library_privately_owned_artist_detaila_bpo_CT73qekAhOa_LxIIdHJpcGxlIGo",
            "name": "Triple J",
        }
    ],
    "audioPlaylistId": "MLPRb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
    "duration": "1 hour, 53 minutes",
    "duration_seconds": 6860,
    "isExplicit": False,
    "thumbnails": [
        {
            "height": 60,
            "url": "https://i9.ytimg.com/vi_locker/-bmF_PJAiXk/locker.png?sqp=-oaymwEGCDwQPCAA&rs=AMzJL3n7zmOsUSeXmePho49cV3s3eaUyng",
            "width": 60,
        },
        {
            "height": 120,
            "url": "https://i9.ytimg.com/vi_locker/-bmF_PJAiXk/locker.png?sqp=-oaymwEGCHgQeCAA&rs=AMzJL3kB1rurWxjW4QMzHntmKrBfuYnWsw",
            "width": 120,
        },
        {
            "height": 226,
            "url": "https://i9.ytimg.com/vi_locker/-bmF_PJAiXk/locker.png?sqp=-oaymwEICOIBEOIBIAA&rs=AMzJL3m82t3ApSC6uXUwG2xjVaFFUYsZHQ",
            "width": 226,
        },
        {
            "height": 544,
            "url": "https://i9.ytimg.com/vi_locker/-bmF_PJAiXk/locker.png?sqp=-oaymwEICKAEEKAEIAA&rs=AMzJL3mIe_PG03eE36pcZ5MTGOagbFfuYA",
            "width": 544,
        },
    ],
    "title": "Hottest 100 Volume 8",
    "trackCount": 30,
    "tracks": [
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIMZm9vIGZpZ2h0ZXJz",
                    "name": "Foo Fighters",
                }
            ],
            "duration": "3:48",
            "duration_seconds": 228,
            "entityId": "t_po_CT73qekAhOa_LxDXnvGL_v____8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Generator",
            "videoId": "hXNpyB3zEC0",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxICdTI",
                    "name": "U2",
                }
            ],
            "duration": "4:06",
            "duration_seconds": 246,
            "entityId": "t_po_CT73qekAhOa_LxDY38GI-P____8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Beautiful Day",
            "videoId": "9hN9UGacewE",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxINZGFuZHkgd2FyaG9scw",
                    "name": "The Dandy Warhols",
                }
            ],
            "duration": "3:29",
            "duration_seconds": 209,
            "entityId": "t_po_CT73qekAhOa_LxCEgYrD______8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Bohemian Like You",
            "videoId": "9u-xrNmybNI",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIKbWFnaWMgZGlydA",
                    "name": "Magic Dirt",
                }
            ],
            "duration": "3:42",
            "duration_seconds": 222,
            "entityId": "t_po_CT73qekAhOa_LxDm3veI______8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Dirty Jeans",
            "videoId": "MAmoydFGiyE",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIHd2hlYXR1cw",
                    "name": "Wheatus",
                }
            ],
            "duration": "4:04",
            "duration_seconds": 244,
            "entityId": "t_po_CT73qekAhOa_LxCrmOjgBA",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Teenage Dirtbag",
            "videoId": "7LT99uWhH3I",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIIeW91IGFtIGk",
                    "name": "You Am I",
                }
            ],
            "duration": "3:28",
            "duration_seconds": 208,
            "entityId": "t_po_CT73qekAhOa_LxD9ucHzAw",
            "likeStatus": "LIKE",
            "thumbnails": None,
            "title": "Damage",
            "videoId": "YeOb1iLxw3U",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIKbGl2aW5nIGVuZA",
                    "name": "The Living End",
                }
            ],
            "duration": "3:17",
            "duration_seconds": 197,
            "entityId": "t_po_CT73qekAhOa_LxC_oeWH-_____8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Pictures in the Mirror",
            "videoId": "ZLpFPQt04Uo",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIJcmFkaW9oZWFk",
                    "name": "Radiohead",
                }
            ],
            "duration": "4:11",
            "duration_seconds": 251,
            "entityId": "t_po_CT73qekAhOa_LxDil_Cg______8B",
            "likeStatus": "LIKE",
            "thumbnails": None,
            "title": "Everything in its Right Place",
            "videoId": "n0jv893g9Bk",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIGbG8gdGVs",
                    "name": "Lo-Tel",
                }
            ],
            "duration": "4:29",
            "duration_seconds": 269,
            "entityId": "t_po_CT73qekAhOa_LxCx77CDBQ",
            "likeStatus": "LIKE",
            "thumbnails": None,
            "title": "Teenager of the Year",
            "videoId": "j009bhwM0Ug",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIHMjggZGF5cw",
                    "name": "28 Days",
                }
            ],
            "duration": "3:40",
            "duration_seconds": 220,
            "entityId": "t_po_CT73qekAhOa_LxDovdKUBw",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Rip It Up",
            "videoId": "LN4kWch-aCk",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIJYmxpbmsgMTgy",
                    "name": "Blink 182",
                }
            ],
            "duration": "2:46",
            "duration_seconds": 166,
            "entityId": "t_po_CT73qekAhOa_LxDYivPYAQ",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Man Overboard",
            "videoId": "zgWSBGk917I",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIKYXZhbGFuY2hlcw",
                    "name": "The Avalanches",
                }
            ],
            "duration": "4:49",
            "duration_seconds": 289,
            "entityId": "t_po_CT73qekAhOa_LxD8u77QAg",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Frontier Psychiatrist",
            "videoId": "1kL0B9qXGQk",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIJc2t1bmtob3Vy",
                    "name": "Skunkhour",
                }
            ],
            "duration": "3:03",
            "duration_seconds": 183,
            "entityId": "t_po_CT73qekAhOa_LxCouea2_P____8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Kick in the Door",
            "videoId": "sXn3w79dolA",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIGYXJlYSA3",
                    "name": "Area 7",
                }
            ],
            "duration": "3:31",
            "duration_seconds": 211,
            "entityId": "t_po_CT73qekAhOa_LxDJ-e_JAg",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Start Makin Sense",
            "videoId": "dfDwyl0fMT4",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIMcG93ZGVyZmluZ2Vy",
                    "name": "Powderfinger",
                }
            ],
            "duration": "4:39",
            "duration_seconds": 279,
            "entityId": "t_po_CT73qekAhOa_LxCOv_q_-v____8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "My Hapiness",
            "videoId": "Ht7L_YKmWD0",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIUbWFjaGluZSBndW4gZmVsbGF0aW8",
                    "name": "Machine Gun Fellatio",
                }
            ],
            "duration": "5:11",
            "duration_seconds": 311,
            "entityId": "t_po_CT73qekAhOa_LxCrz_7sAg",
            "likeStatus": "LIKE",
            "thumbnails": None,
            "title": "Unsent Letter",
            "videoId": "_xy-UloaFDM",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIKc3VwZXJqZXN1cw",
                    "name": "The Superjesus",
                }
            ],
            "duration": "4:01",
            "duration_seconds": 241,
            "entityId": "t_po_CT73qekAhOa_LxD8g6-4-P____8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Gravity",
            "videoId": "Z9b03mYYfns",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxILbWlsbGVuY29saW4",
                    "name": "Millencolin",
                }
            ],
            "duration": "2:54",
            "duration_seconds": 174,
            "entityId": "t_po_CT73qekAhOa_LxCklc3z_P____8B",
            "likeStatus": "LIKE",
            "thumbnails": None,
            "title": "Penguins And Polar Bears",
            "videoId": "hb5CZ22gMOg",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIIY29sZHBsYXk",
                    "name": "Coldplay",
                }
            ],
            "duration": "4:30",
            "duration_seconds": 270,
            "entityId": "t_po_CT73qekAhOa_LxDjy-uG-_____8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Coldplay - Yellow",
            "videoId": "A2AGZmJ0iZo",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIHcGxhY2Vibw",
                    "name": "Placebo",
                }
            ],
            "duration": "4:01",
            "duration_seconds": 241,
            "entityId": "t_po_CT73qekAhOa_LxCXqdq9______8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Taste In Men",
            "videoId": "ifmPqMn1qjk",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIDb3Bt",
                    "name": "Opm",
                }
            ],
            "duration": "4:19",
            "duration_seconds": 259,
            "entityId": "t_po_CT73qekAhOa_LxDDlr7y_v____8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Heaven Is A Halfpipe",
            "videoId": "-bmF_PJAiXk",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIJcGogaGFydmV5",
                    "name": "PJ Harvey",
                }
            ],
            "duration": "3:21",
            "duration_seconds": 201,
            "entityId": "t_po_CT73qekAhOa_LxDbt5WeBA",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Good Fortune",
            "videoId": "clmRUOMd78c",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIXcXVlZW5zIG9mIHRoZSBzdG9uZSBhZ2U",
                    "name": "Queens Of The Stone Age",
                }
            ],
            "duration": "2:43",
            "duration_seconds": 163,
            "entityId": "t_po_CT73qekAhOa_LxCX1qzpAg",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Feel Good Hit Of The Summer",
            "videoId": "TFjNHlTvQ6Y",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxILdGV4IHBlcmtpbnM",
                    "name": "Tex Perkins",
                }
            ],
            "duration": "4:32",
            "duration_seconds": 272,
            "entityId": "t_po_CT73qekAhOa_LxCPh_PvAw",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "I Know You Know I Know",
            "videoId": "JB2LoK_zfD4",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIOc2luZWFkIG9jb25uZXI",
                    "name": "Sinead O'Conner",
                }
            ],
            "duration": "3:00",
            "duration_seconds": 180,
            "entityId": "t_po_CT73qekAhOa_LxDO-qrMAw",
            "likeStatus": "LIKE",
            "thumbnails": None,
            "title": "Daddy I'm Fine",
            "videoId": "yG547K3V7Ps",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIEZWVscw",
                    "name": "Eels",
                }
            ],
            "duration": "3:59",
            "duration_seconds": 239,
            "entityId": "t_po_CT73qekAhOa_LxCE2sfYAw",
            "likeStatus": "LIKE",
            "thumbnails": None,
            "title": "Mr E's Beautiful Blues",
            "videoId": "j_7rgSXXwk4",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIKcGF1bCBrZWxseQ",
                    "name": "Paul Kelly",
                }
            ],
            "duration": "3:37",
            "duration_seconds": 217,
            "entityId": "t_po_CT73qekAhOa_LxCQoOeTBg",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Every Fucking City",
            "videoId": "KvJatWaWpNk",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIHYm9keWphcg",
                    "name": "Bodyjar",
                }
            ],
            "duration": "3:09",
            "duration_seconds": 189,
            "entityId": "t_po_CT73qekAhOa_LxD4_-C7-_____8B",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Not The Same",
            "videoId": "D_Ccp3g1qfY",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIGZ2Vvcmdl",
                    "name": "George",
                }
            ],
            "duration": "3:19",
            "duration_seconds": 199,
            "entityId": "t_po_CT73qekAhOa_LxCr2aGFAw",
            "likeStatus": "LIKE",
            "thumbnails": None,
            "title": "Bastard Son",
            "videoId": "weTHUJilOzY",
        },
        {
            "album": {
                "id": "FEmusic_library_privately_owned_release_detailb_po_CT73qekAhOa_LxIUaG90dGVzdCAxMDAgdm9sdW1lIDgaCHRyaXBsZSBqIgNncG0",
                "name": "Hottest 100 Volume 8",
            },
            "artists": [
                {
                    "id": "FEmusic_library_privately_owned_artist_detaila_po_CT73qekAhOa_LxIIZXZlcmxhc3Q",
                    "name": "Everlast",
                }
            ],
            "duration": "4:42",
            "duration_seconds": 282,
            "entityId": "t_po_CT73qekAhOa_LxDgq-sK",
            "likeStatus": "INDIFFERENT",
            "thumbnails": None,
            "title": "Black Jesus",
            "videoId": "fOQZyhmrahE",
        },
    ],
    "type": "Album",
    "year": "2000",
}


def test_parse_uploaded_album(provider: YoutubeMusicProvider) -> None:
    """Check parsing of an uploaded album is sane."""
    album: Album = provider._parse_album(upload_album_dict, "SomeID")
    assert album.album_type == AlbumType.ALBUM
    assert album.name == "Hottest 100 Volume 8"
    assert album.year == '2000'
