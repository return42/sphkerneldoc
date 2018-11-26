.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/hw-txe.c

.. _`mei_txe_reg_read`:

mei_txe_reg_read
================

.. c:function:: u32 mei_txe_reg_read(void __iomem *base_addr, unsigned long offset)

    Reads 32bit data from the txe device

    :param base_addr:
        registers base address
    :type base_addr: void __iomem \*

    :param offset:
        register offset
    :type offset: unsigned long

.. _`mei_txe_reg_read.return`:

Return
------

register value

.. _`mei_txe_reg_write`:

mei_txe_reg_write
=================

.. c:function:: void mei_txe_reg_write(void __iomem *base_addr, unsigned long offset, u32 value)

    Writes 32bit data to the txe device

    :param base_addr:
        registers base address
    :type base_addr: void __iomem \*

    :param offset:
        register offset
    :type offset: unsigned long

    :param value:
        the value to write
    :type value: u32

.. _`mei_txe_sec_reg_read_silent`:

mei_txe_sec_reg_read_silent
===========================

.. c:function:: u32 mei_txe_sec_reg_read_silent(struct mei_txe_hw *hw, unsigned long offset)

    Reads 32bit data from the SeC BAR

    :param hw:
        the txe hardware structure
    :type hw: struct mei_txe_hw \*

    :param offset:
        register offset
    :type offset: unsigned long

.. _`mei_txe_sec_reg_read_silent.description`:

Description
-----------

Doesn't check for aliveness while Reads 32bit data from the SeC BAR

.. _`mei_txe_sec_reg_read_silent.return`:

Return
------

register value

.. _`mei_txe_sec_reg_read`:

mei_txe_sec_reg_read
====================

.. c:function:: u32 mei_txe_sec_reg_read(struct mei_txe_hw *hw, unsigned long offset)

    Reads 32bit data from the SeC BAR

    :param hw:
        the txe hardware structure
    :type hw: struct mei_txe_hw \*

    :param offset:
        register offset
    :type offset: unsigned long

.. _`mei_txe_sec_reg_read.description`:

Description
-----------

Reads 32bit data from the SeC BAR and shout loud if aliveness is not set

.. _`mei_txe_sec_reg_read.return`:

Return
------

register value

.. _`mei_txe_sec_reg_write_silent`:

mei_txe_sec_reg_write_silent
============================

.. c:function:: void mei_txe_sec_reg_write_silent(struct mei_txe_hw *hw, unsigned long offset, u32 value)

    Writes 32bit data to the SeC BAR doesn't check for aliveness

    :param hw:
        the txe hardware structure
    :type hw: struct mei_txe_hw \*

    :param offset:
        register offset
    :type offset: unsigned long

    :param value:
        value to write
    :type value: u32

.. _`mei_txe_sec_reg_write_silent.description`:

Description
-----------

Doesn't check for aliveness while writes 32bit data from to the SeC BAR

.. _`mei_txe_sec_reg_write`:

mei_txe_sec_reg_write
=====================

.. c:function:: void mei_txe_sec_reg_write(struct mei_txe_hw *hw, unsigned long offset, u32 value)

    Writes 32bit data to the SeC BAR

    :param hw:
        the txe hardware structure
    :type hw: struct mei_txe_hw \*

    :param offset:
        register offset
    :type offset: unsigned long

    :param value:
        value to write
    :type value: u32

.. _`mei_txe_sec_reg_write.description`:

Description
-----------

Writes 32bit data from the SeC BAR and shout loud if aliveness is not set

.. _`mei_txe_br_reg_read`:

mei_txe_br_reg_read
===================

.. c:function:: u32 mei_txe_br_reg_read(struct mei_txe_hw *hw, unsigned long offset)

    Reads 32bit data from the Bridge BAR

    :param hw:
        the txe hardware structure
    :type hw: struct mei_txe_hw \*

    :param offset:
        offset from which to read the data
    :type offset: unsigned long

.. _`mei_txe_br_reg_read.return`:

Return
------

the byte read.

