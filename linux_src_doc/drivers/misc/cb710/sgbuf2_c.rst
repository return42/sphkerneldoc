.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/cb710/sgbuf2.c

.. _`cb710_sg_dwiter_read_next_block`:

cb710_sg_dwiter_read_next_block
===============================

.. c:function:: uint32_t cb710_sg_dwiter_read_next_block(struct sg_mapping_iter *miter)

    get next 32-bit word from sg buffer

    :param struct sg_mapping_iter \*miter:
        sg mapping iterator used for reading

.. _`cb710_sg_dwiter_read_next_block.description`:

Description
-----------

Returns 32-bit word starting at byte pointed to by \ ``miter``\ @
handling any alignment issues.  Bytes past the buffer's end
are not accessed (read) but are returned as zeroes.  \ ``miter``\ @
is advanced by 4 bytes or to the end of buffer whichever is
closer.

.. _`cb710_sg_dwiter_read_next_block.context`:

Context
-------

Same requirements as in \ :c:func:`sg_miter_next`\ .

.. _`cb710_sg_dwiter_read_next_block.return`:

Return
------

32-bit word just read.

.. _`cb710_sg_dwiter_write_next_block`:

cb710_sg_dwiter_write_next_block
================================

.. c:function:: void cb710_sg_dwiter_write_next_block(struct sg_mapping_iter *miter, uint32_t data)

    write next 32-bit word to sg buffer

    :param struct sg_mapping_iter \*miter:
        sg mapping iterator used for writing

    :param uint32_t data:
        *undescribed*

.. _`cb710_sg_dwiter_write_next_block.description`:

Description
-----------

Writes 32-bit word starting at byte pointed to by \ ``miter``\ @
handling any alignment issues.  Bytes which would be written
past the buffer's end are silently discarded. \ ``miter``\ @ is
advanced by 4 bytes or to the end of buffer whichever is closer.

.. _`cb710_sg_dwiter_write_next_block.context`:

Context
-------

Same requirements as in \ :c:func:`sg_miter_next`\ .

.. This file was automatic generated / don't edit.

