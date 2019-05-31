import time
from LEDController import LEDController
from SoundController import SoundController

LEDController = LEDController()
SoundController = SoundController()

# Display yellow, red, and flashing red lights as alarm time approaches

# Display yellow warn for 50 minutes
LEDController.display_yellow()
time.sleep(60 * 50) 

# Display red warn for ten minutes, minues ten seconds for flashing
LEDController.display_red()
time.sleep((10 * 60) - 10)

# Flash red warn light for ten seconds
LEDController.flash_red(10)

# Play alarm sound
SoundController.playAlarm(5)