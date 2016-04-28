.. -*- coding: utf-8; mode: rst -*-

.. _API-intlog10:

========
intlog10
========

*man intlog10(9)*

*4.6.0-rc5*

computes log10 of a value; the result is shifted left by 24 bits


Synopsis
========

.. c:function:: unsigned int intlog10( u32 value )

Arguments
=========

``value``
    The value (must be != 0)


to use rational values you can use the following method
=======================================================

intlog10(value) = intlog10(value * 10^x) - x * 2^24


An usecase example
==================


.. code-block:: c

        intlog10(1000) will give 3 << 24 = 3 * 2^24
         due to the implementation intlog10(1000) might be not exactly 3 * 2^24

       look at intlog2 for similar examples


return
======

log10(value) * 2^24


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
