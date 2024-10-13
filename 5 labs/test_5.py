import unittest
from labs_5 import Complex

class TestFindNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.ComplexClass = Complex

    def testComplex_str(self):
        c1 = self.ComplexClass(1., 2.)
        expected = "1.0 + 2.0*i"
        actual = c1.__str__()
        self.assertEqual(expected, actual)

    def testComplex_str_zero(self):
        c1 = self.ComplexClass(0., 0.)
        expected = "0.0 + 0.0*i"
        actual = str(c1)
        self.assertEqual(expected, actual)

    def testComplex_str_negative(self):
        c1 = self.ComplexClass(-1.5, -2.5)
        expected = "-1.5 - 2.5*i"
        actual = str(c1)
        self.assertEqual(expected, actual)


    def testComplex_add(self):
        c1 = self.ComplexClass(1., 2.)
        c2 = self.ComplexClass(2., 3.)
        expected = self.ComplexClass(3., 5.)
        actual = c1 + c2
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_add_zero(self):
        c1 = self.ComplexClass(0., 0.)
        c2 = self.ComplexClass(0., 0.)
        expected = self.ComplexClass(0., 0.)
        actual = c1 + c2
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_add_negative(self):
        c1 = self.ComplexClass(-1., -2.)
        c2 = self.ComplexClass(-3., -4.)
        expected = self.ComplexClass(-4., -6.)
        actual = c1 + c2
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_iadd(self):
        c1 = self.ComplexClass(1., 2.)
        c2 = self.ComplexClass(2., 3.)
        expected = self.ComplexClass(3., 5.)
        c1 += c2
        actual = c1
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_iadd_zero(self):
        c1 = self.ComplexClass(1., 1.)
        c2 = self.ComplexClass(0., 0.)
        expected = self.ComplexClass(1., 1.)
        c1 += c2
        self.assertEqual(c1.real, expected.real)
        self.assertEqual(c1.imaginary, expected.imaginary)

    def testComplex_iadd_negative(self):
        c1 = self.ComplexClass(3., 3.)
        c2 = self.ComplexClass(-1., -1.)
        expected = self.ComplexClass(2., 2.)
        c1 += c2
        self.assertEqual(c1.real, expected.real)
        self.assertEqual(c1.imaginary, expected.imaginary)

    def testComplex_sub(self):
        c1 = self.ComplexClass(5., 7.)
        c2 = self.ComplexClass(3., 4.)
        expected = self.ComplexClass(2., 3.)
        actual = c1 - c2
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_sub_zero(self):
        c1 = self.ComplexClass(5., 5.)
        c2 = self.ComplexClass(0., 0.)
        expected = self.ComplexClass(5., 5.)
        actual = c1 - c2
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_sub_negative(self):
        c1 = self.ComplexClass(5., 5.)
        c2 = self.ComplexClass(-3., -3.)
        expected = self.ComplexClass(8., 8.)
        actual = c1 - c2
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_isub(self):
        c1 = self.ComplexClass(5., 7.)
        c2 = self.ComplexClass(3., 4.)
        expected = self.ComplexClass(2., 3.)
        c1 -= c2
        actual = c1
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_isub_zero(self):
        c1 = self.ComplexClass(2., 2.)
        c2 = self.ComplexClass(0., 0.)
        expected = self.ComplexClass(2., 2.)
        c1 -= c2
        self.assertEqual(c1.real, expected.real)
        self.assertEqual(c1.imaginary, expected.imaginary)

    def testComplex_isub_negative(self):
        c1 = self.ComplexClass(5., 5.)
        c2 = self.ComplexClass(-2., -3.)
        expected = self.ComplexClass(7., 8.)
        c1 -= c2
        self.assertEqual(c1.real, expected.real)
        self.assertEqual(c1.imaginary, expected.imaginary)

    def testComplex_mul(self):
        c1 = self.ComplexClass(1., 2.)
        c2 = self.ComplexClass(3., 4.)
        expected = self.ComplexClass(-5., 10.)
        actual = c1 * c2
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_mul_zero(self):
        c1 = self.ComplexClass(0., 0.)
        c2 = self.ComplexClass(1., 1.)
        expected = self.ComplexClass(0., 0.)
        actual = c1 * c2
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_mul_negative(self):
        c1 = self.ComplexClass(-1., -2.)
        c2 = self.ComplexClass(2., 3.)
        expected = self.ComplexClass(4., -7.)
        actual = c1 * c2
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_imul(self):
        c1 = self.ComplexClass(1., 2.)
        c2 = self.ComplexClass(3., 4.)
        expected = self.ComplexClass(-5., 10.)
        c1 *= c2
        actual = c1
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_imul_zero(self):
        c1 = self.ComplexClass(1., 1.)
        c2 = self.ComplexClass(0., 0.)
        expected = self.ComplexClass(0., 0.)
        c1 *= c2
        self.assertEqual(c1.real, expected.real)
        self.assertEqual(c1.imaginary, expected.imaginary)

    def testComplex_imul_negative(self):
        c1 = self.ComplexClass(-2., -3.)
        c2 = self.ComplexClass(1., 1.)
        expected = self.ComplexClass(1., -5.)
        c1 *= c2
        self.assertEqual(c1.real, expected.real)
        self.assertEqual(c1.imaginary, expected.imaginary)

    def testComplex_truediv(self):
        c1 = self.ComplexClass(1., 2.)
        c2 = self.ComplexClass(3., 4.)
        expected = self.ComplexClass(0.44, 0.08)
        actual = c1 / c2
        self.assertAlmostEqual(actual.real, expected.real, places=2)
        self.assertAlmostEqual(actual.imaginary, expected.imaginary, places=2)

    def testComplex_truediv_zero(self):
        c1 = self.ComplexClass(1., 1.)
        c2 = self.ComplexClass(1., 0.)
        expected = self.ComplexClass(1., 1.)
        actual = c1 / c2
        self.assertEqual(actual.real, expected.real)
        self.assertEqual(actual.imaginary, expected.imaginary)

    def testComplex_truediv_negative(self):
        c1 = self.ComplexClass(-4., 6.)
        c2 = self.ComplexClass(1., -2.)
        expected = self.ComplexClass(-3.2, -0.4)
        actual = c1 / c2
        self.assertAlmostEqual(actual.real, expected.real, places=2)
        self.assertAlmostEqual(actual.imaginary, expected.imaginary, places=2)

    def testComplex_itruediv(self):
        c1 = self.ComplexClass(1., 2.)
        c2 = self.ComplexClass(3., 4.)
        expected = self.ComplexClass(0.44, 0.08)
        c1 /= c2
        actual = c1
        self.assertAlmostEqual(actual.real, expected.real, places=2)
        self.assertAlmostEqual(actual.imaginary, expected.imaginary, places=2)

    def testComplex_itruediv_zero(self):
        c1 = self.ComplexClass(1., 1.)
        c2 = self.ComplexClass(1., 1.)
        expected = self.ComplexClass(1., 0.)
        c1 /= c2
        self.assertAlmostEqual(c1.real, expected.real, places=2)
        self.assertAlmostEqual(c1.imaginary, expected.imaginary, places=2)

    def testComplex_itruediv_negative(self):
        c1 = self.ComplexClass(5., 6.)
        c2 = self.ComplexClass(-2., 3.)
        expected = self.ComplexClass(0.6154, -2.0769)
        c1 /= c2
        self.assertAlmostEqual(c1.real, expected.real, places=2)
        self.assertAlmostEqual(c1.imaginary, expected.imaginary, places=2)

    def testComplex_abs(self):
        c1 = self.ComplexClass(3., 4.)
        expected = 5.
        actual = abs(c1)
        self.assertEqual(actual, expected)
    def testComplex_abs_zero(self):
        c1 = self.ComplexClass(0., 0.)
        expected = 0.
        actual = abs(c1)
        self.assertEqual(actual, expected)

    def testComplex_abs_negative(self):
        c1 = self.ComplexClass(-3., -4.)
        expected = 5.
        actual = abs(c1)
        self.assertEqual(actual, expected)

    def testComplex_eq(self):
        c1 = self.ComplexClass(1., 2.)
        c2 = self.ComplexClass(1., 2.)
        self.assertTrue(c1 == c2)

    def testComplex_eq_zero(self):
        c1 = self.ComplexClass(0., 0.)
        c2 = self.ComplexClass(0., 0.)
        self.assertTrue(c1 == c2)

    def testComplex_eq_negative(self):
        c1 = self.ComplexClass(-1., -1.)
        c2 = self.ComplexClass(-1., -1.)
        self.assertTrue(c1 == c2)


    def testComplex_neq(self):
        c1 = self.ComplexClass(1., 2.)
        c2 = self.ComplexClass(2., 3.)
        self.assertTrue(c1 != c2)

    def testComplex_neq_zero(self):
        c1 = self.ComplexClass(0., 0.)
        c2 = self.ComplexClass(1., 1.)
        self.assertTrue(c1 != c2)

    def testComplex_neq_negative(self):
        c1 = self.ComplexClass(-1., -2.)
        c2 = self.ComplexClass(-2., -3.)
        self.assertTrue(c1 != c2)


