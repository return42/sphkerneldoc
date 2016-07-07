.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/ef10_sriov.h

.. _`ef10_vf`:

struct ef10_vf
==============

.. c:type:: struct ef10_vf

    PF's store of VF data

.. _`ef10_vf.definition`:

Definition
----------

.. code-block:: c

    struct ef10_vf {
        struct efx_nic *efx;
        struct pci_dev *pci_dev;
        unsigned int vport_id;
        unsigned int vport_assigned;
        u8 mac[ETH_ALEN];
        u16 vlan;
        #define EFX_EF10_NO_VLAN 0
    }

.. _`ef10_vf.members`:

Members
-------

efx
    efx_nic struct for the current VF

pci_dev
    the pci_dev struct for the VF, retained while the VF is assigned

vport_id
    vport ID for the VF

vport_assigned
    record whether the vport is currently assigned to the VF

mac
    MAC address for the VF, zero when address is removed from the vport

vlan
    Default VLAN for the VF or #EFX_EF10_NO_VLAN

.. This file was automatic generated / don't edit.

