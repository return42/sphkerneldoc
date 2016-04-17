.. -*- coding: utf-8; mode: rst -*-

===========
hash_core.c
===========


.. _`hash_driver_data`:

struct hash_driver_data
=======================

.. c:type:: hash_driver_data

    data specific to the driver.


.. _`hash_driver_data.definition`:

Definition
----------

.. code-block:: c

  struct hash_driver_data {
    struct klist device_list;
    struct semaphore device_allocation;
  };


.. _`hash_driver_data.members`:

Members
-------

:``device_list``:
    A list of registered devices to choose from.

:``device_allocation``:
    A semaphore initialized with number of devices.




.. _`hash_messagepad`:

hash_messagepad
===============

.. c:function:: void hash_messagepad (struct hash_device_data *device_data, const u32 *message, u8 index_bytes)

    Pads a message and write the nblw bits.

    :param struct hash_device_data \*device_data:
        Structure for the hash device.

    :param const u32 \*message:
        Last word of a message

    :param u8 index_bytes:
        The number of bytes in the last message



.. _`hash_messagepad.description`:

Description
-----------

This function manages the final part of the digest calculation, when less
than 512 bits (64 bytes) remain in message. This means index_bytes < 64.



.. _`release_hash_device`:

release_hash_device
===================

.. c:function:: void release_hash_device (struct hash_device_data *device_data)

    Releases a previously allocated hash device.

    :param struct hash_device_data \*device_data:
        Structure for the hash device.



.. _`get_empty_message_digest`:

get_empty_message_digest
========================

.. c:function:: int get_empty_message_digest (struct hash_device_data *device_data, u8 *zero_hash, u32 *zero_hash_size, bool *zero_digest)

    Returns a pre-calculated digest for the empty message.

    :param struct hash_device_data \*device_data:
        Structure for the hash device.

    :param u8 \*zero_hash:
        Buffer to return the empty message digest.

    :param u32 \*zero_hash_size:
        Hash size of the empty message digest.

    :param bool \*zero_digest:
        True if zero_digest returned.



.. _`hash_disable_power`:

hash_disable_power
==================

.. c:function:: int hash_disable_power (struct hash_device_data *device_data, bool save_device_state)

    Request to disable power and clock.

    :param struct hash_device_data \*device_data:
        Structure for the hash device.

    :param bool save_device_state:
        If true, saves the current hw state.



.. _`hash_disable_power.description`:

Description
-----------

This function request for disabling power (regulator) and clock,
and could also save current hw state.



.. _`hash_enable_power`:

hash_enable_power
=================

.. c:function:: int hash_enable_power (struct hash_device_data *device_data, bool restore_device_state)

    Request to enable power and clock.

    :param struct hash_device_data \*device_data:
        Structure for the hash device.

    :param bool restore_device_state:
        If true, restores a previous saved hw state.



.. _`hash_enable_power.description`:

Description
-----------

This function request for enabling power (regulator) and clock,
and could also restore a previously saved hw state.



.. _`hash_get_device_data`:

hash_get_device_data
====================

.. c:function:: int hash_get_device_data (struct hash_ctx *ctx, struct hash_device_data **device_data)

    Checks for an available hash device and return it.

    :param struct hash_ctx \*ctx:

        *undescribed*

    :param struct hash_device_data \*\*device_data:
        Structure for the hash device.



.. _`hash_get_device_data.description`:

Description
-----------

This function check for an available hash device and return it to
the caller.
Note! Caller need to release the device, calling :c:func:`up`.



.. _`hash_hw_write_key`:

hash_hw_write_key
=================

.. c:function:: void hash_hw_write_key (struct hash_device_data *device_data, const u8 *key, unsigned int keylen)

    Writes the key to the hardware registries.

    :param struct hash_device_data \*device_data:
        Structure for the hash device.

    :param const u8 \*key:
        Key to be written.

    :param unsigned int keylen:
        The lengt of the key.



.. _`hash_hw_write_key.description`:

Description
-----------

Note! This function DOES NOT write to the NBLW registry, even though
specified in the the hw design spec. Either due to incorrect info in the
spec or due to a bug in the hw.



.. _`init_hash_hw`:

init_hash_hw
============

