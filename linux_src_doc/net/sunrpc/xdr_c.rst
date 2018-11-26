.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xdr.c

.. _`xdr_encode_opaque_fixed`:

xdr_encode_opaque_fixed
=======================

.. c:function:: __be32 *xdr_encode_opaque_fixed(__be32 *p, const void *ptr, unsigned int nbytes)

    Encode fixed length opaque data

    :param p:
        pointer to current position in XDR buffer.
    :type p: __be32 \*

    :param ptr:
        pointer to data to encode (or NULL)
    :type ptr: const void \*

    :param nbytes:
        size of data.
    :type nbytes: unsigned int

.. _`xdr_encode_opaque_fixed.description`:

Description
-----------

Copy the array of data of length nbytes at ptr to the XDR buffer
at position p, then align to the next 32-bit boundary by padding
with zero bytes (see RFC1832).

.. _`xdr_encode_opaque_fixed.note`:

Note
----

if ptr is NULL, only the padding is performed.

Returns the updated current XDR buffer position

.. _`xdr_encode_opaque`:

xdr_encode_opaque
=================

.. c:function:: __be32 *xdr_encode_opaque(__be32 *p, const void *ptr, unsigned int nbytes)

    Encode variable length opaque data

    :param p:
        pointer to current position in XDR buffer.
    :type p: __be32 \*

    :param ptr:
        pointer to data to encode (or NULL)
    :type ptr: const void \*

    :param nbytes:
        size of data.
    :type nbytes: unsigned int

.. _`xdr_encode_opaque.description`:

Description
-----------

Returns the updated current XDR buffer position

.. _`xdr_terminate_string`:

xdr_terminate_string
====================

.. c:function:: void xdr_terminate_string(struct xdr_buf *buf, const u32 len)

    '\0'-terminate a string residing in an xdr_buf

    :param buf:
        XDR buffer where string resides
    :type buf: struct xdr_buf \*

    :param len:
        length of string, in bytes
    :type len: const u32

.. _`_shift_data_right_pages`:

_shift_data_right_pages
=======================

.. c:function:: void _shift_data_right_pages(struct page **pages, size_t pgto_base, size_t pgfrom_base, size_t len)

    :param pages:
        vector of pages containing both the source and dest memory area.
    :type pages: struct page \*\*

    :param pgto_base:
        page vector address of destination
    :type pgto_base: size_t

    :param pgfrom_base:
        page vector address of source
    :type pgfrom_base: size_t

    :param len:
        number of bytes to copy
    :type len: size_t

.. _`_shift_data_right_pages.note`:

Note
----

the addresses pgto_base and pgfrom_base are both calculated in

.. _`_shift_data_right_pages.the-same-way`:

the same way
------------

           if a memory area starts at byte 'base' in page 'pages[i]',
           then its address is given as (i << PAGE_SHIFT) + base
Also note: pgfrom_base must be < pgto_base, but the memory areas
     they point to may overlap.

.. _`_copy_to_pages`:

_copy_to_pages
==============

.. c:function:: void _copy_to_pages(struct page **pages, size_t pgbase, const char *p, size_t len)

    :param pages:
        array of pages
    :type pages: struct page \*\*

    :param pgbase:
        page vector address of destination
    :type pgbase: size_t

    :param p:
        pointer to source data
    :type p: const char \*

    :param len:
        length
    :type len: size_t

.. _`_copy_to_pages.description`:

Description
-----------

Copies data from an arbitrary memory location into an array of pages
The copy is assumed to be non-overlapping.

.. _`_copy_from_pages`:

_copy_from_pages
================

.. c:function:: void _copy_from_pages(char *p, struct page **pages, size_t pgbase, size_t len)

    :param p:
        pointer to destination
    :type p: char \*

    :param pages:
        array of pages
    :type pages: struct page \*\*

    :param pgbase:
        offset of source data
    :type pgbase: size_t

    :param len:
        length
    :type len: size_t

.. _`_copy_from_pages.description`:

Description
-----------

Copies data into an arbitrary memory location from an array of pages
The copy is assumed to be non-overlapping.

.. _`xdr_shrink_bufhead`:

xdr_shrink_bufhead
==================

.. c:function:: void xdr_shrink_bufhead(struct xdr_buf *buf, size_t len)

    :param buf:
        xdr_buf
    :type buf: struct xdr_buf \*

    :param len:
        bytes to remove from buf->head[0]
    :type len: size_t

.. _`xdr_shrink_bufhead.description`:

Description
-----------

