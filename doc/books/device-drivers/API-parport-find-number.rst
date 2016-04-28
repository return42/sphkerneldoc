.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-find-number:

===================
parport_find_number
===================

*man parport_find_number(9)*

*4.6.0-rc5*

find a parallel port by number


Synopsis
========

.. c:function:: struct parport * parport_find_number( int number )

Arguments
=========

``number``
    parallel port number


Description
===========

This returns the parallel port with the specified number, or ``NULL`` if
there is none.

There is an implicit ``parport_get_port`` done already; to throw away
the reference to the port that ``parport_find_number`` gives you, use
``parport_put_port``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
