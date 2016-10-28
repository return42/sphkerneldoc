.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_iba7322.c

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

.. _`qib_read_ureg`:

qib_read_ureg
=============

.. c:function:: u64 qib_read_ureg(const struct qib_devdata *dd, enum qib_ureg regno, int ctxt)

    read virtualized per-context register

    :param const struct qib_devdata \*dd:
        device

    :param enum qib_ureg regno:
        register number

    :param int ctxt:
        context number

.. _`qib_read_ureg.description`:

Description
-----------

Return the contents of a register that is virtualized to be per context.
Returns -1 on errors (not distinguishable from valid contents at
runtime; we may add a separate error variable at some point).

.. _`qib_write_ureg`:

qib_write_ureg
==============

.. c:function:: void qib_write_ureg(const struct qib_devdata *dd, enum qib_ureg regno, u64 value, int ctxt)

    write virtualized per-context register

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

.. _`qib_7322_handle_hwerrors`:

qib_7322_handle_hwerrors
========================

.. c:function:: void qib_7322_handle_hwerrors(struct qib_devdata *dd, char *msg, size_t msgl)

    display hardware errors.

    :param struct qib_devdata \*dd:
        the qlogic_ib device

    :param char \*msg:
        the output buffer

    :param size_t msgl:
        the size of the output buffer

.. _`qib_7322_handle_hwerrors.description`:

Description
-----------

Use same msg buffer as regular errors to avoid excessive stack
use.  Most hardware errors are catastrophic, but for right now,
we'll print them and continue.  We reuse the same message buffer as
\ :c:func:`qib_handle_errors`\  to avoid excessive stack usage.

.. _`qib_7322_init_hwerrors`:

qib_7322_init_hwerrors
======================

.. c:function:: void qib_7322_init_hwerrors(struct qib_devdata *dd)

    enable hardware errors

    :param struct qib_devdata \*dd:
        the qlogic_ib device

.. _`qib_7322_init_hwerrors.description`:

Description
-----------

now that we have finished initializing everything that might reasonably
cause a hardware error, and cleared those errors bits as they occur,
we can enable hardware errors in the mask (potentially enabling
freeze mode), and enable hardware errors as errors (along with
everything else) in errormask

.. _`qib_7322_bringup_serdes`:

qib_7322_bringup_serdes
=======================

.. c:function:: int qib_7322_bringup_serdes(struct qib_pportdata *ppd)

    bring up the serdes

    :param struct qib_pportdata \*ppd:
        physical port on the qlogic_ib device

.. _`qib_7322_mini_quiet_serdes`:

qib_7322_mini_quiet_serdes
==========================

.. c:function:: void qib_7322_mini_quiet_serdes(struct qib_pportdata *ppd)

    set serdes to txidle

    :param struct qib_pportdata \*ppd:
        *undescribed*

.. _`qib_setup_7322_setextled`:

qib_setup_7322_setextled
========================

.. c:function:: void qib_setup_7322_setextled(struct qib_pportdata *ppd, u32 on)

    set the state of the two external LEDs

    :param struct qib_pportdata \*ppd:
        physical port on the qlogic_ib device

    :param u32 on:
        whether the link is up or not

.. _`qib_setup_7322_setextled.description`:

Description
-----------

The exact combo of LEDs if on is true is determined by looking
at the ibcstatus.

These LEDs indicate the physical and logical state of IB link.
For this chip (at least with recommended board pinouts), LED1
is Yellow (logical state) and LED2 is Green (physical state),

.. _`qib_setup_7322_setextled.note`:

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

.. _`qib_7322_boardname`:

qib_7322_boardname
==================

.. c:function:: unsigned qib_7322_boardname(struct qib_devdata *dd)

    fill in the board name and note features

    :param struct qib_devdata \*dd:
        the qlogic_ib device

.. _`qib_7322_boardname.description`:

Description
-----------

info will be based on the board revision register

.. _`qib_7322_put_tid`:

qib_7322_put_tid
================

.. c:function:: void qib_7322_put_tid(struct qib_devdata *dd, u64 __iomem *tidptr, u32 type, unsigned long pa)

    write a TID to the chip

    :param struct qib_devdata \*dd:
        the qlogic_ib device

    :param u64 __iomem \*tidptr:
        pointer to the expected TID (in chip) to update

    :param u32 type:
        *undescribed*

    :param unsigned long pa:
        physical address of in memory buffer; tidinvalid if freeing

.. _`qib_7322_clear_tids`:

qib_7322_clear_tids
===================

.. c:function:: void qib_7322_clear_tids(struct qib_devdata *dd, struct qib_ctxtdata *rcd)

    clear all TID entries for a ctxt, expected and eager

    :param struct qib_devdata \*dd:
        the qlogic_ib device

    :param struct qib_ctxtdata \*rcd:
        *undescribed*

.. _`qib_7322_clear_tids.description`:

Description
-----------

clear all TID entries for a ctxt, expected and eager.
Used from \ :c:func:`qib_close`\ .

.. _`qib_7322_tidtemplate`:

qib_7322_tidtemplate
====================

.. c:function:: void qib_7322_tidtemplate(struct qib_devdata *dd)

    setup constants for TID updates

    :param struct qib_devdata \*dd:
        the qlogic_ib device

.. _`qib_7322_tidtemplate.description`:

Description
-----------

We setup stuff that we use a lot, to avoid calculating each time

.. _`qib_7322_get_base_info`:

qib_7322_get_base_info
======================

.. c:function:: int qib_7322_get_base_info(struct qib_ctxtdata *rcd, struct qib_base_info *kinfo)

    set chip-specific flags for user code

    :param struct qib_ctxtdata \*rcd:
        the qlogic_ib ctxt

    :param struct qib_base_info \*kinfo:
        *undescribed*

.. _`qib_7322_get_base_info.description`:

Description
-----------

We set the PCIE flag because the lower bandwidth on PCIe vs
HyperTransport can affect some user packet algorithims.

.. _`qib_portcntr_7322`:

qib_portcntr_7322
=================

.. c:function:: u64 qib_portcntr_7322(struct qib_pportdata *ppd, u32 reg)

    read a per-port chip counter

    :param struct qib_pportdata \*ppd:
        the qlogic_ib pport

    :param u32 reg:
        *undescribed*

.. _`qib_get_7322_faststats`:

qib_get_7322_faststats
======================

.. c:function:: void qib_get_7322_faststats(unsigned long opaque)

    get word counters from chip before they overflow \ ``opaque``\  - contains a pointer to the qlogic_ib device qib_devdata

    :param unsigned long opaque:
        *undescribed*

.. _`qib_get_7322_faststats.description`:

Description
-----------

VESTIGIAL IBA7322 has no "small fast counters", so the only
real purpose of this function is to maintain the notion of
"active time", which in turn is only logged into the eeprom,
which we don;t have, yet, for 7322-based boards.

called from add_timer

.. _`qib_init_iba7322_funcs`:

qib_init_iba7322_funcs
======================

.. c:function:: struct qib_devdata *qib_init_iba7322_funcs(struct pci_dev *pdev, const struct pci_device_id *ent)

    set up the chip-specific function pointers

    :param struct pci_dev \*pdev:
        *undescribed*

    :param const struct pci_device_id \*ent:
        pci_device_id struct for this dev

.. _`qib_init_iba7322_funcs.description`:

Description
-----------

Also allocates, inits, and returns the devdata struct for this
device instance

This is global, and is called directly at init to set up the
chip-specific function pointers for later use.

.. This file was automatic generated / don't edit.

