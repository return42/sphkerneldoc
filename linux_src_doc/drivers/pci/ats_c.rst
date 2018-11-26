.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/ats.c

.. _`pci_enable_ats`:

pci_enable_ats
==============

.. c:function:: int pci_enable_ats(struct pci_dev *dev, int ps)

    enable the ATS capability

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

    :param ps:
        the IOMMU page shift
    :type ps: int

.. _`pci_enable_ats.description`:

Description
-----------

Returns 0 on success, or negative on failure.

.. _`pci_disable_ats`:

pci_disable_ats
===============

.. c:function:: void pci_disable_ats(struct pci_dev *dev)

    disable the ATS capability

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_ats_queue_depth`:

pci_ats_queue_depth
===================

.. c:function:: int pci_ats_queue_depth(struct pci_dev *dev)

    query the ATS Invalidate Queue Depth

    :param dev:
        the PCI device
    :type dev: struct pci_dev \*

.. _`pci_ats_queue_depth.description`:

Description
-----------

Returns the queue depth on success, or negative on failure.

The ATS spec uses 0 in the Invalidate Queue Depth field to
indicate that the function can accept 32 Invalidate Request.
But here we use the \`real' values (i.e. 1~32) for the Queue
Depth; and 0 indicates the function shares the Queue with
other functions (doesn't exclusively own a Queue).

.. _`pci_enable_pri`:

pci_enable_pri
==============

.. c:function:: int pci_enable_pri(struct pci_dev *pdev, u32 reqs)

    Enable PRI capability \ ````\  pdev: PCI device structure

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

    :param reqs:
        *undescribed*
    :type reqs: u32

.. _`pci_enable_pri.description`:

Description
-----------

Returns 0 on success, negative value on error

.. _`pci_disable_pri`:

pci_disable_pri
===============

.. c:function:: void pci_disable_pri(struct pci_dev *pdev)

    Disable PRI capability

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`pci_disable_pri.description`:

Description
-----------

Only clears the enabled-bit, regardless of its former value

.. _`pci_restore_pri_state`:

pci_restore_pri_state
=====================

.. c:function:: void pci_restore_pri_state(struct pci_dev *pdev)

    Restore PRI

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`pci_reset_pri`:

pci_reset_pri
=============

.. c:function:: int pci_reset_pri(struct pci_dev *pdev)

    Resets device's PRI state

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`pci_reset_pri.description`:

Description
-----------

The PRI capability must be disabled before this function is called.
Returns 0 on success, negative value on error.

.. _`pci_enable_pasid`:

pci_enable_pasid
================

.. c:function:: int pci_enable_pasid(struct pci_dev *pdev, int features)

    Enable the PASID capability

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

    :param features:
        Features to enable
    :type features: int

.. _`pci_enable_pasid.description`:

Description
-----------

Returns 0 on success, negative value on error. This function checks
whether the features are actually supported by the device and returns
an error if not.

.. _`pci_disable_pasid`:

pci_disable_pasid
=================

.. c:function:: void pci_disable_pasid(struct pci_dev *pdev)

    Disable the PASID capability

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`pci_restore_pasid_state`:

pci_restore_pasid_state
=======================

.. c:function:: void pci_restore_pasid_state(struct pci_dev *pdev)

    Restore PASID capabilities

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`pci_pasid_features`:

pci_pasid_features
==================

.. c:function:: int pci_pasid_features(struct pci_dev *pdev)

    Check which PASID features are supported

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`pci_pasid_features.description`:

Description
-----------

Returns a negative value when no PASI capability is present.
Otherwise is returns a bitmask with supported features. Current

.. _`pci_pasid_features.features-reported-are`:

features reported are
---------------------

PCI_PASID_CAP_EXEC - Execute permission supported
PCI_PASID_CAP_PRIV - Privileged mode supported

.. _`pci_max_pasids`:

pci_max_pasids
==============

.. c:function:: int pci_max_pasids(struct pci_dev *pdev)

    Get maximum number of PASIDs supported by device

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`pci_max_pasids.description`:

Description
-----------

Returns negative value when PASID capability is not present.
Otherwise it returns the numer of supported PASIDs.

.. This file was automatic generated / don't edit.

