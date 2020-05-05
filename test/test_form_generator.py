import json
from wickedhot.form_generator import generate_form


def test_form_generation():

    stats = {'weight': {'median': 160.5}, 'height': {'median': 6.0}}

    # can also try with stats = None
    # stats = None

    packaged = {'max_levels_default': 10000,
                'numeric_cols': ['weight', 'height'],
                'numeric_stats': stats,
                'categorical_n_levels_dict': {'animal': 2, 'color': 1},
                'one_hot_encoder_dicts': {'animal': {'cat': 0, 'mouse': 1}, 'color': {'blue': 0}}}

    index_html = generate_form(packaged)

    assert isinstance(index_html, str)
    assert "<html" in index_html

    filename = 'junk_index.html'
    fp = open(filename, 'w')
    fp.write(index_html)
    fp.close()

    print("wrote: %s" % filename)





