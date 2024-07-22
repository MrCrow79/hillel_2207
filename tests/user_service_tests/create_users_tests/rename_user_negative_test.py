import unittest


class TestRenameUserNegative(unittest.TestCase):

    # before test create user: pre-condition
    # after test delete user post-condition

    run_teardown = True

    def setUp(self):  # unittest magic: do before each test
        print('Precodition for test stuff')
        __class__.run_teardown = True

    def tearDown(self):  # unittest magic: do after each test
        if __class__.run_teardown is True:
            print('Post-condition for test stuff')

    @classmethod
    def setUpClass(cls):  # unittest magic: do before each test
        # send_request to get first 10 users
        print('Precodition for class stuff')

    @classmethod
    def tearDownClass(cls):  # unittest magic: do after each test
        print('Post-condition for class stuff')
        #  send request to database for deleting all users that was created in all class tests


    def test_rename_with_none(self):
        # send request to create user
       print('Test test_rename_with_none')
        # send request to delete user

    def test_rename_with_less_than_min_len_of_name(self):
        # send request to create user

        print('Test test_rename_with_less_than_min_len_of_name')

        __class__.run_teardown = False
        # send request to delete user
