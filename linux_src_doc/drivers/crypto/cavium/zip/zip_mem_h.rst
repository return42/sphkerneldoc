.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/zip/zip_mem.h

.. _`zip_cmd_qbuf_free`:

zip_cmd_qbuf_free
=================

.. c:function:: void zip_cmd_qbuf_free(struct zip_device *zip, int q)

    Frees the cmd Queue buffer

    :param struct zip_device \*zip:
        Pointer to zip device structure

    :param int q:
        Queue nmber to free buffer of

.. _`zip_cmd_qbuf_alloc`:

zip_cmd_qbuf_alloc
==================

.. c:function:: int zip_cmd_qbuf_alloc(struct zip_device *zip, int q)

    Allocates a Chunk/cmd buffer for ZIP Inst(cmd) Queue

    :param struct zip_device \*zip:
        Pointer to zip device structure

    :param int q:
        Queue number to allocate bufffer to

.. _`zip_cmd_qbuf_alloc.return`:

Return
------

0 if successful, 1 otherwise

.. _`zip_data_buf_alloc`:

zip_data_buf_alloc
==================

.. c:function:: u8 *zip_data_buf_alloc(u64 size)

    Allocates memory for a data bufffer

    :param u64 size:
        Size of the buffer to allocate

.. _`zip_data_buf_alloc.return`:

Return
------

Pointer to the buffer allocated

.. _`zip_data_buf_free`:

zip_data_buf_free
=================

.. c:function:: void zip_data_buf_free(u8 *ptr, u64 size)

    Frees the memory of a data buffer

    :param u8 \*ptr:
        Pointer to the buffer

    :param u64 size:
        Buffer size

.. This file was automatic generated / don't edit.

