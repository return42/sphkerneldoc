.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/reed_solomon/reed_solomon.c

.. _`codec_init`:

codec_init
==========

.. c:function:: struct rs_codec *codec_init(int symsize, int gfpoly, int (*gffunc)(int), int fcr, int prim, int nroots, gfp_t gfp)

    Initialize a Reed-Solomon codec

    :param symsize:
        symbol size, bits (1-8)
    :type symsize: int

    :param gfpoly:
        Field generator polynomial coefficients
    :type gfpoly: int

    :param int (\*gffunc)(int):
        Field generator function

    :param fcr:
        first root of RS code generator polynomial, index form
    :type fcr: int

    :param prim:
        primitive element to generate polynomial roots
    :type prim: int

    :param nroots:
        RS code generator polynomial degree (number of roots)
    :type nroots: int

    :param gfp:
        GFP_ flags for allocations
    :type gfp: gfp_t

.. _`codec_init.description`:

Description
-----------

Allocate a codec structure and the polynom arrays for faster
en/decoding. Fill the arrays according to the given parameters.

.. _`free_rs`:

free_rs
=======

.. c:function:: void free_rs(struct rs_control *rs)

    Free the rs control structure

    :param rs:
        The control structure which is not longer used by the
        caller
    :type rs: struct rs_control \*

.. _`free_rs.description`:

Description
-----------

Free the control structure. If \ ``rs``\  is the last user of the associated
codec, free the codec as well.

.. _`init_rs_internal`:

init_rs_internal
================

.. c:function:: struct rs_control *init_rs_internal(int symsize, int gfpoly, int (*gffunc)(int), int fcr, int prim, int nroots, gfp_t gfp)

    Allocate rs control, find a matching codec or allocate a new one

    :param symsize:
        the symbol size (number of bits)
    :type symsize: int

    :param gfpoly:
        the extended Galois field generator polynomial coefficients,
        with the 0th coefficient in the low order bit. The polynomial
        must be primitive;
    :type gfpoly: int

    :param int (\*gffunc)(int):
        pointer to function to generate the next field element,
        or the multiplicative identity element if given 0.  Used
        instead of gfpoly if gfpoly is 0

    :param fcr:
        the first consecutive root of the rs code generator polynomial
        in index form
    :type fcr: int

    :param prim:
        primitive element to generate polynomial roots
    :type prim: int

    :param nroots:
        RS code generator polynomial degree (number of roots)
    :type nroots: int

    :param gfp:
        GFP_ flags for allocations
    :type gfp: gfp_t

.. _`init_rs_gfp`:

init_rs_gfp
===========

.. c:function:: struct rs_control *init_rs_gfp(int symsize, int gfpoly, int fcr, int prim, int nroots, gfp_t gfp)

    Create a RS control struct and initialize it

    :param symsize:
        the symbol size (number of bits)
    :type symsize: int

    :param gfpoly:
        the extended Galois field generator polynomial coefficients,
        with the 0th coefficient in the low order bit. The polynomial
        must be primitive;
    :type gfpoly: int

    :param fcr:
        the first consecutive root of the rs code generator polynomial
        in index form
    :type fcr: int

    :param prim:
        primitive element to generate polynomial roots
    :type prim: int

    :param nroots:
        RS code generator polynomial degree (number of roots)
    :type nroots: int

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`init_rs_non_canonical`:

init_rs_non_canonical
=====================

.. c:function:: struct rs_control *init_rs_non_canonical(int symsize, int (*gffunc)(int), int fcr, int prim, int nroots)

    Allocate rs control struct for fields with non-canonical representation

    :param symsize:
        the symbol size (number of bits)
    :type symsize: int

    :param int (\*gffunc)(int):
        pointer to function to generate the next field element,
        or the multiplicative identity element if given 0.  Used
        instead of gfpoly if gfpoly is 0

    :param fcr:
        the first consecutive root of the rs code generator polynomial
        in index form
    :type fcr: int

    :param prim:
        primitive element to generate polynomial roots
    :type prim: int

    :param nroots:
        RS code generator polynomial degree (number of roots)
    :type nroots: int

.. _`encode_rs8`:

encode_rs8
==========

