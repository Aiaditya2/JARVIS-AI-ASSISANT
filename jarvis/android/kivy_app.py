"""
Kivy Android App for JARVIS
Main application entry point for Android
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import logging

logger = logging.getLogger(__name__)


class JARVISApp(App):
    """Main Kivy application for Android"""
    
    def build(self):
        """Build the app UI"""
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title = Label(
            text='JARVIS - Hindi Voice Assistant',
            size_hint=(1, 0.2),
            font_size='24sp'
        )
        layout.add_widget(title)
        
        # Status label
        self.status_label = Label(
            text='Ready to listen...',
            size_hint=(1, 0.3),
            font_size='18sp'
        )
        layout.add_widget(self.status_label)
        
        # Listen button
        self.listen_btn = Button(
            text='Listen (Hindi)',
            size_hint=(1, 0.2),
            font_size='20sp'
        )
        self.listen_btn.bind(on_press=self.on_listen)
        layout.add_widget(self.listen_btn)
        
        # Response label
        self.response_label = Label(
            text='',
            size_hint=(1, 0.3),
            font_size='16sp',
            text_size=(None, None)
        )
        layout.add_widget(self.response_label)
        
        return layout
    
    def on_listen(self, instance):
        """Handle listen button press"""
        self.status_label.text = "Listening..."
        self.listen_btn.disabled = True
        
        # Import here to avoid issues if not on Android
        try:
            from jarvis.android.android_voice import AndroidVoiceHandler
            from jarvis.main import JARVIS
            
            # Initialize JARVIS
            jarvis = JARVIS(use_android=True)
            
            # Start listening
            def on_recognized(text):
                Clock.schedule_once(lambda dt: self._process_command(text), 0)
            
            android_voice = AndroidVoiceHandler()
            android_voice.start_listening_hindi(on_recognized)
        except Exception as e:
            logger.error(f"Error in on_listen: {e}")
            self.status_label.text = f"Error: {str(e)}"
            self.listen_btn.disabled = False
    
    def _process_command(self, text):
        """Process recognized command"""
        self.status_label.text = f"Heard: {text}"
        # Process with JARVIS and update response_label
        self.response_label.text = "Processing..."
        self.listen_btn.disabled = False


if __name__ == '__main__':
    JARVISApp().run()
