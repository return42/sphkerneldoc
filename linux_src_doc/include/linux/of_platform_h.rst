.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/of_platform.h

.. _`of_dev_auxdata`:

struct of_dev_auxdata
=====================

.. c:type:: struct of_dev_auxdata

    lookup table entry for device names & platform_data

.. _`of_dev_auxdata.definition`:

Definition
----------

.. code-block:: c

    struct of_dev_auxdata {
        char *compatible;
        resource_size_t phys_addr;
        char *name;
        void *platform_data;
    }

.. _`of_dev_auxdata.members`:

Members
-------

compatible
    compatible value of node to match against node

phys_addr
    Start address of registers to match against node

name
    Name to assign for matching nodes

platform_data
    platform_data to assign for matching nodes

.. _`of_dev_auxdata.description`:

Description
-----------

This lookup table allows the caller of \ :c:func:`of_platform_populate`\  to override
the names of devices when creating devices from the device tree.  The table
should be terminated with an empty entry.  It also allows the platform_data
pointer to be set.

The reason for this functionality is that some Linux infrastructure uses
the device name to look up a specific device, but the Linux-specific names
are not encoded into the device tree, so the kernel needs to provide specific
values.

.. _`of_dev_auxdata.note`:

Note
----

Using an auxdata lookup table should be considered a last resort when
converting a platform to use the DT.  Normally the automatically generated
device name will not matter, and drivers should obtain data from the device
node instead of from an anonymous platform_data pointer.

.. This file was automatic generated / don't edit.

