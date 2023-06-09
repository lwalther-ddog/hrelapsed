from datetime import datetime
from datadog_checks.base import AgentCheck

__version__= "1.0.4"

class MyClass(AgentCheck):
    def check(self, instance):
      
      now = datetime.now()
      hours_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()/3600
      hours_since_bom = (now - now.replace(month=now.month,day=1,hour=0, minute=0, second=0, microsecond=0)).total_seconds()/3600
      hours_since_boy = (now - now.replace(month=1,day=1,hour=0, minute=0, second=0, microsecond=0)).total_seconds()/3600
      self.gauge('hrelapsed.day',hours_since_midnight,tags=["hour_meter:daily"])
      self.gauge('hrelapsed.bom',hours_since_bom,tags=["hour_meter:bom"])
      self.gauge('hrelapsed.boy',hours_since_boy,tags=["hour_meter:boy"])
      
