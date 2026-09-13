from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = 10

@test_case(points=4, hidden=False)
def test_q1(mean_of, assert_equal):
    assert_equal('mean_of([1, 2, 3])', mean_of([1, 2, 3]), 2)

