#ifdef TEST

#include "unity.h"

#include "abs.h"

void setUp(void)
{
}

void tearDown(void)
{
}

void test_abs(void)
{
   uint8_t x = absVal(-1);
   TEST_ASSERT_EQUAL(1,x);
}

#endif // TEST
