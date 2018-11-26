.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/eeh_pseries.c

.. _`pseries_eeh_init`:

pseries_eeh_init
================

.. c:function:: int pseries_eeh_init( void)

    EEH platform dependent initialization

    :param void:
        no arguments
    :type void: 

.. _`pseries_eeh_init.description`:

Description
-----------

EEH platform dependent initialization on pseries.

.. _`pseries_eeh_probe`:

pseries_eeh_probe
=================

.. c:function:: void *pseries_eeh_probe(struct pci_dn *pdn, void *data)

    EEH probe on the given device

    :param pdn:
        PCI device node
    :type pdn: struct pci_dn \*

    :param data:
        Unused
    :type data: void \*

.. _`pseries_eeh_probe.description`:

Description
-----------

When EEH module is installed during system boot, all PCI devices
are checked one by one to see if it supports EEH. The function
is introduced for the purpose.

.. _`pseries_eeh_set_option`:

pseries_eeh_set_option
======================

.. c:function:: int pseries_eeh_set_option(struct eeh_pe *pe, int option)

    Initialize EEH or MMIO/DMA reenable

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

    :param option:
        operation to be issued
    :type option: int

.. _`pseries_eeh_set_option.description`:

Description
-----------

The function is used to control the EEH functionality globally.
Currently, following options are support according to PAPR:
Enable EEH, Disable EEH, Enable MMIO and Enable DMA

.. _`pseries_eeh_get_pe_addr`:

pseries_eeh_get_pe_addr
=======================

.. c:function:: int pseries_eeh_get_pe_addr(struct eeh_pe *pe)

    Retrieve PE address

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

.. _`pseries_eeh_get_pe_addr.description`:

Description
-----------

Retrieve the assocated PE address. Actually, there're 2 RTAS
function calls dedicated for the purpose. We need implement
it through the new function and then the old one. Besides,
you should make sure the config address is figured out from
FDT node before calling the function.

It's notable that zero'ed return value means invalid PE config
address.

.. _`pseries_eeh_get_state`:

pseries_eeh_get_state
=====================

.. c:function:: int pseries_eeh_get_state(struct eeh_pe *pe, int *delay)

    Retrieve PE state

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

    :param delay:
        suggested time to wait if state is unavailable
    :type delay: int \*

.. _`pseries_eeh_get_state.description`:

Description
-----------

Retrieve the state of the specified PE. On RTAS compliant
pseries platform, there already has one dedicated RTAS function
for the purpose. It's notable that the associated PE config address
might be ready when calling the function. Therefore, endeavour to
use the PE config address if possible. Further more, there're 2
RTAS calls for the purpose, we need to try the new one and back
to the old one if the new one couldn't work properly.

.. _`pseries_eeh_reset`:

pseries_eeh_reset
=================

.. c:function:: int pseries_eeh_reset(struct eeh_pe *pe, int option)

    Reset the specified PE

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

    :param option:
        reset option
    :type option: int

.. _`pseries_eeh_reset.description`:

Description
-----------

Reset the specified PE

.. _`pseries_eeh_get_log`:

pseries_eeh_get_log
===================

.. c:function:: int pseries_eeh_get_log(struct eeh_pe *pe, int severity, char *drv_log, unsigned long len)

    Retrieve error log

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

    :param severity:
        temporary or permanent error log
    :type severity: int

    :param drv_log:
        driver log to be combined with retrieved error log
    :type drv_log: char \*

    :param len:
        length of driver log
    :type len: unsigned long

.. _`pseries_eeh_get_log.description`:

Description
-----------

Retrieve the temporary or permanent error from the PE.
Actually, the error will be retrieved through the dedicated
RTAS call.

.. _`pseries_eeh_configure_bridge`:

pseries_eeh_configure_bridge
============================

.. c:function:: int pseries_eeh_configure_bridge(struct eeh_pe *pe)

    Configure PCI bridges in the indicated PE

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

.. _`pseries_eeh_configure_bridge.description`:

Description
-----------

The function will be called to reconfigure the bridges included
in the specified PE so that the mulfunctional PE would be recovered
again.

.. _`pseries_eeh_read_config`:

pseries_eeh_read_config
=======================

.. c:function:: int pseries_eeh_read_config(struct pci_dn *pdn, int where, int size, u32 *val)

    Read PCI config space

    :param pdn:
        PCI device node
    :type pdn: struct pci_dn \*

    :param where:
        PCI address
    :type where: int

    :param size:
        size to read
    :type size: int

    :param val:
        return value
    :type val: u32 \*

.. _`pseries_eeh_read_config.description`:

Description
-----------

Read config space from the speicifed device

.. _`pseries_eeh_write_config`:

pseries_eeh_write_config
========================

.. c:function:: int pseries_eeh_write_config(struct pci_dn *pdn, int where, int size, u32 val)

    Write PCI config space

    :param pdn:
        PCI device node
    :type pdn: struct pci_dn \*

    :param where:
        PCI address
    :type where: int

    :param size:
        size to write
    :type size: int

    :param val:
        value to be written
    :type val: u32

.. _`pseries_eeh_write_config.description`:

Description
-----------

Write config space to the specified device

.. _`eeh_pseries_init`:

eeh_pseries_init
================

.. c:function:: int eeh_pseries_init( void)

    Register platform dependent EEH operations

    :param void:
        no arguments
    :type void: 

.. _`eeh_pseries_init.description`:

Description
-----------

EEH initialization on pseries platform. This function should be
called before any EEH related functions.

.. This file was automatic generated / don't edit.

