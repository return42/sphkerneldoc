.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/zip/zip_mem.h

.. _`zip_cmd_qbuf_free`:

zip_cmd_qbuf_free
=================

.. c:function:: void zip_cmd_qbuf_free(struct zip_device *zip, int q)

    Frees the cmd Queue buffer

    :param zip:
        Pointer to zip device structure
    :type zip: struct zip_device \*

    :param q:
        Queue nmber to free buffer of
    :type q: int

.. _`zip_cmd_qbuf_alloc`:

zip_cmd_qbuf_alloc
==================

.. c:function:: int zip_cmd_qbuf_alloc(struct zip_device *zip, int q)

    Allocates a Chunk/cmd buffer for ZIP Inst(cmd) Queue

    :param zip:
        Pointer to zip device structure
    :type zip: struct zip_device \*

    :param q:
        Queue number to allocate bufffer to
    :type q: int

.. _`zip_cmd_qbuf_alloc.return`:

Return
------

0 if successful, 1 otherwise

.. _`zip_data_buf_alloc`:

zip_data_buf_alloc
==================

.. c:function:: u8 *zip_data_buf_alloc(u64 size)

    Allocates memory for a data bufffer

    :param size:
        Size of the buffer to allocate
    :type size: u64

.. _`zip_data_buf_alloc.return`:

Return
------

Pointer to the buffer allocated

.. _`zip_data_buf_free`:

zip_data_buf_free
=================

.. c:function:: void zip_data_buf_free(u8 *ptr, u64 size)

    Frees the memory of a data buffer

    :param ptr:
        Pointer to the buffer
    :type ptr: u8 \*

    :param size:
        Buffer size
    :type size: u64

.. This file was automatic generated / don't edit.

