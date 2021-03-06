import RPi.GPIO as gpio
import time

# =========================================
# Makers! Implement your own actions here.
# =========================================

playshell = None
class play(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, voice_command):

        track = voice_command.replace(self.keyword, '', 1)

        global playshell
        if (playshell == None):
            playshell = subprocess.Popen(["/usr/local/bin/mpsyt",""],stdin=subprocess.PIPE ,stdout=subprocess.PIPE)

        playshell.stdin.write(bytes('/' + track + '\n1\n', 'utf-8'))
        playshell.stdin.flush()

        gpio.setmode(gpio.BCM)
        gpio.setup(23, gpio.IN)

        while gpio.input(23):
             time.sleep(1)

        pkill = subprocess.Popen(["/usr/bin/pkill","vlc"],stdin=subprocess.PIPE)

        
    # =========================================
    # Makers! Add your own voice commands here.
    # =========================================

    actor.add_keyword(_('play'), play(say,_('play')))
