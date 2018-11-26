.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/agp/backend.c

.. _`agp_backend_acquire`:

agp_backend_acquire
===================

.. c:function:: struct agp_bridge_data *agp_backend_acquire(struct pci_dev *pdev)

    attempt to acquire an agp backend.

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

.. _`agp_backend_release`:

agp_backend_release
===================

.. c:function:: void agp_backend_release(struct agp_bridge_data *bridge)

    release the lock on the agp backend.

    :param bridge:
        *undescribed*
    :type bridge: struct agp_bridge_data \*

.. _`agp_backend_release.description`:

Description
-----------

The caller must insure that the graphics aperture translation table
is read for use by another entity.

(Ensure that all memory it bound is unbound.)

.. This file was automatic generated / don't edit.

