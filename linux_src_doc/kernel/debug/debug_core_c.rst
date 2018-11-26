.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/debug/debug_core.c

.. _`kgdb_register_io_module`:

kgdb_register_io_module
=======================

.. c:function:: int kgdb_register_io_module(struct kgdb_io *new_dbg_io_ops)

    register KGDB IO module

    :param new_dbg_io_ops:
        the io ops vector
    :type new_dbg_io_ops: struct kgdb_io \*

.. _`kgdb_register_io_module.description`:

Description
-----------

Register it with the KGDB core.

.. _`kgdb_unregister_io_module`:

kgdb_unregister_io_module
=========================

.. c:function:: void kgdb_unregister_io_module(struct kgdb_io *old_dbg_io_ops)

    unregister KGDB IO module

    :param old_dbg_io_ops:
        the io ops vector
    :type old_dbg_io_ops: struct kgdb_io \*

.. _`kgdb_unregister_io_module.description`:

Description
-----------

Unregister it with the KGDB core.

.. _`kgdb_breakpoint`:

kgdb_breakpoint
===============

.. c:function:: void kgdb_breakpoint( void)

    generate breakpoint exception

    :param void:
        no arguments
    :type void: 

.. _`kgdb_breakpoint.description`:

Description
-----------

This function will generate a breakpoint exception.  It is used at the
beginning of a program to sync up with a debugger and can be used
otherwise as a quick means to stop program execution and "break" into
the debugger.

.. This file was automatic generated / don't edit.

