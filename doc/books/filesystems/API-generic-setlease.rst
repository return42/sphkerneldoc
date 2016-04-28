.. -*- coding: utf-8; mode: rst -*-

.. _API-generic-setlease:

================
generic_setlease
================

*man generic_setlease(9)*

*4.6.0-rc5*

sets a lease on an open file


Synopsis
========

.. c:function:: int generic_setlease( struct file * filp, long arg, struct file_lock ** flp, void ** priv )

Arguments
=========

``filp``
    file pointer

``arg``
    type of lease to obtain

``flp``
    input - file_lock to use, output - file_lock inserted

``priv``
    private data for lm_setup (may be NULL if lm_setup doesn't require
    it)


Description
===========

The (input) flp->fl_lmops->lm_break function is required by
``break_lease``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
