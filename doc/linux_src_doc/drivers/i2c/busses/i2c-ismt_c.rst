.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-ismt.c

.. _`__ismt_desc_dump`:

__ismt_desc_dump
================

.. c:function:: void __ismt_desc_dump(struct device *dev, const struct ismt_desc *desc)

    dump the contents of a specific descriptor

    :param struct device \*dev:
        *undescribed*

    :param const struct ismt_desc \*desc:
        *undescribed*

.. _`ismt_desc_dump`:

ismt_desc_dump
==============

.. c:function:: void ismt_desc_dump(struct ismt_priv *priv)

    dump the contents of a descriptor for debug purposes

    :param struct ismt_priv \*priv:
        iSMT private data

.. _`ismt_gen_reg_dump`:

ismt_gen_reg_dump
=================

.. c:function:: void ismt_gen_reg_dump(struct ismt_priv *priv)

    dump the iSMT General Registers

    :param struct ismt_priv \*priv:
        iSMT private data

.. _`ismt_mstr_reg_dump`:

ismt_mstr_reg_dump
==================

.. c:function:: void ismt_mstr_reg_dump(struct ismt_priv *priv)

    dump the iSMT Master Registers

    :param struct ismt_priv \*priv:
        iSMT private data

.. _`ismt_submit_desc`:

ismt_submit_desc
================

.. c:function:: void ismt_submit_desc(struct ismt_priv *priv)

    add a descriptor to the ring

    :param struct ismt_priv \*priv:
        iSMT private data

.. _`ismt_process_desc`:

ismt_process_desc
=================

.. c:function:: int ismt_process_desc(const struct ismt_desc *desc, union i2c_smbus_data *data, struct ismt_priv *priv, int size, char read_write)

    handle the completion of the descriptor

    :param const struct ismt_desc \*desc:
        the iSMT hardware descriptor

    :param union i2c_smbus_data \*data:
        data buffer from the upper layer

    :param struct ismt_priv \*priv:
        ismt_priv struct holding our dma buffer

    :param int size:
        SMBus transaction type

    :param char read_write:
        flag to indicate if this is a read or write

.. _`ismt_access`:

ismt_access
===========

.. c:function:: int ismt_access(struct i2c_adapter *adap, u16 addr, unsigned short flags, char read_write, u8 command, int size, union i2c_smbus_data *data)

    process an SMBus command

    :param struct i2c_adapter \*adap:
        the i2c host adapter

    :param u16 addr:
        address of the i2c/SMBus target

    :param unsigned short flags:
        command options

    :param char read_write:
        read from or write to device

    :param u8 command:
        the i2c/SMBus command to issue

    :param int size:
        SMBus transaction type

    :param union i2c_smbus_data \*data:
        read/write data buffer

.. _`ismt_func`:

ismt_func
=========

.. c:function:: u32 ismt_func(struct i2c_adapter *adap)

    report which i2c commands are supported by this adapter

    :param struct i2c_adapter \*adap:
        the i2c host adapter

.. _`ismt_handle_isr`:

ismt_handle_isr
===============

.. c:function:: irqreturn_t ismt_handle_isr(struct ismt_priv *priv)

    interrupt handler bottom half

    :param struct ismt_priv \*priv:
        iSMT private data

.. _`ismt_do_interrupt`:

ismt_do_interrupt
=================

.. c:function:: irqreturn_t ismt_do_interrupt(int vec, void *data)

    IRQ interrupt handler

    :param int vec:
        interrupt vector

    :param void \*data:
        iSMT private data

.. _`ismt_do_msi_interrupt`:

ismt_do_msi_interrupt
=====================

.. c:function:: irqreturn_t ismt_do_msi_interrupt(int vec, void *data)

    MSI interrupt handler

    :param int vec:
        interrupt vector

    :param void \*data:
        iSMT private data

.. _`ismt_hw_init`:

ismt_hw_init
============

.. c:function:: void ismt_hw_init(struct ismt_priv *priv)

    initialize the iSMT hardware

    :param struct ismt_priv \*priv:
        iSMT private data

.. _`ismt_dev_init`:

ismt_dev_init
=============

.. c:function:: int ismt_dev_init(struct ismt_priv *priv)

    initialize the iSMT data structures

    :param struct ismt_priv \*priv:
        iSMT private data

.. _`ismt_int_init`:

ismt_int_init
=============

.. c:function:: int ismt_int_init(struct ismt_priv *priv)

    initialize interrupts

    :param struct ismt_priv \*priv:
        iSMT private data

.. _`ismt_probe`:

ismt_probe
==========

.. c:function:: int ismt_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    probe for iSMT devices

    :param struct pci_dev \*pdev:
        PCI-Express device

    :param const struct pci_device_id \*id:
        PCI-Express device ID

.. _`ismt_remove`:

ismt_remove
===========

.. c:function:: void ismt_remove(struct pci_dev *pdev)

    release driver resources

    :param struct pci_dev \*pdev:
        PCI-Express device

.. This file was automatic generated / don't edit.

