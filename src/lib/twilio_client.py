from datetime import datetime
import logging
from django.conf import settings
from twilio.rest import TwilioRestClient

TZ = settings.PYTZ_TIMEZONE

DAILY_MSG = "Reminder: Your appointment with Dr. %s is at %s today.  Pre-register with CALMD to expedite your check-in: http://bit.ly/1lVulKg"

ALERT_MSG = "Notice: Your %s appt with Dr. %s is delayed, we are behind schedule about %s minutes, reply yes to receive a call within 30 mins to reschedule."

logger = logging.getLogger(settings.MEDHACK_LOG)

account_sid = "ACa3fdc1411eb36335de167012d401da08"
auth_token = "1473ab34f368354265cd552b7977e251"
twilio_number = +12025172570
hanke = "+17035319189"

twilio_client = TwilioRestClient(account_sid, auth_token)


class TwilioClient(object):

    def alert_daily(self, appointments):

        for appointment in appointments:
            start_time = TZ.normalize(appointment.end_time).strftime("%I:%M %p")
            dr_lastname = appointment.calendar.doctor.last_name

            logger.info("Alerting %s: %s %s: %s" % (appointment.id, appointment.patient.first_name, appointment.patient.last_name, start_time))
            msg = DAILY_MSG % (dr_lastname, start_time, )

            logger.info(msg)

            if settings.SEND_TWILIO:
                twilio_client.sms.messages.create(body=msg, to=hanke, from_=twilio_number)

    def alert_status(self, appointment, minutes_behind):
        start_time = TZ.normalize(appointment.end_time).strftime("%I:%M %p")
        dr_lastname = appointment.calendar.doctor.last_name

        msg = ALERT_MSG % (start_time, dr_lastname, minutes_behind)

        logger.info(msg)

        if settings.SEND_TWILIO:
            twilio_client.sms.messages.create(body=msg, to=hanke, from_=twilio_number)
