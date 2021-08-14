import os
import tempfile

here = os.path.dirname(os.path.abspath(__file__))

CFG_FILE = os.path.join(here, "sample_spectra_gen.cfg")

TEMPDIR = tempfile.gettempdir() + "/"
PID = os.getpid()
SYNTH_FILE = TEMPDIR + "turboseti_stream." + str(os.getpid()) + ".fil"
MAX_DRIFT_RATE = 4.0
MIN_SNR = 25.0

