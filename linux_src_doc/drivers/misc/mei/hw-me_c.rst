.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/hw-me.c

.. _`mei_me_reg_read`:

mei_me_reg_read
===============

.. c:function:: u32 mei_me_reg_read(const struct mei_me_hw *hw, unsigned long offset)

    Reads 32bit data from the mei device

    :param const struct mei_me_hw \*hw:
        the me hardware structure

    :param unsigned long offset:
        offset from which to read the data

.. _`mei_me_reg_read.return`:

Return
------

register value (u32)

.. _`mei_me_reg_write`:

mei_me_reg_write
================

.. c:function:: void mei_me_reg_write(const struct mei_me_hw *hw, unsigned long offset, u32 value)

    Writes 32bit data to the mei device

    :param const struct mei_me_hw \*hw:
        the me hardware structure

    :param unsigned long offset:
        offset from which to write the data

    :param u32 value:
        register value to write (u32)

.. _`mei_me_mecbrw_read`:

mei_me_mecbrw_read
==================

.. c:function:: u32 mei_me_mecbrw_read(const struct mei_device *dev)

    Reads 32bit data from ME circular buffer read window register

    :param const struct mei_device \*dev:
        the device structure

.. _`mei_me_mecbrw_read.return`:

Return
------

ME_CB_RW register value (u32)

.. _`mei_me_hcbww_write`:

mei_me_hcbww_write
==================

.. c:function:: void mei_me_hcbww_write(struct mei_device *dev, u32 data)

    write 32bit data to the host circular buffer

    :param struct mei_device \*dev:
        the device structure

    :param u32 data:
        32bit data to be written to the host circular buffer

.. _`mei_me_mecsr_read`:

mei_me_mecsr_read
=================

.. c:function:: u32 mei_me_mecsr_read(const struct mei_device *dev)

    Reads 32bit data from the ME CSR

    :param const struct mei_device \*dev:
        the device structure

.. _`mei_me_mecsr_read.return`:

Return
------

ME_CSR_HA register value (u32)

.. _`mei_hcsr_read`:

mei_hcsr_read
=============

.. c:function:: u32 mei_hcsr_read(const struct mei_device *dev)

    Reads 32bit data from the host CSR

    :param const struct mei_device \*dev:
        the device structure

.. _`mei_hcsr_read.return`:

Return
------

H_CSR register value (u32)

.. _`mei_hcsr_write`:

mei_hcsr_write
==============

.. c:function:: void mei_hcsr_write(struct mei_device *dev, u32 reg)

    writes H_CSR register to the mei device

    :param struct mei_device \*dev:
        the device structure

    :param u32 reg:
        new register value

.. _`mei_hcsr_set`:

mei_hcsr_set
============

.. c:function:: void mei_hcsr_set(struct mei_device *dev, u32 reg)

    writes H_CSR register to the mei device, and ignores the H_IS bit for it is write-one-to-zero.

    :param struct mei_device \*dev:
        the device structure

    :param u32 reg:
        new register value

.. _`mei_me_d0i3c_read`:

mei_me_d0i3c_read
=================

.. c:function:: u32 mei_me_d0i3c_read(const struct mei_device *dev)

    Reads 32bit data from the D0I3C register

    :param const struct mei_device \*dev:
        the device structure

.. _`mei_me_d0i3c_read.return`:

Return
------

H_D0I3C register value (u32)

.. _`mei_me_d0i3c_write`:

mei_me_d0i3c_write
==================

.. c:function:: void mei_me_d0i3c_write(struct mei_device *dev, u32 reg)

    writes H_D0I3C register to device

    :param struct mei_device \*dev:
        the device structure

    :param u32 reg:
        new register value

.. _`mei_me_fw_status`:

mei_me_fw_status
================

.. c:function:: int mei_me_fw_status(struct mei_device *dev, struct mei_fw_status *fw_status)

    read fw status register from pci config space

    :param struct mei_device \*dev:
        mei device

    :param struct mei_fw_status \*fw_status:
        fw status register values

.. _`mei_me_fw_status.return`:

Return
------

0 on success, error otherwise

.. _`mei_me_hw_config`:

mei_me_hw_config
================

