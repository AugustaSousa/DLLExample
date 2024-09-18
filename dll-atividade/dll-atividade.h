#pragma once

#ifdef DLLATIVIDADE_EXPORTS
#define DLLATIVIDADE __declspec(dllexport)
#else
#define DLLATIVIDADE __declspec(dllimport)
#endif

#include <iostream>
using namespace std;

extern "C" {
	DLLATIVIDADE void somar(double a, double b);
}

extern "C" {
	DLLATIVIDADE void subtrair(double a, double b);
}

extern "C" {
	DLLATIVIDADE void multiplicar(double a, double b);
}

extern "C" {
	DLLATIVIDADE void dividir(double a, double b);
}

//extern "C" {
//void ordenar(int* v, int tam);
//}