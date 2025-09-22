""" Vérifier si un mot ou une phrase est un palindrome ou pas"""

#### Fonction secondaire

def clean (x):
    """Enlever espace, accent et majuscule"""
    x = x.replace(" ","")
    x = x.replace(",","")
    x = x.replace ("'","")
    x = x.replace("-","")
    x = x.replace(":","")
    x = x.replace("?","")
    x = x.replace("!","")
    x = x.replace("é","e")
    x = x.replace("è","e")
    x = x.replace("ë","e")
    x = x.replace("ê","e")
    x = x.replace("ô","o")
    x = x.replace("à","a")
    x = x.replace("ù","u")
    x = x.replace("û","u")
    x = x.replace("ç","c")
    x = x.replace ("É","e")
    x = x.replace ("À","a")
    x = x.lower()
    return x


def ispalindrome(s):
    """ 
    Vérifier si une chaine de caractère est un palindrome ou pas.
    Args :
        s : chaine de caractère
    Returns :
        booléens qui dit si s est un palindrome ou non
    """
    x = clean(s)
    n = len(x)
    if n % 2 == 0:
        for i in range (n):
            if x[i] != x[n-i-1]:
                return False
    else:
        m = int(((n -1)/2) +1)
        for i in range (m):
            if x[i] != x[n-i-1]:
                return False
    return True

#### Fonction principale


def main():
    """test la fonction"""

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
