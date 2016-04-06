
.. _API-intlog2:

=======
intlog2
=======

*man intlog2(9)*

*4.6.0-rc1*

computes log2 of a value; the result is shifted left by 24 bits


Synopsis
========

.. c:function:: unsigned int intlog2( u32 value )

Arguments
=========

``value``
    The value (must be != 0)


to use rational values you can use the following method
=======================================================

intlog2(value) = intlog2(value ⋆ 2^x) - x ⋆ 2^24


Some usecase examples
=====================


.. code-block:: c

        intlog2(8) will give 3 << 24 = 3 * 2^24
        intlog2(9) will give 3 << 24 + ... = 3.16... * 2^24
        intlog2(1.5) = intlog2(3) - 2^24 = 0.584... * 2^24


return
======

log2(value) ⋆ 2^24