.. _`mei_txe_br_reg_write`:

mei_txe_br_reg_write
====================

.. c:function:: void mei_txe_br_reg_write(struct mei_txe_hw *hw, unsigned long offset, u32 value)

    Writes 32bit data to the Bridge BAR

    :param hw:
        the txe hardware structure
    :type hw: struct mei_txe_hw \*

    :param offset:
        offset from which to write the data
    :type offset: unsigned long

    :param value:
        the byte to write
    :type value: u32

.. _`mei_txe_aliveness_set`:

mei_txe_aliveness_set
=====================

.. c:function:: bool mei_txe_aliveness_set(struct mei_device *dev, u32 req)

    request for aliveness change

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param req:
        requested aliveness value
    :type req: u32

.. _`mei_txe_aliveness_set.description`:

Description
-----------

Request for aliveness change and returns true if the change is
really needed and false if aliveness is already
in the requested state

.. _`mei_txe_aliveness_set.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_txe_aliveness_set.return`:

Return
------

true if request was send

.. _`mei_txe_aliveness_req_get`:

mei_txe_aliveness_req_get
=========================

.. c:function:: u32 mei_txe_aliveness_req_get(struct mei_device *dev)

    get aliveness requested register value

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_aliveness_req_get.description`:

Description
-----------

Extract HICR_HOST_ALIVENESS_RESP_ACK bit from
from HICR_HOST_ALIVENESS_REQ register value

.. _`mei_txe_aliveness_req_get.return`:

Return
------

SICR_HOST_ALIVENESS_REQ_REQUESTED bit value

.. _`mei_txe_aliveness_get`:

mei_txe_aliveness_get
=====================

.. c:function:: u32 mei_txe_aliveness_get(struct mei_device *dev)

    get aliveness response register value

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_aliveness_get.return`:

Return
------

HICR_HOST_ALIVENESS_RESP_ACK bit from HICR_HOST_ALIVENESS_RESP
register

.. _`mei_txe_aliveness_poll`:

mei_txe_aliveness_poll
======================

.. c:function:: int mei_txe_aliveness_poll(struct mei_device *dev, u32 expected)

    waits for aliveness to settle

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param expected:
        expected aliveness value
    :type expected: u32

.. _`mei_txe_aliveness_poll.description`:

Description
-----------

Polls for HICR_HOST_ALIVENESS_RESP.ALIVENESS_RESP to be set

.. _`mei_txe_aliveness_poll.return`:

Return
------

0 if the expected value was received, -ETIME otherwise

.. _`mei_txe_aliveness_wait`:

mei_txe_aliveness_wait
======================

.. c:function:: int mei_txe_aliveness_wait(struct mei_device *dev, u32 expected)

    waits for aliveness to settle

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param expected:
        expected aliveness value
    :type expected: u32

.. _`mei_txe_aliveness_wait.description`:

Description
-----------

Waits for HICR_HOST_ALIVENESS_RESP.ALIVENESS_RESP to be set

.. _`mei_txe_aliveness_wait.return`:

Return
------

0 on success and < 0 otherwise

.. _`mei_txe_aliveness_set_sync`:

mei_txe_aliveness_set_sync
==========================

.. c:function:: int mei_txe_aliveness_set_sync(struct mei_device *dev, u32 req)

    sets an wait for aliveness to complete

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param req:
        requested aliveness value
    :type req: u32

.. _`mei_txe_aliveness_set_sync.return`:

Return
------

0 on success and < 0 otherwise

.. _`mei_txe_pg_in_transition`:

mei_txe_pg_in_transition
========================

.. c:function:: bool mei_txe_pg_in_transition(struct mei_device *dev)

    is device now in pg transition

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_pg_in_transition.return`:

Return
------

true if in pg transition, false otherwise

.. _`mei_txe_pg_is_enabled`:

mei_txe_pg_is_enabled
=====================

.. c:function:: bool mei_txe_pg_is_enabled(struct mei_device *dev)

    detect if PG is supported by HW

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_pg_is_enabled.return`:

Return
------

