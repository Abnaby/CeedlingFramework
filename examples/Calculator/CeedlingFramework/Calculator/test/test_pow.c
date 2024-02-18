#ifdef TEST

#include "unity.h"

#include "pow.h"

void setUp(void)
{
}

void tearDown(void)
{
}

void test_pow(void)
{
    uint16_t x =  power(2 , 2);
    TEST_ASSERT_EQUAL(4,x);
}

#endif // TEST
