.. -*- coding: utf-8; mode: rst -*-

.. _API-init-rs:

=======
init_rs
=======

*man init_rs(9)*

*4.6.0-rc5*

Find a matching or allocate a new rs control structure


Synopsis
========

.. c:function:: struct rs_control * init_rs( int symsize, int gfpoly, int fcr, int prim, int nroots )

Arguments
=========

``symsize``
    the symbol size (number of bits)

``gfpoly``
    the extended Galois field generator polynomial coefficients, with
    the 0th coefficient in the low order bit. The polynomial must be
    primitive;

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
