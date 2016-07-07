.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/acpi/acpi_bus.h

.. _`module_acpi_driver`:

module_acpi_driver
==================

.. c:function::  module_acpi_driver( __acpi_driver)

    Helper macro for registering an ACPI driver

    :param  __acpi_driver:
        acpi_driver struct

.. _`module_acpi_driver.description`:

Description
-----------

Helper macro for ACPI drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. This file was automatic generated / don't edit.

