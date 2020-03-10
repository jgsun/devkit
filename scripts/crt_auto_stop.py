# $language = "python"
# $interface = "1.0"

class State:
	loop = 0
	timout = 10
	idle = 0
	keep_typing = "\n"
	stage = "none"

def f_none(state):
	pass

def f_uboot(state):
	state.stage = "uboot"
	objTab = crt.GetScriptTab()
	objTab.Screen.Send("ftest\n")

def linux_login():
	objTab = crt.GetScriptTab()
	objTab.Screen.Send("\n")
#	ok = objTab.Screen.WaitForString("isam-reborn login:", 1)
	ok = objTab.Screen.WaitForString("shelf-ne login:", 1)
	if not ok:
		return
	objTab.Screen.Send("root\n")
	ok = objTab.Screen.WaitForString("Password:", 1)
	if not ok:
		return
	objTab.Screen.Send("2x2=4\n")

def f_linux(state):
	state.stage = "linux"
	linux_login()
	#state.keep_typing = "s6-rc -a list\n"

action_dict = {
	"ISAM:Press 'f' to enter UBOOT prompt": f_uboot,
	"Octeon cust_cfntb": f_none,
	"Welcome to ISAM reborn!": f_linux,
	"s6-rc: info: service s6rc-oneshot-runner started successfully": f_none,
	"Alarm Install end": f_none,
	"Configuring confd": f_none,
	"s6-rc: info: processing service S_confd: starting": f_none,
	"System initialized successfully.": f_none,
	#"s6-rc: warning: received TERM, aborting longrun transitions": f_reboot_force,
}

def Main():

	objTab = crt.GetScriptTab()
	objTab.Screen.Synchronous = True
	objTab.Screen.IgnoreEscape = True
	state = State()
	
	while state.stage != "stop":
#		objTab.Screen.Send(state.keep_typing)
		
		#in seconds, should be less than auto logout time
		index = objTab.Screen.WaitForStrings(action_dict.keys(), state.timout)
		#0 is time out
		if index:
			state.idle = 0
			action_dict[action_dict.keys()[index-1]](state)
		else:
			state.idle = state.idle + 1
#		if state.idle * state.timout > 60*60:
#			f_reboot_force(state)
#		state.loop = state.loop + 1


Main()
