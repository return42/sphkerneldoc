.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/module.c

.. _`is_module_percpu_address`:

is_module_percpu_address
========================

.. c:function:: bool is_module_percpu_address(unsigned long addr)

    test whether address is from module static percpu

    :param addr:
        address to test
    :type addr: unsigned long

.. _`is_module_percpu_address.description`:

Description
-----------

Test whether \ ``addr``\  belongs to module static percpu area.

.. _`is_module_percpu_address.return`:

Return
------

\ ``true``\  if \ ``addr``\  is from module static percpu area

.. _`module_refcount`:

module_refcount
===============

.. c:function:: int module_refcount(struct module *mod)

    return the refcount or -1 if unloading

    :param mod:
        the module we're checking
    :type mod: struct module \*

.. _`module_refcount.return`:

Return
------

-1 if the module is in the process of unloading
otherwise the number of references in the kernel to the module

.. This file was automatic generated / don't edit.