true is pg supported, false otherwise

.. _`mei_txe_pg_state`:

mei_txe_pg_state
================

.. c:function:: enum mei_pg_state mei_txe_pg_state(struct mei_device *dev)

    translate aliveness register value to the mei power gating state

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_pg_state.return`:

Return
------

MEI_PG_OFF if aliveness is on and MEI_PG_ON otherwise

.. _`mei_txe_input_ready_interrupt_enable`:

mei_txe_input_ready_interrupt_enable
====================================

.. c:function:: void mei_txe_input_ready_interrupt_enable(struct mei_device *dev)

    sets the Input Ready Interrupt

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_input_doorbell_set`:

mei_txe_input_doorbell_set
==========================

.. c:function:: void mei_txe_input_doorbell_set(struct mei_txe_hw *hw)

    sets bit 0 in SEC_IPC_INPUT_DOORBELL.IPC_INPUT_DOORBELL.

    :param hw:
        the txe hardware structure
    :type hw: struct mei_txe_hw \*

.. _`mei_txe_output_ready_set`:

mei_txe_output_ready_set
========================

.. c:function:: void mei_txe_output_ready_set(struct mei_txe_hw *hw)

    Sets the SICR_SEC_IPC_OUTPUT_STATUS bit to 1

    :param hw:
        the txe hardware structure
    :type hw: struct mei_txe_hw \*

.. _`mei_txe_is_input_ready`:

mei_txe_is_input_ready
======================

.. c:function:: bool mei_txe_is_input_ready(struct mei_device *dev)

    check if TXE is ready for receiving data

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_is_input_ready.return`:

Return
------

true if INPUT STATUS READY bit is set

.. _`mei_txe_intr_clear`:

mei_txe_intr_clear
==================

.. c:function:: void mei_txe_intr_clear(struct mei_device *dev)

    clear all interrupts

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_intr_disable`:

mei_txe_intr_disable
====================

.. c:function:: void mei_txe_intr_disable(struct mei_device *dev)

    disable all interrupts

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_intr_enable`:

mei_txe_intr_enable
===================

.. c:function:: void mei_txe_intr_enable(struct mei_device *dev)

    enable all interrupts

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_synchronize_irq`:

mei_txe_synchronize_irq
=======================

.. c:function:: void mei_txe_synchronize_irq(struct mei_device *dev)

    wait for pending IRQ handlers

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_pending_interrupts`:

mei_txe_pending_interrupts
==========================

.. c:function:: bool mei_txe_pending_interrupts(struct mei_device *dev)

    check if there are pending interrupts only Aliveness, Input ready, and output doorbell are of relevance

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_pending_interrupts.description`:

Description
-----------

Checks if there are pending interrupts
only Aliveness, Readiness, Input ready, and Output doorbell are relevant

.. _`mei_txe_pending_interrupts.return`:

Return
------

true if there are pending interrupts

.. _`mei_txe_input_payload_write`:

mei_txe_input_payload_write
===========================

.. c:function:: void mei_txe_input_payload_write(struct mei_device *dev, unsigned long idx, u32 value)

    write a dword to the host buffer at offset idx

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param idx:
        index in the host buffer
    :type idx: unsigned long

    :param value:
        value
    :type value: u32

.. _`mei_txe_out_data_read`:

mei_txe_out_data_read
=====================

.. c:function:: u32 mei_txe_out_data_read(const struct mei_device *dev, unsigned long idx)

    read dword from the device buffer at offset idx

    :param dev:
        the device structure
    :type dev: const struct mei_device \*

    :param idx:
        index in the device buffer
    :type idx: unsigned long

.. _`mei_txe_out_data_read.return`:

Return
------

register value at index

.. _`mei_txe_readiness_set_host_rdy`:

mei_txe_readiness_set_host_rdy
==============================

.. c:function:: void mei_txe_readiness_set_host_rdy(struct mei_device *dev)

    set host readiness bit

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_readiness_clear`:

mei_txe_readiness_clear
=======================

.. c:function:: void mei_txe_readiness_clear(struct mei_device *dev)

    clear host readiness bit

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_readiness_get`:

mei_txe_readiness_get
=====================

.. c:function:: u32 mei_txe_readiness_get(struct mei_device *dev)

    Reads and returns the HICR_SEC_IPC_READINESS register value

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_readiness_get.return`:

Return
------

the HICR_SEC_IPC_READINESS register value

.. _`mei_txe_readiness_is_sec_rdy`:

mei_txe_readiness_is_sec_rdy
============================

.. c:function:: bool mei_txe_readiness_is_sec_rdy(u32 readiness)

    check readiness for HICR_SEC_IPC_READINESS_SEC_RDY

    :param readiness:
        cached readiness state
    :type readiness: u32

.. _`mei_txe_readiness_is_sec_rdy.return`:

Return
------

true if readiness bit is set

.. _`mei_txe_hw_is_ready`:

mei_txe_hw_is_ready
===================

.. c:function:: bool mei_txe_hw_is_ready(struct mei_device *dev)

    check if the hw is ready

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_hw_is_ready.return`:

Return
------

true if sec is ready

.. _`mei_txe_host_is_ready`:

mei_txe_host_is_ready
=====================

.. c:function:: bool mei_txe_host_is_ready(struct mei_device *dev)

    check if the host is ready

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_host_is_ready.return`:

Return
------

true if host is ready

.. _`mei_txe_readiness_wait`:

mei_txe_readiness_wait
======================

.. c:function:: int mei_txe_readiness_wait(struct mei_device *dev)

    wait till readiness settles

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_readiness_wait.return`:

Return
------

0 on success and -ETIME on timeout

.. _`mei_txe_fw_status`:

mei_txe_fw_status
=================

.. c:function:: int mei_txe_fw_status(struct mei_device *dev, struct mei_fw_status *fw_status)

    read fw status register from pci config space

    :param dev:
        mei device
    :type dev: struct mei_device \*

    :param fw_status:
        fw status register values
    :type fw_status: struct mei_fw_status \*

.. _`mei_txe_fw_status.return`:

Return
------

0 on success, error otherwise

.. _`mei_txe_hw_config`:

mei_txe_hw_config
=================

.. c:function:: void mei_txe_hw_config(struct mei_device *dev)

    configure hardware at the start of the devices

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_hw_config.description`:

Description
-----------

Configure hardware at the start of the device should be done only
once at the device probe time

.. _`mei_txe_write`:

mei_txe_write
=============

.. c:function:: int mei_txe_write(struct mei_device *dev, const void *hdr, size_t hdr_len, const void *data, size_t data_len)

    writes a message to device.

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param hdr:
        header of message
    :type hdr: const void \*

    :param hdr_len:
        header length in bytes - must multiplication of a slot (4bytes)
    :type hdr_len: size_t

    :param data:
        payload
    :type data: const void \*

    :param data_len:
        paylead length in bytes
    :type data_len: size_t

.. _`mei_txe_write.return`:

Return
------

0 if success, < 0 - otherwise.

.. _`mei_txe_hbuf_depth`:

mei_txe_hbuf_depth
==================

.. c:function:: u32 mei_txe_hbuf_depth(const struct mei_device *dev)

    mimics the me hbuf circular buffer

    :param dev:
        the device structure
    :type dev: const struct mei_device \*

.. _`mei_txe_hbuf_depth.return`:

Return
------

the TXE_HBUF_DEPTH

.. _`mei_txe_hbuf_empty_slots`:

mei_txe_hbuf_empty_slots
========================

.. c:function:: int mei_txe_hbuf_empty_slots(struct mei_device *dev)

    mimics the me hbuf circular buffer

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_hbuf_empty_slots.return`:

Return
------

always TXE_HBUF_DEPTH

.. _`mei_txe_count_full_read_slots`:

mei_txe_count_full_read_slots
=============================