.. c:function:: void mei_me_hw_config(struct mei_device *dev)

    configure hw dependent settings

    :param struct mei_device \*dev:
        mei device

.. _`mei_me_pg_state`:

mei_me_pg_state
===============

.. c:function:: enum mei_pg_state mei_me_pg_state(struct mei_device *dev)

    translate internal pg state to the mei power gating state

    :param struct mei_device \*dev:
        mei device

.. _`mei_me_pg_state.return`:

Return
------

MEI_PG_OFF if aliveness is on and MEI_PG_ON otherwise

.. _`me_intr_disable`:

me_intr_disable
===============

.. c:function:: void me_intr_disable(struct mei_device *dev, u32 hcsr)

    disables mei device interrupts using supplied hcsr register value.

    :param struct mei_device \*dev:
        the device structure

    :param u32 hcsr:
        supplied hcsr register value

.. _`me_intr_clear`:

me_intr_clear
=============

.. c:function:: void me_intr_clear(struct mei_device *dev, u32 hcsr)

    clear and stop interrupts

    :param struct mei_device \*dev:
        the device structure

    :param u32 hcsr:
        supplied hcsr register value

.. _`mei_me_intr_clear`:

mei_me_intr_clear
=================

.. c:function:: void mei_me_intr_clear(struct mei_device *dev)

    clear and stop interrupts

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_intr_enable`:

mei_me_intr_enable
==================

.. c:function:: void mei_me_intr_enable(struct mei_device *dev)

    enables mei device interrupts

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_intr_disable`:

mei_me_intr_disable
===================

.. c:function:: void mei_me_intr_disable(struct mei_device *dev)

    disables mei device interrupts

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_synchronize_irq`:

mei_me_synchronize_irq
======================

.. c:function:: void mei_me_synchronize_irq(struct mei_device *dev)

    wait for pending IRQ handlers

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_hw_reset_release`:

mei_me_hw_reset_release
=======================

.. c:function:: void mei_me_hw_reset_release(struct mei_device *dev)

    release device from the reset

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_host_set_ready`:

mei_me_host_set_ready
=====================

.. c:function:: void mei_me_host_set_ready(struct mei_device *dev)

    enable device

    :param struct mei_device \*dev:
        mei device

.. _`mei_me_host_is_ready`:

mei_me_host_is_ready
====================

.. c:function:: bool mei_me_host_is_ready(struct mei_device *dev)

    check whether the host has turned ready

    :param struct mei_device \*dev:
        mei device

.. _`mei_me_host_is_ready.return`:

Return
------

bool

.. _`mei_me_hw_is_ready`:

mei_me_hw_is_ready
==================

.. c:function:: bool mei_me_hw_is_ready(struct mei_device *dev)

    check whether the me(hw) has turned ready

    :param struct mei_device \*dev:
        mei device

.. _`mei_me_hw_is_ready.return`:

Return
------

bool

.. _`mei_me_hw_ready_wait`:

mei_me_hw_ready_wait
====================

.. c:function:: int mei_me_hw_ready_wait(struct mei_device *dev)

    wait until the me(hw) has turned ready or timeout is reached

    :param struct mei_device \*dev:
        mei device

.. _`mei_me_hw_ready_wait.return`:

Return
------

0 on success, error otherwise

.. _`mei_me_hw_start`:

mei_me_hw_start
===============

.. c:function:: int mei_me_hw_start(struct mei_device *dev)

    hw start routine

    :param struct mei_device \*dev:
        mei device

.. _`mei_me_hw_start.return`:

Return
------

0 on success, error otherwise

.. _`mei_hbuf_filled_slots`:

mei_hbuf_filled_slots
=====================

.. c:function:: unsigned char mei_hbuf_filled_slots(struct mei_device *dev)

    gets number of device filled buffer slots

    :param struct mei_device \*dev:
        the device structure

.. _`mei_hbuf_filled_slots.return`:

Return
------

number of filled slots

.. _`mei_me_hbuf_is_empty`:

mei_me_hbuf_is_empty
====================

.. c:function:: bool mei_me_hbuf_is_empty(struct mei_device *dev)

    checks if host buffer is empty.

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_hbuf_is_empty.return`:

Return
------

true if empty, false - otherwise.

.. _`mei_me_hbuf_empty_slots`:

