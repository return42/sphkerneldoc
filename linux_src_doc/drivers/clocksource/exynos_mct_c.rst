.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/exynos_mct.c

.. _`exynos4_read_count_64`:

exynos4_read_count_64
=====================

.. c:function:: u64 exynos4_read_count_64( void)

    Read all 64-bits of the global counter

    :param void:
        no arguments
    :type void: 

.. _`exynos4_read_count_64.description`:

Description
-----------

This will read all 64-bits of the global counter taking care to make sure
that the upper and lower half match.  Note that reading the MCT can be quite
slow (hundreds of nanoseconds) so you should use the 32-bit (lower half
only) version when possible.

Returns the number of cycles in the global counter.

.. _`exynos4_read_count_32`:

exynos4_read_count_32
=====================

.. c:function:: u32 notrace exynos4_read_count_32( void)

    Read the lower 32-bits of the global counter

    :param void:
        no arguments
    :type void: 

.. _`exynos4_read_count_32.description`:

Description
-----------

This will read just the lower 32-bits of the global counter.  This is marked
as notrace so it can be used by the scheduler clock.

Returns the number of cycles in the global counter (lower 32 bits).

.. This file was automatic generated / don't edit.

