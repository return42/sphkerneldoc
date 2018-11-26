.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ux500/cryp/cryp.c

.. _`cryp_wait_until_done`:

cryp_wait_until_done
====================

.. c:function:: void cryp_wait_until_done(struct cryp_device_data *device_data)

    Ericsson SA 2010

    :param device_data:
        *undescribed*
    :type device_data: struct cryp_device_data \*

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

    :param device_data:
        Pointer to the device data struct for base address.
    :type device_data: struct cryp_device_data \*

.. _`cryp_activity`:

cryp_activity
=============

.. c:function:: void cryp_activity(struct cryp_device_data *device_data, enum cryp_crypen cryp_crypen)

    This routine enables/disable the cryptography function.

    :param device_data:
        Pointer to the device data struct for base address.
    :type device_data: struct cryp_device_data \*

    :param cryp_crypen:
        Enable/Disable functionality
    :type cryp_crypen: enum cryp_crypen

.. _`cryp_flush_inoutfifo`:

cryp_flush_inoutfifo
====================

.. c:function:: void cryp_flush_inoutfifo(struct cryp_device_data *device_data)

    Resets both the input and the output FIFOs

    :param device_data:
        Pointer to the device data struct for base address.
    :type device_data: struct cryp_device_data \*

.. _`cryp_set_configuration`:

cryp_set_configuration
======================

.. c:function:: int cryp_set_configuration(struct cryp_device_data *device_data, struct cryp_config *cryp_config, u32 *control_register)

    This routine set the cr CRYP IP

    :param device_data:
        Pointer to the device data struct for base address.
    :type device_data: struct cryp_device_data \*

    :param cryp_config:
        Pointer to the configuration parameter
    :type cryp_config: struct cryp_config \*

    :param control_register:
        The control register to be written later on.
    :type control_register: u32 \*

.. _`cryp_configure_protection`:

cryp_configure_protection
=========================

.. c:function:: int cryp_configure_protection(struct cryp_device_data *device_data, struct cryp_protection_config *p_protect_config)

    set the protection bits in the CRYP logic.

    :param device_data:
        Pointer to the device data struct for base address.
    :type device_data: struct cryp_device_data \*

    :param p_protect_config:
        Pointer to the protection mode and
        secure mode configuration
    :type p_protect_config: struct cryp_protection_config \*

.. _`cryp_is_logic_busy`:

cryp_is_logic_busy
==================

.. c:function:: int cryp_is_logic_busy(struct cryp_device_data *device_data)

    returns the busy status of the CRYP logic

    :param device_data:
        Pointer to the device data struct for base address.
    :type device_data: struct cryp_device_data \*

.. _`cryp_configure_for_dma`:

cryp_configure_for_dma
======================

.. c:function:: void cryp_configure_for_dma(struct cryp_device_data *device_data, enum cryp_dma_req_type dma_req)

    configures the CRYP IP for DMA operation

    :param device_data:
        Pointer to the device data struct for base address.
    :type device_data: struct cryp_device_data \*

    :param dma_req:
        Specifies the DMA request type value.
    :type dma_req: enum cryp_dma_req_type

.. _`cryp_configure_key_values`:

cryp_configure_key_values
=========================

.. c:function:: int cryp_configure_key_values(struct cryp_device_data *device_data, enum cryp_key_reg_index key_reg_index, struct cryp_key_value key_value)

    configures the key values for CRYP operations

    :param device_data:
        Pointer to the device data struct for base address.
    :type device_data: struct cryp_device_data \*

    :param key_reg_index:
        Key value index register
    :type key_reg_index: enum cryp_key_reg_index

    :param key_value:
        The key value struct
    :type key_value: struct cryp_key_value

.. _`cryp_configure_init_vector`:

cryp_configure_init_vector
==========================

.. c:function:: int cryp_configure_init_vector(struct cryp_device_data *device_data, enum cryp_init_vector_index init_vector_index, struct cryp_init_vector_value init_vector_value)

    configures the initialization vector register

    :param device_data:
        Pointer to the device data struct for base address.
    :type device_data: struct cryp_device_data \*

    :param init_vector_index:
        Specifies the index of the init vector.
    :type init_vector_index: enum cryp_init_vector_index

    :param init_vector_value:
        Specifies the value for the init vector.
    :type init_vector_value: struct cryp_init_vector_value

.. _`cryp_save_device_context`:

cryp_save_device_context
========================

.. c:function:: void cryp_save_device_context(struct cryp_device_data *device_data, struct cryp_device_context *ctx, int cryp_mode)

    Store hardware registers and other device context parameter

    :param device_data:
        Pointer to the device data struct for base address.
    :type device_data: struct cryp_device_data \*

    :param ctx:
        Crypto device context
    :type ctx: struct cryp_device_context \*

    :param cryp_mode:
        *undescribed*
    :type cryp_mode: int

.. _`cryp_restore_device_context`:

cryp_restore_device_context
===========================

.. c:function:: void cryp_restore_device_context(struct cryp_device_data *device_data, struct cryp_device_context *ctx)

    Restore hardware registers and other device context parameter

    :param device_data:
        Pointer to the device data struct for base address.
    :type device_data: struct cryp_device_data \*

    :param ctx:
        Crypto device context
    :type ctx: struct cryp_device_context \*

.. This file was automatic generated / don't edit.

