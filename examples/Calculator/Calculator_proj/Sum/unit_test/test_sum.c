#include "unity.h"
#include "sum.h"

void setUp(void)
{
}

void tearDown(void)
{
}


void test_sum(void)
{
  uint16_t x =  sum(4 , 2);
  TEST_ASSERT_EQUAL(6,x);
}
