.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-core/dvb_math.h

.. _`intlog2`:

intlog2
=======

.. c:function:: unsigned int intlog2(u32 value)

    computes log2 of a value; the result is shifted left by 24 bits

    :param u32 value:
        The value (must be != 0)

.. _`intlog2.to-use-rational-values-you-can-use-the-following-method`:

to use rational values you can use the following method
-------------------------------------------------------

intlog2(value) = intlog2(value \* 2^x) - x \* 2^24

.. _`intlog2.some-usecase-examples`:

Some usecase examples
---------------------

intlog2(8) will give 3 << 24 = 3 \* 2^24
intlog2(9) will give 3 << 24 + ... = 3.16... \* 2^24
intlog2(1.5) = intlog2(3) - 2^24 = 0.584... \* 2^24

.. _`intlog2.return`:

Return
------

log2(value) \* 2^24

.. _`intlog10`:

intlog10
========

.. c:function:: unsigned int intlog10(u32 value)

    computes log10 of a value; the result is shifted left by 24 bits

    :param u32 value:
        The value (must be != 0)

.. _`intlog10.to-use-rational-values-you-can-use-the-following-method`:

to use rational values you can use the following method
-------------------------------------------------------

intlog10(value) = intlog10(value \* 10^x) - x \* 2^24

.. _`intlog10.an-usecase-example`:

An usecase example
------------------

intlog10(1000) will give 3 << 24 = 3 \* 2^24
due to the implementation intlog10(1000) might be not exactly 3 \* 2^24

look at intlog2 for similar examples

.. _`intlog10.return`:

Return
------

log10(value) \* 2^24

.. This file was automatic generated / don't edit.

