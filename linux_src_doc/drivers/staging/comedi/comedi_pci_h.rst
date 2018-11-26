.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/comedi_pci.h

.. _`module_comedi_pci_driver`:

module_comedi_pci_driver
========================

.. c:function::  module_comedi_pci_driver( __comedi_driver,  __pci_driver)

    Helper macro for registering a comedi PCI driver

    :param __comedi_driver:
        comedi_driver struct
    :type __comedi_driver: 

    :param __pci_driver:
        pci_driver struct
    :type __pci_driver: 

.. _`module_comedi_pci_driver.description`:

Description
-----------

Helper macro for comedi PCI drivers which do not do anything special
in module init/exit. This eliminates a lot of boilerplate. Each
module may only use this macro once, and calling it replaces
\ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. This file was automatic generated / don't edit.

