.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/compress.c

.. _`ubifs_compress`:

ubifs_compress
==============

.. c:function:: void ubifs_compress(const struct ubifs_info *c, const void *in_buf, int in_len, void *out_buf, int *out_len, int *compr_type)

    compress data.

    :param const struct ubifs_info \*c:
        *undescribed*

    :param const void \*in_buf:
        data to compress

    :param int in_len:
        length of the data to compress

    :param void \*out_buf:
        output buffer where compressed data should be stored

    :param int \*out_len:
        output buffer length is returned here

    :param int \*compr_type:
        type of compression to use on enter, actually used compression
        type on exit

.. _`ubifs_compress.description`:

Description
-----------

This function compresses input buffer \ ``in_buf``\  of length \ ``in_len``\  and stores
the result in the output buffer \ ``out_buf``\  and the resulting length in
\ ``out_len``\ . If the input buffer does not compress, it is just copied to the
\ ``out_buf``\ . The same happens if \ ``compr_type``\  is \ ``UBIFS_COMPR_NONE``\  or if
compression error occurred.

Note, if the input buffer was not compressed, it is copied to the output
buffer and \ ``UBIFS_COMPR_NONE``\  is returned in \ ``compr_type``\ .

.. _`ubifs_decompress`:

ubifs_decompress
================

.. c:function:: int ubifs_decompress(const struct ubifs_info *c, const void *in_buf, int in_len, void *out_buf, int *out_len, int compr_type)

    decompress data.

    :param const struct ubifs_info \*c:
        *undescribed*

    :param const void \*in_buf:
        data to decompress

    :param int in_len:
        length of the data to decompress

    :param void \*out_buf:
        output buffer where decompressed data should

    :param int \*out_len:
        output length is returned here

    :param int compr_type:
        type of compression

.. _`ubifs_decompress.description`:

Description
-----------

This function decompresses data from buffer \ ``in_buf``\  into buffer \ ``out_buf``\ .
The length of the uncompressed data is returned in \ ``out_len``\ . This functions
returns \ ``0``\  on success or a negative error code on failure.

.. _`compr_init`:

compr_init
==========

.. c:function:: int compr_init(struct ubifs_compressor *compr)

    initialize a compressor.

    :param struct ubifs_compressor \*compr:
        compressor description object

.. _`compr_init.description`:

Description
-----------

This function initializes the requested compressor and returns zero in case
of success or a negative error code in case of failure.

.. _`compr_exit`:

compr_exit
==========

.. c:function:: void compr_exit(struct ubifs_compressor *compr)

    de-initialize a compressor.

    :param struct ubifs_compressor \*compr:
        compressor description object

.. _`ubifs_compressors_init`:

ubifs_compressors_init
======================

.. c:function:: int ubifs_compressors_init( void)

    initialize UBIFS compressors.

    :param  void:
        no arguments

.. _`ubifs_compressors_init.description`:

Description
-----------

This function initializes the compressor which were compiled in. Returns
zero in case of success and a negative error code in case of failure.

.. _`ubifs_compressors_exit`:

ubifs_compressors_exit
======================

.. c:function:: void ubifs_compressors_exit( void)

    de-initialize UBIFS compressors.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

