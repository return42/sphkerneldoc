.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/greybus/greybus.h

.. _`module_greybus_driver`:

module_greybus_driver
=====================

.. c:function::  module_greybus_driver( __greybus_driver)

    Helper macro for registering a Greybus driver

    :param  __greybus_driver:
        greybus_driver structure

.. _`module_greybus_driver.description`:

Description
-----------

Helper macro for Greybus drivers to set up proper module init / exit
functions.  Replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\  and keeps people from
printing pointless things to the kernel log when their driver is loaded.

.. This file was automatic generated / don't edit.

