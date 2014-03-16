import sys

def getTeam(line):
	line.strip();
	team = [];
	entries = line.split(",");
	team.append(entries[0]);

	for i in range(5, len(entries)):
		team.append(entries[i]);
	return team;


if(len(sys.argv) < 3):
	print "Missing input";
	sys.exit()

iname = sys.argv[1]
oname = sys.argv[2]
i = open(iname, 'r')
o = open(oname, 'w')
i.readline();
for line in i:
	team = getTeam(line)
	for n in team:
		o.write(n);
		o.write('\n');

i.close(); o.close();




