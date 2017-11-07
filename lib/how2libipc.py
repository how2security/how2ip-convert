#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: November 2017
Name: how2libipc.py
Purpose: Criate data encoded with varius type encode.
Description: Script Based on article by Ygor Rocha in H2HC Magazine 12º Edition and 14º Edition H2HC Conference, posted at:
                     <http://www.h2hc.com.br/revista/RevistaH2HC_12.pdf>
Version: 1.0B
Licence: GPLv3
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.

Other itens: Copyright (c) 2017, How2Security All rights reserved.
'''

def d2b(ipv4):
    binario = ''

    while(True):
        binario += str(ipv4 % 2)
        ipv4 = ipv4 // 2
        if ipv4 == 0:
            break

    binario = binario[::-1]
    binario = int(binario)
    
    return ('%08i' % binario)

def b2d(ipv4):
    decimal = 0
    ipv4 = str(ipv4)
    ipv4 = ipv4[::-1]
    tam = len(ipv4)

    for i in range(tam):
        if ipv4[i] == '1':
            decimal += 2**i

    return decimal

def b2o(ipv4):
    octal = ''

    while(True):
        octal += str(ipv4 % 8)
        ipv4 = ipv4 // 8
        if ipv4 == 0:
            break
    
    octal = octal[::-1]
    octal = int(octal)

    return('%04i' % octal)

def d2h(ipv4):
    hexa = ''
    digitos = '0123456789ABCDEF'

    if ipv4 == 0:
       return '0x0'

    while ipv4 != 0:
        hexa += digitos[ipv4 % 16]
        ipv4 = ipv4 // 16

    return ('0x%s' % hexa[::-1])
