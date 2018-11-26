.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/hw_random.h

.. _`hwrng`:

struct hwrng
============

.. c:type:: struct hwrng

    Hardware Random Number Generator driver

.. _`hwrng.definition`:

Definition
----------

.. code-block:: c

    struct hwrng {
        const char *name;
        int (*init)(struct hwrng *rng);
        void (*cleanup)(struct hwrng *rng);
        int (*data_present)(struct hwrng *rng, int wait);
        int (*data_read)(struct hwrng *rng, u32 *data);
        int (*read)(struct hwrng *rng, void *data, size_t max, bool wait);
        unsigned long priv;
        unsigned short quality;
        struct list_head list;
        struct kref ref;
        struct completion cleanup_done;
    }

.. _`hwrng.members`:

Members
-------

name
    Unique RNG name.

init
    Initialization callback (can be NULL).

cleanup
    Cleanup callback (can be NULL).

data_present
    Callback to determine if data is available
    on the RNG. If NULL, it is assumed that
    there is always data available.  \*OBSOLETE\*

data_read
    Read data from the RNG device.
    Returns the number of lower random bytes in "data".
    Must not be NULL.    \*OBSOLETE\*

read
    New API. drivers can fill up to max bytes of data
    into the buffer. The buffer is aligned for any type
    and max is a multiple of 4 and >= 32 bytes.

priv
    Private data, for use by the RNG driver.

quality
    Estimation of true entropy in RNG's bitstream
    (in bits of entropy per 1024 bits of input;
    valid values: 1 to 1024, or 0 for unknown).

list
    *undescribed*

ref
    *undescribed*

cleanup_done
    *undescribed*

.. This file was automatic generated / don't edit.

