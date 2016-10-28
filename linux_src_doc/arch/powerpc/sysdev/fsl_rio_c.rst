.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/sysdev/fsl_rio.c

.. _`fsl_local_config_read`:

fsl_local_config_read
=====================

.. c:function:: int fsl_local_config_read(struct rio_mport *mport, int index, u32 offset, int len, u32 *data)

    Generate a MPC85xx local config space read

    :param struct rio_mport \*mport:
        RapidIO master port info

    :param int index:
        ID of RapdiIO interface

    :param u32 offset:
        Offset into configuration space

    :param int len:
        Length (in bytes) of the maintenance transaction

    :param u32 \*data:
        Value to be read into

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

    :param struct rio_mport \*mport:
        RapidIO master port info

    :param int index:
        ID of RapdiIO interface

    :param u32 offset:
        Offset into configuration space

    :param int len:
        Length (in bytes) of the maintenance transaction

    :param u32 data:
        Value to be written

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

    :param struct rio_mport \*mport:
        RapidIO master port info

    :param int index:
        ID of RapdiIO interface

    :param u16 destid:
        Destination ID of transaction

    :param u8 hopcount:
        Number of hops to target device

    :param u32 offset:
        Offset into configuration space

    :param int len:
        Length (in bytes) of the maintenance transaction

    :param u32 \*val:
        Location to be read into

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

    :param struct rio_mport \*mport:
        RapidIO master port info

    :param int index:
        ID of RapdiIO interface

    :param u16 destid:
        Destination ID of transaction

    :param u8 hopcount:
        Number of hops to target device

    :param u32 offset:
        Offset into configuration space

    :param int len:
        Length (in bytes) of the maintenance transaction

    :param u32 val:
        Value to be written

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

    :param struct platform_device \*dev:
        platform_device pointer

.. _`fsl_rio_setup.description`:

Description
-----------

Initializes MPC85xx RapidIO hardware interface, configures
master port with system-specific info, and registers the
master port with the RapidIO subsystem.

.. This file was automatic generated / don't edit.

