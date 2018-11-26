.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/powernv/eeh-powernv.c

.. _`pnv_eeh_post_init`:

pnv_eeh_post_init
=================

.. c:function:: int pnv_eeh_post_init( void)

    EEH platform dependent post initialization

    :param void:
        no arguments
    :type void: 

.. _`pnv_eeh_post_init.description`:

Description
-----------

EEH platform dependent post initialization on powernv. When
the function is called, the EEH PEs and devices should have
been built. If the I/O cache staff has been built, EEH is
ready to supply service.

.. _`pnv_eeh_probe`:

pnv_eeh_probe
=============

.. c:function:: void *pnv_eeh_probe(struct pci_dn *pdn, void *data)

    Do probe on PCI device

    :param pdn:
        PCI device node
    :type pdn: struct pci_dn \*

    :param data:
        unused
    :type data: void \*

.. _`pnv_eeh_probe.description`:

Description
-----------

When EEH module is installed during system boot, all PCI devices
are checked one by one to see if it supports EEH. The function
is introduced for the purpose. By default, EEH has been enabled
on all PCI devices. That's to say, we only need do necessary
initialization on the corresponding eeh device and create PE
accordingly.

It's notable that's unsafe to retrieve the EEH device through
the corresponding PCI device. During the PCI device hotplug, which
was possiblly triggered by EEH core, the binding between EEH device
and the PCI device isn't built yet.

.. _`pnv_eeh_set_option`:

pnv_eeh_set_option
==================

.. c:function:: int pnv_eeh_set_option(struct eeh_pe *pe, int option)

    Initialize EEH or MMIO/DMA reenable

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

    :param option:
        operation to be issued
    :type option: int

.. _`pnv_eeh_set_option.description`:

Description
-----------

The function is used to control the EEH functionality globally.
Currently, following options are support according to PAPR:
Enable EEH, Disable EEH, Enable MMIO and Enable DMA

.. _`pnv_eeh_get_pe_addr`:

pnv_eeh_get_pe_addr
===================

.. c:function:: int pnv_eeh_get_pe_addr(struct eeh_pe *pe)

    Retrieve PE address

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

.. _`pnv_eeh_get_pe_addr.description`:

Description
-----------

Retrieve the PE address according to the given tranditional
PCI BDF (Bus/Device/Function) address.

.. _`pnv_eeh_get_state`:

pnv_eeh_get_state
=================

.. c:function:: int pnv_eeh_get_state(struct eeh_pe *pe, int *delay)

    Retrieve PE state

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

    :param delay:
        delay while PE state is temporarily unavailable
    :type delay: int \*

.. _`pnv_eeh_get_state.description`:

Description
-----------

Retrieve the state of the specified PE. For IODA-compitable
platform, it should be retrieved from IODA table. Therefore,
we prefer passing down to hardware implementation to handle
it.

.. _`pnv_eeh_reset`:

pnv_eeh_reset
=============

.. c:function:: int pnv_eeh_reset(struct eeh_pe *pe, int option)

    Reset the specified PE

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

    :param option:
        reset option
    :type option: int

.. _`pnv_eeh_reset.description`:

Description
-----------

Do reset on the indicated PE. For PCI bus sensitive PE,
we need to reset the parent p2p bridge. The PHB has to
be reinitialized if the p2p bridge is root bridge. For
PCI device sensitive PE, we will try to reset the device
through FLR. For now, we don't have OPAL APIs to do HARD
reset yet, so all reset would be SOFT (HOT) reset.

.. _`pnv_eeh_get_log`:

pnv_eeh_get_log
===============

.. c:function:: int pnv_eeh_get_log(struct eeh_pe *pe, int severity, char *drv_log, unsigned long len)

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

.. _`pnv_eeh_get_log.description`:

Description
-----------

Retrieve the temporary or permanent error from the PE.

.. _`pnv_eeh_configure_bridge`:

pnv_eeh_configure_bridge
========================

.. c:function:: int pnv_eeh_configure_bridge(struct eeh_pe *pe)

    Configure PCI bridges in the indicated PE

    :param pe:
        EEH PE
    :type pe: struct eeh_pe \*

.. _`pnv_eeh_configure_bridge.description`:

Description
-----------

The function will be called to reconfigure the bridges included
in the specified PE so that the mulfunctional PE would be recovered
again.

.. _`pnv_eeh_err_inject`:

pnv_eeh_err_inject
==================

.. c:function:: int pnv_eeh_err_inject(struct eeh_pe *pe, int type, int func, unsigned long addr, unsigned long mask)

    Inject specified error to the indicated PE

    :param pe:
        the indicated PE
    :type pe: struct eeh_pe \*

    :param type:
        error type
    :type type: int

    :param func:
        specific error type
    :type func: int

    :param addr:
        address
    :type addr: unsigned long

    :param mask:
        address mask
    :type mask: unsigned long

.. _`pnv_eeh_err_inject.description`:

Description
-----------

The routine is called to inject specified error, which is
determined by \ ``type``\  and \ ``func``\ , to the indicated PE for
testing purpose.

.. _`pnv_eeh_next_error`:

pnv_eeh_next_error
==================

.. c:function:: int pnv_eeh_next_error(struct eeh_pe **pe)

    Retrieve next EEH error to handle

    :param pe:
        Affected PE
    :type pe: struct eeh_pe \*\*

.. _`pnv_eeh_next_error.description`:

Description
-----------

The function is expected to be called by EEH core while it gets
special EEH event (without binding PE). The function calls to
OPAL APIs for next error to handle. The informational error is
handled internally by platform. However, the dead IOC, dead PHB,
fenced PHB and frozen PE should be handled by EEH core eventually.

.. _`eeh_powernv_init`:

eeh_powernv_init
================

.. c:function:: int eeh_powernv_init( void)

    Register platform dependent EEH operations

    :param void:
        no arguments
    :type void: 

.. _`eeh_powernv_init.description`:

Description
-----------

EEH initialization on powernv platform. This function should be
called before any EEH related functions.

.. This file was automatic generated / don't edit.

