# Install the assemblyai package by executing the command `pip3 install assemblyai` (macOS) or `pip install assemblyai` (Windows).

# Import the AssemblyAI module
import assemblyai as aai

# Your API token is already set here
aai.settings.api_key = "d184929b02e844f2b92a4b88746f3ae8"

# Create a transcriber object.
transcriber = aai.Transcriber()

# If you have a local audio file, you can transcribe it using the code below.
# Make sure to replace the filename with the path to your local audio file.
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

# Alternatively, if you have a URL to an audio file, you can transcribe it with the following code.
# Uncomment the line below and replace the URL with the link to your audio file.
# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/espn-bears.m4a")
transcript = transcriber.transcribe("https://www.cnn.com/interactive/uploads/20230626-trump_audio.mp3")

# After the transcription is complete, the text is printed out to the console.
print(transcript.text)