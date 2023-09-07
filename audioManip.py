from pydub import AudioSegment
import os
import sys

if __name__ == '__main__': 

    inputName = sys.argv[1]
    outputName = sys.argv[2]
    targetRate = sys.argv[3]

    if not os.path.exists(outputName):
        os.makedirs(outputName)

    for f in os.listdir(inputName):
        if f.endswith('.wav'):
            
            #Load Audio
            audio = AudioSegment.from_wav(os.path.join(input_folder, f))

            # Set to target sample rate
            audio = audio.set_frame_rate(targetRate)

            # Output Path
            outputPath = os.path.join(outputName, f)

            # Export
            audio.export(outputPath, format='wav')
            print(f"Converted {f} to {targetRate} Hz and saved as {outputPath}")
    print(f'Conversion complete, folder {outputName} is ready. ')