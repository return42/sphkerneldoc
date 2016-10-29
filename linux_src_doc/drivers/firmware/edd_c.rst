.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/edd.c

.. _`edd_show_raw_data`:

edd_show_raw_data
=================

.. c:function:: ssize_t edd_show_raw_data(struct edd_device *edev, char *buf)

    copies raw data to buffer for userspace to parse

    :param struct edd_device \*edev:
        target edd_device

    :param char \*buf:
        output buffer

.. _`edd_show_raw_data.return`:

Return
------

number of bytes written, or -EINVAL on failure

.. _`edd_release`:

edd_release
===========

.. c:function:: void edd_release(struct kobject *kobj)

    free edd structure

    :param struct kobject \*kobj:
        kobject of edd structure

.. _`edd_release.description`:

Description
-----------

This is called when the refcount of the edd structure
reaches 0. This should happen right after we unregister,
but just in case, we use the release callback anyway.

.. _`edd_dev_is_type`:

edd_dev_is_type
===============

.. c:function:: int edd_dev_is_type(struct edd_device *edev, const char *type)

    is this EDD device a 'type' device?

    :param struct edd_device \*edev:
        target edd_device

    :param const char \*type:
        a host bus or interface identifier string per the EDD spec

.. _`edd_dev_is_type.description`:

Description
-----------

Returns 1 (TRUE) if it is a 'type' device, 0 otherwise.

.. _`edd_get_pci_dev`:

edd_get_pci_dev
===============

.. c:function:: struct pci_dev *edd_get_pci_dev(struct edd_device *edev)

    finds pci_dev that matches edev

    :param struct edd_device \*edev:
        edd_device

.. _`edd_get_pci_dev.description`:

Description
-----------

Returns pci_dev if found, or NULL

.. _`edd_init`:

edd_init
========

.. c:function:: int edd_init( void)

    creates sysfs tree of EDD data

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.
