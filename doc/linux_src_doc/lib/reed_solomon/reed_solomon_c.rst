.. -*- coding: utf-8; mode: rst -*-

==============
reed_solomon.c
==============

.. _`rs_init`:

rs_init
=======

.. c:function:: struct rs_control *rs_init (int symsize, int gfpoly, int (*gffunc) (int, int fcr, int prim, int nroots)

    Initialize a Reed-Solomon codec

    :param int symsize:
        symbol size, bits (1-8)

    :param int gfpoly:
        Field generator polynomial coefficients

    :param int (\*gffunc) (int):
        Field generator function

    :param int fcr:
        first root of RS code generator polynomial, index form

    :param int prim:
        primitive element to generate polynomial roots

    :param int nroots:
        RS code generator polynomial degree (number of roots)


.. _`rs_init.description`:

Description
-----------

Allocate a control structure and the polynom arrays for faster
en/decoding. Fill the arrays according to the given parameters.


.. _`free_rs`:

free_rs
=======

.. c:function:: void free_rs (struct rs_control *rs)

    Free the rs control structure, if it is no longer used

    :param struct rs_control \*rs:
        the control structure which is not longer used by the
        caller


.. _`init_rs_internal`:

init_rs_internal
================

.. c:function:: struct rs_control *init_rs_internal (int symsize, int gfpoly, int (*gffunc) (int, int fcr, int prim, int nroots)

    Find a matching or allocate a new rs control structure

    :param int symsize:
        the symbol size (number of bits)

    :param int gfpoly:
        the extended Galois field generator polynomial coefficients,
        with the 0th coefficient in the low order bit. The polynomial
        must be primitive;

    :param int (\*gffunc) (int):
        pointer to function to generate the next field element,
        or the multiplicative identity element if given 0.  Used
        instead of gfpoly if gfpoly is 0

    :param int fcr:
        the first consecutive root of the rs code generator polynomial
        in index form

    :param int prim:
        primitive element to generate polynomial roots

    :param int nroots:
        RS code generator polynomial degree (number of roots)


.. _`init_rs`:

init_rs
=======

.. c:function:: struct rs_control *init_rs (int symsize, int gfpoly, int fcr, int prim, int nroots)

    Find a matching or allocate a new rs control structure

    :param int symsize:
        the symbol size (number of bits)

    :param int gfpoly:
        the extended Galois field generator polynomial coefficients,
        with the 0th coefficient in the low order bit. The polynomial
        must be primitive;

    :param int fcr:
        the first consecutive root of the rs code generator polynomial
        in index form

    :param int prim:
        primitive element to generate polynomial roots

    :param int nroots:
        RS code generator polynomial degree (number of roots)


.. _`init_rs_non_canonical`:

init_rs_non_canonical
=====================

.. c:function:: struct rs_control *init_rs_non_canonical (int symsize, int (*gffunc) (int, int fcr, int prim, int nroots)

    Find a matching or allocate a new rs control structure, for fields with non-canonical representation

    :param int symsize:
        the symbol size (number of bits)

    :param int (\*gffunc) (int):
        pointer to function to generate the next field element,
        or the multiplicative identity element if given 0.  Used
        instead of gfpoly if gfpoly is 0

    :param int fcr:
        the first consecutive root of the rs code generator polynomial
        in index form

    :param int prim:
        primitive element to generate polynomial roots

    :param int nroots:
        RS code generator polynomial degree (number of roots)


.. _`encode_rs8`:

encode_rs8
==========

.. c:function:: int encode_rs8 (struct rs_control *rs, uint8_t *data, int len, uint16_t *par, uint16_t invmsk)

    Calculate the parity for data values (8bit data width)

    :param struct rs_control \*rs:
        the rs control structure

    :param uint8_t \*data:
        data field of a given type

    :param int len:
        data length

    :param uint16_t \*par:
        parity data, must be initialized by caller (usually all 0)

    :param uint16_t invmsk:
        invert data mask (will be xored on data)


.. _`encode_rs8.description`:

Description
-----------

The parity uses a uint16_t data type to enable
symbol size > 8. The calling code must take care of encoding of the
syndrome result for storage itself.


.. _`decode_rs8`:

decode_rs8
==========

.. c:function:: int decode_rs8 (struct rs_control *rs, uint8_t *data, uint16_t *par, int len, uint16_t *s, int no_eras, int *eras_pos, uint16_t invmsk, uint16_t *corr)

    Decode codeword (8bit data width)

    :param struct rs_control \*rs:
        the rs control structure

    :param uint8_t \*data:
        data field of a given type

    :param uint16_t \*par:
        received parity data field

    :param int len:
        data length

    :param uint16_t \*s:
        syndrome data field (if NULL, syndrome is calculated)

    :param int no_eras:
        number of erasures

    :param int \*eras_pos:
        position of erasures, can be NULL

    :param uint16_t invmsk:
        invert data mask (will be xored on data, not on parity!)

    :param uint16_t \*corr:
        buffer to store correction bitmask on eras_pos


.. _`decode_rs8.description`:

Description
-----------

The syndrome and parity uses a uint16_t data type to enable
symbol size > 8. The calling code must take care of decoding of the
syndrome result and the received parity before calling this code.
Returns the number of corrected bits or -EBADMSG for uncorrectable errors.


.. _`encode_rs16`:

encode_rs16
===========

.. c:function:: int encode_rs16 (struct rs_control *rs, uint16_t *data, int len, uint16_t *par, uint16_t invmsk)

    Calculate the parity for data values (16bit data width)

    :param struct rs_control \*rs:
        the rs control structure

    :param uint16_t \*data:
        data field of a given type

    :param int len:
        data length

    :param uint16_t \*par:
        parity data, must be initialized by caller (usually all 0)

    :param uint16_t invmsk:
        invert data mask (will be xored on data, not on parity!)


.. _`encode_rs16.description`:

Description
-----------

Each field in the data array contains up to symbol size bits of valid data.


.. _`decode_rs16`:

decode_rs16
===========

.. c:function:: int decode_rs16 (struct rs_control *rs, uint16_t *data, uint16_t *par, int len, uint16_t *s, int no_eras, int *eras_pos, uint16_t invmsk, uint16_t *corr)

    Decode codeword (16bit data width)

    :param struct rs_control \*rs:
        the rs control structure

    :param uint16_t \*data:
        data field of a given type

    :param uint16_t \*par:
        received parity data field

    :param int len:
        data length

    :param uint16_t \*s:
        syndrome data field (if NULL, syndrome is calculated)

    :param int no_eras:
        number of erasures

    :param int \*eras_pos:
        position of erasures, can be NULL

    :param uint16_t invmsk:
        invert data mask (will be xored on data, not on parity!)

    :param uint16_t \*corr:
        buffer to store correction bitmask on eras_pos


.. _`decode_rs16.description`:

Description
-----------

Each field in the data array contains up to symbol size bits of valid data.
Returns the number of corrected bits or -EBADMSG for uncorrectable errors.

