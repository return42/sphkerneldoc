.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_iba6120.c

.. _`qib_read_ureg32`:

qib_read_ureg32
===============

.. c:function:: u32 qib_read_ureg32(const struct qib_devdata *dd, enum qib_ureg regno, int ctxt)

    read 32-bit virtualized per-context register

    :param const struct qib_devdata \*dd:
        device

    :param enum qib_ureg regno:
        register number

    :param int ctxt:
        context number

.. _`qib_read_ureg32.description`:

Description
-----------

Return the contents of a register that is virtualized to be per context.
Returns -1 on errors (not distinguishable from valid contents at
runtime; we may add a separate error variable at some point).

.. _`qib_write_ureg`:

qib_write_ureg
==============

.. c:function:: void qib_write_ureg(const struct qib_devdata *dd, enum qib_ureg regno, u64 value, int ctxt)

    write 32-bit virtualized per-context register

    :param const struct qib_devdata \*dd:
        device

    :param enum qib_ureg regno:
        register number

    :param u64 value:
        value

    :param int ctxt:
        context

.. _`qib_write_ureg.description`:

Description
-----------

Write the contents of a register that is virtualized to be per context.

.. _`qib_write_kreg_ctxt`:

qib_write_kreg_ctxt
===================

.. c:function:: void qib_write_kreg_ctxt(const struct qib_devdata *dd, const u16 regno, unsigned ctxt, u64 value)

    write a device's per-ctxt 64-bit kernel register

    :param const struct qib_devdata \*dd:
        the qlogic_ib device

    :param const u16 regno:
        the register number to write

    :param unsigned ctxt:
        the context containing the register

    :param u64 value:
        the value to write

.. _`qib_handle_6120_hwerrors`:

qib_handle_6120_hwerrors
========================

.. c:function:: void qib_handle_6120_hwerrors(struct qib_devdata *dd, char *msg, size_t msgl)

    display hardware errors.

    :param struct qib_devdata \*dd:
        the qlogic_ib device

    :param char \*msg:
        the output buffer

    :param size_t msgl:
        the size of the output buffer

.. _`qib_handle_6120_hwerrors.description`:

Description
-----------

Use same msg buffer as regular errors to avoid excessive stack
use.  Most hardware errors are catastrophic, but for right now,
we'll print them and continue.  Reuse the same message buffer as
\ :c:func:`handle_6120_errors`\  to avoid excessive stack usage.

.. _`qib_6120_init_hwerrors`:

qib_6120_init_hwerrors
======================

.. c:function:: void qib_6120_init_hwerrors(struct qib_devdata *dd)

    enable hardware errors

    :param struct qib_devdata \*dd:
        the qlogic_ib device

.. _`qib_6120_init_hwerrors.description`:

Description
-----------

now that we have finished initializing everything that might reasonably
cause a hardware error, and cleared those errors bits as they occur,
we can enable hardware errors in the mask (potentially enabling
freeze mode), and enable hardware errors as errors (along with
everything else) in errormask

.. _`qib_6120_bringup_serdes`:

qib_6120_bringup_serdes
=======================

.. c:function:: int qib_6120_bringup_serdes(struct qib_pportdata *ppd)

    bring up the serdes

    :param struct qib_pportdata \*ppd:
        *undescribed*

.. _`qib_6120_quiet_serdes`:

qib_6120_quiet_serdes
=====================

.. c:function:: void qib_6120_quiet_serdes(struct qib_pportdata *ppd)

    set serdes to txidle

    :param struct qib_pportdata \*ppd:
        physical port of the qlogic_ib device
        Called when driver is being unloaded

.. _`qib_6120_setup_setextled`:

qib_6120_setup_setextled
========================

.. c:function:: void qib_6120_setup_setextled(struct qib_pportdata *ppd, u32 on)

    set the state of the two external LEDs

    :param struct qib_pportdata \*ppd:
        *undescribed*

    :param u32 on:
        whether the link is up or not

.. _`qib_6120_setup_setextled.description`:

Description
-----------

The exact combo of LEDs if on is true is determined by looking
at the ibcstatus.
These LEDs indicate the physical and logical state of IB link.
For this chip (at least with recommended board pinouts), LED1
is Yellow (logical state) and LED2 is Green (physical state),

.. _`qib_6120_setup_setextled.note`:

Note
----

We try to match the Mellanox HCA LED behavior as best
we can.  Green indicates physical link state is OK (something is
plugged in, and we can train).
Amber indicates the link is logically up (ACTIVE).
Mellanox further blinks the amber LED to indicate data packet
activity, but we have no hardware support for that, so it would
require waking up every 10-20 msecs and checking the counters
on the chip, and then turning the LED off if appropriate.  That's
visible overhead, so not something we will do.

.. _`qib_6120_setup_cleanup`:

qib_6120_setup_cleanup
======================

.. c:function:: void qib_6120_setup_cleanup(struct qib_devdata *dd)

    clean up any per-chip chip-specific stuff

    :param struct qib_devdata \*dd:
        the qlogic_ib device

.. _`qib_6120_setup_cleanup.description`:

