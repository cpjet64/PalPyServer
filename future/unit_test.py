import unittest
from unittest.mock import patch
import os
from current.difficultypresets import casual_settings
from current.gui import (
    locate_game_server,
    load_settings_from_ini,
    save_settings_to_ini,
    update_settings_preset,
    display_settings,
    get_modified_pairs,
)


class TestGUIFunctions(unittest.TestCase):
    # Mock patches to simulate file dialog and user input
    @patch("gui.filedialog.askdirectory", return_value=os.getcwd())
    def test_locate_game_server(self, mock_ask_directory):
        locate_game_server()
        # Here you add your assertions

    @patch("gui.load_settings", return_value=[("key1", "value1"), ("key2", "value2")])
    def test_load_settings_from_ini(self, mock_load_settings):
        load_settings_from_ini()
        # Here you add your assertions

    @patch("gui.get_modified_pairs", return_value={"key1": "value1", "key2": "value2"})
    @patch("gui.save_modified_pairs")
    @patch("gui.messagebox")
    def test_save_settings_to_ini(
        self, mock_get_modified_pairs, mock_save_modified_pairs, mock_messagebox
    ):
        save_settings_to_ini()
        # Here you add your assertions

    def test_update_settings_preset(self):
        modified_pairs = update_settings_preset("Casual")
        self.assertEqual(modified_pairs, casual_settings)
        # Repeat this for other difficulty presets

    @patch("gui.tree_view")
    def test_display_settings(self, mock_tree_view):
        default_pairs = [("key1", "value1"), ("key2", "value2")]
        modified_pairs = {"key1": "value1", "key2": "value2"}
        display_settings(default_pairs, modified_pairs)
        # Here you add your assertions over what is expected when the function is called

    @patch("gui.tree_view")
    def test_get_modified_pairs(self, mock_tree_view):
        mock_tree_view.get_children.return_value = ["item1", "item2"]
        mock_tree_view.item.side_effect = lambda item, **kwargs: {0: "key", 2: "value"}
        expected_pairs = {"key": "value", "key": "value"}
        self.assertEqual(expected_pairs, get_modified_pairs())


# call all tests
if __name__ == "__main__":
    unittest.main()
