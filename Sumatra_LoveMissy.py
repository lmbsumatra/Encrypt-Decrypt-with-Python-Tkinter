# Encrpyt - Decrypt GUI version
# Love Missy B. Sumatra
# BSIT - 2CD - NS

from tkinter import *
from random import randint
import random
import pyperclip

# creating dictionary, code : character #
code_values = {}
values = ''
key = ['Ba', 'Be', 'Bi', 'Bo', 'Bu', 'Ca', 'Ce', 'Ci', 'Co', 'Cu', 'Da', 'De', 'Di', 'Do', 'Du', 'Fa', 'Fe', 'Fi', 'Fo', 'Fu', 'Ga', 'Ge', 'Gi', 'Go', 'Gu', 'Ha', 'He', 'Hi', 'Ho', 'Hu', 'Ja', 'Je', 'Ji', 'Jo', 'Ju', 'Ka', 'Ke', 'Ki', 'Ko', 'Ku', 'La', 'Le', 'Li', 'Lo', 'Lu', 'Ma', 'Me', 'Mi', 'Mo', 'Mu', 'Na', 'Ne', 'Ni', 'No', 'Nu', 'Pa', 'Pe', 'Pi', 'Po', 'Pu', 'Qa', 'Qe', 'Qi', 'Qo', 'Qu', 'Ra', 'Re', 'Ri', 'Ro', 'Ru', 'Sa', 'Se', 'Si', 'So', 'Su', 'Ta', 'Te', 'Ti', 'To', 'Tu', 'Va', 'Ve', 'Vi', 'Vo', 'Vu', 'Wa', 'We', 'Wi', 'Wo', 'Wu', 'Xa', 'Xe', 'Xi', 'Xo', 'Xu', 'Ya', 'Ye', 'Yi', 'Yo', 'Yu', 'Za', 'Ze', 'Zi', 'Zo', 'Zu', 'Ay', 'By', 'Cy', 'Dy', 'Ey', 'Fy', 'Gy', 'Hy', 'Iy', 'Jy', 'Ky', 'Ly', 'My', 'Ny', 'Oy', 'Py', 'Qy', 'Ry', 'Sy', 'Ty', 'Uy', 'Vy', 'Wy', 'Xy', 'Zy']
for i in range(128):
    values += (chr(i))

for i in range(len(values)):
    code_values[key[i]] = values[i]
    
# creating code word #
word_list = ["abuse", "adult","agent","anger","apple","award","basis","beach","birth", "block","blood","board","brain","bread","break","brown","buyer","cause", "chain","chair","chest","chief","child","china","claim","class","clock", "coach","coast","court","cover","cream","crime","cross","crowd","crown", "cycle","dance","death","depth","doubt","draft","drama","dream","dress", "drink","drive","earth","enemy","entry","error","event","faith","fault", "field","fight","final","floor","focus","force","frame","frank","front", "fruit","glass","grant","grass","green","group","guide","heart","henry", "horse","hotel","house","image","index","input","issue","japan","jones", "judge","knife","laura","layer","level","lewis","light","limit","lunch", "major","march","match","metal","model","money","month","motor","mouth", "music","night","noise","north","novel","nurse","offer","order","other", "owner","panel","paper","party","peace","peter","phase","phone","piece", "pilot","pitch","place","plane","plant","plate","point","pound","power", "press","price","pride","prize","proof","queen","radio","range","ratio", "reply","right","river","round","route","rugby","scale","scene","scope", "score","sense","shape","share","sheep","sheet","shift","shirt","shock", "sight","simon","skill","sleep","smile","smith","smoke","sound","south", "space","speed","spite","sport","squad","staff","stage","start","state", "steam","steel","stock","stone","store","study","stuff","style","sugar", "table","taste","terry","theme","thing","title","total","touch","tower", "track","trade","train","trend","trial","trust","truth","uncle","union", "unity","value","video","visit","voice","waste","watch","water","while", "white","whole","woman","world","youth"]

