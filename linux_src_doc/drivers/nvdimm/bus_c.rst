.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/bus.c

.. _`__nd_driver_register`:

__nd_driver_register
====================

.. c:function:: int __nd_driver_register(struct nd_device_driver *nd_drv, struct module *owner, const char *mod_name)

    register a region or a namespace driver

    :param struct nd_device_driver \*nd_drv:
        driver to register

    :param struct module \*owner:
        automatically set by \ :c:func:`nd_driver_register`\  macro

    :param const char \*mod_name:
        automatically set by \ :c:func:`nd_driver_register`\  macro

.. This file was automatic generated / don't edit.

