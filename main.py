import os
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDButton
import pandas as pd
from kivy.core.window import Window
from kivy_deps import sdl2, glew
from kivymd.uix.card.card import MDCard
from kivymd.uix.label.label import MDLabel
from kivymd.uix.snackbar.snackbar import MDSnackbar, MDSnackbarText
from kivymd.icon_definitions import md_icons
import encodings
import codecs



KV = """
ScreenManager:
    MainScreen:
    ResultScreen:

<MainScreen>:
    name: 'main'
    canvas.before:
        Color:
            rgba: 1, 1, 1, .5  # Optional: Add a white background color behind the image
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'logo.jpg'  # Path to your background image

    MDBoxLayout:
        orientation: 'vertical'
        # padding: 50
        # spacing: 10
        size_hint: 1, 1

        MDBoxLayout:
            orientation: 'vertical'
            spacing: '20dp'
            adaptive_height: True
            size_hint: 0.8, 0.8

            MDCard:
                style: "elevated"
                pos_hint: {"center_x": .6}
                padding: "4dp"
                size_hint: 1, 0.5

                # Sets custom properties.
                theme_shadow_color: "Custom"
                shadow_color: "#5DE2E7"
                theme_bg_color: "Custom"
                md_bg_color: "white"
                md_bg_color_disabled: "grey"
                theme_shadow_offset: "Custom"
                shadow_offset: (1, -2)
                theme_shadow_softness: "Custom"
                shadow_softness: 1
                theme_elevation_level: "Custom"
                elevation_level: 2
                    

                MDButton:
                    on_release: app.file_manager_open('file1')

                    MDButtonText:
                        id: upload_file_one
                        text: "Upload File 1"
                        halign: 'center'
                        theme_text_color: "Custom"
                        text_color: "blue"

                    MDButtonIcon:
                        icon: "file-upload"
                        user_font_size: "38sp"
                        theme_text_color: "Custom"
                        text_color: "blue"

                MDLabel:
                    id: file1_label
                    text: "No file selected"
                    halign: 'center'
                    theme_text_color: "Custom"
                    text_color: "black"

            MDCard:
                style: "elevated"
                pos_hint: {"center_x": .6}
                padding: "4dp"
                size_hint: 1, 0.45
                # Sets custom properties.
                theme_shadow_color: "Custom"
                shadow_color: "#5DE2E7"
                theme_bg_color: "Custom"
                md_bg_color: "white"
                md_bg_color_disabled: "grey"
                theme_shadow_offset: "Custom"
                shadow_offset: (-2, 1)
                theme_shadow_softness: "Custom"
                shadow_softness: 1
                theme_elevation_level: "Custom"
                elevation_level: 2

                MDButton:
                    id: upload_file_two
                    style: 'elevated'
                    theme_shadow_color: "Custom"
                    shadow_color: "#5DE2E7"
                    size_hint: 0.5, 0.9
                    on_release: app.file_manager_open('file2')

                    MDButtonText:
                        text: "Upload File 2"
                        halign: 'center'
                        theme_text_color: "Custom"
                        text_color: "blue"

                    MDButtonIcon:
                        icon: "file-upload"
                        user_font_size: "38sp"
                        theme_icon_color: "Custom"
                        icon_color: "blue"

                MDLabel:
                    id: file2_label
                    text: "No file selected"
                    halign: 'center'
                    theme_text_color: "Custom"
                    text_color: "black"

            MDButton:
                style: "elevated"
                pos_hint: {"center_x": .6}
                size_hint_y: 0.1
                on_release: app.compare_excel_files()# Replace 'ColumnName' with the actual column name

                MDButtonText:
                    text: "Compare Files"
                    halign: 'center'
                    theme_text_color: "Custom"
                    text_color: 'blue'

                MDButtonIcon:
                    icon: "file-compare"
                    theme_font_size: "Custom"
                    font_size: "25sp"
                    theme_text_color: "Custom"
                    text_color: "blue"

<ResultScreen>:
    name: 'result'
    canvas.before:
        Color:
            rgba: 0, 0, 0, .5  # Optional: Add a white background color behind the image
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'logo.jpg'  # Path to your background image
            
    MDBoxLayout:
        orientation: 'vertical'
        padding: '10dp'
        spacing: '10dp'
        size_hint_y: 1  # Ensure the layout fills the screen vertically

        MDLabel:
            text: "Comparison Results"
            font_style: "Headline"
            halign: "center"
            theme_text_color: "Custom"
            text_color: "#5DE2E7"
            size_hint_y: 0.1  # Fixed height for the header

        MDGridLayout:
            cols: 2
            spacing: '10dp'
            padding: '10dp'
            size_hint_y: 0.8  # Take up 80% of the screen height
            size_hint_x: 1  # Take up full width

            # Column for File 1 unique names
            MDBoxLayout:
                orientation: 'vertical'
                spacing: '10dp'
                size_hint_x: 0.5  # Half the width
                size_hint_y: 1  # Fill the height of the MDGridLayout

                MDLabel:
                    text: "Unique to Day 1"
                    font_style: "Body"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: "#5DE2E7"
                    size_hint_y: 0.1  # Fixed height for the sub-header

                MDScrollView:
                    do_scroll_x: False
                    size_hint_y: 0.9  # Take up remaining height

                    MDList:
                        id: unique_to_file1_list
                        size_hint_y: None
                        height: self.minimum_height  # Allow the list to expand

            # Column for File 2 unique names
            MDBoxLayout:
                orientation: 'vertical'
                spacing: '10dp'
                size_hint_x: 0.5  # Half the width
                size_hint_y: 1  # Fill the height of the MDGridLayout

                MDLabel:
                    text: "Unique to Day 2"
                    font_style: "Body"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: "#5DE2E7"
                    size_hint_y: 0.1  # Fixed height for the sub-header

                MDScrollView:
                    do_scroll_x: False
                    size_hint_y: 0.9  # Take up remaining height

                    MDList:
                        id: unique_to_file2_list
                        size_hint_y: None
                        height: self.minimum_height  # Allow the list to expand

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_x': 0.5}
            size_hint_y: 0.1  # Fixed height for the button
            on_release: app.go_back()

<SplashScreen>:
    name: 'splash'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Loading...'
            font_size: 50
        Image:
            source: 'icon.png'

"""

