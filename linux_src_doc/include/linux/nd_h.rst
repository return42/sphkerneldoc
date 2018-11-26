.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/nd.h

.. _`nd_namespace_common`:

struct nd_namespace_common
==========================

.. c:type:: struct nd_namespace_common

    core infrastructure of a namespace

.. _`nd_namespace_common.definition`:

Definition
----------

.. code-block:: c

    struct nd_namespace_common {
        int force_raw;
        struct device dev;
        struct device *claim;
        enum nvdimm_claim_class claim_class;
        int (*rw_bytes)(struct nd_namespace_common *, resource_size_t offset, void *buf, size_t size, int rw, unsigned long flags);
    }

.. _`nd_namespace_common.members`:

Members
-------

force_raw
    ignore other personalities for the namespace (e.g. btt)

dev
    device model node

claim
    when set a another personality has taken ownership of the namespace

claim_class
    restrict claim type to a given class

rw_bytes
    access the raw namespace capacity with byte-aligned transfers

.. _`nd_namespace_io`:

struct nd_namespace_io
======================

.. c:type:: struct nd_namespace_io

    device representation of a persistent memory range

.. _`nd_namespace_io.definition`:

Definition
----------

.. code-block:: c

    struct nd_namespace_io {
        struct nd_namespace_common common;
        struct resource res;
        resource_size_t size;
        void *addr;
        struct badblocks bb;
    }

.. _`nd_namespace_io.members`:

Members
-------

common
    *undescribed*

res
    struct resource conversion of a NFIT SPA table

size
    cached resource_size(@res) for fast path size checks

addr
    virtual address to access the namespace range

bb
    badblocks list for the namespace range

.. _`nd_namespace_pmem`:

struct nd_namespace_pmem
========================

.. c:type:: struct nd_namespace_pmem

    namespace device for dimm-backed interleaved memory

.. _`nd_namespace_pmem.definition`:

Definition
----------

.. code-block:: c

    struct nd_namespace_pmem {
        struct nd_namespace_io nsio;
        unsigned long lbasize;
        char *alt_name;
        u8 *uuid;
        int id;
    }

.. _`nd_namespace_pmem.members`:

Members
-------

nsio
    device and system physical address range to drive

lbasize
    logical sector size for the namespace in block-device-mode

alt_name
    namespace name supplied in the dimm label

uuid
    namespace name supplied in the dimm label

id
    ida allocated id

.. _`nd_namespace_blk`:

struct nd_namespace_blk
=======================

.. c:type:: struct nd_namespace_blk

    namespace for dimm-bounded persistent memory

.. _`nd_namespace_blk.definition`:

Definition
----------

.. code-block:: c

    struct nd_namespace_blk {
        struct nd_namespace_common common;
        char *alt_name;
        u8 *uuid;
        int id;
        unsigned long lbasize;
        resource_size_t size;
        int num_resources;
        struct resource **res;
    }

.. _`nd_namespace_blk.members`:

Members
-------

common
    *undescribed*

alt_name
    namespace name supplied in the dimm label

uuid
    namespace name supplied in the dimm label

id
    ida allocated id

lbasize
    blk namespaces have a native sector size when btt not present

size
    sum of all the resource ranges allocated to this namespace

num_resources
    number of dpa extents to claim

res
    discontiguous dpa extents for given dimm

.. _`nvdimm_read_bytes`:

nvdimm_read_bytes
=================

.. c:function:: int nvdimm_read_bytes(struct nd_namespace_common *ndns, resource_size_t offset, void *buf, size_t size, unsigned long flags)

    synchronously read bytes from an nvdimm namespace

    :param ndns:
        device to read
    :type ndns: struct nd_namespace_common \*

    :param offset:
        namespace-relative starting offset
    :type offset: resource_size_t

    :param buf:
        buffer to fill
    :type buf: void \*

    :param size:
        transfer length
    :type size: size_t

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`nvdimm_read_bytes.description`:

Description
-----------

\ ``buf``\  is up-to-date upon return from this routine.

.. _`nvdimm_write_bytes`:

nvdimm_write_bytes
==================

.. c:function:: int nvdimm_write_bytes(struct nd_namespace_common *ndns, resource_size_t offset, void *buf, size_t size, unsigned long flags)

    synchronously write bytes to an nvdimm namespace

    :param ndns:
        device to read
    :type ndns: struct nd_namespace_common \*

    :param offset:
        namespace-relative starting offset
    :type offset: resource_size_t

    :param buf:
        buffer to drain
    :type buf: void \*

    :param size:
        transfer length
    :type size: size_t

    :param flags:
        *undescribed*
    :type flags: unsigned long

.. _`nvdimm_write_bytes.description`:

Description
-----------

NVDIMM Namepaces disks do not implement sectors internally.  Depending on
the \ ``ndns``\ , the contents of \ ``buf``\  may be in cpu cache, platform buffers,
or on backing memory media upon return from this routine.  Flushing
to media is handled internal to the \ ``ndns``\  driver, if at all.

.. This file was automatic generated / don't edit.

