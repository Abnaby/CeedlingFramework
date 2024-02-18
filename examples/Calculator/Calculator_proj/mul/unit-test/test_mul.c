#include "unity.h"
#include "mul.h"
void setUp(void)
{
}

void tearDown(void)
{
}

void test_mul(void)
{
  uint16_t x = mul(3,1);
  TEST_ASSERT_EQUAL(3,x);
}