encrypt_bank = []
global data

class Window(Frame):

    def __init__(self):

        # window
        Frame.__init__(self)
        self.master.title("Encrypt - Decrypt")
        self.pack(pady = 10, padx = 10, )
        
        # enter text label
        self.EnterLbl = Label(self, text = "Enter a text...", font = ("Century Gothic", 12))
        self.EnterLbl.grid(row = 0, column = 0, sticky = 'w')

        # copy button
        self.EncryptBtn= Button(self, text = "Copy", font = ("Century Gothic", 8), command = self.copy, bg = '#A9A9A9', fg = 'white', borderwidth = 0)
        self.EncryptBtn.grid(row = 0, column = 1, ipadx = 10, pady = 10, sticky = 'e')

        # input box
        self.InputTxt = Text(self, width = 35, height = 10)
        self.InputTxt.focus()
        self.InputTxt.grid(row = 1, columnspan = 2, sticky = 'w', pady = 5)

        # encrypt button
        self.EncryptBtn= Button(self, text = "Encrypt", font = ("Century Gothic", 12), command = self.encryptFunc, bg = '#FF5733', fg = 'white', borderwidth = 0)
        self.EncryptBtn.grid(row = 2, column = 0, ipadx = 27, pady = 10)

        # decrypt button
        self.DecryptBtn = Button(self, text = "Decrypt", font = ("Century Gothic", 12), command = self.decryptFunc, bg = '#50C878', fg = 'white', borderwidth = 0)
        self.DecryptBtn.grid(row = 2, column = 1, ipadx = 27, pady = 10)

        # clear button
        self.ClearBtn = Button(self, text = "Clear", font = ("Century Gothic", 12), command = self.clear, bg = '#A9A9A9', fg = 'white', borderwidth = 0)
        self.ClearBtn.grid(row = 3, column = 0, columnspan = 2, ipadx = 110, pady = 5)

    # # # # # # # # # # copy text # # # # # # # # # #  
    def copy(self): 
        global data 
        data = self.InputTxt.get("1.0",'end-1c')
        pyperclip.copy(data)

    # # # # # # # # # # encrypt text # # # # # # # # # #   
    def encryptFunc(self):
        input_word = self.InputTxt.get("1.0",'end-1c')

        global encrypt_bank
        if(len(encrypt_bank)):
            encrypt_bank = []
            
        self.InputTxt.delete("1.0",'end-1c')

        code_word = ''
        for a in range(len(input_word)):
            word = random.choice(word_list) 
            dis_word = random.sample(word, len(word)) 
            pos = random.choice(word) 

            for x in dis_word:
                if x == pos:
                    index = dis_word.index(pos) 
                    code_word = dis_word[0:index] 

            for key, values in code_values.items():
                if values == input_word[a]:
                    string = key

            code_word.append(string)    
            code_word += (dis_word[index:])
            new_word = ''.join(code_word)
            encrypt_bank.append(new_word)
        # print("Code: ", end = '')    
        # print(' '.join(encrypt_bank))

        self.InputTxt.insert('end', encrypt_bank)

    # # # # # # # # # # decrypt text # # # # # # # # # #
    def decryptFunc(self):
        decode_list = []
        code = ''
        decode_word = ''
        encrypt_bank = self.InputTxt.get("1.0",'end-1c')
        self.InputTxt.delete("1.0",'end-1c')
        
        input_word = encrypt_bank

        for j in range(len(input_word)):
            if input_word[j].isupper():  
                code = input_word[j] + input_word[j+1] 
                decode_list.append(code) 
  
        for code in range(len(decode_list)):
            for key, values in code_values.items():
                if key == decode_list[code]:
                    decode_word += values
        # print("Decode: " + decode_word)

        self.InputTxt.insert('end', decode_word)

    # # # # # # # # # # clear text # # # # # # # # # #
    def clear(self):
        self.InputTxt.delete("1.0",'end-1c')


def main():
    Window().mainloop()

main() 
