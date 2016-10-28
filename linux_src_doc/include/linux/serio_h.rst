.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/serio.h

.. _`module_serio_driver`:

module_serio_driver
===================

.. c:function::  module_serio_driver( __serio_driver)

    Helper macro for registering a serio driver

    :param  __serio_driver:
        serio_driver struct

.. _`module_serio_driver.description`:

Description
-----------

Helper macro for serio drivers which do not do anything special in
module init/exit. This eliminates a lot of boilerplate. Each module
may only use this macro once, and calling it replaces \ :c:func:`module_init`\ 
and \ :c:func:`module_exit`\ .

.. This file was automatic generated / don't edit.

