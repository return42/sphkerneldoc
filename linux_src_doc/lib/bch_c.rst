.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/bch.c

.. _`encode_bch`:

encode_bch
==========

.. c:function:: void encode_bch(struct bch_control *bch, const uint8_t *data, unsigned int len, uint8_t *ecc)

    calculate BCH ecc parity of data

    :param bch:
        BCH control structure
    :type bch: struct bch_control \*

    :param data:
        data to encode
    :type data: const uint8_t \*

    :param len:
        data length in bytes
    :type len: unsigned int

    :param ecc:
        ecc parity data, must be initialized by caller
    :type ecc: uint8_t \*

.. _`encode_bch.description`:

Description
-----------

The \ ``ecc``\  parity array is used both as input and output parameter, in order to
allow incremental computations. It should be of the size indicated by member
\ ``ecc_bytes``\  of \ ``bch``\ , and should be initialized to 0 before the first call.

The exact number of computed ecc parity bits is given by member \ ``ecc_bits``\  of
\ ``bch``\ ; it may be less than m\*t for large values of t.

.. _`decode_bch`:

decode_bch
==========

.. c:function:: int decode_bch(struct bch_control *bch, const uint8_t *data, unsigned int len, const uint8_t *recv_ecc, const uint8_t *calc_ecc, const unsigned int *syn, unsigned int *errloc)

    decode received codeword and find bit error locations

    :param bch:
        BCH control structure
    :type bch: struct bch_control \*

    :param data:
        received data, ignored if \ ``calc_ecc``\  is provided
    :type data: const uint8_t \*

    :param len:
        data length in bytes, must always be provided
    :type len: unsigned int

    :param recv_ecc:
        received ecc, if NULL then assume it was XORed in \ ``calc_ecc``\ 
    :type recv_ecc: const uint8_t \*

    :param calc_ecc:
        calculated ecc, if NULL then calc_ecc is computed from \ ``data``\ 
    :type calc_ecc: const uint8_t \*

    :param syn:
        hw computed syndrome data (if NULL, syndrome is calculated)
    :type syn: const unsigned int \*

    :param errloc:
        output array of error locations
    :type errloc: unsigned int \*

.. _`decode_bch.return`:

Return
------

The number of errors found, or -EBADMSG if decoding failed, or -EINVAL if
invalid parameters were provided

Depending on the available hw BCH support and the need to compute \ ``calc_ecc``\ 
separately (using \ :c:func:`encode_bch`\ ), this function should be called with one of
the following parameter configurations -

by providing \ ``data``\  and \ ``recv_ecc``\  only:
decode_bch(@bch, \ ``data``\ , \ ``len``\ , \ ``recv_ecc``\ , NULL, NULL, \ ``errloc``\ )

by providing \ ``recv_ecc``\  and \ ``calc_ecc``\ :
decode_bch(@bch, NULL, \ ``len``\ , \ ``recv_ecc``\ , \ ``calc_ecc``\ , NULL, \ ``errloc``\ )

by providing ecc = recv_ecc XOR calc_ecc:
decode_bch(@bch, NULL, \ ``len``\ , NULL, ecc, NULL, \ ``errloc``\ )

by providing syndrome results \ ``syn``\ :
decode_bch(@bch, NULL, \ ``len``\ , NULL, NULL, \ ``syn``\ , \ ``errloc``\ )

Once \ :c:func:`decode_bch`\  has successfully returned with a positive value, error
locations returned in array \ ``errloc``\  should be interpreted as follows -

if (errloc[n] >= 8\*len), then n-th error is located in ecc (no need for
data correction)

if (errloc[n] < 8\*len), then n-th error is located in data and can be
corrected with statement data[errloc[n]/8] ^= 1 << (errloc[n] % 8);

Note that this function does not perform any data correction by itself, it
merely indicates error locations.

.. _`init_bch`:

init_bch
========

.. c:function:: struct bch_control *init_bch(int m, int t, unsigned int prim_poly)

    initialize a BCH encoder/decoder

    :param m:
        Galois field order, should be in the range 5-15
    :type m: int

    :param t:
        maximum error correction capability, in bits
    :type t: int

    :param prim_poly:
        user-provided primitive polynomial (or 0 to use default)
    :type prim_poly: unsigned int

.. _`init_bch.return`:

Return
------

a newly allocated BCH control structure if successful, NULL otherwise

This initialization can take some time, as lookup tables are built for fast
encoding/decoding; make sure not to call this function from a time critical
path. Usually, \ :c:func:`init_bch`\  should be called on module/driver init and
\ :c:func:`free_bch`\  should be called to release memory on exit.

You may provide your own primitive polynomial of degree \ ``m``\  in argument
\ ``prim_poly``\ , or let \ :c:func:`init_bch`\  use its default polynomial.

Once \ :c:func:`init_bch`\  has successfully returned a pointer to a newly allocated
BCH control structure, ecc length in bytes is given by member \ ``ecc_bytes``\  of
the structure.

.. _`free_bch`:

free_bch
========

.. c:function:: void free_bch(struct bch_control *bch)

    free the BCH control structure

    :param bch:
        BCH control structure to release
    :type bch: struct bch_control \*

.. This file was automatic generated / don't edit.

