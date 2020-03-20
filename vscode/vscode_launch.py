# $language = "python"
# $interface = "1.0"

class State:
	timout = 2
	vscode_start = "/repo2/jiangusu/devkit/vscode/vscode start p=10086\n"
	vscode_echo = "/repo2/jiangusu/devkit/vscode/vscode echo\n"
	vscode_login = "/repo2/jiangusu/devkit/vscode/vscode login\n"
	vscode_set = "/repo2/jiangusu/devkit/vscode/vscode set\n"
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
	objTab.Screen.WaitForStrings("*:/home/coder/project#", 2)

	objTab.Screen.Send("export src=/repo2/jiangusu/devkit/vscode/\n")
	objTab.Screen.Send("export dst=/root//.local/share/code-server/\n")
#	objTab.Screen.Send("cd /home/jiangusu/work/devkit/vscode/\n")
	objTab.Screen.Send("mkdir -p $dst/User/\n")
	objTab.Screen.Send("mkdir -p $dst/extensions/\n")
	objTab.Screen.Send("cp -f $src/settings.json $dst/User/\n")
	objTab.Screen.Send("cp -f $src/keybindings.json $dst/User/\n")
	objTab.Screen.Send("tar xzf $src/hg_dts_mips_markdown.tar.gz -C $dst/extensions/\n")
	objTab.Screen.Send("tar xzf $src/python.tar.gz -C $dst/extensions/\n")
	objTab.Screen.Send("tar xzf $src/cpp_go_json.tar.gz -C $dst/extensions/\n")
	objTab.Screen.Send("tar xzf $src/make.tar.gz -C $dst/extensions/\n")
	objTab.Screen.Send("exit\n")
	objTab.Screen.WaitForStrings("exit", 20)

	objTab.Screen.Send(state.vscode_echo)

Main()