.. c:function:: int init_hash_hw (struct hash_device_data *device_data, struct hash_ctx *ctx)

    Initialise the hash hardware for a new calculation.

    :param struct hash_device_data \*device_data:
        Structure for the hash device.

    :param struct hash_ctx \*ctx:
        The hash context.



.. _`init_hash_hw.description`:

Description
-----------

This function will enable the bits needed to clear and start a new
calculation.



.. _`hash_get_nents`:

hash_get_nents
==============

.. c:function:: int hash_get_nents (struct scatterlist *sg, int size, bool *aligned)

    Return number of entries (nents) in scatterlist (sg).

    :param struct scatterlist \*sg:
        Scatterlist.

    :param int size:
        Size in bytes.

    :param bool \*aligned:
        True if sg data aligned to work in DMA mode.



.. _`hash_dma_valid_data`:

hash_dma_valid_data
===================

.. c:function:: bool hash_dma_valid_data (struct scatterlist *sg, int datasize)

    checks for dma valid sg data.

    :param struct scatterlist \*sg:
        Scatterlist.

    :param int datasize:
        Datasize in bytes.



.. _`hash_dma_valid_data.description`:

Description
-----------

NOTE! This function checks for dma valid sg data, since dma
only accept datasizes of even wordsize.



.. _`hash_init`:

hash_init
=========

.. c:function:: int hash_init (struct ahash_request *req)

    Common hash init function for SHA1/SHA2 (SHA256).

    :param struct ahash_request \*req:
        The hash request for the job.



.. _`hash_init.description`:

Description
-----------

Initialize structures.



.. _`hash_processblock`:

hash_processblock
=================

.. c:function:: void hash_processblock (struct hash_device_data *device_data, const u32 *message, int length)

    This function processes a single block of 512 bits (64 bytes), word aligned, starting at message.

    :param struct hash_device_data \*device_data:
        Structure for the hash device.

    :param const u32 \*message:
        Block (512 bits) of message to be written to
        the HASH hardware.

    :param int length:

        *undescribed*



.. _`hash_messagepad`:

hash_messagepad
===============

.. c:function:: void hash_messagepad (struct hash_device_data *device_data, const u32 *message, u8 index_bytes)

    Pads a message and write the nblw bits.

    :param struct hash_device_data \*device_data:
        Structure for the hash device.

    :param const u32 \*message:
        Last word of a message.

    :param u8 index_bytes:
        The number of bytes in the last message.



.. _`hash_messagepad.description`:

Description
-----------

This function manages the final part of the digest calculation, when less
than 512 bits (64 bytes) remain in message. This means index_bytes < 64.



.. _`hash_incrementlength`:

hash_incrementlength
====================

.. c:function:: void hash_incrementlength (struct hash_req_ctx *ctx, u32 incr)

    Increments the length of the current message.

    :param struct hash_req_ctx \*ctx:
        Hash context

    :param u32 incr:
        Length of message processed already



.. _`hash_incrementlength.description`:

Description
-----------

Overflow cannot occur, because conditions for overflow are checked in
hash_hw_update.



.. _`hash_setconfiguration`:

hash_setconfiguration
=====================

.. c:function:: int hash_setconfiguration (struct hash_device_data *device_data, struct hash_config *config)

    Sets the required configuration for the hash hardware.

    :param struct hash_device_data \*device_data:
        Structure for the hash device.

    :param struct hash_config \*config:
        Pointer to a configuration structure.



.. _`hash_begin`:

hash_begin
==========

.. c:function:: void hash_begin (struct hash_device_data *device_data, struct hash_ctx *ctx)

    This routine resets some globals and initializes the hash hardware.

    :param struct hash_device_data \*device_data:
        Structure for the hash device.

    :param struct hash_ctx \*ctx:
        Hash context.



.. _`hash_dma_final`:

hash_dma_final
==============

.. c:function:: int hash_dma_final (struct ahash_request *req)

    The hash dma final function for SHA1/SHA256.

    :param struct ahash_request \*req:
        The hash request for the job.



.. _`hash_hw_final`:

hash_hw_final
=============

.. c:function:: int hash_hw_final (struct ahash_request *req)

    The final hash calculation function

    :param struct ahash_request \*req:
        The hash request for the job.



