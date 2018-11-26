.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/sysdev/fsl_rio.c

.. _`fsl_local_config_read`:

fsl_local_config_read
=====================

.. c:function:: int fsl_local_config_read(struct rio_mport *mport, int index, u32 offset, int len, u32 *data)

    Generate a MPC85xx local config space read

    :param mport:
        RapidIO master port info
    :type mport: struct rio_mport \*

    :param index:
        ID of RapdiIO interface
    :type index: int

    :param offset:
        Offset into configuration space
    :type offset: u32

    :param len:
        Length (in bytes) of the maintenance transaction
    :type len: int

    :param data:
        Value to be read into
    :type data: u32 \*

.. _`fsl_local_config_read.description`:

Description
-----------

Generates a MPC85xx local configuration space read. Returns \ ``0``\  on
success or \ ``-EINVAL``\  on failure.

.. _`fsl_local_config_write`:

fsl_local_config_write
======================

.. c:function:: int fsl_local_config_write(struct rio_mport *mport, int index, u32 offset, int len, u32 data)

    Generate a MPC85xx local config space write

    :param mport:
        RapidIO master port info
    :type mport: struct rio_mport \*

    :param index:
        ID of RapdiIO interface
    :type index: int

    :param offset:
        Offset into configuration space
    :type offset: u32

    :param len:
        Length (in bytes) of the maintenance transaction
    :type len: int

    :param data:
        Value to be written
    :type data: u32

.. _`fsl_local_config_write.description`:

Description
-----------

Generates a MPC85xx local configuration space write. Returns \ ``0``\  on
success or \ ``-EINVAL``\  on failure.

.. _`fsl_rio_config_read`:

fsl_rio_config_read
===================

.. c:function:: int fsl_rio_config_read(struct rio_mport *mport, int index, u16 destid, u8 hopcount, u32 offset, int len, u32 *val)

    Generate a MPC85xx read maintenance transaction

    :param mport:
        RapidIO master port info
    :type mport: struct rio_mport \*

    :param index:
        ID of RapdiIO interface
    :type index: int

    :param destid:
        Destination ID of transaction
    :type destid: u16

    :param hopcount:
        Number of hops to target device
    :type hopcount: u8

    :param offset:
        Offset into configuration space
    :type offset: u32

    :param len:
        Length (in bytes) of the maintenance transaction
    :type len: int

    :param val:
        Location to be read into
    :type val: u32 \*

.. _`fsl_rio_config_read.description`:

Description
-----------

Generates a MPC85xx read maintenance transaction. Returns \ ``0``\  on
success or \ ``-EINVAL``\  on failure.

.. _`fsl_rio_config_write`:

fsl_rio_config_write
====================

.. c:function:: int fsl_rio_config_write(struct rio_mport *mport, int index, u16 destid, u8 hopcount, u32 offset, int len, u32 val)

    Generate a MPC85xx write maintenance transaction

    :param mport:
        RapidIO master port info
    :type mport: struct rio_mport \*

    :param index:
        ID of RapdiIO interface
    :type index: int

    :param destid:
        Destination ID of transaction
    :type destid: u16

    :param hopcount:
        Number of hops to target device
    :type hopcount: u8

    :param offset:
        Offset into configuration space
    :type offset: u32

    :param len:
        Length (in bytes) of the maintenance transaction
    :type len: int

    :param val:
        Value to be written
    :type val: u32

.. _`fsl_rio_config_write.description`:

Description
-----------

Generates an MPC85xx write maintenance transaction. Returns \ ``0``\  on
success or \ ``-EINVAL``\  on failure.

.. _`fsl_rio_setup`:

fsl_rio_setup
=============

.. c:function:: int fsl_rio_setup(struct platform_device *dev)

    Setup Freescale PowerPC RapidIO interface

    :param dev:
        platform_device pointer
    :type dev: struct platform_device \*

.. _`fsl_rio_setup.description`:

Description
-----------

Initializes MPC85xx RapidIO hardware interface, configures
master port with system-specific info, and registers the
master port with the RapidIO subsystem.

.. This file was automatic generated / don't edit.

