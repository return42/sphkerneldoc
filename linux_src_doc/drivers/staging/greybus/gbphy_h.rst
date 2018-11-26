.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/greybus/gbphy.h

.. _`module_gbphy_driver`:

module_gbphy_driver
===================

.. c:function::  module_gbphy_driver( __gbphy_driver)

    Helper macro for registering a gbphy driver

    :param __gbphy_driver:
        gbphy_driver structure
    :type __gbphy_driver: 

.. _`module_gbphy_driver.description`:

Description
-----------

Helper macro for gbphy drivers to set up proper module init / exit
functions.  Replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\  and keeps people from
printing pointless things to the kernel log when their driver is loaded.

.. This file was automatic generated / don't edit.

