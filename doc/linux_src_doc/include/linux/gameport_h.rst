.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/gameport.h

.. _`module_gameport_driver`:

module_gameport_driver
======================

.. c:function::  module_gameport_driver( __gameport_driver)

    Helper macro for registering a gameport driver

    :param  __gameport_driver:
        gameport_driver struct

.. _`module_gameport_driver.description`:

Description
-----------

Helper macro for gameport drivers which do not do anything special in
module init/exit. This eliminates a lot of boilerplate. Each module may
only use this macro once, and calling it replaces \ :c:func:`module_init`\  and
\ :c:func:`module_exit`\ .

.. This file was automatic generated / don't edit.

