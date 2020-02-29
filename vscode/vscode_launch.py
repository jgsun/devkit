# $language = "python"
# $interface = "1.0"

class State:
	timout = 2
	vscode_start = "vscode start p=10086\n"
	vscode_echo = "vscode echo\n"
	vscode_login = "vscode login\n"
	vscode_set = "vscode set\n"
	keep_typing = "\n"

def Main():
	objTab = crt.GetScriptTab()
	objTab.Screen.Synchronous = True
	objTab.Screen.IgnoreEscape = True
	state = State()

	objTab.Screen.Send(state.vscode_start)
	objTab.Screen.WaitForStrings("*:/home/coder/project#", 1)

	objTab.Screen.Send(state.vscode_set)
	objTab.Screen.WaitForStrings("*:/home/coder/project#", 1)

	objTab.Screen.Send(state.vscode_login)
	objTab.Screen.WaitForStrings("*:/home/coder/project#", 1)

	objTab.Screen.Send("cd /home/jiangusu/work/devkit/vscode/\n")
	objTab.Screen.Send("mkdir -p /root/.local/share/code-server/User/\n")
	objTab.Screen.Send("cp -f settings.json /root/.local/share/code-server/User/\n")
	objTab.Screen.Send("cp -f keybindings.json /root/.local/share/code-server/User/\n")
	objTab.Screen.Send("tar xzf hg_dts_mips_markdown.tar.gz -C /root/.local/share/code-server/extensions/\n")
	objTab.Screen.Send("tar xzf python.tar.gz -C /root/.local/share/code-server/extensions/\n")
	objTab.Screen.Send("tar xzf cpp_go_json.tar.gz -C /root/.local/share/code-server/extensions/\n")
	objTab.Screen.Send("exit\n")
	objTab.Screen.WaitForStrings("exit", 20)

	objTab.Screen.Send(state.vscode_echo)

Main()
