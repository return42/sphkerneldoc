.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ppp/ppp_deflate.c

.. _`z_comp_free`:

z_comp_free
===========

.. c:function:: void z_comp_free(void *arg)

    free the memory used by a compressor

    :param arg:
        pointer to the private state for the compressor.
    :type arg: void \*

.. _`z_comp_alloc`:

z_comp_alloc
============

.. c:function:: void *z_comp_alloc(unsigned char *options, int opt_len)

    allocate space for a compressor.

    :param options:
        pointer to CCP option data
    :type options: unsigned char \*

    :param opt_len:
        length of the CCP option at \ ``options``\ .
    :type opt_len: int

.. _`z_comp_alloc.description`:

Description
-----------

The \ ``options``\  pointer points to the a buffer containing the
CCP option data for the compression being negotiated.  It is
formatted according to RFC1979, and describes the window
size that the peer is requesting that we use in compressing
data to be sent to it.

Returns the pointer to the private state for the compressor,
or NULL if we could not allocate enough memory.

.. _`z_comp_init`:

z_comp_init
===========

.. c:function:: int z_comp_init(void *arg, unsigned char *options, int opt_len, int unit, int hdrlen, int debug)

    initialize a previously-allocated compressor.

    :param arg:
        pointer to the private state for the compressor
    :type arg: void \*

    :param options:
        pointer to the CCP option data describing the
        compression that was negotiated with the peer
    :type options: unsigned char \*

    :param opt_len:
        length of the CCP option data at \ ``options``\ 
    :type opt_len: int

    :param unit:
        PPP unit number for diagnostic messages
    :type unit: int

    :param hdrlen:
        ignored (present for backwards compatibility)
    :type hdrlen: int

    :param debug:
        debug flag; if non-zero, debug messages are printed.
    :type debug: int

.. _`z_comp_init.description`:

Description
-----------

The CCP options described by \ ``options``\  must match the options
specified when the compressor was allocated.  The compressor
history is reset.  Returns 0 for failure (CCP options don't
match) or 1 for success.

.. _`z_comp_reset`:

z_comp_reset
============

.. c:function:: void z_comp_reset(void *arg)

    reset a previously-allocated compressor.

    :param arg:
        pointer to private state for the compressor.
    :type arg: void \*

.. _`z_comp_reset.description`:

Description
-----------

This clears the history for the compressor and makes it
ready to start emitting a new compressed stream.

.. _`z_compress`:

z_compress
==========

.. c:function:: int z_compress(void *arg, unsigned char *rptr, unsigned char *obuf, int isize, int osize)

    compress a PPP packet with Deflate compression.

    :param arg:
        pointer to private state for the compressor
    :type arg: void \*

    :param rptr:
        uncompressed packet (input)
    :type rptr: unsigned char \*

    :param obuf:
        compressed packet (output)
    :type obuf: unsigned char \*

    :param isize:
        size of uncompressed packet
    :type isize: int

    :param osize:
        space available at \ ``obuf``\ 
    :type osize: int

.. _`z_compress.description`:

Description
-----------

Returns the length of the compressed packet, or 0 if the
packet is incompressible.

.. _`z_comp_stats`:

z_comp_stats
============

.. c:function:: void z_comp_stats(void *arg, struct compstat *stats)

    return compression statistics for a compressor or decompressor.

    :param arg:
        pointer to private space for the (de)compressor
    :type arg: void \*

    :param stats:
        pointer to a struct compstat to receive the result.
    :type stats: struct compstat \*

.. _`z_decomp_free`:

z_decomp_free
=============

.. c:function:: void z_decomp_free(void *arg)

    Free the memory used by a decompressor.

    :param arg:
        pointer to private space for the decompressor.
    :type arg: void \*

.. _`z_decomp_alloc`:

z_decomp_alloc
==============

.. c:function:: void *z_decomp_alloc(unsigned char *options, int opt_len)

    allocate space for a decompressor.

    :param options:
        pointer to CCP option data
    :type options: unsigned char \*

    :param opt_len:
        length of the CCP option at \ ``options``\ .
    :type opt_len: int

.. _`z_decomp_alloc.description`:

Description
-----------

The \ ``options``\  pointer points to the a buffer containing the
CCP option data for the compression being negotiated.  It is
formatted according to RFC1979, and describes the window
size that we are requesting the peer to use in compressing
data to be sent to us.

Returns the pointer to the private state for the decompressor,
or NULL if we could not allocate enough memory.

.. _`z_decomp_init`:

z_decomp_init
=============

.. c:function:: int z_decomp_init(void *arg, unsigned char *options, int opt_len, int unit, int hdrlen, int mru, int debug)

    initialize a previously-allocated decompressor.

    :param arg:
        pointer to the private state for the decompressor
    :type arg: void \*

    :param options:
        pointer to the CCP option data describing the
        compression that was negotiated with the peer
    :type options: unsigned char \*

    :param opt_len:
        length of the CCP option data at \ ``options``\ 
    :type opt_len: int

    :param unit:
        PPP unit number for diagnostic messages
    :type unit: int

    :param hdrlen:
        ignored (present for backwards compatibility)
    :type hdrlen: int

    :param mru:
        maximum length of decompressed packets
    :type mru: int

    :param debug:
        debug flag; if non-zero, debug messages are printed.
    :type debug: int

.. _`z_decomp_init.description`:

Description
-----------

The CCP options described by \ ``options``\  must match the options
specified when the decompressor was allocated.  The decompressor
history is reset.  Returns 0 for failure (CCP options don't
match) or 1 for success.

.. _`z_decomp_reset`:

z_decomp_reset
==============

.. c:function:: void z_decomp_reset(void *arg)

    reset a previously-allocated decompressor.

    :param arg:
        pointer to private state for the decompressor.
    :type arg: void \*

.. _`z_decomp_reset.description`:

Description
-----------

This clears the history for the decompressor and makes it
ready to receive a new compressed stream.

.. _`z_decompress`:

z_decompress
============

.. c:function:: int z_decompress(void *arg, unsigned char *ibuf, int isize, unsigned char *obuf, int osize)

    decompress a Deflate-compressed packet.

    :param arg:
        pointer to private state for the decompressor
    :type arg: void \*

    :param ibuf:
        pointer to input (compressed) packet data
    :type ibuf: unsigned char \*

    :param isize:
        length of input packet
    :type isize: int

    :param obuf:
        pointer to space for output (decompressed) packet
    :type obuf: unsigned char \*

    :param osize:
        amount of space available at \ ``obuf``\ 
    :type osize: int

.. _`z_decompress.description`:

Description
-----------

Because of patent problems, we return DECOMP_ERROR for errors
found by inspecting the input data and for system problems, but
DECOMP_FATALERROR for any errors which could possibly be said to
be being detected "after" decompression.  For DECOMP_ERROR,
we can issue a CCP reset-request; for DECOMP_FATALERROR, we may be
infringing a patent of Motorola's if we do, so we take CCP down
instead.

Given that the frame has the correct sequence number and a good FCS,
errors such as invalid codes in the input most likely indicate a
bug, so we return DECOMP_FATALERROR for them in order to turn off
compression, even though they are detected by inspecting the input.

.. _`z_incomp`:

z_incomp
========

.. c:function:: void z_incomp(void *arg, unsigned char *ibuf, int icnt)

    add incompressible input data to the history.

    :param arg:
        pointer to private state for the decompressor
    :type arg: void \*

    :param ibuf:
        pointer to input packet data
    :type ibuf: unsigned char \*

    :param icnt:
        length of input data.
    :type icnt: int

.. This file was automatic generated / don't edit.