mei_me_hbuf_empty_slots
=======================

.. c:function:: int mei_me_hbuf_empty_slots(struct mei_device *dev)

    counts write empty slots.

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_hbuf_empty_slots.return`:

Return
------

-EOVERFLOW if overflow, otherwise empty slots count

.. _`mei_me_hbuf_max_len`:

mei_me_hbuf_max_len
===================

.. c:function:: size_t mei_me_hbuf_max_len(const struct mei_device *dev)

    returns size of hw buffer.

    :param const struct mei_device \*dev:
        the device structure

.. _`mei_me_hbuf_max_len.return`:

Return
------

size of hw buffer in bytes

.. _`mei_me_hbuf_write`:

mei_me_hbuf_write
=================

.. c:function:: int mei_me_hbuf_write(struct mei_device *dev, struct mei_msg_hdr *header, const unsigned char *buf)

    writes a message to host hw buffer.

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_msg_hdr \*header:
        mei HECI header of message

    :param const unsigned char \*buf:
        message payload will be written

.. _`mei_me_hbuf_write.return`:

Return
------

-EIO if write has failed

.. _`mei_me_count_full_read_slots`:

mei_me_count_full_read_slots
============================

.. c:function:: int mei_me_count_full_read_slots(struct mei_device *dev)

    counts read full slots.

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_count_full_read_slots.return`:

Return
------

-EOVERFLOW if overflow, otherwise filled slots count

.. _`mei_me_read_slots`:

mei_me_read_slots
=================

.. c:function:: int mei_me_read_slots(struct mei_device *dev, unsigned char *buffer, unsigned long buffer_length)

    reads a message from mei device.

    :param struct mei_device \*dev:
        the device structure

    :param unsigned char \*buffer:
        message buffer will be written

    :param unsigned long buffer_length:
        message size will be read

.. _`mei_me_read_slots.return`:

Return
------

always 0

.. _`mei_me_pg_set`:

mei_me_pg_set
=============

.. c:function:: void mei_me_pg_set(struct mei_device *dev)

    write pg enter register

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_pg_unset`:

mei_me_pg_unset
===============

.. c:function:: void mei_me_pg_unset(struct mei_device *dev)

    write pg exit register

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_pg_legacy_enter_sync`:

mei_me_pg_legacy_enter_sync
===========================

.. c:function:: int mei_me_pg_legacy_enter_sync(struct mei_device *dev)

    perform legacy pg entry procedure

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_pg_legacy_enter_sync.return`:

Return
------

0 on success an error code otherwise

.. _`mei_me_pg_legacy_exit_sync`:

mei_me_pg_legacy_exit_sync
==========================

.. c:function:: int mei_me_pg_legacy_exit_sync(struct mei_device *dev)

    perform legacy pg exit procedure

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_pg_legacy_exit_sync.return`:

Return
------

0 on success an error code otherwise

.. _`mei_me_pg_in_transition`:

mei_me_pg_in_transition
=======================

.. c:function:: bool mei_me_pg_in_transition(struct mei_device *dev)

    is device now in pg transition

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_pg_in_transition.return`:

Return
------

true if in pg transition, false otherwise

.. _`mei_me_pg_is_enabled`:

mei_me_pg_is_enabled
====================

.. c:function:: bool mei_me_pg_is_enabled(struct mei_device *dev)

    detect if PG is supported by HW

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_pg_is_enabled.return`:

Return
------

true is pg supported, false otherwise

.. _`mei_me_d0i3_set`:

mei_me_d0i3_set
===============

.. c:function:: u32 mei_me_d0i3_set(struct mei_device *dev, bool intr)

    write d0i3 register bit on mei device.

    :param struct mei_device \*dev:
        the device structure

    :param bool intr:
        ask for interrupt

.. _`mei_me_d0i3_set.return`:

Return
------

D0I3C register value

.. _`mei_me_d0i3_unset`:

mei_me_d0i3_unset
=================

.. c:function:: u32 mei_me_d0i3_unset(struct mei_device *dev)

    clean d0i3 register bit on mei device.

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_d0i3_unset.return`:

Return
------

D0I3C register value

.. _`mei_me_d0i3_enter_sync`:

mei_me_d0i3_enter_sync
======================

.. c:function:: int mei_me_d0i3_enter_sync(struct mei_device *dev)

    perform d0i3 entry procedure

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_d0i3_enter_sync.return`:

