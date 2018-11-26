.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sunrpc/xdr.h

.. _`xdr_stream_remaining`:

xdr_stream_remaining
====================

.. c:function:: size_t xdr_stream_remaining(const struct xdr_stream *xdr)

    Return the number of bytes remaining in the stream

    :param xdr:
        pointer to struct xdr_stream
    :type xdr: const struct xdr_stream \*

.. _`xdr_stream_remaining.return-value`:

Return value
------------

Number of bytes remaining in \ ``xdr``\  before xdr->end

.. _`xdr_align_size`:

xdr_align_size
==============

.. c:function:: size_t xdr_align_size(size_t n)

    Calculate padded size of an object

    :param n:
        Size of an object being XDR encoded (in bytes)
    :type n: size_t

.. _`xdr_align_size.return-value`:

Return value
------------

Size (in bytes) of the object including xdr padding

.. _`xdr_stream_encode_u32`:

xdr_stream_encode_u32
=====================

.. c:function:: ssize_t xdr_stream_encode_u32(struct xdr_stream *xdr, __u32 n)

    Encode a 32-bit integer

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param n:
        integer to encode
    :type n: __u32

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

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param n:
        64-bit integer to encode
    :type n: __u64

.. _`xdr_stream_encode_u64.return-values`:

Return values
-------------

On success, returns length in bytes of XDR buffer consumed
\ ``-EMSGSIZE``\  on XDR buffer overflow

.. _`xdr_stream_encode_opaque_inline`:

xdr_stream_encode_opaque_inline
===============================

.. c:function:: ssize_t xdr_stream_encode_opaque_inline(struct xdr_stream *xdr, void **ptr, size_t len)

    Encode opaque xdr data

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param ptr:
        pointer to void pointer
    :type ptr: void \*\*

    :param len:
        size of object
    :type len: size_t

.. _`xdr_stream_encode_opaque_inline.return-values`:

Return values
-------------

On success, returns length in bytes of XDR buffer consumed
\ ``-EMSGSIZE``\  on XDR buffer overflow

.. _`xdr_stream_encode_opaque_fixed`:

xdr_stream_encode_opaque_fixed
==============================

.. c:function:: ssize_t xdr_stream_encode_opaque_fixed(struct xdr_stream *xdr, const void *ptr, size_t len)

    Encode fixed length opaque xdr data

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param ptr:
        pointer to opaque data object
    :type ptr: const void \*

    :param len:
        size of object pointed to by \ ``ptr``\ 
    :type len: size_t

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

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param ptr:
        pointer to opaque data object
    :type ptr: const void \*

    :param len:
        size of object pointed to by \ ``ptr``\ 
    :type len: size_t

.. _`xdr_stream_encode_opaque.return-values`:

Return values
-------------

On success, returns length in bytes of XDR buffer consumed
\ ``-EMSGSIZE``\  on XDR buffer overflow

.. _`xdr_stream_encode_uint32_array`:

xdr_stream_encode_uint32_array
==============================

.. c:function:: ssize_t xdr_stream_encode_uint32_array(struct xdr_stream *xdr, const __u32 *array, size_t array_size)

    Encode variable length array of integers

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param array:
        array of integers
    :type array: const __u32 \*

    :param array_size:
        number of elements in \ ``array``\ 
    :type array_size: size_t

.. _`xdr_stream_encode_uint32_array.return-values`:

Return values
-------------

On success, returns length in bytes of XDR buffer consumed
\ ``-EMSGSIZE``\  on XDR buffer overflow

.. _`xdr_stream_decode_u32`:

xdr_stream_decode_u32
=====================

.. c:function:: ssize_t xdr_stream_decode_u32(struct xdr_stream *xdr, __u32 *ptr)

    Decode a 32-bit integer

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param ptr:
        location to store integer
    :type ptr: __u32 \*

.. _`xdr_stream_decode_u32.return-values`:

Return values
-------------

\ ``0``\  on success
\ ``-EBADMSG``\  on XDR buffer overflow

.. _`xdr_stream_decode_opaque_fixed`:

xdr_stream_decode_opaque_fixed
==============================

.. c:function:: ssize_t xdr_stream_decode_opaque_fixed(struct xdr_stream *xdr, void *ptr, size_t len)

    Decode fixed length opaque xdr data

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param ptr:
        location to store data
    :type ptr: void \*

    :param len:
        size of buffer pointed to by \ ``ptr``\ 
    :type len: size_t

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

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param ptr:
        location to store pointer to opaque data
    :type ptr: void \*\*

    :param maxlen:
        maximum acceptable object size
    :type maxlen: size_t

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

.. _`xdr_stream_decode_uint32_array`:

xdr_stream_decode_uint32_array
==============================

.. c:function:: ssize_t xdr_stream_decode_uint32_array(struct xdr_stream *xdr, __u32 *array, size_t array_size)

    Decode variable length array of integers

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param array:
        location to store the integer array or NULL
    :type array: __u32 \*

    :param array_size:
        number of elements to store
    :type array_size: size_t

.. _`xdr_stream_decode_uint32_array.return-values`:

Return values
-------------

On success, returns number of elements stored in \ ``array``\ 
\ ``-EBADMSG``\  on XDR buffer overflow
\ ``-EMSGSIZE``\  if the size of the array exceeds \ ``array_size``\ 

.. This file was automatic generated / don't edit.

