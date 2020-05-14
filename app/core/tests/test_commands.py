from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        # simulate behavior of django when db is available
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # mock object is gi here
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)  # call_count is useful

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        # check for OperationalError, wait for one second and try again
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # side effect and raise OperationalError five times
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
