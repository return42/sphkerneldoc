.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/qat/qat_common/adf_dev_mgr.c

.. _`adf_clean_vf_map`:

adf_clean_vf_map
================

.. c:function:: void adf_clean_vf_map(bool vf)

    Cleans VF id mapings

    :param bool vf:
        flag indicating whether mappings is cleaned
        for vfs only or for vfs and pfs

.. _`adf_clean_vf_map.description`:

Description
-----------

Function cleans internal ids for virtual functions.

.. _`adf_devmgr_update_class_index`:

adf_devmgr_update_class_index
=============================

.. c:function:: void adf_devmgr_update_class_index(struct adf_hw_device_data *hw_data)

    Update internal index

    :param struct adf_hw_device_data \*hw_data:
        Pointer to internal device data.

.. _`adf_devmgr_update_class_index.description`:

Description
-----------

Function updates internal dev index for VFs

.. _`adf_devmgr_add_dev`:

adf_devmgr_add_dev
==================

.. c:function:: int adf_devmgr_add_dev(struct adf_accel_dev *accel_dev, struct adf_accel_dev *pf)

    Add accel_dev to the acceleration framework

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

    :param struct adf_accel_dev \*pf:
        Corresponding PF if the accel_dev is a VF

.. _`adf_devmgr_add_dev.description`:

Description
-----------

Function adds acceleration device to the acceleration framework.
To be used by QAT device specific drivers.

.. _`adf_devmgr_add_dev.return`:

Return
------

0 on success, error code otherwise.

.. _`adf_devmgr_rm_dev`:

adf_devmgr_rm_dev
=================

.. c:function:: void adf_devmgr_rm_dev(struct adf_accel_dev *accel_dev, struct adf_accel_dev *pf)

    Remove accel_dev from the acceleration framework.

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

    :param struct adf_accel_dev \*pf:
        Corresponding PF if the accel_dev is a VF

.. _`adf_devmgr_rm_dev.description`:

Description
-----------

Function removes acceleration device from the acceleration framework.
To be used by QAT device specific drivers.

.. _`adf_devmgr_rm_dev.return`:

Return
------

void

.. _`adf_devmgr_pci_to_accel_dev`:

adf_devmgr_pci_to_accel_dev
===========================

.. c:function:: struct adf_accel_dev *adf_devmgr_pci_to_accel_dev(struct pci_dev *pci_dev)

    Get accel_dev associated with the pci_dev.

    :param struct pci_dev \*pci_dev:
        *undescribed*

.. _`adf_devmgr_pci_to_accel_dev.description`:

Description
-----------

Function returns acceleration device associated with the given pci device.
To be used by QAT device specific drivers.

.. _`adf_devmgr_pci_to_accel_dev.return`:

Return
------

pointer to accel_dev or NULL if not found.

.. _`adf_dev_in_use`:

adf_dev_in_use
==============

.. c:function:: int adf_dev_in_use(struct adf_accel_dev *accel_dev)

    Check whether accel_dev is currently in use

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

.. _`adf_dev_in_use.description`:

Description
-----------

To be used by QAT device specific drivers.

.. _`adf_dev_in_use.return`:

Return
------

1 when device is in use, 0 otherwise.

.. _`adf_dev_get`:

adf_dev_get
===========

.. c:function:: int adf_dev_get(struct adf_accel_dev *accel_dev)

    Increment accel_dev reference count

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

.. _`adf_dev_get.description`:

Description
-----------

Increment the accel_dev refcount and if this is the first time
incrementing it during this period the accel_dev is in use,
increment the module refcount too.
To be used by QAT device specific drivers.

.. _`adf_dev_get.return`:

Return
------

0 when successful, EFAULT when fail to bump module refcount

.. _`adf_dev_put`:

adf_dev_put
===========

.. c:function:: void adf_dev_put(struct adf_accel_dev *accel_dev)

    Decrement accel_dev reference count

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

.. _`adf_dev_put.description`:

Description
-----------

Decrement the accel_dev refcount and if this is the last time
decrementing it during this period the accel_dev is in use,
decrement the module refcount too.
To be used by QAT device specific drivers.

.. _`adf_dev_put.return`:

Return
------

void

.. _`adf_devmgr_in_reset`:

adf_devmgr_in_reset
===================

.. c:function:: int adf_devmgr_in_reset(struct adf_accel_dev *accel_dev)

    Check whether device is in reset

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

.. _`adf_devmgr_in_reset.description`:

Description
-----------

To be used by QAT device specific drivers.

.. _`adf_devmgr_in_reset.return`:

Return
------

1 when the device is being reset, 0 otherwise.

.. _`adf_dev_started`:

adf_dev_started
===============

.. c:function:: int adf_dev_started(struct adf_accel_dev *accel_dev)

    Check whether device has started

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

.. _`adf_dev_started.description`:

Description
-----------

To be used by QAT device specific drivers.

.. _`adf_dev_started.return`:

Return
------

1 when the device has started, 0 otherwise

.. This file was automatic generated / don't edit.

