
#################################################################
#### Function ###################################################
# 1- Parametresiz Returnsuz Function
def hesap_topla1():
    """
    parametresiz Returnsuz function
    """
    sayi1=10
    sayi2=20
    sayi3=sayi1+sayi2
    print(f"toplam1 :{sayi3}")

# Function Calling
hesap_topla1()

#################################################################

# 2- Parametreli Returnsuz Function
def hesap_topla2(sayi1,sayi2):
    """
    parametreli Returnsuz function
    """
    sayi3=sayi1+sayi2
    print(f"toplam2 :{sayi3}")

# Function Calling
hesap_topla2(10,20)

#################################################################
# Default değerler
def hesap_topla222(sayi1,sayi2=90):
    """
    parametreli Returnsuz function
    """
    sayi3=sayi1+sayi2
    print(f"toplam222 :{sayi3}")

# Function Calling
# hesap_topla3(10)  # default değer çalışır
hesap_topla222(10,20)


#######################################################
# 3- Parametresiz Returnlu Function
def hesap_topla3():
    """
    parametresiz Returnlu function
    """
    sayi1=10
    sayi2=20
    sayi3=sayi1+sayi2
    return sayi3

# Function Calling
result3=hesap_topla3()
print(f"toplam3: {result3}")


#######################################################
# 4- Parametreli Returnlu Function
def hesap_topla4(sayi1=40,sayi2=60):
    """
    parametreli Returnlu, default değerli function
    :return:
    """
    sayi3=sayi1+sayi2
    return sayi3

# Function Calling
result4=hesap_topla4(10,20)
print(f"toplam4: {result4}")


#######################################################
# 5- Global/local variable
global_variable=99

def hesap_topla5():
    global global_variable
    print(global_variable)

    local_variable=11
    print(local_variable)

# Function Calling
hesap_topla5()

print(f"{global_variable}")
# print(f"{local_variable}")