#include "G:/COURSES/UnitTest/Ceedling/0.Repo/examples/Calculator/Calculator_proj/sub/sub.h"
#include "C:/Ruby27-x64/lib/ruby/gems/2.7.0/gems/ceedling-0.31.1/vendor/unity/src/unity.h"
void setUp(void)

{

}



void tearDown(void)

{

}



void test_sub(void)

{

  uint8_t x = sub(5,4);

  UnityAssertEqualNumber((UNITY_INT)((1)), (UNITY_INT)((x)), (

 ((void *)0)

 ), (UNITY_UINT)(14), UNITY_DISPLAY_STYLE_INT);

}
