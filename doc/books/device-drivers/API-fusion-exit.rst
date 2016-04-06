
.. _API-fusion-exit:

===========
fusion_exit
===========

*man fusion_exit(9)*

*4.6.0-rc1*

Perform driver unload cleanup.


Synopsis
========

.. c:function:: void __exit fusion_exit( void )

Arguments
=========

``void``
    no arguments


Description
===========

This routine frees all resources associated with each MPT adapter and removes all ``MPT_PROCFS_MPTBASEDIR`` entries.
