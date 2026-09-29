import pytest
from PIL import Image

from szurubooru import errors
from szurubooru.func import images


def test_heif_conversion_of_decompression_bomb(read_asset, monkeypatch):
    monkeypatch.setattr(Image, "MAX_IMAGE_PIXELS", 1)
    with pytest.raises(errors.ProcessingError):
        images.convert_heif_to_png(read_asset("heif.heif"))
