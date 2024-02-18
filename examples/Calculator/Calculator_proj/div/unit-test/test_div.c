#include "unity.h"
#include "div.h"
void setUp(void)
{
}

void tearDown(void)
{
}
void testdiv(void)
{
  uint8_t res  ; 
  res = div(6,2);
  TEST_ASSERT_EQUAL(4, res);
}
