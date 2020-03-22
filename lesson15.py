import random as r

print("                       Բարի գալուստ 'CLEAN CAR' ավտոլվացում")
name = input('Inch e cer anun? ')
lvanal = input('uzuum eq lvanal cer meqenan, ete ayo nsheq "y", hakarak depqum "n" tar@? ') == "y"
taxamas = ('davitashen', 'masiv', 'bangladesh', 'zeytun')
choices = ("a", "k", "m", "c")
choices2 = ("b", "q", "e", "r")
choices3 = ("t", "y", "u", "i")
choices4 = ("o", "p", "s", "x")
while  True:
	if lvanal:
		print('					menq voxjunum enq mer carayutyunneric ogtvelu hamar, \n 				nshenq vor unenq 4 masnajyx - "davitashen", "masiv", "bangladesh" ev "zeytun" ')
		vortex = input(name+' vortex kcankanaq lvacnl dzer meqenan?  ')
		if vortex == 'davitashen' or vortex == 'masiv' or vortex == 'bangladesh' or vortex == 'zeytun':
			tesak = input(name+ ' xndrem nsheq cer meqenan "sedan" te "jip" e? ')
			if tesak == 'sedan':
				tesak == 500
				computer = r.choice(choices)
				computer2 = r.choice(choices2)
				computer3 = r.choice(choices3)
				computer4 = r.choice(choices4)
				print('shnorhakalutyun mez @ntrelu hamar '+ name+ ' mer '+ vortex +' masnajyuxum cer sedan meqenan karox eq lvanal 500 dramov, xndrum enq ays kod@ ogtagorcel moykayum- " '+computer+computer2+computer3+computer4+'"')
			     
			elif tesak == 'jip':
				tesak == 1000
				computer = r.choice(choices)
				computer2 = r.choice(choices2)
				computer3 = r.choice(choices3)
				computer4 = r.choice(choices4)
				print('shnorhakalutyun mez @ntrelu hamar '+name+ ' mer '+ vortex+ ' masnajyuxum cer sedan meqenan karox eq lvanal 1000 dramov, xndrum enq ays kod@ ogtagorcel moykayum- " '+computer+computer2+computer3+computer4+'"')	
                
			else:
				print('				@nterq sedan kam jip tarberak@! ')
				
		elif vortex != 'davitashen' or vortex != 'masiv' or vortex != 'bangladesh' or vortex != 'zeytun':
			print(                  name+ ' cer nshvac vayrum masnajyux chunenq')
			
	else:
		break

	break