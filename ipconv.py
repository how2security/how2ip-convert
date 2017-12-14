#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Wellington Silva a.k.a. Well
Date: November 2017
Name: ipconv.py
Purpose: Criate data encoded with varius type encode.
Description: Script Based on article by Ygor Rocha in H2HC Magazine 12º Edition and 14º Edition H2HC Conference, posted at:
                	<http://www.h2hc.com.br/revista/RevistaH2HC_12.pdf>
	     I also got some tips from Synetech on the Superuser site, pusted at:
			<https://superuser.com/questions/486788/why-does-pinging-192-168-072-only-2-dots-return-a-response-from-192-168-0-58>
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

import sys
sys.path.append('.lib')
import argparse
from colors import *
from how2libipc import *

   
def main():
    
    usage = '''%(prog)s [-a ipv4_addr]'''
    
    parser = argparse.ArgumentParser(usage=usage)
    
    parser.add_argument( '-a', '--addr', action='store', type=str, default='127.0.0.1', dest='ipv4', help='IP Address to be converted')
    parser.add_argument("--version", action="version", version="%(prog)s 1.0b")
    
    args = parser.parse_args()
    
    ipv4 = args.ipv4
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    '''
      Para entendermos como funciona o utilitário ping basta executamos alguns testes.
	  
	  por exemplo:
	  
	  > ping 1		-->		pinging 0.0.0.1
	  > ping 1.2		-->		pinging 1.0.0.2
	  > ping 1.2.3		-->		pinging 1.2.0.3
	  > ping 1.2.3.4	-->		pinging 1.2.3.4
	  > ping 256		-->		pinging 0.0.1.0
	  
	  Como podemos ver, podemos omitir a parte com zero nos octetos menos significativos (com exceção ao primeiro exemplo).
	  No último exemplo podemos observar que ele interpretou o valor 256 como 0.0.1.0, isso porque, 256 é igual a 1.00000000
	  em binário (e o valor máximo para um octeto é 255), que se convertemos noavamente para decimal cada octeto equivale a 
	  1.0 e dai foi só ele complementar os octetos mais significativos com 0s.
	  
	  O utilitário ping é poliglota e aceita diversos outros formatos, tais como:
	  .	Hexadecimal (com pontos ou sem pontos) --> bastando colocar o prefixo 0x em cada octeto ou pegando o valor total em decimal e convertendo para hexadecimal direto necessitando neste caso apenas do prefixo 0x no início; 
	  .	Octal (com ou sem pontos) --> bastando colocar o prefixo 0 (zero) na frente de cada octeto ou pegando o valor total em decimal e convertendo para octal direto necessitando neste caso apenas do prefixo 0 (zero) no início;
	  .	Decimal (com ou sem pontos) --> e por fim temos a soma de todos os bits 1 elevado pela sua posição e base 2.
	  .	Ainda podemos combinar os octetos passando decimal, hexadecimal e octal.
	  
	  Veja os exemplos feito no endereço do Google:
	  
	  google.com          => (domain name)
      172.217.29.238      => (dotted decimal)
      1249763844          => (flat decimal)
      0254.0331.0035.0356 => (dotted octal)
      025466216756        => (flat octal)
      0xAC.0xD9.0x1D.0xEE => (dotted hex)
      0xACD91DEE          => (flat hex)
      172.0331.0x1D.238   => (ಠ_ಠ)
      
      Estes não respondem pois não é interpretado pelo ping
      10101100110110010001110111101110 => (flat binary)
      10101100.11011001.00011101.11101110 => (dotted binary)
	  
	  Qualquer caracter diferente dos aceitos resulturá em uma tentativa de resolver o endereço passado como se fosse o nome de dominio.
	  
	  Observação: Embora o utilitário ping interprete diversos formatos para representar um endereço IPv4, isso não significa necessariamente que você possa usar em todos os lugares. Alguns programas podem forçar a fornecer os 4 octetos em dicimal, outros podem aceitar porém em um único formato e não permite misturá-los.
	  
	  Gostei do fim da explanação do Synetech, que diz:
	  "Oh well, I guess that’s what you get for not being fluent in multiple number-bases... there are 10 types of people: those who know binary and those who don’t."
	  
	  "Bem, acho que é isso que você recebe quando não é fluente em várias bases de números... Existem 10 tipos de pessoas: as que conhecem binário e as que não comnhece" :-)
    '''
	
    try:
      #for i in ipv4.split('.'):
      #    ip_bin += str(d2b(int(i)))
      ip_bin = [str(d2b(int(i))) for i in ipv4.split('.')]
      ip_bin = ''.join(ip_bin)
      
      #for i in ipv4.split('.'):
      #    ip_oct += str(b2o(int(i))) + '.'
      ip_oct = [str(b2o(int(i))) for i in ipv4.split('.')]
      ip_oct = '.'.join(ip_oct)
      
      #for i in ipv4.split('.'):
      #    ip_hex += str(d2h(int(i))) + '.'
      ip_hex = [str(d2h(int(i))) for i in ipv4.split('.')]
      ip_hex = '.'.join(ip_hex)
      
      ip_bin = int(ip_bin)
      ip_dec = b2d(ip_bin)
      
      ip_oct_f = b2o(ip_dec)
      ip_hex_f = d2h(ip_dec)
      
      print(color("IP Address IPv4 (dotted decimal)\t => ", 2, 1) + "%s" % ipv4)    
      print(color("IP Address in Binary\t\t\t => ", 3, 1) + "%s" % ip_bin)
      print(color("IP Address in Octal (dotted octal)\t => ", 2, 1) + "%s" % ip_oct)
      print(color("IP Address in Octal (flat octal)\t => ", 2, 1) + "0%s" % ip_oct_f)
      print(color("IP Address in Hexadecimal (dotted hex)\t => ", 2, 1) + "%s" % ip_hex)
      print(color("IP Address in Hexadecimal (flat hex)\t => ", 2, 1) + "%s" % ip_hex_f)
      print(color("IP Address in Decimal (flat decimal)\t => ", 2, 1) + "%s" % ip_dec)
     
      '''
        Estes são necessários caso utilizemos os for para fazer o loop.
        Pois no final do loop anexamos um ponto (.) após o retorno
        da função
      '''
     #print("IP Address in Octal\t\t => %s" % ip_oct[:-1])
     #print("IP Address in Hexadecimal\t => %s" % ip_hex[:-1])
   
    except AttributeError:
        print(color("\n[!] This data is not valid", 1, 1))
        parser.print_help()
        sys.exit(1)
    except TypeError:
        print(color("\n[!] This data non base[16|32|64]", 1, 1))
        parser.print_help()
        sys.exit(1)
    except ValueError:
        print(color("\n[!] This data is not valid", 1, 1))
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
