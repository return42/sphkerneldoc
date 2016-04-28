.. -*- coding: utf-8; mode: rst -*-

.. _API-init-rs-non-canonical:

=====================
init_rs_non_canonical
=====================

*man init_rs_non_canonical(9)*

*4.6.0-rc5*

Find a matching or allocate a new rs control structure, for fields with
non-canonical representation


Synopsis
========

.. c:function:: struct rs_control * init_rs_non_canonical( int symsize, int (*gffunc) int, int fcr, int prim, int nroots )

Arguments
=========

``symsize``
    the symbol size (number of bits)

``gffunc``
    pointer to function to generate the next field element, or the
    multiplicative identity element if given 0. Used instead of gfpoly
    if gfpoly is 0

``fcr``
    the first consecutive root of the rs code generator polynomial in
    index form

``prim``
    primitive element to generate polynomial roots

``nroots``
    RS code generator polynomial degree (number of roots)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
