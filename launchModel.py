import model.virusModel as vm

model = vm.VirusModel()

days = 6
for day in range(1,days+1):
    print('Day '+ str(day))
    model.step()
