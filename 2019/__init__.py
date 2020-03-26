import check50
import check50.c
import filecmp

@check50.check()
def exists():
    """U1.c egzistuoja"""
    check50.exists("U1.c")
    check50.include("1.txt", "2.txt")

@check50.check(exists)
def compiles():
    """U1.c kompiliuojasi"""
    check50.c.compile("U1.c", lcs50=True)

#bandymas patikrinti ar .cpp file'as kompiliuojasi
# bet neveikia: error: invalid argument '-std=c11' not allowed with 'C++'
#@check50.check(exists)
#def compiles1():
#    """testU1.cpp kompiliuojasi"""
#    check50.c.compile("testU1.cpp", lcs50=True)

# bandymas paleisti sukompiliuota .cpp file'ą, bet nesigauna.
#@check50.check(compiles)
#def testingCPP():
#    """Ar pasileidžia sukompiliuotas CPP file'as"""
#    out = check50.run("./testU1").stdin("1").stdout()
#    out = check50.run("./testU1").stdout()
#    compare_values(out, open("2.txt").read())
#    check50.run("./testU1").stdout(1)
    
@check50.check(exists)
def isOutput():
    """Rastas U1rez.txt"""
    check50.exists("U1rez.txt")
    
@check50.check(exists)    
def read_first_file_line(exists):
    """Ar teisingai apskaičiuoja pripiltų indų ir likusio aliejaus skaičius?"""
    compare_files(open("U1rez.txt").readline(), open("1.txt").readline())
    
@check50.check(compiles)
def test1():
    """Tikrina užduoties "Aliejus" korektišką atlikimą"""
#    out = check50.run("./U1 U1rez.txt").stdin("8").stdout()
#    compare_files(out, open("1.txt").read())
    compare_files(open("U1rez.txt").read(), open("1.txt").read())

def compare_files(output, correct):
    if output == correct:
        return 
    raise check50.Mismatch(correct, output, help= None)


    
# Skirta .cpp output patikrinimui
#def compare_values(output, correct):
#    if output == correct:
#        return 
#    raise check50.Mismatch(correct, output, help= None)
