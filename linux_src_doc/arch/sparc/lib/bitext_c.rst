.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sparc/lib/bitext.c

.. _`bit_map_string_get`:

bit_map_string_get
==================

.. c:function:: int bit_map_string_get(struct bit_map *t, int len, int align)

    find and set a bit string in bit map.

    :param t:
        the bit map.
    :type t: struct bit_map \*

    :param len:
        requested string length
    :type len: int

    :param align:
        requested alignment
    :type align: int

.. _`bit_map_string_get.description`:

Description
-----------

Returns offset in the map or -1 if out of space.

Not safe to call from an interrupt (uses spin_lock).

.. This file was automatic generated / don't edit.

