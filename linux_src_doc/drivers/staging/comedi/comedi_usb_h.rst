.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/comedi_usb.h

.. _`module_comedi_usb_driver`:

module_comedi_usb_driver
========================

.. c:function::  module_comedi_usb_driver( __comedi_driver,  __usb_driver)

    Helper macro for registering a comedi USB driver

    :param __comedi_driver:
        comedi_driver struct
    :type __comedi_driver: 

    :param __usb_driver:
        usb_driver struct
    :type __usb_driver: 

.. _`module_comedi_usb_driver.description`:

Description
-----------

Helper macro for comedi USB drivers which do not do anything special
in module init/exit. This eliminates a lot of boilerplate. Each
module may only use this macro once, and calling it replaces
\ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. This file was automatic generated / don't edit.

