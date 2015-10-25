import win32serviceutil
import win32service
import win32event
import os
import sys
import time

sys.stopservice = "false"
def main():
	sys.path.insert(0,os.getcwd())
	import service_module
	a = service_module.service_test()
class ServiceLauncher(win32serviceutil.ServiceFramework):
	_svc_name_ = 'ServiceTest'
	_scv_display_name_ ='ServiceTesting'
	def __init__(self, args):
		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

	def SvcStop(self):
		sys.stopservice = "true"
		win32event.SetEvent(self.hWaitStop)

	def SvcDoRun(self):
		main()
