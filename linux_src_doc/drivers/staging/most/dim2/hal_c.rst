.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/most/dim2/hal.c

.. _`alloc_dbr`:

alloc_dbr
=========

.. c:function:: int alloc_dbr(u16 size)

    \ ``param``\  size Allocating memory size. \ ``return``\  Offset in DBR memory by success or DBR_SIZE if out of memory.

    :param size:
        *undescribed*
    :type size: u16

.. _`dim_norm_isoc_buffer_size`:

dim_norm_isoc_buffer_size
=========================

.. c:function:: u16 dim_norm_isoc_buffer_size(u16 buf_size, u16 packet_length)

    conform to given packet length and not bigger than given buffer size.

    :param buf_size:
        *undescribed*
    :type buf_size: u16

    :param packet_length:
        *undescribed*
    :type packet_length: u16

.. _`dim_norm_isoc_buffer_size.description`:

Description
-----------

Returns non-zero correct buffer size or zero by error.

.. _`dim_norm_sync_buffer_size`:

dim_norm_sync_buffer_size
=========================

.. c:function:: u16 dim_norm_sync_buffer_size(u16 buf_size, u16 bytes_per_frame)

    conform to given bytes per frame and not bigger than given buffer size.

    :param buf_size:
        *undescribed*
    :type buf_size: u16

    :param bytes_per_frame:
        *undescribed*
    :type bytes_per_frame: u16

.. _`dim_norm_sync_buffer_size.description`:

Description
-----------

Returns non-zero correct buffer size or zero by error.

.. This file was automatic generated / don't edit.

