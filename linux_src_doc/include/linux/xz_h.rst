.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/xz.h

.. _`xz_mode`:

enum xz_mode
============

.. c:type:: enum xz_mode

    Operation mode

.. _`xz_mode.definition`:

Definition
----------

.. code-block:: c

    enum xz_mode {
        XZ_SINGLE,
        XZ_PREALLOC,
        XZ_DYNALLOC
    };

.. _`xz_mode.constants`:

Constants
---------

XZ_SINGLE
    Single-call mode. This uses less RAM than
    than multi-call modes, because the LZMA2
    dictionary doesn't need to be allocated as
    part of the decoder state. All required data
    structures are allocated at initialization,
    so \ :c:func:`xz_dec_run`\  cannot return XZ_MEM_ERROR.

XZ_PREALLOC
    Multi-call mode with preallocated LZMA2
    dictionary buffer. All data structures are
    allocated at initialization, so \ :c:func:`xz_dec_run`\ 
    cannot return XZ_MEM_ERROR.

XZ_DYNALLOC
    Multi-call mode. The LZMA2 dictionary is
    allocated once the required size has been
    parsed from the stream headers. If the
    allocation fails, \ :c:func:`xz_dec_run`\  will return
    XZ_MEM_ERROR.

.. _`xz_mode.description`:

Description
-----------

It is possible to enable support only for a subset of the above
modes at compile time by defining XZ_DEC_SINGLE, XZ_DEC_PREALLOC,
or XZ_DEC_DYNALLOC. The xz_dec kernel module is always compiled
with support for all operation modes, but the preboot code may
be built with fewer features to minimize code size.

.. _`xz_ret`:

enum xz_ret
===========

.. c:type:: enum xz_ret

    Return codes

.. _`xz_ret.definition`:

Definition
----------

.. code-block:: c

    enum xz_ret {
        XZ_OK,
        XZ_STREAM_END,
        XZ_UNSUPPORTED_CHECK,
        XZ_MEM_ERROR,
        XZ_MEMLIMIT_ERROR,
        XZ_FORMAT_ERROR,
        XZ_OPTIONS_ERROR,
        XZ_DATA_ERROR,
        XZ_BUF_ERROR
    };

.. _`xz_ret.constants`:

Constants
---------

XZ_OK
    Everything is OK so far. More input or more
    output space is required to continue. This
    return code is possible only in multi-call mode
    (XZ_PREALLOC or XZ_DYNALLOC).

XZ_STREAM_END
    Operation finished successfully.

XZ_UNSUPPORTED_CHECK
    Integrity check type is not supported. Decoding
    is still possible in multi-call mode by simply
    calling \ :c:func:`xz_dec_run`\  again.
    Note that this return value is used only if
    XZ_DEC_ANY_CHECK was defined at build time,
    which is not used in the kernel. Unsupported
    check types return XZ_OPTIONS_ERROR if
    XZ_DEC_ANY_CHECK was not defined at build time.

XZ_MEM_ERROR
    Allocating memory failed. This return code is
    possible only if the decoder was initialized
    with XZ_DYNALLOC. The amount of memory that was
    tried to be allocated was no more than the
    dict_max argument given to \ :c:func:`xz_dec_init`\ .

XZ_MEMLIMIT_ERROR
    A bigger LZMA2 dictionary would be needed than
    allowed by the dict_max argument given to
    \ :c:func:`xz_dec_init`\ . This return value is possible
    only in multi-call mode (XZ_PREALLOC or
    XZ_DYNALLOC); the single-call mode (XZ_SINGLE)
    ignores the dict_max argument.

XZ_FORMAT_ERROR
    File format was not recognized (wrong magic
    bytes).

XZ_OPTIONS_ERROR
    This implementation doesn't support the requested
    compression options. In the decoder this means
    that the header CRC32 matches, but the header
    itself specifies something that we don't support.

XZ_DATA_ERROR
    Compressed data is corrupt.

XZ_BUF_ERROR
    Cannot make any progress. Details are slightly
    different between multi-call and single-call
    mode; more information below.

.. _`xz_ret.description`:

Description
-----------

In multi-call mode, XZ_BUF_ERROR is returned when two consecutive calls
to XZ code cannot consume any input and cannot produce any new output.
This happens when there is no new input available, or the output buffer
is full while at least one output byte is still pending. Assuming your
code is not buggy, you can get this error only when decoding a compressed
stream that is truncated or otherwise corrupt.

In single-call mode, XZ_BUF_ERROR is returned only when the output buffer
is too small or the compressed input is corrupt in a way that makes the
decoder produce more output than the caller expected. When it is
(relatively) clear that the compressed input is truncated, XZ_DATA_ERROR
is used instead of XZ_BUF_ERROR.

.. _`xz_buf`:

struct xz_buf
=============

.. c:type:: struct xz_buf

    Passing input and output buffers to XZ code

.. _`xz_buf.definition`:

Definition
----------

.. code-block:: c

    struct xz_buf {
        const uint8_t *in;
        size_t in_pos;
        size_t in_size;
        uint8_t *out;
        size_t out_pos;
        size_t out_size;
    }

.. _`xz_buf.members`:

Members
-------

in
    Beginning of the input buffer. This may be NULL if and only
    if in_pos is equal to in_size.

in_pos
    Current position in the input buffer. This must not exceed
    in_size.

in_size
    Size of the input buffer

