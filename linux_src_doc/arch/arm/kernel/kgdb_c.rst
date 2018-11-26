.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kernel/kgdb.c

.. _`kgdb_arch_init`:

kgdb_arch_init
==============

.. c:function:: int kgdb_arch_init( void)

    Perform any architecture specific initalization.

    :param void:
        no arguments
    :type void: 

.. _`kgdb_arch_init.description`:

Description
-----------

This function will handle the initalization of any architecture
specific callbacks.

.. _`kgdb_arch_exit`:

kgdb_arch_exit
==============

.. c:function:: void kgdb_arch_exit( void)

    Perform any architecture specific uninitalization.

    :param void:
        no arguments
    :type void: 

.. _`kgdb_arch_exit.description`:

Description
-----------

This function will handle the uninitalization of any architecture
specific callbacks, for dynamic registration and unregistration.

.. This file was automatic generated / don't edit.

