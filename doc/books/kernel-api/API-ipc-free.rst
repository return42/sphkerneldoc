.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-free:

========
ipc_free
========

*man ipc_free(9)*

*4.6.0-rc5*

free ipc space


Synopsis
========

.. c:function:: void ipc_free( void * ptr )

Arguments
=========

``ptr``
    pointer returned by ipc_alloc


Description
===========

Free a block created with ``ipc_alloc``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
