.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/edac_pci.h

.. _`edac_pci_alloc_ctl_info`:

edac_pci_alloc_ctl_info
=======================

.. c:function:: struct edac_pci_ctl_info *edac_pci_alloc_ctl_info(unsigned int sz_pvt, const char *edac_pci_name)

    The \ :c:func:`alloc`\  function for the 'edac_pci' control info structure.

    :param sz_pvt:
        size of the private info at struct \ :c:type:`struct edac_pci_ctl_info <edac_pci_ctl_info>`\ 
    :type sz_pvt: unsigned int

    :param edac_pci_name:
        name of the PCI device
    :type edac_pci_name: const char \*

.. _`edac_pci_alloc_ctl_info.description`:

Description
-----------

The chip driver will allocate one of these for each
edac_pci it is going to control/register with the EDAC CORE.

.. _`edac_pci_alloc_ctl_info.return`:

Return
------

a pointer to struct \ :c:type:`struct edac_pci_ctl_info <edac_pci_ctl_info>`\  on success; \ ``NULL``\  otherwise.

.. _`edac_pci_free_ctl_info`:

edac_pci_free_ctl_info
======================

.. c:function:: void edac_pci_free_ctl_info(struct edac_pci_ctl_info *pci)

    Last action on the pci control structure.

    :param pci:
        pointer to struct \ :c:type:`struct edac_pci_ctl_info <edac_pci_ctl_info>`\ 
    :type pci: struct edac_pci_ctl_info \*

.. _`edac_pci_free_ctl_info.description`:

Description
-----------

Calls the remove sysfs information, which will unregister
this control struct's kobj. When that kobj's ref count
goes to zero, its release function will be call and then
\ :c:func:`kfree`\  the memory.

.. _`edac_pci_alloc_index`:

edac_pci_alloc_index
====================

.. c:function:: int edac_pci_alloc_index( void)

    Allocate a unique PCI index number

    :param void:
        no arguments
    :type void: 

.. _`edac_pci_alloc_index.return`:

Return
------

     allocated index number

.. _`edac_pci_add_device`:

edac_pci_add_device
===================

.. c:function:: int edac_pci_add_device(struct edac_pci_ctl_info *pci, int edac_idx)

    Insert the 'edac_dev' structure into the edac_pci global list and create sysfs entries associated with edac_pci structure.

    :param pci:
        pointer to the edac_device structure to be added to the list
    :type pci: struct edac_pci_ctl_info \*

    :param edac_idx:
        A unique numeric identifier to be assigned to the
        'edac_pci' structure.
    :type edac_idx: int

.. _`edac_pci_add_device.return`:

Return
------

     0 on Success, or an error code on failure

.. _`edac_pci_del_device`:

edac_pci_del_device
===================

.. c:function:: struct edac_pci_ctl_info *edac_pci_del_device(struct device *dev)

    Remove sysfs entries for specified edac_pci structure and then remove edac_pci structure from global list

    :param dev:
        Pointer to 'struct device' representing edac_pci structure
        to remove
    :type dev: struct device \*

.. _`edac_pci_del_device.return`:

Return
------

     Pointer to removed edac_pci structure,
     or \ ``NULL``\  if device not found

.. _`edac_pci_create_generic_ctl`:

edac_pci_create_generic_ctl
===========================

.. c:function:: struct edac_pci_ctl_info *edac_pci_create_generic_ctl(struct device *dev, const char *mod_name)

    A generic constructor for a PCI parity polling device Some systems have more than one domain of PCI busses. For systems with one domain, then this API will provide for a generic poller.

    :param dev:
        pointer to struct \ :c:type:`struct device <device>`\ ;
    :type dev: struct device \*

    :param mod_name:
        name of the PCI device
    :type mod_name: const char \*

.. _`edac_pci_create_generic_ctl.description`:

Description
-----------

This routine calls the \ :c:func:`edac_pci_alloc_ctl_info`\  for
the generic device, with default values

.. _`edac_pci_create_generic_ctl.return`:

Return
------

Pointer to struct \ :c:type:`struct edac_pci_ctl_info <edac_pci_ctl_info>`\  on success, \ ``NULL``\  on
     failure.

.. _`edac_pci_release_generic_ctl`:

edac_pci_release_generic_ctl
============================

.. c:function:: void edac_pci_release_generic_ctl(struct edac_pci_ctl_info *pci)

    The release function of a generic EDAC PCI polling device

    :param pci:
        pointer to struct \ :c:type:`struct edac_pci_ctl_info <edac_pci_ctl_info>`\ 
    :type pci: struct edac_pci_ctl_info \*

.. _`edac_pci_create_sysfs`:

edac_pci_create_sysfs
=====================

.. c:function:: int edac_pci_create_sysfs(struct edac_pci_ctl_info *pci)

    Create the controls/attributes for the specified EDAC PCI device

    :param pci:
        pointer to struct \ :c:type:`struct edac_pci_ctl_info <edac_pci_ctl_info>`\ 
    :type pci: struct edac_pci_ctl_info \*

.. _`edac_pci_remove_sysfs`:

edac_pci_remove_sysfs
=====================

.. c:function:: void edac_pci_remove_sysfs(struct edac_pci_ctl_info *pci)

    remove the controls and attributes for this EDAC PCI device

    :param pci:
        pointer to struct \ :c:type:`struct edac_pci_ctl_info <edac_pci_ctl_info>`\ 
    :type pci: struct edac_pci_ctl_info \*

.. This file was automatic generated / don't edit.

