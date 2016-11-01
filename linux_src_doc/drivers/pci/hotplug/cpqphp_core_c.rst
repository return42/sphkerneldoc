.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/hotplug/cpqphp_core.c

.. _`detect_smbios_pointer`:

detect_SMBIOS_pointer
=====================

.. c:function:: void __iomem *detect_SMBIOS_pointer(void __iomem *begin, void __iomem *end)

    find the System Management BIOS Table in mem region.

    :param void __iomem \*begin:
        begin pointer for region to be scanned.

    :param void __iomem \*end:
        end pointer for region to be scanned.

.. _`detect_smbios_pointer.description`:

Description
-----------

Returns pointer to the head of the SMBIOS tables (or \ ``NULL``\ ).

.. _`init_serr`:

init_SERR
=========

.. c:function:: int init_SERR(struct controller *ctrl)

    Initializes the per slot SERR generation.

    :param struct controller \*ctrl:
        controller to use

.. _`init_serr.description`:

Description
-----------

For unexpected switch opens

.. _`get_subsequent_smbios_entry`:

get_subsequent_smbios_entry
===========================

.. c:function:: void __iomem *get_subsequent_smbios_entry(void __iomem *smbios_start, void __iomem *smbios_table, void __iomem *curr)

    get the next entry from bios table.

    :param void __iomem \*smbios_start:
        where to start in the SMBIOS table

    :param void __iomem \*smbios_table:
        location of the SMBIOS table

    :param void __iomem \*curr:
        %NULL or pointer to previously returned structure

.. _`get_subsequent_smbios_entry.description`:

Description
-----------

Gets the first entry if previous == NULL;
otherwise, returns the next entry.
Uses global SMBIOS Table pointer.

Returns a pointer to an SMBIOS structure or NULL if none found.

.. _`get_smbios_entry`:

get_SMBIOS_entry
================

.. c:function:: void __iomem *get_SMBIOS_entry(void __iomem *smbios_start, void __iomem *smbios_table, u8 type, void __iomem *previous)

    return the requested SMBIOS entry or \ ``NULL``\ 

    :param void __iomem \*smbios_start:
        where to start in the SMBIOS table

    :param void __iomem \*smbios_table:
        location of the SMBIOS table

    :param u8 type:
        SMBIOS structure type to be returned

    :param void __iomem \*previous:
        %NULL or pointer to previously returned structure

.. _`get_smbios_entry.description`:

Description
-----------

Gets the first entry of the specified type if previous == \ ``NULL``\ ;
Otherwise, returns the next entry of the given type.
Uses global SMBIOS Table pointer.
Uses get_subsequent_smbios_entry.

Returns a pointer to an SMBIOS structure or \ ``NULL``\  if none found.

.. _`get_slot_mapping`:

get_slot_mapping
================

.. c:function:: int get_slot_mapping(struct pci_bus *bus, u8 bus_num, u8 dev_num, u8 *slot)

    determine logical slot mapping for PCI device

    :param struct pci_bus \*bus:
        *undescribed*

    :param u8 bus_num:
        *undescribed*

    :param u8 dev_num:
        *undescribed*

    :param u8 \*slot:
        *undescribed*

.. _`get_slot_mapping.description`:

Description
-----------

Won't work for more than one PCI-PCI bridge in a slot.

\ ``bus_num``\  - bus number of PCI device
\ ``dev_num``\  - device number of PCI device
\ ``slot``\  - Pointer to u8 where slot number will be returned

.. _`get_slot_mapping.output`:

Output
------

SUCCESS or FAILURE

.. _`cpqhp_set_attention_status`:

cpqhp_set_attention_status
==========================

.. c:function:: int cpqhp_set_attention_status(struct controller *ctrl, struct pci_func *func, u32 status)

    Turns the Amber LED for a slot on or off

    :param struct controller \*ctrl:
        struct controller to use

    :param struct pci_func \*func:
        PCI device/function info

    :param u32 status:
        LED control flag: 1 = LED on, 0 = LED off

.. _`set_attention_status`:

set_attention_status
====================

.. c:function:: int set_attention_status(struct hotplug_slot *hotplug_slot, u8 status)

    Turns the Amber LED for a slot on or off

    :param struct hotplug_slot \*hotplug_slot:
        slot to change LED on

    :param u8 status:
        LED control flag

.. This file was automatic generated / don't edit.

