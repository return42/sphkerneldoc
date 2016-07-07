.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/openrisc/kernel/setup.c

.. _`or32_early_setup`:

or32_early_setup
================

.. c:function:: void or32_early_setup(void *fdt)

    :param void \*fdt:
        *undescribed*

.. _`or32_early_setup.description`:

Description
-----------

Handles the pointer to the device tree that this kernel is to use
for establishing the available platform devices.

Falls back on built-in device tree in case null pointer is passed.

.. This file was automatic generated / don't edit.