.. c:function:: int mei_txe_count_full_read_slots(struct mei_device *dev)

    mimics the me device circular buffer

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_count_full_read_slots.return`:

Return
------

always buffer size in dwords count

.. _`mei_txe_read_hdr`:

mei_txe_read_hdr
================

.. c:function:: u32 mei_txe_read_hdr(const struct mei_device *dev)

    read message header which is always in 4 first bytes

    :param dev:
        the device structure
    :type dev: const struct mei_device \*

.. _`mei_txe_read_hdr.return`:

Return
------

mei message header

.. _`mei_txe_read`:

mei_txe_read
============

.. c:function:: int mei_txe_read(struct mei_device *dev, unsigned char *buf, unsigned long len)

    reads a message from the txe device.

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param buf:
        message buffer will be written
    :type buf: unsigned char \*

    :param len:
        message size will be read
    :type len: unsigned long

.. _`mei_txe_read.return`:

Return
------

-EINVAL on error wrong argument and 0 on success

.. _`mei_txe_hw_reset`:

mei_txe_hw_reset
================

.. c:function:: int mei_txe_hw_reset(struct mei_device *dev, bool intr_enable)

    resets host and fw.

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param intr_enable:
        if interrupt should be enabled after reset.
    :type intr_enable: bool

.. _`mei_txe_hw_reset.return`:

Return
------

0 on success and < 0 in case of error

.. _`mei_txe_hw_start`:

mei_txe_hw_start
================

.. c:function:: int mei_txe_hw_start(struct mei_device *dev)

    start the hardware after reset

    :param dev:
        the device structure
    :type dev: struct mei_device \*

.. _`mei_txe_hw_start.return`:

Return
------

0 on success an error code otherwise

.. _`mei_txe_check_and_ack_intrs`:

mei_txe_check_and_ack_intrs
===========================

.. c:function:: bool mei_txe_check_and_ack_intrs(struct mei_device *dev, bool do_ack)

    translate multi BAR interrupt into single bit mask and acknowledge the interrupts

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param do_ack:
        acknowledge interrupts
    :type do_ack: bool

.. _`mei_txe_check_and_ack_intrs.return`:

Return
------

true if found interrupts to process.

.. _`mei_txe_irq_quick_handler`:

mei_txe_irq_quick_handler
=========================

.. c:function:: irqreturn_t mei_txe_irq_quick_handler(int irq, void *dev_id)

    The ISR of the MEI device

    :param irq:
        The irq number
    :type irq: int

    :param dev_id:
        pointer to the device structure
    :type dev_id: void \*

.. _`mei_txe_irq_quick_handler.return`:

Return
------

IRQ_WAKE_THREAD if interrupt is designed for the device
IRQ_NONE otherwise

.. _`mei_txe_irq_thread_handler`:

mei_txe_irq_thread_handler
==========================

.. c:function:: irqreturn_t mei_txe_irq_thread_handler(int irq, void *dev_id)

    txe interrupt thread

    :param irq:
        The irq number
    :type irq: int

    :param dev_id:
        pointer to the device structure
    :type dev_id: void \*

.. _`mei_txe_irq_thread_handler.return`:

Return
------

IRQ_HANDLED

.. _`mei_txe_dev_init`:

mei_txe_dev_init
================

.. c:function:: struct mei_device *mei_txe_dev_init(struct pci_dev *pdev)

    allocates and initializes txe hardware specific structure

    :param pdev:
        pci device
    :type pdev: struct pci_dev \*

.. _`mei_txe_dev_init.return`:

Return
------

struct mei_device \* on success or NULL

.. _`mei_txe_setup_satt2`:

mei_txe_setup_satt2
===================

.. c:function:: int mei_txe_setup_satt2(struct mei_device *dev, phys_addr_t addr, u32 range)

    SATT2 configuration for DMA support.

    :param dev:
        the device structure
    :type dev: struct mei_device \*

    :param addr:
        physical address start of the range
    :type addr: phys_addr_t

    :param range:
        physical range size
    :type range: u32

.. _`mei_txe_setup_satt2.return`:

Return
------

0 on success an error code otherwise

.. This file was automatic generated / don't edit.