Shrinks XDR buffer's header kvec buf->head[0] by
'len' bytes. The extra data is not lost, but is instead
moved into the inlined pages and/or the tail.

.. _`xdr_shrink_pagelen`:

xdr_shrink_pagelen
==================

.. c:function:: void xdr_shrink_pagelen(struct xdr_buf *buf, size_t len)

    :param buf:
        xdr_buf
    :type buf: struct xdr_buf \*

    :param len:
        bytes to remove from buf->pages
    :type len: size_t

.. _`xdr_shrink_pagelen.description`:

Description
-----------

Shrinks XDR buffer's page array buf->pages by
'len' bytes. The extra data is not lost, but is instead
moved into the tail.

.. _`xdr_stream_pos`:

xdr_stream_pos
==============

.. c:function:: unsigned int xdr_stream_pos(const struct xdr_stream *xdr)

    Return the current offset from the start of the xdr_stream

    :param xdr:
        pointer to struct xdr_stream
    :type xdr: const struct xdr_stream \*

.. _`xdr_init_encode`:

xdr_init_encode
===============

.. c:function:: void xdr_init_encode(struct xdr_stream *xdr, struct xdr_buf *buf, __be32 *p)

    Initialize a struct xdr_stream for sending data.

    :param xdr:
        pointer to xdr_stream struct
    :type xdr: struct xdr_stream \*

    :param buf:
        pointer to XDR buffer in which to encode data
    :type buf: struct xdr_buf \*

    :param p:
        current pointer inside XDR buffer
    :type p: __be32 \*

.. _`xdr_init_encode.note`:

Note
----

at the moment the RPC client only passes the length of our
      scratch buffer in the xdr_buf's header kvec. Previously this
      meant we needed to call \ :c:func:`xdr_adjust_iovec`\  after encoding the
      data. With the new scheme, the xdr_stream manages the details
      of the buffer length, and takes care of adjusting the kvec
      length for us.

.. _`xdr_commit_encode`:

xdr_commit_encode
=================

.. c:function:: void xdr_commit_encode(struct xdr_stream *xdr)

    Ensure all data is written to buffer

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

.. _`xdr_commit_encode.description`:

Description
-----------

We handle encoding across page boundaries by giving the caller a
temporary location to write to, then later copying the data into
place; xdr_commit_encode does that copying.

Normally the caller doesn't need to call this directly, as the
following xdr_reserve_space will do it.  But an explicit call may be
required at the end of encoding, or any other time when the xdr_buf
data might be read.

.. _`xdr_reserve_space`:

xdr_reserve_space
=================

.. c:function:: __be32 *xdr_reserve_space(struct xdr_stream *xdr, size_t nbytes)

    Reserve buffer space for sending

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param nbytes:
        number of bytes to reserve
    :type nbytes: size_t

.. _`xdr_reserve_space.description`:

Description
-----------

Checks that we have enough buffer space to encode 'nbytes' more
bytes of data. If so, update the total xdr_buf length, and
adjust the length of the current kvec.

.. _`xdr_truncate_encode`:

xdr_truncate_encode
===================

.. c:function:: void xdr_truncate_encode(struct xdr_stream *xdr, size_t len)

    truncate an encode buffer

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param len:
        new length of buffer
    :type len: size_t

.. _`xdr_truncate_encode.description`:

Description
-----------

Truncates the xdr stream, so that xdr->buf->len == len,
and xdr->p points at offset len from the start of the buffer, and
head, tail, and page lengths are adjusted to correspond.

If this means moving xdr->p to a different buffer, we assume that
that the end pointer should be set to the end of the current page,
except in the case of the head buffer when we assume the head
buffer's current length represents the end of the available buffer.

This is *not* safe to use on a buffer that already has inlined page
cache pages (as in a zero-copy server read reply), except for the
simple case of truncating from one position in the tail to another.

.. _`xdr_restrict_buflen`:

xdr_restrict_buflen
===================

.. c:function:: int xdr_restrict_buflen(struct xdr_stream *xdr, int newbuflen)

    decrease available buffer space

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param newbuflen:
        new maximum number of bytes available
    :type newbuflen: int

.. _`xdr_restrict_buflen.description`:

Description
-----------

Adjust our idea of how much space is available in the buffer.
If we've already used too much space in the buffer, returns -1.
If the available space is already smaller than newbuflen, returns 0
and does nothing.  Otherwise, adjusts xdr->buf->buflen to newbuflen
and ensures xdr->end is set at most offset newbuflen from the start
of the buffer.

.. _`xdr_write_pages`:

xdr_write_pages
===============

