import numpy as np
import scitools.sound

# Generate Note Tones
def noteGenerator(frequency=440, length=0.2, amplitude=1, sample_rate=44100):
    '''
    # Signal Formula -data- f(t) = A*sin(2*π*f*t+ϕ) or f(t) = A*sin(ω*t+ϕ)
    # signal basic settings - sound may vary by device type
    base_tone_freq = 440    # hertz (Hz) - 0.44kHz (Sound Frequency(Hz)) - Note A4(La4)
    base_duration = .2      # (Basic Duration Unit in Seconds) or length = 0.2
    sampleRate = 44100      # Samples Per Second Hz - 44.1kHz (Sample Rate)
    samples = base_duration*sampleRate  #
    
    # Produces a t second Audio-File
    t = np.linspace(0, time, time*sampleRate)  # timepoints
    A = np.iinfo(np.int16).max  # Volume (Amplitude) - the volume measure (max is 32768) or the Peak Value
    '''
    timepoints = np.linspace(0, length, int(length*sample_rate))
    data = amplitude*np.sin(2*np.pi*frequency*timepoints)  # A*sin(2*π*f*t) and .astype(np.float32)
    return data

notes =   ('F3', 'F#3', 'G3',  'G#3',  'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4',  'G#4',  'A4')
notesDo = ('Fa3','Fa#3','Sol3','Sol#3','La3','La#3','Si3','Do4','Do#4','Re4','Re#4','Mi4','Fa4','Fa#4','Sol4','Sol#4','La4')
base_freq = 440*(2**(1/12))**-16  # edited for example
notes2freq   = {notes[i].casefold(): base_freq*2**(i/12.0) for i in range(len(notes))}
notesDo2freq = {notesDo[i].casefold(): base_freq*2**(i/12.0) for i in range(len(notes))}

composition_letters = """
G3-0.4 G3-0.4 A3-0.8 G3-0.8 C4-0.7 B3-1.5 
G3-0.4 G3-0.4 A3-0.8 G3-0.8 D4-0.7 C4-1.4 
G3-0.4 G3-0.4 G4-0.7 E4-0.7 C4-0.8 D4-0.8 E4-0.8
F4-0.4 F4-0.4 E4-0.8 C4-0.8 D4-0.8 C4-1.6 
"""  # Happy Birthday to You - DoReMi-CDE

comp_letters_list = composition_letters.split()
tones = []
for letter in comp_letters_list:
    note, duration = letter.split('-')
    if note.title() in notes:
        s = noteGenerator(notes2freq[note.casefold()], float(duration))
        tones.append(s)
    elif note.title() in notesDo:
        s = noteGenerator(notesDo2freq[note.casefold()], float(duration))
        tones.append(s)
    else:
        print('Someting is wrong! Check and Try Again.')
        pass

tones_wave = (np.concatenate(tones)*(np.iinfo(np.int16).max))  # Amplitude run 1 time

# A 2D array where the left and right tones are contained in their respective rows
tones_wave_stereo = np.vstack((tones_wave, tones_wave))

# Reshape 2D array so that the left and right tones are contained in their respective columns
tones_wave_stereo = tones_wave_stereo.transpose()

scitools.sound.write(data=tones_wave_stereo, filename="HapyBirthday-DoReMi-MuCe.wav", sample_rate=44100)

# tones_wave_stereo features
print(len(tones_wave_stereo))
print(np.max(tones_wave_stereo))
print(np.min(tones_wave_stereo))