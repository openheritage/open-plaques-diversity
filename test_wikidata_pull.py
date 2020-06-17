# Pytest for the plaque diversity repo

from Plaque_diversity_ethnic_group import q_wikidata

import pytest

# Test the query function
@pytest.mark.parametrize('q, result',[
    ('Q8016', 'English people'),
    ('Q257911', 'African Americans')])
def test_q_wikidata(q, result):
    # Q8016 Winston Churchill - ethnic group - English people
    assert q_wikidata(q) == result

if __name__ == '__main__':
    test_q_wikidata()