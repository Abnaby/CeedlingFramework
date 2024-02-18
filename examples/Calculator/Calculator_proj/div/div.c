
#include <stdio.h>
#include "div.h"


uint16_t div(uint8_t a , uint8_t b)
{
	if(b == 0)
		return 0 ; 
	else 
		return (a/b);
}