import sys
from django.test.runner import DiscoverRunner
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner


class GradescopeDjangoRunner(DiscoverRunner):
    """Replacing Django Default Unit Test Runner with Gradescope Test Runner"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run_suite(self, suite, **kwargs):
        return JSONTestRunner(
            stream=sys.stdout, descriptions=True, verbosity=1,
            failfast=False, buffer=True, visibility="visible",
            stdout_visibility=None, post_processor=None,
            failure_prefix="Test Failed: "
        ).run(suite)
