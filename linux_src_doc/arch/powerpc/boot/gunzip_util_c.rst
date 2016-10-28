.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/boot/gunzip_util.c

.. _`gunzip_start`:

gunzip_start
============

.. c:function:: void gunzip_start(struct gunzip_state *state, void *src, int srclen)

    prepare to decompress gzip data

    :param struct gunzip_state \*state:
        decompressor state structure to be initialized

    :param void \*src:
        buffer containing gzip compressed or uncompressed data

    :param int srclen:
        size in bytes of the buffer at src

.. _`gunzip_start.description`:

Description
-----------

If the buffer at \ ``src``\  contains a gzip header, this function
initializes zlib to decompress the data, storing the decompression
state in \ ``state``\ .  The other functions in this file can then be used
to decompress data from the gzipped stream.

If the buffer at \ ``src``\  does not contain a gzip header, it is assumed
to contain uncompressed data.  The buffer information is recorded
in \ ``state``\  and the other functions in this file will simply copy
data from the uncompressed data stream at \ ``src``\ .

Any errors, such as bad compressed data, cause an error to be
printed an the platform's \ :c:func:`exit`\  function to be called.

.. _`gunzip_partial`:

gunzip_partial
==============

.. c:function:: int gunzip_partial(struct gunzip_state *state, void *dst, int dstlen)

    extract bytes from a gzip data stream

    :param struct gunzip_state \*state:
        gzip state structure previously initialized by \ :c:func:`gunzip_start`\ 

    :param void \*dst:
        buffer to store extracted data

    :param int dstlen:
        maximum number of bytes to extract

.. _`gunzip_partial.description`:

Description
-----------

This function extracts at most \ ``dstlen``\  bytes from the data stream
previously associated with \ ``state``\  by \ :c:func:`gunzip_start`\ , decompressing
if necessary.  Exactly \ ``dstlen``\  bytes are extracted unless the data
stream doesn't contain enough bytes, in which case the entire
remainder of the stream is decompressed.

Returns the actual number of bytes extracted.  If any errors occur,
such as a corrupted compressed stream, an error is printed an the
platform's \ :c:func:`exit`\  function is called.

.. _`gunzip_exactly`:

gunzip_exactly
==============

.. c:function:: void gunzip_exactly(struct gunzip_state *state, void *dst, int dstlen)

    extract a fixed number of bytes from a gzip data stream

    :param struct gunzip_state \*state:
        gzip state structure previously initialized by \ :c:func:`gunzip_start`\ 

    :param void \*dst:
        buffer to store extracted data

    :param int dstlen:
        number of bytes to extract

.. _`gunzip_exactly.description`:

Description
-----------

This function extracts exactly \ ``dstlen``\  bytes from the data stream
previously associated with \ ``state``\  by \ :c:func:`gunzip_start`\ , decompressing
if necessary.

If there are less \ ``dstlen``\  bytes available in the data stream, or if
any other errors occur, such as a corrupted compressed stream, an
error is printed an the platform's \ :c:func:`exit`\  function is called.

.. _`gunzip_discard`:

gunzip_discard
==============

.. c:function:: void gunzip_discard(struct gunzip_state *state, int len)

    discard bytes from a gzip data stream

    :param struct gunzip_state \*state:
        gzip state structure previously initialized by \ :c:func:`gunzip_start`\ 

    :param int len:
        number of bytes to discard

.. _`gunzip_discard.description`:

Description
-----------

This function extracts, then discards exactly \ ``len``\  bytes from the
data stream previously associated with \ ``state``\  by \ :c:func:`gunzip_start`\ .
Subsequent \ :c:func:`gunzip_partial`\ , \ :c:func:`gunzip_exactly`\  or \ :c:func:`gunzip_finish`\ 
calls will extract the data following the discarded bytes in the
data stream.

If there are less \ ``len``\  bytes available in the data stream, or if
any other errors occur, such as a corrupted compressed stream, an
error is printed an the platform's \ :c:func:`exit`\  function is called.

.. _`gunzip_finish`:

gunzip_finish
=============

.. c:function:: int gunzip_finish(struct gunzip_state *state, void *dst, int dstlen)

    extract all remaining bytes from a gzip data stream

    :param struct gunzip_state \*state:
        gzip state structure previously initialized by \ :c:func:`gunzip_start`\ 

    :param void \*dst:
        buffer to store extracted data

    :param int dstlen:
        maximum number of bytes to extract

.. _`gunzip_finish.description`:

Description
-----------

This function extracts all remaining data, or at most \ ``dstlen``\ 
bytes, from the stream previously associated with \ ``state``\  by
\ :c:func:`gunzip_start`\ .  zlib is then shut down, so it is an error to use
any of the functions in this file on \ ``state``\  until it is
re-initialized with another call to \ :c:func:`gunzip_start`\ .

If any errors occur, such as a corrupted compressed stream, an
error is printed an the platform's \ :c:func:`exit`\  function is called.

.. This file was automatic generated / don't edit.

