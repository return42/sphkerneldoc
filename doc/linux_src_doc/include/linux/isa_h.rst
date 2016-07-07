.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/isa.h

.. _`module_isa_driver`:

module_isa_driver
=================

.. c:function::  module_isa_driver( __isa_driver,  __num_isa_dev)

    Helper macro for registering a ISA driver

    :param  __isa_driver:
        isa_driver struct

    :param  __num_isa_dev:
        number of devices to register

.. _`module_isa_driver.description`:

Description
-----------

Helper macro for ISA drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate code. Each module may only
use this macro once, and calling it replaces module_init and module_exit.

.. _`max_num_isa_dev`:

max_num_isa_dev
===============

.. c:function::  max_num_isa_dev( __isa_dev_ext)

    Maximum possible number registered of an ISA device

    :param  __isa_dev_ext:
        *undescribed*

.. _`max_num_isa_dev.description`:

Description
-----------

The highest base address possible for an ISA device is 0x3FF; this results in
1024 possible base addresses. Dividing the number of possible base addresses
by the address extent taken by each device results in the maximum number of
devices on a system.

.. This file was automatic generated / don't edit.

