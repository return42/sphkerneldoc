.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/bus.c

.. _`__nd_driver_register`:

\__nd_driver_register
=====================

.. c:function:: int __nd_driver_register(struct nd_device_driver *nd_drv, struct module *owner, const char *mod_name)

    register a region or a namespace driver

    :param nd_drv:
        driver to register
    :type nd_drv: struct nd_device_driver \*

    :param owner:
        automatically set by \ :c:func:`nd_driver_register`\  macro
    :type owner: struct module \*

    :param mod_name:
        automatically set by \ :c:func:`nd_driver_register`\  macro
    :type mod_name: const char \*

.. This file was automatic generated / don't edit.

