import time
from LEDController import LEDController
from SoundController import SoundController
from StrobeController import StrobeController
import setproctitle

setproctitle.setproctitle("TACO_driver")

LEDController = LEDController()
SoundController = SoundController()
StrobeController = StrobeController()

# Display yellow, red, and flashing red lights as alarm time approaches

# Display yellow warn for 50 minutes
LEDController.display_yellow()
time.sleep(50 * 60) 

# Display red warn for ten minutes, minues ten seconds for flashing
LEDController.display_red()
time.sleep((10 * 60) - 10)

# Flash red warn light for ten seconds
LEDController.flash_red(10)

# Play alarm sound
SoundController.playAlarm(500)

# Flash strobe
StrobeController.enable_strobe()