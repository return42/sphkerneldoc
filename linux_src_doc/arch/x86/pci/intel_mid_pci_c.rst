.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/pci/intel_mid_pci.c

.. _`fixed_bar_cap`:

fixed_bar_cap
=============

.. c:function:: int fixed_bar_cap(struct pci_bus *bus, unsigned int devfn)

    return the offset of the fixed BAR cap if found

    :param struct pci_bus \*bus:
        PCI bus

    :param unsigned int devfn:
        device in question

.. _`fixed_bar_cap.description`:

Description
-----------

Look for the fixed BAR cap on \ ``bus``\  and \ ``devfn``\ , returning its offset
if found or 0 otherwise.

.. _`type1_access_ok`:

type1_access_ok
===============

.. c:function:: bool type1_access_ok(unsigned int bus, unsigned int devfn, int reg)

    check whether to use type 1

    :param unsigned int bus:
        bus number

    :param unsigned int devfn:
        device & function in question

    :param int reg:
        *undescribed*

.. _`type1_access_ok.description`:

Description
-----------

If the bus is on a Lincroft chip and it exists, or is not on a Lincroft at
all, the we can go ahead with any reads & writes.  If it's on a Lincroft,
but doesn't exist, avoid the access altogether to keep the chip from
hanging.

.. _`intel_mid_pci_init`:

intel_mid_pci_init
==================

.. c:function:: int intel_mid_pci_init( void)

    installs intel_mid_pci_ops

    :param  void:
        no arguments

.. _`intel_mid_pci_init.description`:

Description
-----------

Moorestown has an interesting PCI implementation (see above).
Called when the early platform detection installs it.

.. This file was automatic generated / don't edit.

