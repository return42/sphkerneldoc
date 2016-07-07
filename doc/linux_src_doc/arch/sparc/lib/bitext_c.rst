.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sparc/lib/bitext.c

.. _`bit_map_string_get`:

bit_map_string_get
==================

.. c:function:: int bit_map_string_get(struct bit_map *t, int len, int align)

    find and set a bit string in bit map.

    :param struct bit_map \*t:
        the bit map.

    :param int len:
        requested string length

    :param int align:
        requested alignment

.. _`bit_map_string_get.description`:

Description
-----------

Returns offset in the map or -1 if out of space.

Not safe to call from an interrupt (uses spin_lock).

.. This file was automatic generated / don't edit.

