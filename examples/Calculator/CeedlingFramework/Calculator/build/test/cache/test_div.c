#include "G:/COURSES/UnitTest/Ceedling/0.Repo/examples/Calculator/Calculator_proj/div/div.h"
#include "C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/ceedling-0.31.1/vendor/unity/src/unity.h"
void setUp(void)

{

}



void tearDown(void)

{

}

void testdiv(void)

{

  uint8_t res ;

  res = div(6,2);

  UnityAssertEqualNumber((UNITY_INT)((4)), (UNITY_INT)((res)), (

 ((void *)0)

 ), (UNITY_UINT)(14), UNITY_DISPLAY_STYLE_INT);

}
