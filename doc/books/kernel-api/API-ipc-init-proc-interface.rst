
.. _API-ipc-init-proc-interface:

=======================
ipc_init_proc_interface
=======================

*man ipc_init_proc_interface(9)*

*4.6.0-rc1*

create a proc interface for sysipc types using a seq_file interface.


Synopsis
========

.. c:function:: void ipc_init_proc_interface( const char * path, const char * header, int ids, int (*show) struct seq_file *, void * )

Arguments
=========

``path``
    Path in procfs

``header``
    Banner to be printed at the beginning of the file.

``ids``
    ipc id table to iterate.

``show``
    show routine.
