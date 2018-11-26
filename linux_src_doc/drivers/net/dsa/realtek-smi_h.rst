.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/dsa/realtek-smi.h

.. _`realtek_smi_ops`:

struct realtek_smi_ops
======================

.. c:type:: struct realtek_smi_ops

    vtable for the per-SMI-chiptype operations

.. _`realtek_smi_ops.definition`:

Definition
----------

.. code-block:: c

    struct realtek_smi_ops {
        int (*detect)(struct realtek_smi *smi);
        int (*reset_chip)(struct realtek_smi *smi);
        int (*setup)(struct realtek_smi *smi);
        void (*cleanup)(struct realtek_smi *smi);
        int (*get_mib_counter)(struct realtek_smi *smi,int port,struct rtl8366_mib_counter *mib, u64 *mibvalue);
        int (*get_vlan_mc)(struct realtek_smi *smi, u32 index, struct rtl8366_vlan_mc *vlanmc);
        int (*set_vlan_mc)(struct realtek_smi *smi, u32 index, const struct rtl8366_vlan_mc *vlanmc);
        int (*get_vlan_4k)(struct realtek_smi *smi, u32 vid, struct rtl8366_vlan_4k *vlan4k);
        int (*set_vlan_4k)(struct realtek_smi *smi, const struct rtl8366_vlan_4k *vlan4k);
        int (*get_mc_index)(struct realtek_smi *smi, int port, int *val);
        int (*set_mc_index)(struct realtek_smi *smi, int port, int index);
        bool (*is_vlan_valid)(struct realtek_smi *smi, unsigned int vlan);
        int (*enable_vlan)(struct realtek_smi *smi, bool enable);
        int (*enable_vlan4k)(struct realtek_smi *smi, bool enable);
        int (*enable_port)(struct realtek_smi *smi, int port, bool enable);
        int (*phy_read)(struct realtek_smi *smi, int phy, int regnum);
        int (*phy_write)(struct realtek_smi *smi, int phy, int regnum, u16 val);
    }

.. _`realtek_smi_ops.members`:

Members
-------

detect
    detects the chiptype

reset_chip
    *undescribed*

setup
    *undescribed*

cleanup
    *undescribed*

get_mib_counter
    *undescribed*

get_vlan_mc
    *undescribed*

set_vlan_mc
    *undescribed*

get_vlan_4k
    *undescribed*

set_vlan_4k
    *undescribed*

get_mc_index
    *undescribed*

set_mc_index
    *undescribed*

is_vlan_valid
    *undescribed*

enable_vlan
    *undescribed*

enable_vlan4k
    *undescribed*

enable_port
    *undescribed*

phy_read
    *undescribed*

phy_write
    *undescribed*

.. This file was automatic generated / don't edit.

