from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

def generate_image(request):
    image = Image.new("RGB", (400, 200), "white")
    draw = ImageDraw.Draw(image)

    # ফন্ট লোড করা
    font_path = "F:/GitHub/Gemten-Ai/server/Helper/static/kalpurush.ttf"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(BASE_DIR, 'static', 'kalpurush.ttf')
    font = ImageFont.truetype(font_path, 30)

    # টেক্সট লিখা
    text = "'গোল্ডেন ডোম' প্রতিরক্ষা ব্যবস্থা চালুর পরিকল্পনার কথা জানিয়েছেন ট্রাম্প"
    draw.text((20, 20), text, font=font, fill="black")

    # Save to disk
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_image_{timestamp}.png"
    save_dir = "generated_images"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, filename)

    image.save(save_path)

    print("Image saved to:", save_path)
    return save_path

# Example usage
# generate_image("HelloWorld")




import os
from django.utils import timezone
from django_cron import CronJobBase, Schedule

# Get base directory (where manage.py is)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # myapp/
PROJECT_DIR = os.path.dirname(BASE_DIR)  # root of project where manage.py is

# Path to log file
LOG_FILE_PATH = os.path.join(PROJECT_DIR, 'cron_logs.txt')

def log_cron_message(message: str):
    cute_message = f"{timezone.now()} - {message}\n"
    with open(LOG_FILE_PATH, 'a', encoding='utf-8') as log_file:
        log_file.write(cute_message)

# Every 1 minutes
class OneMinuteCron(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.five_minute_cron'

    def do(self):
        msg = "⏱️ [1-minute Cron] Running task..."
        print(msg)
        log_cron_message(msg)

# Every 5 minutes
class FiveMinuteCron(CronJobBase):
    RUN_EVERY_MINS = 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.five_minute_cron'

    def do(self):
        msg = "⏱️ [5-minute Cron] Running task..."
        print(msg)
        log_cron_message(msg)

# Every 15 minutes
class FifteenMinuteCron(CronJobBase):
    RUN_EVERY_MINS = 15
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.fifteen_minute_cron'

    def do(self):
        msg = "⏲️ [15-minute Cron] Performing scheduled task."
        print(msg)
        log_cron_message(msg)

# Every hour
class HourlyCron(CronJobBase):
    RUN_EVERY_MINS = 60
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.hourly_cron'

    def do(self):
        msg = "🕐 [Hourly Cron] Hello from the hourly job!"
        print(msg)
        log_cron_message(msg)
