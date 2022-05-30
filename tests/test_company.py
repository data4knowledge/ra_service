import pytest
from model.company import Company

def test_company_valid():
    params = {'identifier': 'xxx', 'country_code': "DNK"}
    item = Company(**params)
    assert item.identifier == 'xxx'
    assert item.country_code == "DNK"

def test_company_invalid():
    params = {'identifier': 'xxx', 'country_code': "DKK"}
    with pytest.raises(ValueError):
      item = Company(**params)


