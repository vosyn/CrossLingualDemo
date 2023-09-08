from pydub import AudioSegment
import sys
import os

def convert_to_mono(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    mono_audio = audio.set_channels(1)
    mono_audio.export(output_file, format="wav")

if __name__ == '__main__': 

    inputDir = sys.argv[1]
    outputDir = sys.argv[2]

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for f in os.listdir(inputDir):
        if f.endswith('.wav'):
            
            #Load Audio
            audio = AudioSegment.from_wav(os.path.join(inputDir, f))

            # Set to mono
            convert_to_mono(os.path.join(inputDir, f), os.path.join(outputDir, f))

            print(f"Converted {f} to Mono and saved as {outputDir}/{f}")
    print(f'Conversion complete, folder {outputDir} is ready. ')