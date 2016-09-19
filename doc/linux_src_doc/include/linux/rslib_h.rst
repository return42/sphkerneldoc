.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rslib.h

.. _`rs_control`:

struct rs_control
=================

.. c:type:: struct rs_control

    rs control structure

.. _`rs_control.definition`:

Definition
----------

.. code-block:: c

    struct rs_control {
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

.. _`rs_control.members`:

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
    List entry for the rs control list

.. This file was automatic generated / don't edit.

