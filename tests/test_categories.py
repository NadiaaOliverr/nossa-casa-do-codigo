from model.category import Category
from dao.category_dao import CategoryDatabase

import pytest

def test_not_should_allow_add_name_in_blank():
    name = ''
    with pytest.raises(Exception):
        Category(name)

def test_not_should_allow_add_category_with_the_same_name():
    name_1 = 'Romance'
    name_2 = 'Romance'
    categories = CategoryDatabase()

    with pytest.raises(Exception):
        categories.add(name_1)
        categories.add(name_2)
