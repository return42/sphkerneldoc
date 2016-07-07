.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fixp-arith.h

.. _`__fixp_sin32`:

__fixp_sin32
============

.. c:function:: s32 __fixp_sin32(int degrees)

    :param int degrees:
        angle, in degrees, from 0 to 360.

.. _`__fixp_sin32.description`:

Description
-----------

The returned value ranges from -0x7fffffff to +0x7fffffff.

.. _`fixp_sin32`:

fixp_sin32
==========

.. c:function:: s32 fixp_sin32(int degrees)

    :param int degrees:
        angle, in degrees. The angle can be positive or negative

.. _`fixp_sin32.description`:

Description
-----------

The returned value ranges from -0x7fffffff to +0x7fffffff.

.. _`fixp_sin32_rad`:

fixp_sin32_rad
==============

.. c:function:: s32 fixp_sin32_rad(u32 radians, u32 twopi)

    calculates the sin of an angle in radians

    :param u32 radians:
        angle, in radians

    :param u32 twopi:
        value to be used for 2\*pi

.. _`fixp_sin32_rad.description`:

Description
-----------

Provides a variant for the cases where just 360
values is not enough. This function uses linear
interpolation to a wider range of values given by
twopi var.

Experimental tests gave a maximum difference of
0.000038 between the value calculated by \ :c:func:`sin`\  and
the one produced by this function, when twopi is
equal to 360000. That seems to be enough precision
for practical purposes.

Please notice that two high numbers for twopi could cause
overflows, so the routine will not allow values of twopi
bigger than 1^18.

.. This file was automatic generated / don't edit.

