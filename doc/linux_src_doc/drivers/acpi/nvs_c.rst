.. -*- coding: utf-8; mode: rst -*-

=====
nvs.c
=====


.. _`suspend_nvs_register`:

suspend_nvs_register
====================

.. c:function:: int suspend_nvs_register (unsigned long start, unsigned long size)

    register platform NVS memory region to save @start - physical address of the region @size - size of the region

    :param unsigned long start:

        *undescribed*

    :param unsigned long size:

        *undescribed*



.. _`suspend_nvs_register.description`:

Description
-----------


The NVS region need not be page-aligned (both ends) and we arrange
things so that the data from page-aligned addresses in this region will
be copied into separate RAM pages.



.. _`suspend_nvs_free`:

suspend_nvs_free
================

.. c:function:: void suspend_nvs_free ( void)

    free data pages allocated for saving NVS regions

    :param void:
        no arguments



.. _`suspend_nvs_alloc`:

suspend_nvs_alloc
=================

.. c:function:: int suspend_nvs_alloc ( void)

    allocate memory necessary for saving NVS regions

    :param void:
        no arguments



.. _`suspend_nvs_save`:

suspend_nvs_save
================

.. c:function:: int suspend_nvs_save ( void)

    save NVS memory regions

    :param void:
        no arguments



.. _`suspend_nvs_restore`:

suspend_nvs_restore
===================

.. c:function:: void suspend_nvs_restore ( void)

    restore NVS memory regions

    :param void:
        no arguments



.. _`suspend_nvs_restore.description`:

Description
-----------


This function is going to be called with interrupts disabled, so it
cannot iounmap the virtual addresses used to access the NVS region.

