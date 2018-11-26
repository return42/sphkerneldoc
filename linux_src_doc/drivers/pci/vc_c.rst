.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/vc.c

.. _`pci_vc_save_restore_dwords`:

pci_vc_save_restore_dwords
==========================

.. c:function:: void pci_vc_save_restore_dwords(struct pci_dev *dev, int pos, u32 *buf, int dwords, bool save)

    Save or restore a series of dwords

    :param dev:
        device
    :type dev: struct pci_dev \*

    :param pos:
        starting config space position
    :type pos: int

    :param buf:
        buffer to save to or restore from
    :type buf: u32 \*

    :param dwords:
        number of dwords to save/restore
    :type dwords: int

    :param save:
        whether to save or restore
    :type save: bool

.. _`pci_vc_load_arb_table`:

pci_vc_load_arb_table
=====================

.. c:function:: void pci_vc_load_arb_table(struct pci_dev *dev, int pos)

    load and wait for VC arbitration table

    :param dev:
        device
    :type dev: struct pci_dev \*

    :param pos:
        starting position of VC capability (VC/VC9/MFVC)
    :type pos: int

.. _`pci_vc_load_arb_table.description`:

Description
-----------

Set Load VC Arbitration Table bit requesting hardware to apply the VC
Arbitration Table (previously loaded).  When the VC Arbitration Table
Status clears, hardware has latched the table into VC arbitration logic.

.. _`pci_vc_load_port_arb_table`:

pci_vc_load_port_arb_table
==========================

.. c:function:: void pci_vc_load_port_arb_table(struct pci_dev *dev, int pos, int res)

    Load and wait for VC port arbitration table

    :param dev:
        device
    :type dev: struct pci_dev \*

    :param pos:
        starting position of VC capability (VC/VC9/MFVC)
    :type pos: int

    :param res:
        VC resource number, ie. VCn (0-7)
    :type res: int

.. _`pci_vc_load_port_arb_table.description`:

Description
-----------

Set Load Port Arbitration Table bit requesting hardware to apply the Port
Arbitration Table (previously loaded).  When the Port Arbitration Table
Status clears, hardware has latched the table into port arbitration logic.

.. _`pci_vc_enable`:

pci_vc_enable
=============

.. c:function:: void pci_vc_enable(struct pci_dev *dev, int pos, int res)

    Enable virtual channel

    :param dev:
        device
    :type dev: struct pci_dev \*

    :param pos:
        starting position of VC capability (VC/VC9/MFVC)
    :type pos: int

    :param res:
        VC res number, ie. VCn (0-7)
    :type res: int

.. _`pci_vc_enable.description`:

Description
-----------

A VC is enabled by setting the enable bit in matching resource control
registers on both sides of a link.  We therefore need to find the opposite
end of the link.  To keep this simple we enable from the downstream device.
RC devices do not have an upstream device, nor does it seem that VC9 do
(spec is unclear).  Once we find the upstream device, match the VC ID to
get the correct resource, disable and enable on both ends.

.. _`pci_vc_do_save_buffer`:

pci_vc_do_save_buffer
=====================

.. c:function:: int pci_vc_do_save_buffer(struct pci_dev *dev, int pos, struct pci_cap_saved_state *save_state, bool save)

    Size, save, or restore VC state

    :param dev:
        device
    :type dev: struct pci_dev \*

    :param pos:
        starting position of VC capability (VC/VC9/MFVC)
    :type pos: int

    :param save_state:
        buffer for save/restore
    :type save_state: struct pci_cap_saved_state \*

    :param save:
        if provided a buffer, this indicates what to do with it
    :type save: bool

.. _`pci_vc_do_save_buffer.description`:

Description
-----------

Walking Virtual Channel config space to size, save, or restore it
is complicated, so we do it all from one function to reduce code and
guarantee ordering matches in the buffer.  When called with NULL
\ ``save_state``\ , return the size of the necessary save buffer.  When called
with a non-NULL \ ``save_state``\ , \ ``save``\  determines whether we save to the
buffer or restore from it.

.. _`pci_save_vc_state`:

pci_save_vc_state
=================

.. c:function:: int pci_save_vc_state(struct pci_dev *dev)

    Save VC state to pre-allocate save buffer

    :param dev:
        device
    :type dev: struct pci_dev \*

.. _`pci_save_vc_state.description`:

Description
-----------

For each type of VC capability, VC/VC9/MFVC, find the capability and
save it to the pre-allocated save buffer.

.. _`pci_restore_vc_state`:

pci_restore_vc_state
====================

.. c:function:: void pci_restore_vc_state(struct pci_dev *dev)

    Restore VC state from save buffer

    :param dev:
        device
    :type dev: struct pci_dev \*

.. _`pci_restore_vc_state.description`:

Description
-----------

For each type of VC capability, VC/VC9/MFVC, find the capability and
restore it from the previously saved buffer.

.. _`pci_allocate_vc_save_buffers`:

pci_allocate_vc_save_buffers
============================

.. c:function:: void pci_allocate_vc_save_buffers(struct pci_dev *dev)

    Allocate save buffers for VC caps

    :param dev:
        device
    :type dev: struct pci_dev \*

.. _`pci_allocate_vc_save_buffers.description`:

Description
-----------

For each type of VC capability, VC/VC9/MFVC, find the capability, size
it, and allocate a buffer for save/restore.

.. This file was automatic generated / don't edit.

