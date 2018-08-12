.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rslib.h

.. _`rs_codec`:

struct rs_codec
===============

.. c:type:: struct rs_codec

    rs codec data

.. _`rs_codec.definition`:

Definition
----------

.. code-block:: c

    struct rs_codec {
        int mm;
        int nn;
        uint16_t *alpha_to;
        uint16_t *index_of;
        uint16_t *genpoly;
        int nroots;
        int fcr;
        int prim;
        int iprim;
        int gfpoly;
        int (*gffunc)(int);
        int users;
        struct list_head list;
    }

.. _`rs_codec.members`:

Members
-------

mm
    Bits per symbol

nn
    Symbols per block (= (1<<mm)-1)

alpha_to
    log lookup table

index_of
    Antilog lookup table

genpoly
    Generator polynomial

nroots
    Number of generator roots = number of parity symbols

fcr
    First consecutive root, index form

prim
    Primitive element, index form

iprim
    prim-th root of 1, index form

gfpoly
    The primitive generator polynominal

gffunc
    Function to generate the field, if non-canonical representation

users
    Users of this structure

list
    List entry for the rs codec list

.. _`rs_control`:

struct rs_control
=================

.. c:type:: struct rs_control

    rs control structure per instance

.. _`rs_control.definition`:

Definition
----------

.. code-block:: c

    struct rs_control {
        struct rs_codec *codec;
        uint16_t buffers[0];
    }

.. _`rs_control.members`:

Members
-------

codec
    The codec used for this instance

buffers
    Internal scratch buffers used in calls to \ :c:func:`decode_rs`\ 

.. _`init_rs`:

init_rs
=======

.. c:function:: struct rs_control *init_rs(int symsize, int gfpoly, int fcr, int prim, int nroots)

    Create a RS control struct and initialize it

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

.. _`init_rs.description`:

Description
-----------

Allocations use GFP_KERNEL.

.. This file was automatic generated / don't edit.

