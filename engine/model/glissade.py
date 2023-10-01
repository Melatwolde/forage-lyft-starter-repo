from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine

def needs_service(self):
    for service_year in range(self.last_service_date.year, self.last_service_date.year + 3):
        for service_month in range(1, 13):
            for service_day in range(1, 32):
                service_date = datetime(service_year, service_month, service_day)
                if service_date <= datetime.today().date() and self.engine_should_be_serviced(service_date):
                    return True
    return False
