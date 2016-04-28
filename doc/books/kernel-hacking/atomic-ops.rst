.. -*- coding: utf-8; mode: rst -*-

.. _atomic-ops:

=================
Atomic Operations
=================

Certain operations are guaranteed atomic on all platforms. The first
class of operations work on ``atomic_t`` ``include/asm/atomic.h``; this
contains a signed integer (at least 32 bits long), and you must use
these functions to manipulate or read atomic_t variables.
``atomic_read()`` and ``atomic_set()`` get and set the counter,
``atomic_add()``, ``atomic_sub()``, ``atomic_inc()``, ``atomic_dec()``,
and ``atomic_dec_and_test()`` (returns true if it was decremented to
zero).

Yes. It returns true (i.e. != 0) if the atomic variable is zero.

Note that these functions are slower than normal arithmetic, and so
should not be used unnecessarily.

The second class of atomic operations is atomic bit operations on an
``unsigned long``, defined in ``include/linux/bitops.h``. These
operations generally take a pointer to the bit pattern, and a bit
number: 0 is the least significant bit. ``set_bit()``, ``clear_bit()``
and ``change_bit()`` set, clear, and flip the given bit.
``test_and_set_bit()``, ``test_and_clear_bit()`` and
``test_and_change_bit()`` do the same thing, except return true if the
bit was previously set; these are particularly useful for atomically
setting flags.

It is possible to call these operations with bit indices greater than
BITS_PER_LONG. The resulting behavior is strange on big-endian
platforms though so it is a good idea not to do this.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
