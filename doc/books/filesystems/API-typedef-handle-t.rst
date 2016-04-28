.. -*- coding: utf-8; mode: rst -*-

.. _API-typedef-handle-t:

================
typedef handle_t
================

*man typedef handle_t(9)*

The handle_t type represents a single atomic update being performed by
some process.


Synopsis
========

.. code-block:: c

    typedef handle_t;


Description
===========

All filesystem modifications made by the process go through this handle.
Recursive operations (such as quota operations) are gathered into a
single update.

The buffer credits field is used to account for journaled buffers being
modified by the running process. To ensure that there is enough log
space for all outstanding operations, we need to limit the number of
outstanding buffers possible at any time. When the operation completes,
any buffer credits not used are credited back to the transaction, so
that at all times we know how many buffers the outstanding updates on a
transaction might possibly touch.

This is an opaque datatype.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