.. c:function:: void xdr_write_pages(struct xdr_stream *xdr, struct page **pages, unsigned int base, unsigned int len)

    Insert a list of pages into an XDR buffer for sending

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param pages:
        list of pages
    :type pages: struct page \*\*

    :param base:
        offset of first byte
    :type base: unsigned int

    :param len:
        length of data in bytes
    :type len: unsigned int

.. _`xdr_init_decode`:

xdr_init_decode
===============

.. c:function:: void xdr_init_decode(struct xdr_stream *xdr, struct xdr_buf *buf, __be32 *p)

    Initialize an xdr_stream for decoding data.

    :param xdr:
        pointer to xdr_stream struct
    :type xdr: struct xdr_stream \*

    :param buf:
        pointer to XDR buffer from which to decode data
    :type buf: struct xdr_buf \*

    :param p:
        current pointer inside XDR buffer
    :type p: __be32 \*

.. _`xdr_init_decode_pages`:

xdr_init_decode_pages
=====================

.. c:function:: void xdr_init_decode_pages(struct xdr_stream *xdr, struct xdr_buf *buf, struct page **pages, unsigned int len)

    Initialize an xdr_stream for decoding into pages

    :param xdr:
        pointer to xdr_stream struct
    :type xdr: struct xdr_stream \*

    :param buf:
        pointer to XDR buffer from which to decode data
    :type buf: struct xdr_buf \*

    :param pages:
        list of pages to decode into
    :type pages: struct page \*\*

    :param len:
        length in bytes of buffer in pages
    :type len: unsigned int

.. _`xdr_set_scratch_buffer`:

xdr_set_scratch_buffer
======================

.. c:function:: void xdr_set_scratch_buffer(struct xdr_stream *xdr, void *buf, size_t buflen)

    Attach a scratch buffer for decoding data.

    :param xdr:
        pointer to xdr_stream struct
    :type xdr: struct xdr_stream \*

    :param buf:
        pointer to an empty buffer
    :type buf: void \*

    :param buflen:
        size of 'buf'
    :type buflen: size_t

.. _`xdr_set_scratch_buffer.description`:

Description
-----------

The scratch buffer is used when decoding from an array of pages.
If an \ :c:func:`xdr_inline_decode`\  call spans across page boundaries, then
we copy the data into the scratch buffer in order to allow linear
access.

.. _`xdr_inline_decode`:

xdr_inline_decode
=================

.. c:function:: __be32 *xdr_inline_decode(struct xdr_stream *xdr, size_t nbytes)

    Retrieve XDR data to decode

    :param xdr:
        pointer to xdr_stream struct
    :type xdr: struct xdr_stream \*

    :param nbytes:
        number of bytes of data to decode
    :type nbytes: size_t

.. _`xdr_inline_decode.description`:

Description
-----------

Check if the input buffer is long enough to enable us to decode
'nbytes' more bytes of data starting at the current position.
If so return the current pointer, then update the current
pointer position.

.. _`xdr_read_pages`:

xdr_read_pages
==============

.. c:function:: unsigned int xdr_read_pages(struct xdr_stream *xdr, unsigned int len)

    Ensure page-based XDR data to decode is aligned at current pointer position

    :param xdr:
        pointer to xdr_stream struct
    :type xdr: struct xdr_stream \*

    :param len:
        number of bytes of page data
    :type len: unsigned int

.. _`xdr_read_pages.description`:

Description
-----------

Moves data beyond the current pointer position from the XDR head[] buffer
into the page list. Any data that lies beyond current position + "len"
bytes is moved into the XDR tail[].

Returns the number of XDR encoded bytes now contained in the pages

.. _`xdr_enter_page`:

xdr_enter_page
==============

.. c:function:: void xdr_enter_page(struct xdr_stream *xdr, unsigned int len)

    decode data from the XDR page

    :param xdr:
        pointer to xdr_stream struct
    :type xdr: struct xdr_stream \*

    :param len:
        number of bytes of page data
    :type len: unsigned int

.. _`xdr_enter_page.description`:

Description
-----------

Moves data beyond the current pointer position from the XDR head[] buffer
into the page list. Any data that lies beyond current position + "len"
bytes is moved into the XDR tail[]. The current pointer is then
repositioned at the beginning of the first XDR page.

.. _`xdr_buf_subsegment`:

xdr_buf_subsegment
==================

.. c:function:: int xdr_buf_subsegment(struct xdr_buf *buf, struct xdr_buf *subbuf, unsigned int base, unsigned int len)

    set subbuf to a portion of buf

    :param buf:
        an xdr buffer
    :type buf: struct xdr_buf \*

    :param subbuf:
        the result buffer
    :type subbuf: struct xdr_buf \*

    :param base:
        beginning of range in bytes
    :type base: unsigned int

    :param len:
        length of range in bytes
    :type len: unsigned int

