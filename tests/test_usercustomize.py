"""Testing of module usercustomize."""

def test_import_usercustomize():

    try:
        import usercustomize
        assert True
    except ImportError:
        # package usercustomize-entrypoints is not installed
        assert False
