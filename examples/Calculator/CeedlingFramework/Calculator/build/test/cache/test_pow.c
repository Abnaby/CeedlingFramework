#include "src/pow.h"
#include "C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/ceedling-0.31.1/vendor/unity/src/unity.h"








void setUp(void)

{

}



void tearDown(void)

{

}



void test_pow(void)

{

    uint16_t x = power(2 , 2);

    UnityAssertEqualNumber((UNITY_INT)((4)), (UNITY_INT)((x)), (

   ((void *)0)

   ), (UNITY_UINT)(18), UNITY_DISPLAY_STYLE_INT);

}
