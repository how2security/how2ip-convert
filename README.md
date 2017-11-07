# how2ip-convert #

Estes scripts foram criados inspirado no artigo do Ygor Rocha (@dmr) publicado na Revista H2HC 12ª Edição da 14ª Edição da Conferência da H2HC de 2017. Aonde o Ygor explica como podemos utilizar outras formas de representar um endereço IPv4 baseado no filme A Rede (The Net) com a Sandra Bullock no papel de Angela Bennett como uma consultora de segurança (hacker) pesquisando o endereço IPv4 23.75.345.200.

Além disso, utilizei no help desse script uma explicação do Synetech no site Superuser sobre a duvida de um usuário que aparentemente colocou um 0 (zero) no início de um octeto e como em um passe de mágica ele traduziu o erro e tentou "pingar" um endereço IP com o final diferente do que ele queria.

Vou colocar uma tradução livre da resposta do Synetech:

Para entendermos como funciona o utilitário ping basta executamos alguns testes.
	  
por exemplo:


	$ ping 1			-->		pinging 0.0.0.1
	$ ping 1.2			-->		pinging 1.0.0.2
	$ ping 1.2.3			-->		pinging 1.2.0.3
	$ ping 1.2.3.4			-->		pinging 1.2.3.4
	$ ping 256			-->		pinging 0.0.1.0

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

Espero que gostem do script.

# Uso #

    ./ipconv.py -h
	
	usage: ipv4.py [-a ipv4_addr]
	
	optional arguments:
	-h, --help            show this help message and exit
	-a IPV4, --addr IPV4  IP Address to be converted
	--version             Show program's version number and exit
	
    ./ipconv.py -a 172.217.29.238
	
	IP Address IPv4 (dotted decimal)         => 172.217.29.238
	IP Address in Binary                     => 10101100110110010001110111101110
	IP Address in Octal (dotted octal)       => 0254.0331.0035.0356
	IP Address in Octal (flat octal)         => 025466216756
	IP Address in Hexadecimal (dotted hex)   => 0xAC.0xD9.0x1D.0xEE
	IP Address in Hexadecimal (flat hex)     => 0xACD91DEE
	IP Address in Decimal (flat decimal)     => 2899910126

# Licença #

Author: Wellington Silva a.k.a. Well

Date: July 2017

Version: 1.0B

Licence: GNU3
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

More details: <http://www.how2security.com.br>