.. _`hash_hw_update`:

hash_hw_update
==============

.. c:function:: int hash_hw_update (struct ahash_request *req)

    Updates current HASH computation hashing another part of the message.

    :param struct ahash_request \*req:
        Byte array containing the message to be hashed (caller
        allocated).



.. _`hash_resume_state`:

hash_resume_state
=================

.. c:function:: int hash_resume_state (struct hash_device_data *device_data, const struct hash_state *device_state)

    Function that resumes the state of an calculation.

    :param struct hash_device_data \*device_data:
        Pointer to the device structure.

    :param const struct hash_state \*device_state:
        The state to be restored in the hash hardware



.. _`hash_save_state`:

hash_save_state
===============

.. c:function:: int hash_save_state (struct hash_device_data *device_data, struct hash_state *device_state)

    Function that saves the state of hardware.

    :param struct hash_device_data \*device_data:
        Pointer to the device structure.

    :param struct hash_state \*device_state:
        The strucure where the hardware state should be saved.



.. _`hash_check_hw`:

hash_check_hw
=============

.. c:function:: int hash_check_hw (struct hash_device_data *device_data)

    This routine checks for peripheral Ids and PCell Ids.

    :param struct hash_device_data \*device_data:



.. _`hash_get_digest`:

hash_get_digest
===============

.. c:function:: void hash_get_digest (struct hash_device_data *device_data, u8 *digest, int algorithm)

    Gets the digest.

    :param struct hash_device_data \*device_data:
        Pointer to the device structure.

    :param u8 \*digest:
        User allocated byte array for the calculated digest.

    :param int algorithm:
        The algorithm in use.



.. _`ahash_update`:

ahash_update
============

.. c:function:: int ahash_update (struct ahash_request *req)

    The hash update function for SHA1/SHA2 (SHA256).

    :param struct ahash_request \*req:
        The hash request for the job.



.. _`ahash_final`:

ahash_final
===========

.. c:function:: int ahash_final (struct ahash_request *req)

    The hash final function for SHA1/SHA2 (SHA256).

    :param struct ahash_request \*req:
        The hash request for the job.



.. _`ahash_algs_register_all`:

ahash_algs_register_all
=======================

.. c:function:: int ahash_algs_register_all (struct hash_device_data *device_data)

    :param struct hash_device_data \*device_data:

        *undescribed*



.. _`ahash_algs_unregister_all`:

ahash_algs_unregister_all
=========================

.. c:function:: void ahash_algs_unregister_all (struct hash_device_data *device_data)

    :param struct hash_device_data \*device_data:

        *undescribed*



.. _`ux500_hash_probe`:

ux500_hash_probe
================

.. c:function:: int ux500_hash_probe (struct platform_device *pdev)

    Function that probes the hash hardware.

    :param struct platform_device \*pdev:
        The platform device.



.. _`ux500_hash_remove`:

ux500_hash_remove
=================

.. c:function:: int ux500_hash_remove (struct platform_device *pdev)

    Function that removes the hash device from the platform.

    :param struct platform_device \*pdev:
        The platform device.



.. _`ux500_hash_shutdown`:

ux500_hash_shutdown
===================

.. c:function:: void ux500_hash_shutdown (struct platform_device *pdev)

    Function that shutdown the hash device.

    :param struct platform_device \*pdev:
        The platform device



.. _`ux500_hash_suspend`:

ux500_hash_suspend
==================

.. c:function:: int ux500_hash_suspend (struct device *dev)

    Function that suspends the hash device.

    :param struct device \*dev:
        Device to suspend.



.. _`ux500_hash_resume`:

ux500_hash_resume
=================

.. c:function:: int ux500_hash_resume (struct device *dev)

    Function that resume the hash device.

    :param struct device \*dev:
        Device to resume.



.. _`ux500_hash_mod_init`:

ux500_hash_mod_init
===================

.. c:function:: int ux500_hash_mod_init ( void)

    The kernel module init function.

    :param void:
        no arguments



.. _`ux500_hash_mod_fini`:

ux500_hash_mod_fini
===================

.. c:function:: void __exit ux500_hash_mod_fini ( void)

    The kernel module exit function.

    :param void:
        no arguments

