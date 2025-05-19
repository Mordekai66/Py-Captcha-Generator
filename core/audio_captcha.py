import wave
import os
def generate_audio_captcha(data, output_path, voice_dir):
    infiles = []
    for i in data:
        infiles.append(os.path.join(voice_dir, f"{i.lower()}.wav"))
    outfile = os.path.join(output_path,"captcha.wav")

    data= []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()

    output = wave.open(outfile, 'wb')
    for i in range(len(data)):
        if i == 0:
            output.setparams(data[i][0])
        output.writeframes(data[i][1])
    output.close()