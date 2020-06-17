# Pytest for the plaque diversity repo

from Plaque_diversity_ethnic_group import q_wikidata

import pytest

# Test the query function
@pytest.mark.parametrize('q, result',[
    ('Q8016', 'English people'), # Q8016 Winston Churchill - English people
    ('Q257911', 'African Americans'),
    ('Q704954', 'Jewish people')])
def test_q_wikidata(q, result):
    assert q_wikidata(q) == result

if __name__ == '__main__':
    test_q_wikidata()