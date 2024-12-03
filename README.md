# EllipticCurveTool 
# A tool for elliptic curve visualization and computation (for python course project of HSE)

1. Структура программы
Эта программа реализует нормализацию эллиптической кривой и вычисление таких математических параметров, как структура группы, функция j, инварианты и другие характеристики, связанные с эллиптическими кривыми.
Программа визуализирует эти характеристики с помощью графиков и символических вычислений, а также выполняет вычисления, такие как порядок точки и описание алгебраических свойств кривой.
2. Используемые библиотеки
SymPy: библиотека Python для символических вычислений и алгебры. Используется для символического решения уравнений и выполнения алгебраических операций.
Matplotlib: библиотека для создания графиков и визуализации данных. Используется для построения графиков эллиптических кривых.
NumPy: библиотека для численных вычислений. В основном используется для работы с массивами и матрицами.
3. Функции программы
Нормализация эллиптической кривой: преобразует уравнение эллиптической кривой в стандартную форму.
Вычисление структуры группы: предоставляет порядок группы точек на эллиптической кривой.
Вычисление функции j: функция j эллиптической кривой описывает её автоморфные свойства.
///////////////////////////////////////////////////

1 Program Structure
This program implements the normalization of elliptic curves and calculates mathematical parameters related to the elliptic curve, such as group structure, j-function, invariants, and others.
It visualizes these characteristics through graphical representation and symbolic computation, also performing calculations such as point order and describing the curve's algebraic properties.
2 Libraries Used
SymPy: A Python library for symbolic mathematics and algebra. It is used for symbolic equation solving and performing algebraic operations.
Matplotlib: A library for creating graphs and visualizing data. It is used to plot elliptic curve graphs.
NumPy: A library for numerical computations. It is mainly used for working with arrays and matrices.
3 Program Features
Normalization of Elliptic Curve: Converts the elliptic curve equation into standard form.
Group Structure Calculation: Provides the order of the group of points on the elliptic curve.
j-function Calculation: The j-function of the elliptic curve describes its automorphic properties.
//////////////////////////////////////////////////

Elliptic Curve Tool
Overview
Elliptic curves are a class of algebraic curves that are important in mathematics, cryptography, and number theory. This project implements a tool to help users visualize and compute the standard form of elliptic curves, group structure, j-function, derivatives, and more.

Introduction to Elliptic Curves
An elliptic curve is defined by the equation:
y^2 = x^3 + ax + b

where a and b are constants, and x and y are variables. To ensure the curve has no singular points, the parameters a and b must satisfy the condition:
4a^3 + 27b^2 != 0

Basic Properties of Elliptic Curves
Group Structure: The points on an elliptic curve form an additive group, meaning that the operation of point addition is defined. Given two points P and Q, their sum P + Q can be computed.

Identity Element: The identity element is the point at infinity, denoted as O, and it acts as the neutral element in the addition operation.

j-function: The j-function is an invariant of the elliptic curve, computed by the formula:
j = 1728 * (4a^3) / (4a^3 + 27b^2)
This function helps determine if two elliptic curves are isomorphic.

Derivatives: The derivatives of the curve are used for advanced mathematical and cryptographic computations.

User Input Parameters
Users are required to input the following parameters:

Parameter a: Defines the shape of the curve.
Parameter b: Affects the curve's shape.
Users can also input points P and Q for point addition computation.

///////////////////////////////////////////////////////
///////////////////////////////////////////////////////
Инструмент для эллиптических кривых
Обзор
Эллиптические кривые — это тип алгебраических кривых, которые играют важную роль в математике, криптографии и теории чисел. В этом проекте представлен инструмент, который помогает визуализировать и вычислять стандартную форму эллиптической кривой, структуру группы, функцию 
𝑗
j, а также ее производные.

Введение в эллиптические кривые
Эллиптическая кривая определяется уравнением:
y^2 = x^3 + ax + b

где a и b — это константы, а x и y — переменные. Чтобы кривая не имела сингулярных точек, параметры a и b должны удовлетворять условию:
4a^3 + 27b^2 != 0

Основные свойства эллиптической кривой
Структура группы: Точки на эллиптической кривой образуют аддитивную группу, что означает, что можно определять операцию сложения точек. Для двух точек P и Q существует операция сложения P + Q, которая вычисляется.

Единичный элемент: Единичным элементом является точка на бесконечности, обычно обозначаемая как O, которая является нейтральным элементом при операции сложения.

Функция 𝑗
j: Функция 𝑗
j является инвариантом эллиптической кривой, вычисляется по формуле:
j = 1728 * (4a^3) / (4a^3 + 27b^2)

Эта функция помогает определить, эквивалентна ли данная кривая другой.

Производные: Производные кривой используются для вычислений в математике и криптографии.

Входные параметры
Пользователи вводят следующие параметры:

Параметр a: определяет форму кривой.
Параметр b: влияет на форму кривой.
Пользователи также могут вводить точки P и Q для вычисления суммы точек.
