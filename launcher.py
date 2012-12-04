import os,re,subprocess

# launcher config
username = "MrTander"
minecraft_dir = os.environ['APPDATA']+"/.minecraft"

# launcher code
p = re.compile("^minecraft.*\.jar$")
i = 0
jarfile = {}

for x in os.listdir(minecraft_dir +'/bin/'):
	if p.search(x) != None:
		print(str(i) + ': ' + x)
		jarfile[i] = x;
		i += 1

selected_number = int(input('\nSelect number of the file: '))
selected_file = jarfile[selected_number]

subprocess.Popen(['java', '-Xmx1024m', '-Djava.library.path=' + minecraft_dir + '/bin/natives', '-cp', '' + minecraft_dir + '/bin/'+selected_file+';' + minecraft_dir + '/bin/jinput.jar;' + minecraft_dir + '/bin/lwjgl.jar;' + minecraft_dir + '/bin/lwjgl_util.jar', 'net.minecraft.client.Minecraft', username],creationflags=8)