Return
------

0 on success an error code otherwise

.. _`mei_me_d0i3_enter`:

mei_me_d0i3_enter
=================

.. c:function:: int mei_me_d0i3_enter(struct mei_device *dev)

    perform d0i3 entry procedure no hbm PG handshake no waiting for confirmation; runs with interrupts disabled

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_d0i3_enter.return`:

Return
------

0 on success an error code otherwise

.. _`mei_me_d0i3_exit_sync`:

mei_me_d0i3_exit_sync
=====================

.. c:function:: int mei_me_d0i3_exit_sync(struct mei_device *dev)

    perform d0i3 exit procedure

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_d0i3_exit_sync.return`:

Return
------

0 on success an error code otherwise

.. _`mei_me_pg_legacy_intr`:

mei_me_pg_legacy_intr
=====================

.. c:function:: void mei_me_pg_legacy_intr(struct mei_device *dev)

    perform legacy pg processing in interrupt thread handler

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_d0i3_intr`:

mei_me_d0i3_intr
================

.. c:function:: void mei_me_d0i3_intr(struct mei_device *dev, u32 intr_source)

    perform d0i3 processing in interrupt thread handler

    :param struct mei_device \*dev:
        the device structure

    :param u32 intr_source:
        interrupt source

.. _`mei_me_pg_intr`:

mei_me_pg_intr
==============

.. c:function:: void mei_me_pg_intr(struct mei_device *dev, u32 intr_source)

    perform pg processing in interrupt thread handler

    :param struct mei_device \*dev:
        the device structure

    :param u32 intr_source:
        interrupt source

.. _`mei_me_pg_enter_sync`:

mei_me_pg_enter_sync
====================

.. c:function:: int mei_me_pg_enter_sync(struct mei_device *dev)

    perform runtime pm entry procedure

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_pg_enter_sync.return`:

Return
------

0 on success an error code otherwise

.. _`mei_me_pg_exit_sync`:

mei_me_pg_exit_sync
===================

.. c:function:: int mei_me_pg_exit_sync(struct mei_device *dev)

    perform runtime pm exit procedure

    :param struct mei_device \*dev:
        the device structure

.. _`mei_me_pg_exit_sync.return`:

Return
------

0 on success an error code otherwise

.. _`mei_me_hw_reset`:

mei_me_hw_reset
===============

.. c:function:: int mei_me_hw_reset(struct mei_device *dev, bool intr_enable)

    resets fw via mei csr register.

    :param struct mei_device \*dev:
        the device structure

    :param bool intr_enable:
        if interrupt should be enabled after reset.

.. _`mei_me_hw_reset.return`:

Return
------

0 on success an error code otherwise

.. _`mei_me_irq_quick_handler`:

mei_me_irq_quick_handler
========================

.. c:function:: irqreturn_t mei_me_irq_quick_handler(int irq, void *dev_id)

    The ISR of the MEI device

    :param int irq:
        The irq number

    :param void \*dev_id:
        pointer to the device structure

.. _`mei_me_irq_quick_handler.return`:

Return
------

irqreturn_t

.. _`mei_me_irq_thread_handler`:

mei_me_irq_thread_handler
=========================

.. c:function:: irqreturn_t mei_me_irq_thread_handler(int irq, void *dev_id)

    function called after ISR to handle the interrupt processing.

    :param int irq:
        The irq number

    :param void \*dev_id:
        pointer to the device structure

.. _`mei_me_irq_thread_handler.return`:

Return
------

irqreturn_t

.. _`mei_me_dev_init`:

mei_me_dev_init
===============

.. c:function:: struct mei_device *mei_me_dev_init(struct pci_dev *pdev, const struct mei_cfg *cfg)

    allocates and initializes the mei device structure

    :param struct pci_dev \*pdev:
        The pci device structure

    :param const struct mei_cfg \*cfg:
        per device generation config

.. _`mei_me_dev_init.return`:

Return
------

The mei_device_device pointer on success, NULL on failure.

.. This file was automatic generated / don't edit.

