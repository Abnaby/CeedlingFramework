#include "unity.h"
#include "sub.h"
void setUp(void)
{
}

void tearDown(void)
{
}

void test_sub(void)
{
  uint8_t x = sub(5,4);
  TEST_ASSERT_EQUAL(1,x);
}

