from datetime import datetime

from engine.sternman_engine import SternmanEngine


class Palindrome(SternmanEngine):
    def needs_service(self):
        start_date = self.last_service_date
        end_date = start_date.replace(year=start_date.year + 4)

        while start_date < end_date:
            mid_date = (start_date + end_date) // 2

            if self.engine_should_be_serviced(mid_date):
               return True
            elif mid_date < datetime.today().date():
                start_date = mid_date + 1
            else:
                end_date = mid_date - 1

        return False