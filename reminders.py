# reminders.py
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from notifier import send_email_notification

def start_reminder_checker(manager):
    def check_reminders():
        now = datetime.now()
        soon = now + timedelta(hours=1)

        for event in manager.get_all_events():
            try:
                start = datetime.fromisoformat(event.start_time)
                if now <= start <= soon:
                    print(f"⏰ Reminder: '{event.title}' at {event.start_time}")

                    # Send email reminder if email is present
                    if event.email:
                        subject = f"Reminder: {event.title} starts soon!"
                        body = f"""
Hello,

This is a reminder for your event:

Title: {event.title}
Description: {event.description}
Start Time: {event.start_time}
End Time: {event.end_time}

Thanks,
Event Scheduler
"""
                        send_email_notification(event.email, subject, body)
            except Exception as e:
                print(f"Reminder error: {e}")

    scheduler = BackgroundScheduler()
    scheduler.add_job(check_reminders, 'interval', minutes=1)
    scheduler.start()
