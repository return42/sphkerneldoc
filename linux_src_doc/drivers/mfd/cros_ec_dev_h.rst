.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/cros_ec_dev.h

.. _`cros_ec_readmem`:

struct cros_ec_readmem
======================

.. c:type:: struct cros_ec_readmem

    Struct used to read mapped memory.

.. _`cros_ec_readmem.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_readmem {
        uint32_t offset;
        uint32_t bytes;
        uint8_t buffer[EC_MEMMAP_SIZE];
    }

.. _`cros_ec_readmem.members`:

Members
-------

offset
    Within EC_LPC_ADDR_MEMMAP region.

bytes
    Number of bytes to read. Zero means "read a string" (including '\0')
    At most only EC_MEMMAP_SIZE bytes can be read.

buffer
    Where to store the result. The ioctl returns the number of bytes
    read or negative on error.

.. This file was automatic generated / don't edit.