.. c:function:: int encode_rs8(struct rs_control *rsc, uint8_t *data, int len, uint16_t *par, uint16_t invmsk)

    Calculate the parity for data values (8bit data width)

    :param rsc:
        the rs control structure
    :type rsc: struct rs_control \*

    :param data:
        data field of a given type
    :type data: uint8_t \*

    :param len:
        data length
    :type len: int

    :param par:
        parity data, must be initialized by caller (usually all 0)
    :type par: uint16_t \*

    :param invmsk:
        invert data mask (will be xored on data)
    :type invmsk: uint16_t

.. _`encode_rs8.description`:

Description
-----------

 The parity uses a uint16_t data type to enable
 symbol size > 8. The calling code must take care of encoding of the
 syndrome result for storage itself.

.. _`decode_rs8`:

decode_rs8
==========

.. c:function:: int decode_rs8(struct rs_control *rsc, uint8_t *data, uint16_t *par, int len, uint16_t *s, int no_eras, int *eras_pos, uint16_t invmsk, uint16_t *corr)

    Decode codeword (8bit data width)

    :param rsc:
        the rs control structure
    :type rsc: struct rs_control \*

    :param data:
        data field of a given type
    :type data: uint8_t \*

    :param par:
        received parity data field
    :type par: uint16_t \*

    :param len:
        data length
    :type len: int

    :param s:
        syndrome data field (if NULL, syndrome is calculated)
    :type s: uint16_t \*

    :param no_eras:
        number of erasures
    :type no_eras: int

    :param eras_pos:
        position of erasures, can be NULL
    :type eras_pos: int \*

    :param invmsk:
        invert data mask (will be xored on data, not on parity!)
    :type invmsk: uint16_t

    :param corr:
        buffer to store correction bitmask on eras_pos
    :type corr: uint16_t \*

.. _`decode_rs8.description`:

Description
-----------

 The syndrome and parity uses a uint16_t data type to enable
 symbol size > 8. The calling code must take care of decoding of the
 syndrome result and the received parity before calling this code.

.. _`decode_rs8.note`:

Note
----

The rs_control struct \ ``rsc``\  contains buffers which are used for
 decoding, so the caller has to ensure that decoder invocations are
 serialized.

 Returns the number of corrected bits or -EBADMSG for uncorrectable errors.

.. _`encode_rs16`:

encode_rs16
===========

.. c:function:: int encode_rs16(struct rs_control *rsc, uint16_t *data, int len, uint16_t *par, uint16_t invmsk)

    Calculate the parity for data values (16bit data width)

    :param rsc:
        the rs control structure
    :type rsc: struct rs_control \*

    :param data:
        data field of a given type
    :type data: uint16_t \*

    :param len:
        data length
    :type len: int

    :param par:
        parity data, must be initialized by caller (usually all 0)
    :type par: uint16_t \*

    :param invmsk:
        invert data mask (will be xored on data, not on parity!)
    :type invmsk: uint16_t

.. _`encode_rs16.description`:

Description
-----------

 Each field in the data array contains up to symbol size bits of valid data.

.. _`decode_rs16`:

decode_rs16
===========

.. c:function:: int decode_rs16(struct rs_control *rsc, uint16_t *data, uint16_t *par, int len, uint16_t *s, int no_eras, int *eras_pos, uint16_t invmsk, uint16_t *corr)

    Decode codeword (16bit data width)

    :param rsc:
        the rs control structure
    :type rsc: struct rs_control \*

    :param data:
        data field of a given type
    :type data: uint16_t \*

    :param par:
        received parity data field
    :type par: uint16_t \*

    :param len:
        data length
    :type len: int

    :param s:
        syndrome data field (if NULL, syndrome is calculated)
    :type s: uint16_t \*

    :param no_eras:
        number of erasures
    :type no_eras: int

    :param eras_pos:
        position of erasures, can be NULL
    :type eras_pos: int \*

    :param invmsk:
        invert data mask (will be xored on data, not on parity!)
    :type invmsk: uint16_t

    :param corr:
        buffer to store correction bitmask on eras_pos
    :type corr: uint16_t \*

.. _`decode_rs16.description`:

Description
-----------

 Each field in the data array contains up to symbol size bits of valid data.

.. _`decode_rs16.note`:

Note
----

The rc_control struct \ ``rsc``\  contains buffers which are used for
 decoding, so the caller has to ensure that decoder invocations are
 serialized.

 Returns the number of corrected bits or -EBADMSG for uncorrectable errors.

.. This file was automatic generated / don't edit.