.. _`xdr_buf_subsegment.description`:

Description
-----------

sets \ ``subbuf``\  to an xdr buffer representing the portion of \ ``buf``\  of
length \ ``len``\  starting at offset \ ``base``\ .

\ ``buf``\  and \ ``subbuf``\  may be pointers to the same struct xdr_buf.

Returns -1 if base of length are out of bounds.

.. _`xdr_buf_trim`:

xdr_buf_trim
============

.. c:function:: void xdr_buf_trim(struct xdr_buf *buf, unsigned int len)

    lop at most "len" bytes off the end of "buf"

    :param buf:
        buf to be trimmed
    :type buf: struct xdr_buf \*

    :param len:
        number of bytes to reduce "buf" by
    :type len: unsigned int

.. _`xdr_buf_trim.description`:

Description
-----------

Trim an xdr_buf by the given number of bytes by fixing up the lengths. Note
that it's possible that we'll trim less than that amount if the xdr_buf is
too small, or if (for instance) it's all in the head and the parser has
already read too far into it.

.. _`xdr_stream_decode_opaque`:

xdr_stream_decode_opaque
========================

.. c:function:: ssize_t xdr_stream_decode_opaque(struct xdr_stream *xdr, void *ptr, size_t size)

    Decode variable length opaque

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param ptr:
        location to store opaque data
    :type ptr: void \*

    :param size:
        size of storage buffer \ ``ptr``\ 
    :type size: size_t

.. _`xdr_stream_decode_opaque.return-values`:

Return values
-------------

  On success, returns size of object stored in *@ptr
  \ ``-EBADMSG``\  on XDR buffer overflow
  \ ``-EMSGSIZE``\  on overflow of storage buffer \ ``ptr``\ 

.. _`xdr_stream_decode_opaque_dup`:

xdr_stream_decode_opaque_dup
============================

.. c:function:: ssize_t xdr_stream_decode_opaque_dup(struct xdr_stream *xdr, void **ptr, size_t maxlen, gfp_t gfp_flags)

    Decode and duplicate variable length opaque

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param ptr:
        location to store pointer to opaque data
    :type ptr: void \*\*

    :param maxlen:
        maximum acceptable object size
    :type maxlen: size_t

    :param gfp_flags:
        GFP mask to use
    :type gfp_flags: gfp_t

.. _`xdr_stream_decode_opaque_dup.return-values`:

Return values
-------------

  On success, returns size of object stored in *@ptr
  \ ``-EBADMSG``\  on XDR buffer overflow
  \ ``-EMSGSIZE``\  if the size of the object would exceed \ ``maxlen``\ 
  \ ``-ENOMEM``\  on memory allocation failure

.. _`xdr_stream_decode_string`:

xdr_stream_decode_string
========================

.. c:function:: ssize_t xdr_stream_decode_string(struct xdr_stream *xdr, char *str, size_t size)

    Decode variable length string

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param str:
        location to store string
    :type str: char \*

    :param size:
        size of storage buffer \ ``str``\ 
    :type size: size_t

.. _`xdr_stream_decode_string.return-values`:

Return values
-------------

  On success, returns length of NUL-terminated string stored in *@str
  \ ``-EBADMSG``\  on XDR buffer overflow
  \ ``-EMSGSIZE``\  on overflow of storage buffer \ ``str``\ 

.. _`xdr_stream_decode_string_dup`:

xdr_stream_decode_string_dup
============================

.. c:function:: ssize_t xdr_stream_decode_string_dup(struct xdr_stream *xdr, char **str, size_t maxlen, gfp_t gfp_flags)

    Decode and duplicate variable length string

    :param xdr:
        pointer to xdr_stream
    :type xdr: struct xdr_stream \*

    :param str:
        location to store pointer to string
    :type str: char \*\*

    :param maxlen:
        maximum acceptable string length
    :type maxlen: size_t

    :param gfp_flags:
        GFP mask to use
    :type gfp_flags: gfp_t

.. _`xdr_stream_decode_string_dup.return-values`:

Return values
-------------

  On success, returns length of NUL-terminated string stored in *@ptr
  \ ``-EBADMSG``\  on XDR buffer overflow
  \ ``-EMSGSIZE``\  if the size of the string would exceed \ ``maxlen``\ 
  \ ``-ENOMEM``\  on memory allocation failure

.. This file was automatic generated / don't edit.

