.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sunrpc/xdr.h

.. _`xdr_stream_remaining`:

xdr_stream_remaining
====================

.. c:function:: size_t xdr_stream_remaining(const struct xdr_stream *xdr)

    Return the number of bytes remaining in the stream

    :param const struct xdr_stream \*xdr:
        pointer to struct xdr_stream

.. _`xdr_stream_remaining.return-value`:

Return value
------------

Number of bytes remaining in \ ``xdr``\  before xdr->end

.. _`xdr_align_size`:

xdr_align_size
==============

.. c:function:: size_t xdr_align_size(size_t n)

    Calculate padded size of an object

    :param size_t n:
        Size of an object being XDR encoded (in bytes)

.. _`xdr_align_size.return-value`:

Return value
------------

Size (in bytes) of the object including xdr padding

.. _`xdr_stream_encode_u32`:

xdr_stream_encode_u32
=====================

.. c:function:: ssize_t xdr_stream_encode_u32(struct xdr_stream *xdr, __u32 n)

    Encode a 32-bit integer

    :param struct xdr_stream \*xdr:
        pointer to xdr_stream

    :param __u32 n:
        integer to encode

.. _`xdr_stream_encode_u32.return-values`:

Return values
-------------

On success, returns length in bytes of XDR buffer consumed
\ ``-EMSGSIZE``\  on XDR buffer overflow

.. _`xdr_stream_encode_u64`:

xdr_stream_encode_u64
=====================

.. c:function:: ssize_t xdr_stream_encode_u64(struct xdr_stream *xdr, __u64 n)

    Encode a 64-bit integer

    :param struct xdr_stream \*xdr:
        pointer to xdr_stream

    :param __u64 n:
        64-bit integer to encode

.. _`xdr_stream_encode_u64.return-values`:

Return values
-------------

On success, returns length in bytes of XDR buffer consumed
\ ``-EMSGSIZE``\  on XDR buffer overflow

.. _`xdr_stream_encode_opaque_fixed`:

xdr_stream_encode_opaque_fixed
==============================

.. c:function:: ssize_t xdr_stream_encode_opaque_fixed(struct xdr_stream *xdr, const void *ptr, size_t len)

    Encode fixed length opaque xdr data

    :param struct xdr_stream \*xdr:
        pointer to xdr_stream

    :param const void \*ptr:
        pointer to opaque data object

    :param size_t len:
        size of object pointed to by \ ``ptr``\ 

.. _`xdr_stream_encode_opaque_fixed.return-values`:

Return values
-------------

On success, returns length in bytes of XDR buffer consumed
\ ``-EMSGSIZE``\  on XDR buffer overflow

.. _`xdr_stream_encode_opaque`:

xdr_stream_encode_opaque
========================

.. c:function:: ssize_t xdr_stream_encode_opaque(struct xdr_stream *xdr, const void *ptr, size_t len)

    Encode variable length opaque xdr data

    :param struct xdr_stream \*xdr:
        pointer to xdr_stream

    :param const void \*ptr:
        pointer to opaque data object

    :param size_t len:
        size of object pointed to by \ ``ptr``\ 

.. _`xdr_stream_encode_opaque.return-values`:

Return values
-------------

On success, returns length in bytes of XDR buffer consumed
\ ``-EMSGSIZE``\  on XDR buffer overflow

.. _`xdr_stream_decode_u32`:

xdr_stream_decode_u32
=====================

.. c:function:: ssize_t xdr_stream_decode_u32(struct xdr_stream *xdr, __u32 *ptr)

    Decode a 32-bit integer

    :param struct xdr_stream \*xdr:
        pointer to xdr_stream

    :param __u32 \*ptr:
        location to store integer

.. _`xdr_stream_decode_u32.return-values`:

Return values
-------------

%0 on success
\ ``-EBADMSG``\  on XDR buffer overflow

.. _`xdr_stream_decode_opaque_fixed`:

xdr_stream_decode_opaque_fixed
==============================

.. c:function:: ssize_t xdr_stream_decode_opaque_fixed(struct xdr_stream *xdr, void *ptr, size_t len)

    Decode fixed length opaque xdr data

    :param struct xdr_stream \*xdr:
        pointer to xdr_stream

    :param void \*ptr:
        location to store data

    :param size_t len:
        size of buffer pointed to by \ ``ptr``\ 

.. _`xdr_stream_decode_opaque_fixed.return-values`:

Return values
-------------

On success, returns size of object stored in \ ``ptr``\ 
\ ``-EBADMSG``\  on XDR buffer overflow

.. _`xdr_stream_decode_opaque_inline`:

xdr_stream_decode_opaque_inline
===============================

.. c:function:: ssize_t xdr_stream_decode_opaque_inline(struct xdr_stream *xdr, void **ptr, size_t maxlen)

    Decode variable length opaque xdr data

    :param struct xdr_stream \*xdr:
        pointer to xdr_stream

    :param void \*\*ptr:
        location to store pointer to opaque data

    :param size_t maxlen:
        maximum acceptable object size

.. _`xdr_stream_decode_opaque_inline.note`:

Note
----

the pointer stored in \ ``ptr``\  cannot be assumed valid after the XDR
buffer has been destroyed, or even after calling \ :c:func:`xdr_inline_decode`\ 
on \ ``xdr``\ . It is therefore expected that the object it points to should
be processed immediately.

.. _`xdr_stream_decode_opaque_inline.return-values`:

Return values
-------------

On success, returns size of object stored in \*@ptr
\ ``-EBADMSG``\  on XDR buffer overflow
\ ``-EMSGSIZE``\  if the size of the object would exceed \ ``maxlen``\ 

.. This file was automatic generated / don't edit.

