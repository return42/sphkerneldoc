
.. _API-kgdb-skipexception:

==================
kgdb_skipexception
==================

*man kgdb_skipexception(9)*

*4.6.0-rc1*

(optional) exit kgdb_handle_exception early


Synopsis
========

.. c:function:: int kgdb_skipexception( int exception, struct pt_regs * regs )

Arguments
=========

``exception``
    Exception vector number

``regs``
    Current ``struct pt_regs``.


Description
===========

On some architectures it is required to skip a breakpoint exception when it occurs after a breakpoint has been removed. This can be implemented in the architecture specific portion
of kgdb.