out
    Beginning of the output buffer. This may be NULL if and only
    if out_pos is equal to out_size.

out_pos
    Current position in the output buffer. This must not exceed
    out_size.

out_size
    Size of the output buffer

.. _`xz_buf.description`:

Description
-----------

Only the contents of the output buffer from out[out_pos] onward, and
the variables in_pos and out_pos are modified by the XZ code.

.. _`xz_dec_init`:

xz_dec_init
===========

.. c:function:: XZ_EXTERN struct xz_dec *xz_dec_init(enum xz_mode mode, uint32_t dict_max)

    Allocate and initialize a XZ decoder state

    :param mode:
        Operation mode
    :type mode: enum xz_mode

    :param dict_max:
        Maximum size of the LZMA2 dictionary (history buffer) for
        multi-call decoding. This is ignored in single-call mode
        (mode == XZ_SINGLE). LZMA2 dictionary is always 2^n bytes
        or 2^n + 2^(n-1) bytes (the latter sizes are less common
        in practice), so other values for dict_max don't make sense.
        In the kernel, dictionary sizes of 64 KiB, 128 KiB, 256 KiB,
        512 KiB, and 1 MiB are probably the only reasonable values,
        except for kernel and initramfs images where a bigger
        dictionary can be fine and useful.
    :type dict_max: uint32_t

.. _`xz_dec_init.description`:

Description
-----------

Single-call mode (XZ_SINGLE): \ :c:func:`xz_dec_run`\  decodes the whole stream at
once. The caller must provide enough output space or the decoding will
fail. The output space is used as the dictionary buffer, which is why
there is no need to allocate the dictionary as part of the decoder's
internal state.

Because the output buffer is used as the workspace, streams encoded using
a big dictionary are not a problem in single-call mode. It is enough that
the output buffer is big enough to hold the actual uncompressed data; it
can be smaller than the dictionary size stored in the stream headers.

Multi-call mode with preallocated dictionary (XZ_PREALLOC): dict_max bytes
of memory is preallocated for the LZMA2 dictionary. This way there is no
risk that \ :c:func:`xz_dec_run`\  could run out of memory, since \ :c:func:`xz_dec_run`\  will
never allocate any memory. Instead, if the preallocated dictionary is too
small for decoding the given input stream, \ :c:func:`xz_dec_run`\  will return
XZ_MEMLIMIT_ERROR. Thus, it is important to know what kind of data will be
decoded to avoid allocating excessive amount of memory for the dictionary.

Multi-call mode with dynamically allocated dictionary (XZ_DYNALLOC):
dict_max specifies the maximum allowed dictionary size that \ :c:func:`xz_dec_run`\ 
may allocate once it has parsed the dictionary size from the stream
headers. This way excessive allocations can be avoided while still
limiting the maximum memory usage to a sane value to prevent running the
system out of memory when decompressing streams from untrusted sources.

On success, \ :c:func:`xz_dec_init`\  returns a pointer to struct xz_dec, which is
ready to be used with \ :c:func:`xz_dec_run`\ . If memory allocation fails,
\ :c:func:`xz_dec_init`\  returns NULL.

.. _`xz_dec_run`:

xz_dec_run
==========

.. c:function:: XZ_EXTERN enum xz_ret xz_dec_run(struct xz_dec *s, struct xz_buf *b)

    Run the XZ decoder

    :param s:
        Decoder state allocated using \ :c:func:`xz_dec_init`\ 
    :type s: struct xz_dec \*

    :param b:
        Input and output buffers
    :type b: struct xz_buf \*

.. _`xz_dec_run.description`:

Description
-----------

The possible return values depend on build options and operation mode.
See enum xz_ret for details.

Note that if an error occurs in single-call mode (return value is not
XZ_STREAM_END), b->in_pos and b->out_pos are not modified and the
contents of the output buffer from b->out[b->out_pos] onward are
undefined. This is true even after XZ_BUF_ERROR, because with some filter
chains, there may be a second pass over the output buffer, and this pass
cannot be properly done if the output buffer is truncated. Thus, you
cannot give the single-call decoder a too small buffer and then expect to
get that amount valid data from the beginning of the stream. You must use
the multi-call decoder if you don't want to uncompress the whole stream.

.. _`xz_dec_reset`:

xz_dec_reset
============

.. c:function:: XZ_EXTERN void xz_dec_reset(struct xz_dec *s)

    Reset an already allocated decoder state

    :param s:
        Decoder state allocated using \ :c:func:`xz_dec_init`\ 
    :type s: struct xz_dec \*

.. _`xz_dec_reset.description`:

Description
-----------

This function can be used to reset the multi-call decoder state without
freeing and reallocating memory with \ :c:func:`xz_dec_end`\  and \ :c:func:`xz_dec_init`\ .

In single-call mode, \ :c:func:`xz_dec_reset`\  is always called in the beginning of
\ :c:func:`xz_dec_run`\ . Thus, explicit call to \ :c:func:`xz_dec_reset`\  is useful only in
multi-call mode.

.. _`xz_dec_end`:

xz_dec_end
==========

.. c:function:: XZ_EXTERN void xz_dec_end(struct xz_dec *s)

    Free the memory allocated for the decoder state

    :param s:
        Decoder state allocated using \ :c:func:`xz_dec_init`\ . If s is NULL,
        this function does nothing.
    :type s: struct xz_dec \*

.. This file was automatic generated / don't edit.

