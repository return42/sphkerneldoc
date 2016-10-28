.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/packer.c

.. _`ib_pack`:

ib_pack
=======

.. c:function:: void ib_pack(const struct ib_field *desc, int desc_len, void *structure, void *buf)

    Pack a structure into a buffer

    :param const struct ib_field \*desc:
        Array of structure field descriptions

    :param int desc_len:
        Number of entries in \ ``desc``\ 

    :param void \*structure:
        Structure to pack from

    :param void \*buf:
        Buffer to pack into

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

    :param const struct ib_field \*desc:
        Array of structure field descriptions

    :param int desc_len:
        Number of entries in \ ``desc``\ 

    :param void \*buf:
        Buffer to unpack from

    :param void \*structure:
        Structure to unpack into

.. _`ib_unpack.description`:

Description
-----------

\ :c:func:`ib_pack`\  unpacks a list of structure fields from a buffer,
controlled by the array of fields in \ ``desc``\ .

.. This file was automatic generated / don't edit.