Description
-----------

This is called during driver unload.

.. _`pe_boardname`:

pe_boardname
============

.. c:function:: void pe_boardname(struct qib_devdata *dd)

    fill in the board name

    :param struct qib_devdata \*dd:
        the qlogic_ib device

.. _`pe_boardname.description`:

Description
-----------

info is based on the board revision register

.. _`qib_6120_put_tid`:

qib_6120_put_tid
================

.. c:function:: void qib_6120_put_tid(struct qib_devdata *dd, u64 __iomem *tidptr, u32 type, unsigned long pa)

    write a TID in chip

    :param struct qib_devdata \*dd:
        the qlogic_ib device

    :param u64 __iomem \*tidptr:
        pointer to the expected TID (in chip) to update

    :param u32 type:
        *undescribed*

    :param unsigned long pa:
        physical address of in memory buffer; tidinvalid if freeing

.. _`qib_6120_put_tid.description`:

Description
-----------

This exists as a separate routine to allow for special locking etc.
It's used for both the full cleanup on exit, as well as the normal
setup and teardown.

.. _`qib_6120_put_tid_2`:

qib_6120_put_tid_2
==================

.. c:function:: void qib_6120_put_tid_2(struct qib_devdata *dd, u64 __iomem *tidptr, u32 type, unsigned long pa)

    write a TID in chip, Revision 2 or higher

    :param struct qib_devdata \*dd:
        the qlogic_ib device

    :param u64 __iomem \*tidptr:
        pointer to the expected TID (in chip) to update

    :param u32 type:
        *undescribed*

    :param unsigned long pa:
        physical address of in memory buffer; tidinvalid if freeing

.. _`qib_6120_put_tid_2.description`:

Description
-----------

This exists as a separate routine to allow for selection of the
appropriate "flavor". The static calls in cleanup just use the
revision-agnostic form, as they are not performance critical.

.. _`qib_6120_clear_tids`:

qib_6120_clear_tids
===================

.. c:function:: void qib_6120_clear_tids(struct qib_devdata *dd, struct qib_ctxtdata *rcd)

    clear all TID entries for a context, expected and eager

    :param struct qib_devdata \*dd:
        the qlogic_ib device

    :param struct qib_ctxtdata \*rcd:
        *undescribed*

.. _`qib_6120_clear_tids.description`:

Description
-----------

clear all TID entries for a context, expected and eager.
Used from \ :c:func:`qib_close`\ .  On this chip, TIDs are only 32 bits,
not 64, but they are still on 64 bit boundaries, so tidbase
is declared as u64 \* for the pointer math, even though we write 32 bits

.. _`qib_6120_tidtemplate`:

qib_6120_tidtemplate
====================

.. c:function:: void qib_6120_tidtemplate(struct qib_devdata *dd)

    setup constants for TID updates

    :param struct qib_devdata \*dd:
        the qlogic_ib device

.. _`qib_6120_tidtemplate.description`:

Description
-----------

We setup stuff that we use a lot, to avoid calculating each time

.. _`qib_6120_get_base_info`:

qib_6120_get_base_info
======================

.. c:function:: int qib_6120_get_base_info(struct qib_ctxtdata *rcd, struct qib_base_info *kinfo)

    set chip-specific flags for user code

    :param struct qib_ctxtdata \*rcd:
        the qlogic_ib ctxt

    :param struct qib_base_info \*kinfo:
        *undescribed*

.. _`qib_6120_get_base_info.description`:

Description
-----------

We set the PCIE flag because the lower bandwidth on PCIe vs
HyperTransport can affect some user packet algorithms.

.. _`qib_portcntr_6120`:

qib_portcntr_6120
=================

.. c:function:: u64 qib_portcntr_6120(struct qib_pportdata *ppd, u32 reg)

    read a per-port counter

    :param struct qib_pportdata \*ppd:
        *undescribed*

    :param u32 reg:
        *undescribed*

.. _`qib_get_6120_faststats`:

qib_get_6120_faststats
======================

.. c:function:: void qib_get_6120_faststats(struct timer_list *t)

    get word counters from chip before they overflow \ ``opaque``\  - contains a pointer to the qlogic_ib device qib_devdata

    :param struct timer_list \*t:
        *undescribed*

.. _`qib_get_6120_faststats.description`:

Description
-----------

This needs more work; in particular, decision on whether we really
need traffic_wds done the way it is
called from add_timer

.. _`qib_init_iba6120_funcs`:

qib_init_iba6120_funcs
======================

.. c:function:: struct qib_devdata *qib_init_iba6120_funcs(struct pci_dev *pdev, const struct pci_device_id *ent)

    set up the chip-specific function pointers

    :param struct pci_dev \*pdev:
        pci_dev of the qlogic_ib device

    :param const struct pci_device_id \*ent:
        pci_device_id matching this chip

.. _`qib_init_iba6120_funcs.description`:

Description
-----------

This is global, and is called directly at init to set up the
chip-specific function pointers for later use.

It also allocates/partially-inits the qib_devdata struct for
this device.

.. This file was automatic generated / don't edit.

