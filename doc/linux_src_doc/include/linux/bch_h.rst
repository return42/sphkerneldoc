.. -*- coding: utf-8; mode: rst -*-

=====
bch.h
=====


.. _`bch_control`:

struct bch_control
==================

.. c:type:: bch_control

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
  };


.. _`bch_control.members`:

Members
-------

:``m``:
    Galois field order

:``n``:
    maximum codeword size in bits (= 2^m-1)

:``t``:
    error correction capability in bits

:``ecc_bits``:
    ecc exact size in bits, i.e. generator polynomial degree (<=m\\*t)

:``ecc_bytes``:
    ecc max size (m\\*t bits) in bytes