import os
os.environ['KIVY_LOG_LEVEL'] = 'debug'

Window.size = (400, 600)

Window.resizable = False


class SplashScreen(Screen):
    pass

class MainScreen(Screen):
    pass


class ResultScreen(Screen):
    pass


class TARMCompareApp(MDApp):

    try:
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            Window.bind(on_keyboard=self.events)
            self.manager_open = False
            self.file_manager = MDFileManager(
                # preview=True,
                exit_manager=self.exit_manager, select_path=self.select_path
            )

            self.file1 = None  # To store the first file path
            self.file2 = None  # To store the second file path
            self.file_to_set = None  # To track which file is being set (file1 or file2)

        def build(self):
            self.theme_cls.primary_palette = "Blue"
            self.theme_cls.theme_style = "Light"
            # self.root.current = 'splash'
            # # self.sm.add_widget(MainScreen(name='main'))
            # Clock.schedule_once(self.switch_to_main, 3)
            return Builder.load_string(KV)

        def switch_to_main(self, dt):
            self.root.current = 'main'

        def file_manager_open(self, file_to_set):
            """
            Open the file manager and set which file (file1 or file2) is being selected.
            """
            self.file_to_set = file_to_set  # Track which file is being set
            self.file_manager.show(os.path.expanduser("~"))  # Open file manager at the home directory
            self.manager_open = True

        def select_path(self, path: str):
            """
            Called when a file path is selected.
            """
            self.exit_manager()

            # Store the selected path in the appropriate variable (file1 or file2)
            if self.file_to_set == "file1":
                self.file1 = path
                self.root.get_screen('main').ids.file1_label.text = f"File 1: {os.path.basename(path)}"
                print(self.root.get_screen('main').ids.file1_label.text)
            elif self.file_to_set == "file2":
                self.file2 = path
                print(path)
                self.root.get_screen('main').ids.file2_label.text = f"File 2: {os.path.basename(path)}"

            # Show a snackbar with the selected path
            MDSnackbar(
                MDSnackbarText(
                    text=f"Selected: {os.path.basename(path)}",
                ),
                y='24dp',
                pos_hint={"center_x": 0.5},
                size_hint_x=0.8,
            ).open()

        def exit_manager(self, *args):
            """
            Close the file manager.
            """
            self.manager_open = False
            self.file_manager.close()

        def events(self, instance, keyboard, keycode, text, modifiers):
            """
            Handle keyboard events (e.g., back button on Android).
            """
            if keyboard in (1001, 27):
                if self.manager_open:
                    self.file_manager.back()
            return True
        

        def compare_excel_files(self):
            """
            Compare the two Excel files based on the combined 'name' and 'surname' columns.
            """
            if not self.file1 or not self.file2:
                MDSnackbar(
                    MDSnackbarText(
                        text="Please select both files before comparing.",
                    ),
                    y='24dp',
                    pos_hint={"center_x": 0.5},
                    size_hint_x=0.8,
                ).open()
                return

            try:
                # Read the Excel files
                df1 = pd.read_excel(self.file1)
                df2 = pd.read_excel(self.file2)

                # Check if the required columns exist in both files
                required_columns = ['name', 'surname']
                for column in required_columns:
                    if column not in df1.columns or column not in df2.columns:
                        MDSnackbar(
                            MDSnackbarText(
                                text=f"Column '{column}' not found in one or both files.",
                            ),
                            y='24dp',
                            pos_hint={"center_x": 0.5},
                            size_hint_x=0.8,
                        ).open()
                        return

                # Combine 'name' and 'surname' into a single 'full_name' column
                df1['full_name'] = df1['name'] + ' ' + df1['surname']
                df2['full_name'] = df2['name'] + ' ' + df2['surname']

                # Extract the full names from the combined column
                full_names1 = set(df1['full_name'])
                full_names2 = set(df2['full_name'])

                # Find names that are unique to each file
                unique_to_file1 = full_names1 - full_names2
                unique_to_file2 = full_names2 - full_names1

                # Clear previous results
                self.root.get_screen('result').ids.unique_to_file1_list.clear_widgets()
                self.root.get_screen('result').ids.unique_to_file2_list.clear_widgets()

                # Add names unique to File 1
                for name in unique_to_file1:
                    card = MDCard(
                        style = "elevated",
                        padding = "8dp",
                        size_hint_y=None,
                        height="100dp",
                        ripple_behavior=True,
                    )
                    card.add_widget(
                        MDLabel(
                            text=name,
                            theme_text_color="Custom",
                            font_style="Title",
                        )
                    )
                    self.root.get_screen('result').ids.unique_to_file1_list.add_widget(card)

                # Add names unique to File 2
                for name in unique_to_file2:
                    card = MDCard(
                        style = "elevated",
                        padding = "8dp",
                        size_hint_y=None,
                        height="100dp",
                        elevation=1,
                        ripple_behavior=True,
                    )
                    card.add_widget(
                        MDLabel(
                            text=name,
                            theme_text_color="Custom",
                            font_style="Title",
                        )
                    )
                    self.root.get_screen('result').ids.unique_to_file2_list.add_widget(card)

                # Switch to the result screen
                self.root.current = 'result'

            except Exception as e:
                print(e)  # Log the error for debugging
                MDSnackbar(
                    MDSnackbarText(
                        text="An error occurred while comparing the files. Please check the file format.",
                    ),
                    y='24dp',
                    pos_hint={"center_x": 0.5},
                    size_hint_x=0.8,
                ).open()  

        def go_back(self):
            """
            Return to the main screen.
            """
            self.root.current = 'main'
    
    except Exception as e:
        print(e)


if __name__ == '__main__':
    TARMCompareApp().run()