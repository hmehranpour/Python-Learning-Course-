new_text_1 = "i am hamid mehranpour i  am a civil engineer"
method_1 = new_text_1.split()
print('split : ', method_1)
print('index of split : ', method_1[1:3])
#
new_text_2 = "i,am,hamid,mehranpour,i,am,a,civil,engineer"
method_2 = new_text_2.split(',')
print('split', method_2)
print('index of split : ', method_2[1:4])
#
new_text_3 = "i=+am=+hamid=+mehranpour=+i=+am=+a=+civil=+engineer"
method_3 = new_text_3.split('=+')
print('split', method_3)
print('index of split : ', method_3[1:5])

#
method_4 = new_text_1.replace('hamid', 'ali')
print('replace : ', "\n", new_text_1, '\n', method_4)
