.. -*- coding: utf-8; mode: rst -*-

========
cordic.h
========


.. _`cordic_iq`:

struct cordic_iq
================

.. c:type:: cordic_iq

    i/q coordinate.


.. _`cordic_iq.definition`:

Definition
----------

.. code-block:: c

  struct cordic_iq {
    s32 i;
    s32 q;
  };


.. _`cordic_iq.members`:

Members
-------

:``i``:
    real part of coordinate (in phase).

:``q``:
    imaginary part of coordinate (quadrature).




.. _`cordic_calc_iq`:

cordic_calc_iq
==============

.. c:function:: struct cordic_iq cordic_calc_iq (s32 theta)

    calculates the i/q coordinate for given angle.

    :param s32 theta:
        angle in degrees for which i/q coordinate is to be calculated.



.. _`cordic_calc_iq.description`:

Description
-----------

The function calculates the i/q coordinate for a given angle using the
CORDIC algorithm. The coordinate consists of a real (i) and an
imaginary (q) part. The real part is essentially the cosine of the
angle and the imaginary part is the sine of the angle. The returned
values are scaled by 2^16 for precision. The range for theta is
for -180 degrees to +180 degrees. Passed values outside this range are
converted before doing the actual calculation.

