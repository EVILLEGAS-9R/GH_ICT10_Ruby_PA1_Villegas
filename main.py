from pyscript import display, document

def check_temp(e):
    f = float(document.getElementById("fahrenheit").value)
    c = (f - 32) * 5 / 9
    c = round(c, 2)

    document.getElementById("output").innerHTML = ""

    display(c, target="output")

    if c >= 37.8:
        display("Fever", target="output")
    else:
        display("Normal temperature", target="output")
