import qrcode
import PySimpleGUI as sg
import os

def deletefiles(counter):
    for num in range(counter):
        if os.path.exists(f"link_{num}.png"):
            os.remove(f"link_{num}.png")
        else:
            print("File does not exsist")
            
counter = 0


layout = [  [sg.Text("Enter a website link to recivie a QR Code."), sg.InputText(key='-LINK-')],
            [sg.Button("Submit"), sg.Button("Cancel")],
            [sg.Image(filename='Sunny_GitHub.png', key='-IMAGE-')]]
        

window = sg.Window("QR Code Generator", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        deletefiles(counter)
        break
    elif event == 'Submit':
        qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
        link = values['-LINK-']
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color = 'black', back_color = 'white')
        img.save(f'link_{counter}.png')
        window['-IMAGE-'].update(filename='')
        print('Image cleared')
        window.refresh()
        window['-IMAGE-'].update(filename=f"link_{counter}.png")
        print('Image added')
        counter = counter + 1
        print("Counter added")
        
window.close()
