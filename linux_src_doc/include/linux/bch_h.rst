.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/bch.h

.. _`bch_control`:

struct bch_control
==================

.. c:type:: struct bch_control

    BCH control structure

.. _`bch_control.definition`:

Definition
----------

.. code-block:: c

    struct bch_control {
        unsigned int m;
        unsigned int n;
        unsigned int t;
        unsigned int ecc_bits;
        unsigned int ecc_bytes;
        uint16_t *a_pow_tab;
        uint16_t *a_log_tab;
        uint32_t *mod8_tab;
        uint32_t *ecc_buf;
        uint32_t *ecc_buf2;
        unsigned int *xi_tab;
        unsigned int *syn;
        int *cache;
        struct gf_poly *elp;
        struct gf_poly *poly_2t[4];
    }

.. _`bch_control.members`:

Members
-------

m
    Galois field order

n
    maximum codeword size in bits (= 2^m-1)

t
    error correction capability in bits

ecc_bits
    ecc exact size in bits, i.e. generator polynomial degree (<=m\*t)

ecc_bytes
    ecc max size (m\*t bits) in bytes

a_pow_tab
    Galois field GF(2^m) exponentiation lookup table

a_log_tab
    Galois field GF(2^m) log lookup table

mod8_tab
    remainder generator polynomial lookup tables

ecc_buf
    ecc parity words buffer

ecc_buf2
    ecc parity words buffer

xi_tab
    GF(2^m) base for solving degree 2 polynomial roots

syn
    syndrome buffer

cache
    log-based polynomial representation buffer

elp
    error locator polynomial

poly_2t
    temporary polynomials of degree 2t

.. This file was automatic generated / don't edit.

