.. -*- coding: utf-8; mode: rst -*-

.. _API-do-sigtimedwait:

===============
do_sigtimedwait
===============

*man do_sigtimedwait(9)*

*4.6.0-rc5*

wait for queued signals specified in ``which``


Synopsis
========

.. c:function:: int do_sigtimedwait( const sigset_t * which, siginfo_t * info, const struct timespec * ts )

Arguments
=========

``which``
    queued signals to wait for

``info``
    if non-null, the signal's siginfo is returned here

``ts``
    upper bound on process time suspension


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
