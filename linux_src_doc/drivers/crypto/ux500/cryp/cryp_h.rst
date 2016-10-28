.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ux500/cryp/cryp.h

.. _`cryp_config`:

struct cryp_config
==================

.. c:type:: struct cryp_config


.. _`cryp_config.definition`:

Definition
----------

.. code-block:: c

    struct cryp_config {
        int keysize;
        enum cryp_algo_mode algomode;
        enum cryp_algorithm_dir algodir;
    }

.. _`cryp_config.members`:

Members
-------

keysize
    Key size for AES

algomode
    AES modes

algodir
    Cryp Encryption or Decryption

.. _`cryp_config.description`:

Description
-----------

CRYP configuration structure to be passed to set configuration

.. _`cryp_protection_config`:

struct cryp_protection_config
=============================

.. c:type:: struct cryp_protection_config


.. _`cryp_protection_config.definition`:

Definition
----------

.. code-block:: c

    struct cryp_protection_config {
        enum cryp_state privilege_access;
        enum cryp_state secure_access;
    }

.. _`cryp_protection_config.members`:

Members
-------

privilege_access
    Privileged cryp state enable/disable

secure_access
    Secure cryp state enable/disable

.. _`cryp_protection_config.description`:

Description
-----------

Protection configuration structure for setting privilage access

.. _`cryp_device_context`:

struct cryp_device_context
==========================

.. c:type:: struct cryp_device_context

    structure for a cryp context.

.. _`cryp_device_context.definition`:

Definition
----------

.. code-block:: c

    struct cryp_device_context {
        u32 cr;
        u32 dmacr;
        u32 imsc;
        u32 key_1_l;
        u32 key_1_r;
        u32 key_2_l;
        u32 key_2_r;
        u32 key_3_l;
        u32 key_3_r;
        u32 key_4_l;
        u32 key_4_r;
        u32 init_vect_0_l;
        u32 init_vect_0_r;
        u32 init_vect_1_l;
        u32 init_vect_1_r;
        u32 din;
        u32 dout;
    }

.. _`cryp_device_context.members`:

Members
-------

cr
    control register

dmacr
    DMA control register

imsc
    Interrupt mask set/clear register

key_1_l
    Key 1l register

key_1_r
    Key 1r register

key_2_l
    Key 2l register

key_2_r
    Key 2r register

key_3_l
    Key 3l register

key_3_r
    Key 3r register

key_4_l
    Key 4l register

key_4_r
    Key 4r register

init_vect_0_l
    Initialization vector 0l register

init_vect_0_r
    Initialization vector 0r register

init_vect_1_l
    Initialization vector 1l register

init_vect_1_r
    Initialization vector 0r register

din
    Data in register

dout
    Data out register

.. _`cryp_device_context.description`:

Description
-----------

CRYP power management specifc structure.

.. _`cryp_device_data`:

struct cryp_device_data
=======================

.. c:type:: struct cryp_device_data

    structure for a cryp device.

.. _`cryp_device_data.definition`:

Definition
----------

.. code-block:: c

    struct cryp_device_data {
        struct cryp_register __iomem *base;
        phys_addr_t phybase;
        struct device *dev;
        struct clk *clk;
        struct regulator *pwr_regulator;
        int power_status;
        struct spinlock ctx_lock;
        struct cryp_ctx *current_ctx;
        struct klist_node list_node;
        struct cryp_dma dma;
        bool power_state;
        struct spinlock power_state_spinlock;
        bool restore_dev_ctx;
    }

.. _`cryp_device_data.members`:

Members
-------

base
    Pointer to virtual base address of the cryp device.

phybase
    Pointer to physical memory location of the cryp device.

dev
    Pointer to the devices dev structure.

clk
    Pointer to the device's clock control.

pwr_regulator
    Pointer to the device's power control.

power_status
    Current status of the power.

ctx_lock
    Lock for current_ctx.

current_ctx
    Pointer to the currently allocated context.

list_node
    For inclusion into a klist.

dma
    The dma structure holding channel configuration.

power_state
    TRUE = power state on, FALSE = power state off.

power_state_spinlock
    Spinlock for power_state.

restore_dev_ctx
    TRUE = saved ctx, FALSE = no saved ctx.

.. _`cryp_write_indata`:

cryp_write_indata
=================

.. c:function:: int cryp_write_indata(struct cryp_device_data *device_data, u32 write_data)

    This routine writes 32 bit data into the data input register of the cryptography IP.

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

    :param u32 write_data:
        Data to write.

.. _`cryp_read_outdata`:

cryp_read_outdata
=================

.. c:function:: int cryp_read_outdata(struct cryp_device_data *device_data, u32 *read_data)

    This routine reads the data from the data output register of the CRYP logic

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

    :param u32 \*read_data:
        Read the data from the output FIFO.

.. This file was automatic generated / don't edit.

