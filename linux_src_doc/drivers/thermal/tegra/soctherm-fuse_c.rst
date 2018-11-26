.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/tegra/soctherm-fuse.c

.. _`div64_s64_precise`:

div64_s64_precise
=================

.. c:function:: s64 div64_s64_precise(s64 a, s32 b)

    wrapper for \ :c:func:`div64_s64`\ 

    :param a:
        the dividend
    :type a: s64

    :param b:
        the divisor
    :type b: s32

.. _`div64_s64_precise.description`:

Description
-----------

Implements division with fairly accurate rounding instead of truncation by
shifting the dividend to the left by 16 so that the quotient has a
much higher precision.

.. _`div64_s64_precise.return`:

Return
------

the quotient of a / b.

.. This file was automatic generated / don't edit.

