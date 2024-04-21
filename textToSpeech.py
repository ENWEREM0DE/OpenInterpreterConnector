from pathlib import Path
from openai import OpenAI
import  pygame


client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Michael is a bitch"
)

response.stream_to_file(speech_file_path)


def play_mp3(file_path):
  # Initialize pygame
  pygame.init()

  try:
    # Load the MP3 file
    pygame.mixer.music.load(file_path)

    # Play the MP3 file
    pygame.mixer.music.play()

    # Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)
  except pygame.error:
    print("Error: Unable to load or play the MP3 file")

  # Quit pygame
  pygame.quit()


# Example usage
mp3_file_path = "./speech.mp3"
play_mp3(mp3_file_path)