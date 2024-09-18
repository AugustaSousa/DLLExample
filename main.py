import ctypes

dll = ctypes.CDLL("dll-atividade/x64/Debug/dll-atividade.dll")

dll.somar.argtypes = (ctypes.c_double, ctypes.c_double)
#dll.somar.restype = ctypes.c_double
dll.somar(5,5)

dll.subtrair.argtypes = (ctypes.c_double, ctypes.c_double)
#dll.subtrair.restype = ctypes.c_double
dll.subtrair(1,9)

dll.multiplicar.argtypes = (ctypes.c_double, ctypes.c_double)
#dll.multiplicar.restype = ctypes.c_double
dll.multiplicar(4,50)

dll.dividir.argtypes = (ctypes.c_double, ctypes.c_double)
#dll.dividir.restype = ctypes.c_double
dll.dividir(28,3)

#Estava tentando passar uma array, não finalizado
#dll.ordenar.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
#dll.ordenar.restype = None
#v = [1,9,8,6,3]
#v1 = (ctypes.c_int*len(v))(*v)
#dll.ordenar(v1, len(v))
#v2 = list(v1)
#print(v2)