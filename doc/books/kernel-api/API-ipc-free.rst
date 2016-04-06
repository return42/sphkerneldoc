
.. _API-ipc-free:

========
ipc_free
========

*man ipc_free(9)*

*4.6.0-rc1*

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
