.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/packer.c

.. _`ib_pack`:

ib_pack
=======

.. c:function:: void ib_pack(const struct ib_field *desc, int desc_len, void *structure, void *buf)

    Pack a structure into a buffer

    :param desc:
        Array of structure field descriptions
    :type desc: const struct ib_field \*

    :param desc_len:
        Number of entries in \ ``desc``\ 
    :type desc_len: int

    :param structure:
        Structure to pack from
    :type structure: void \*

    :param buf:
        Buffer to pack into
    :type buf: void \*

.. _`ib_pack.description`:

Description
-----------

\ :c:func:`ib_pack`\  packs a list of structure fields into a buffer,
controlled by the array of fields in \ ``desc``\ .

.. _`ib_unpack`:

ib_unpack
=========

.. c:function:: void ib_unpack(const struct ib_field *desc, int desc_len, void *buf, void *structure)

    Unpack a buffer into a structure

    :param desc:
        Array of structure field descriptions
    :type desc: const struct ib_field \*

    :param desc_len:
        Number of entries in \ ``desc``\ 
    :type desc_len: int

    :param buf:
        Buffer to unpack from
    :type buf: void \*

    :param structure:
        Structure to unpack into
    :type structure: void \*

.. _`ib_unpack.description`:

Description
-----------

\ :c:func:`ib_pack`\  unpacks a list of structure fields from a buffer,
controlled by the array of fields in \ ``desc``\ .

.. This file was automatic generated / don't edit.

