.. -*- coding: utf-8; mode: rst -*-

.. _API-fc-get-event-number:

===================
fc_get_event_number
===================

*man fc_get_event_number(9)*

*4.6.0-rc5*

Obtain the next sequential FC event number


Synopsis
========

.. c:function:: u32 fc_get_event_number( void )

Arguments
=========

``void``
    no arguments


Notes
=====

We could have inlined this, but it would have required fc_event_seq to
be exposed. For now, live with the subroutine call. Atomic used to avoid
lock/unlock...


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
