.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ux500/cryp/cryp.c

.. _`cryp_wait_until_done`:

cryp_wait_until_done
====================

.. c:function:: void cryp_wait_until_done(struct cryp_device_data *device_data)

    Ericsson SA 2010

    :param struct cryp_device_data \*device_data:
        *undescribed*

.. _`cryp_wait_until_done.author`:

Author
------

Shujuan Chen <shujuan.chen@stericsson.com> for ST-Ericsson.

Jonas Linde <jonas.linde@stericsson.com> for ST-Ericsson.

Niklas Hernaeus <niklas.hernaeus@stericsson.com> for ST-Ericsson.

Joakim Bech <joakim.xx.bech@stericsson.com> for ST-Ericsson.

Berne Hebark <berne.herbark@stericsson.com> for ST-Ericsson.

.. _`cryp_wait_until_done.license-terms`:

License terms
-------------

GNU General Public License (GPL) version 2

.. _`cryp_check`:

cryp_check
==========

.. c:function:: int cryp_check(struct cryp_device_data *device_data)

    This routine checks Peripheral and PCell Id

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

.. _`cryp_activity`:

cryp_activity
=============

.. c:function:: void cryp_activity(struct cryp_device_data *device_data, enum cryp_crypen cryp_crypen)

    This routine enables/disable the cryptography function.

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

    :param enum cryp_crypen cryp_crypen:
        Enable/Disable functionality

.. _`cryp_flush_inoutfifo`:

cryp_flush_inoutfifo
====================

.. c:function:: void cryp_flush_inoutfifo(struct cryp_device_data *device_data)

    Resets both the input and the output FIFOs

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

.. _`cryp_set_configuration`:

cryp_set_configuration
======================

.. c:function:: int cryp_set_configuration(struct cryp_device_data *device_data, struct cryp_config *cryp_config, u32 *control_register)

    This routine set the cr CRYP IP

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

    :param struct cryp_config \*cryp_config:
        Pointer to the configuration parameter

    :param u32 \*control_register:
        The control register to be written later on.

.. _`cryp_configure_protection`:

cryp_configure_protection
=========================

.. c:function:: int cryp_configure_protection(struct cryp_device_data *device_data, struct cryp_protection_config *p_protect_config)

    set the protection bits in the CRYP logic.

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

    :param struct cryp_protection_config \*p_protect_config:
        Pointer to the protection mode and
        secure mode configuration

.. _`cryp_is_logic_busy`:

cryp_is_logic_busy
==================

.. c:function:: int cryp_is_logic_busy(struct cryp_device_data *device_data)

    returns the busy status of the CRYP logic

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

.. _`cryp_configure_for_dma`:

cryp_configure_for_dma
======================

.. c:function:: void cryp_configure_for_dma(struct cryp_device_data *device_data, enum cryp_dma_req_type dma_req)

    configures the CRYP IP for DMA operation

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

    :param enum cryp_dma_req_type dma_req:
        Specifies the DMA request type value.

.. _`cryp_configure_key_values`:

cryp_configure_key_values
=========================

.. c:function:: int cryp_configure_key_values(struct cryp_device_data *device_data, enum cryp_key_reg_index key_reg_index, struct cryp_key_value key_value)

    configures the key values for CRYP operations

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

    :param enum cryp_key_reg_index key_reg_index:
        Key value index register

    :param struct cryp_key_value key_value:
        The key value struct

.. _`cryp_configure_init_vector`:

cryp_configure_init_vector
==========================

.. c:function:: int cryp_configure_init_vector(struct cryp_device_data *device_data, enum cryp_init_vector_index init_vector_index, struct cryp_init_vector_value init_vector_value)

    configures the initialization vector register

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

    :param enum cryp_init_vector_index init_vector_index:
        Specifies the index of the init vector.

    :param struct cryp_init_vector_value init_vector_value:
        Specifies the value for the init vector.

.. _`cryp_save_device_context`:

cryp_save_device_context
========================

.. c:function:: void cryp_save_device_context(struct cryp_device_data *device_data, struct cryp_device_context *ctx, int cryp_mode)

    Store hardware registers and other device context parameter

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

    :param struct cryp_device_context \*ctx:
        Crypto device context

    :param int cryp_mode:
        *undescribed*

.. _`cryp_restore_device_context`:

cryp_restore_device_context
===========================

.. c:function:: void cryp_restore_device_context(struct cryp_device_data *device_data, struct cryp_device_context *ctx)

    Restore hardware registers and other device context parameter

    :param struct cryp_device_data \*device_data:
        Pointer to the device data struct for base address.

    :param struct cryp_device_context \*ctx:
        Crypto device context

.. This file was automatic generated / don't edit.

