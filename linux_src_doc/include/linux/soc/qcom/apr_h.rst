.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/soc/qcom/apr.h

.. _`module_apr_driver`:

module_apr_driver
=================

.. c:function::  module_apr_driver( __apr_driver)

    Helper macro for registering a aprbus driver

    :param __apr_driver:
        *undescribed*
    :type __apr_driver: 

.. _`module_apr_driver.description`:

Description
-----------

Helper macro for aprbus drivers which do not do anything special in
module init/exit. This eliminates a lot of boilerplate. Each module
may only use this macro once, and calling it replaces \ :c:func:`module_init`\ 
and \ :c:func:`module_exit`\ 

.. This file was automatic generated / don't edit.

