.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_cppcore.c

.. _`nfp_cpp`:

struct nfp_cpp
==============

.. c:type:: struct nfp_cpp

    main nfpcore device structure Following fields are read-only after \ :c:func:`probe`\  exits or netdevs are spawned.

.. _`nfp_cpp.definition`:

Definition
----------

.. code-block:: c

    struct nfp_cpp {
        struct device dev;
        void *priv;
        u32 model;
        u16 interface;
        u8 serial[NFP_SERIAL_LEN];
        const struct nfp_cpp_operations *op;
        struct list_head resource_list;
        rwlock_t resource_lock;
        wait_queue_head_t waitq;
        u32 imb_cat_table[16];
        struct mutex area_cache_mutex;
        struct list_head area_cache_list;
    }

.. _`nfp_cpp.members`:

Members
-------

dev
    embedded device structure

priv
    private data of the low-level implementation

model
    chip model

interface
    chip interface id we are using to reach it

serial
    chip serial number

op
    low-level implementation ops

resource_list
    NFP CPP resource list

resource_lock
    protects \ ``resource_list``\ 

waitq
    area wait queue

imb_cat_table
    CPP Mapping Table

area_cache_mutex
    protects \ ``area_cache_list``\ 

area_cache_list
    cached areas for cpp/xpb read/write speed up

.. _`nfp_cpp_free`:

nfp_cpp_free
============

.. c:function:: void nfp_cpp_free(struct nfp_cpp *cpp)

    free the CPP handle

    :param struct nfp_cpp \*cpp:
        CPP handle

.. _`nfp_cpp_model`:

nfp_cpp_model
=============

.. c:function:: u32 nfp_cpp_model(struct nfp_cpp *cpp)

    Retrieve the Model ID of the NFP

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

.. _`nfp_cpp_model.return`:

Return
------

NFP CPP Model ID

.. _`nfp_cpp_interface`:

nfp_cpp_interface
=================

.. c:function:: u16 nfp_cpp_interface(struct nfp_cpp *cpp)

    Retrieve the Interface ID of the NFP

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

.. _`nfp_cpp_interface.return`:

Return
------

NFP CPP Interface ID

.. _`nfp_cpp_serial`:

nfp_cpp_serial
==============

.. c:function:: int nfp_cpp_serial(struct nfp_cpp *cpp, const u8 **serial)

    Retrieve the Serial ID of the NFP

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

    :param const u8 \*\*serial:
        Pointer to NFP serial number

.. _`nfp_cpp_serial.return`:

Return
------

Length of NFP serial number

.. _`nfp_cpp_area_alloc_with_name`:

nfp_cpp_area_alloc_with_name
============================

.. c:function:: struct nfp_cpp_area *nfp_cpp_area_alloc_with_name(struct nfp_cpp *cpp, u32 dest, const char *name, unsigned long long address, unsigned long size)

    allocate a new CPP area

    :param struct nfp_cpp \*cpp:
        CPP device handle

    :param u32 dest:
        NFP CPP ID

    :param const char \*name:
        Name of region

    :param unsigned long long address:
        Address of region

    :param unsigned long size:
        Size of region

.. _`nfp_cpp_area_alloc_with_name.description`:

Description
-----------

Allocate and initialize a CPP area structure.  The area must later
be locked down with an 'acquire' before it can be safely accessed.

.. _`nfp_cpp_area_alloc_with_name.note`:

NOTE
----

\ ``address``\  and \ ``size``\  must be 32-bit aligned values.

.. _`nfp_cpp_area_alloc_with_name.return`:

Return
------

NFP CPP area handle, or NULL

.. _`nfp_cpp_area_alloc`:

nfp_cpp_area_alloc
==================

.. c:function:: struct nfp_cpp_area *nfp_cpp_area_alloc(struct nfp_cpp *cpp, u32 dest, unsigned long long address, unsigned long size)

    allocate a new CPP area

    :param struct nfp_cpp \*cpp:
        CPP handle

    :param u32 dest:
        CPP id

    :param unsigned long long address:
        Start address on CPP target

    :param unsigned long size:
        Size of area in bytes

.. _`nfp_cpp_area_alloc.description`:

Description
-----------

Allocate and initialize a CPP area structure.  The area must later
be locked down with an 'acquire' before it can be safely accessed.

.. _`nfp_cpp_area_alloc.note`:

NOTE
----

\ ``address``\  and \ ``size``\  must be 32-bit aligned values.

.. _`nfp_cpp_area_alloc.return`:

Return
------

NFP CPP Area handle, or NULL

.. _`nfp_cpp_area_alloc_acquire`:

nfp_cpp_area_alloc_acquire
==========================

.. c:function:: struct nfp_cpp_area *nfp_cpp_area_alloc_acquire(struct nfp_cpp *cpp, const char *name, u32 dest, unsigned long long address, unsigned long size)

    allocate a new CPP area and lock it down

    :param struct nfp_cpp \*cpp:
        CPP handle

    :param const char \*name:
        Name of region

    :param u32 dest:
        CPP id

    :param unsigned long long address:
        Start address on CPP target

    :param unsigned long size:
        Size of area

.. _`nfp_cpp_area_alloc_acquire.description`:

Description
-----------

Allocate and initialize a CPP area structure, and lock it down so
that it can be accessed directly.

.. _`nfp_cpp_area_alloc_acquire.note`:

NOTE
----

\ ``address``\  and \ ``size``\  must be 32-bit aligned values.
The area must also be 'released' when the structure is freed.

.. _`nfp_cpp_area_alloc_acquire.return`:

Return
------

NFP CPP Area handle, or NULL

.. _`nfp_cpp_area_free`:

nfp_cpp_area_free
=================

.. c:function:: void nfp_cpp_area_free(struct nfp_cpp_area *area)

    free up the CPP area

    :param struct nfp_cpp_area \*area:
        CPP area handle

.. _`nfp_cpp_area_free.description`:

Description
-----------

Frees up memory resources held by the CPP area.

.. _`nfp_cpp_area_acquire`:

nfp_cpp_area_acquire
====================

.. c:function:: int nfp_cpp_area_acquire(struct nfp_cpp_area *area)

    lock down a CPP area for access

    :param struct nfp_cpp_area \*area:
        CPP area handle

.. _`nfp_cpp_area_acquire.description`:

Description
-----------

Locks down the CPP area for a potential long term activity.  Area
must always be locked down before being accessed.

.. _`nfp_cpp_area_acquire.return`:

Return
------

0, or -ERRNO

.. _`nfp_cpp_area_acquire_nonblocking`:

nfp_cpp_area_acquire_nonblocking
================================

.. c:function:: int nfp_cpp_area_acquire_nonblocking(struct nfp_cpp_area *area)

    lock down a CPP area for access

    :param struct nfp_cpp_area \*area:
        CPP area handle

.. _`nfp_cpp_area_acquire_nonblocking.description`:

Description
-----------

Locks down the CPP area for a potential long term activity.  Area
must always be locked down before being accessed.

.. _`nfp_cpp_area_acquire_nonblocking.note`:

NOTE
----

Returns -EAGAIN is no area is available

.. _`nfp_cpp_area_acquire_nonblocking.return`:

Return
------

0, or -ERRNO

.. _`nfp_cpp_area_release`:

nfp_cpp_area_release
====================

.. c:function:: void nfp_cpp_area_release(struct nfp_cpp_area *area)

    release a locked down CPP area

    :param struct nfp_cpp_area \*area:
        CPP area handle

.. _`nfp_cpp_area_release.description`:

Description
-----------

Releases a previously locked down CPP area.

.. _`nfp_cpp_area_release_free`:

nfp_cpp_area_release_free
=========================

.. c:function:: void nfp_cpp_area_release_free(struct nfp_cpp_area *area)

    release CPP area and free it

    :param struct nfp_cpp_area \*area:
        CPP area handle

.. _`nfp_cpp_area_release_free.description`:

Description
-----------

Releases CPP area and frees up memory resources held by the it.

.. _`nfp_cpp_area_read`:

nfp_cpp_area_read
=================

.. c:function:: int nfp_cpp_area_read(struct nfp_cpp_area *area, unsigned long offset, void *kernel_vaddr, size_t length)

    read data from CPP area

    :param struct nfp_cpp_area \*area:
        CPP area handle

    :param unsigned long offset:
        offset into CPP area

    :param void \*kernel_vaddr:
        kernel address to put data into

    :param size_t length:
        number of bytes to read

.. _`nfp_cpp_area_read.description`:

Description
-----------

Read data from indicated CPP region.

.. _`nfp_cpp_area_read.note`:

NOTE
----

\ ``offset``\  and \ ``length``\  must be 32-bit aligned values.
Area must have been locked down with an 'acquire'.

.. _`nfp_cpp_area_read.return`:

Return
------

length of io, or -ERRNO

.. _`nfp_cpp_area_write`:

nfp_cpp_area_write
==================

.. c:function:: int nfp_cpp_area_write(struct nfp_cpp_area *area, unsigned long offset, const void *kernel_vaddr, size_t length)

    write data to CPP area

    :param struct nfp_cpp_area \*area:
        CPP area handle

    :param unsigned long offset:
        offset into CPP area

    :param const void \*kernel_vaddr:
        kernel address to read data from

    :param size_t length:
        number of bytes to write

.. _`nfp_cpp_area_write.description`:

Description
-----------

Write data to indicated CPP region.

.. _`nfp_cpp_area_write.note`:

NOTE
----

\ ``offset``\  and \ ``length``\  must be 32-bit aligned values.
Area must have been locked down with an 'acquire'.

.. _`nfp_cpp_area_write.return`:

Return
------

length of io, or -ERRNO

.. _`nfp_cpp_area_size`:

nfp_cpp_area_size
=================

.. c:function:: size_t nfp_cpp_area_size(struct nfp_cpp_area *cpp_area)

    return size of a CPP area

    :param struct nfp_cpp_area \*cpp_area:
        CPP area handle

.. _`nfp_cpp_area_size.return`:

Return
------

Size of the area

.. _`nfp_cpp_area_name`:

nfp_cpp_area_name
=================

.. c:function:: const char *nfp_cpp_area_name(struct nfp_cpp_area *cpp_area)

    return name of a CPP area

    :param struct nfp_cpp_area \*cpp_area:
        CPP area handle

.. _`nfp_cpp_area_name.return`:

Return
------

Name of the area, or NULL

.. _`nfp_cpp_area_priv`:

nfp_cpp_area_priv
=================

.. c:function:: void *nfp_cpp_area_priv(struct nfp_cpp_area *cpp_area)

    return private struct for CPP area

    :param struct nfp_cpp_area \*cpp_area:
        CPP area handle

.. _`nfp_cpp_area_priv.return`:

Return
------

Private data for the CPP area

.. _`nfp_cpp_area_cpp`:

nfp_cpp_area_cpp
================

.. c:function:: struct nfp_cpp *nfp_cpp_area_cpp(struct nfp_cpp_area *cpp_area)

    return CPP handle for CPP area

    :param struct nfp_cpp_area \*cpp_area:
        CPP area handle

.. _`nfp_cpp_area_cpp.return`:

Return
------

NFP CPP handle

.. _`nfp_cpp_area_resource`:

nfp_cpp_area_resource
=====================

.. c:function:: struct resource *nfp_cpp_area_resource(struct nfp_cpp_area *area)

    get resource

    :param struct nfp_cpp_area \*area:
        CPP area handle

.. _`nfp_cpp_area_resource.note`:

NOTE
----

Area must have been locked down with an 'acquire'.

.. _`nfp_cpp_area_resource.return`:

Return
------

struct resource pointer, or NULL

.. _`nfp_cpp_area_phys`:

nfp_cpp_area_phys
=================

.. c:function:: phys_addr_t nfp_cpp_area_phys(struct nfp_cpp_area *area)

    get physical address of CPP area

    :param struct nfp_cpp_area \*area:
        CPP area handle

.. _`nfp_cpp_area_phys.note`:

NOTE
----

Area must have been locked down with an 'acquire'.

.. _`nfp_cpp_area_phys.return`:

Return
------

phy_addr_t of the area, or NULL

.. _`nfp_cpp_area_iomem`:

nfp_cpp_area_iomem
==================

.. c:function:: void __iomem *nfp_cpp_area_iomem(struct nfp_cpp_area *area)

    get IOMEM region for CPP area

    :param struct nfp_cpp_area \*area:
        CPP area handle

.. _`nfp_cpp_area_iomem.description`:

Description
-----------

Returns an iomem pointer for use with \ :c:func:`readl`\ /writel() style
operations.

.. _`nfp_cpp_area_iomem.note`:

NOTE
----

Area must have been locked down with an 'acquire'.

.. _`nfp_cpp_area_iomem.return`:

Return
------

\__iomem pointer to the area, or NULL

.. _`nfp_cpp_area_readl`:

nfp_cpp_area_readl
==================

.. c:function:: int nfp_cpp_area_readl(struct nfp_cpp_area *area, unsigned long offset, u32 *value)

    Read a u32 word from an area

    :param struct nfp_cpp_area \*area:
        CPP Area handle

    :param unsigned long offset:
        Offset into area

    :param u32 \*value:
        Pointer to read buffer

.. _`nfp_cpp_area_readl.return`:

Return
------

0 on success, or -ERRNO

.. _`nfp_cpp_area_writel`:

nfp_cpp_area_writel
===================

.. c:function:: int nfp_cpp_area_writel(struct nfp_cpp_area *area, unsigned long offset, u32 value)

    Write a u32 word to an area

    :param struct nfp_cpp_area \*area:
        CPP Area handle

    :param unsigned long offset:
        Offset into area

    :param u32 value:
        Value to write

.. _`nfp_cpp_area_writel.return`:

Return
------

0 on success, or -ERRNO

.. _`nfp_cpp_area_readq`:

nfp_cpp_area_readq
==================

.. c:function:: int nfp_cpp_area_readq(struct nfp_cpp_area *area, unsigned long offset, u64 *value)

    Read a u64 word from an area

    :param struct nfp_cpp_area \*area:
        CPP Area handle

    :param unsigned long offset:
        Offset into area

    :param u64 \*value:
        Pointer to read buffer

.. _`nfp_cpp_area_readq.return`:

Return
------

0 on success, or -ERRNO

.. _`nfp_cpp_area_writeq`:

nfp_cpp_area_writeq
===================

.. c:function:: int nfp_cpp_area_writeq(struct nfp_cpp_area *area, unsigned long offset, u64 value)

    Write a u64 word to an area

    :param struct nfp_cpp_area \*area:
        CPP Area handle

    :param unsigned long offset:
        Offset into area

    :param u64 value:
        Value to write

.. _`nfp_cpp_area_writeq.return`:

Return
------

0 on success, or -ERRNO

.. _`nfp_cpp_area_fill`:

nfp_cpp_area_fill
=================

.. c:function:: int nfp_cpp_area_fill(struct nfp_cpp_area *area, unsigned long offset, u32 value, size_t length)

    fill a CPP area with a value

    :param struct nfp_cpp_area \*area:
        CPP area

    :param unsigned long offset:
        offset into CPP area

    :param u32 value:
        value to fill with

    :param size_t length:
        length of area to fill

.. _`nfp_cpp_area_fill.description`:

Description
-----------

Fill indicated area with given value.

.. _`nfp_cpp_area_fill.return`:

Return
------

length of io, or -ERRNO

.. _`nfp_cpp_area_cache_add`:

nfp_cpp_area_cache_add
======================

.. c:function:: int nfp_cpp_area_cache_add(struct nfp_cpp *cpp, size_t size)

    Permanently reserve and area for the hot cache

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

    :param size_t size:
        Size of the area - MUST BE A POWER OF 2.

.. _`nfp_cpp_read`:

nfp_cpp_read
============

.. c:function:: int nfp_cpp_read(struct nfp_cpp *cpp, u32 destination, unsigned long long address, void *kernel_vaddr, size_t length)

    read from CPP target

    :param struct nfp_cpp \*cpp:
        CPP handle

    :param u32 destination:
        CPP id

    :param unsigned long long address:
        offset into CPP target

    :param void \*kernel_vaddr:
        kernel buffer for result

    :param size_t length:
        number of bytes to read

.. _`nfp_cpp_read.return`:

Return
------

length of io, or -ERRNO

.. _`nfp_cpp_write`:

nfp_cpp_write
=============

.. c:function:: int nfp_cpp_write(struct nfp_cpp *cpp, u32 destination, unsigned long long address, const void *kernel_vaddr, size_t length)

    write to CPP target

    :param struct nfp_cpp \*cpp:
        CPP handle

    :param u32 destination:
        CPP id

    :param unsigned long long address:
        offset into CPP target

    :param const void \*kernel_vaddr:
        kernel buffer to read from

    :param size_t length:
        number of bytes to write

.. _`nfp_cpp_write.return`:

Return
------

length of io, or -ERRNO

.. _`nfp_xpb_readl`:

nfp_xpb_readl
=============

.. c:function:: int nfp_xpb_readl(struct nfp_cpp *cpp, u32 xpb_addr, u32 *value)

    Read a u32 word from a XPB location

    :param struct nfp_cpp \*cpp:
        CPP device handle

    :param u32 xpb_addr:
        Address for operation

    :param u32 \*value:
        Pointer to read buffer

.. _`nfp_xpb_readl.return`:

Return
------

0 on success, or -ERRNO

.. _`nfp_xpb_writel`:

nfp_xpb_writel
==============

.. c:function:: int nfp_xpb_writel(struct nfp_cpp *cpp, u32 xpb_addr, u32 value)

    Write a u32 word to a XPB location

    :param struct nfp_cpp \*cpp:
        CPP device handle

    :param u32 xpb_addr:
        Address for operation

    :param u32 value:
        Value to write

.. _`nfp_xpb_writel.return`:

Return
------

0 on success, or -ERRNO

.. _`nfp_xpb_writelm`:

nfp_xpb_writelm
===============

.. c:function:: int nfp_xpb_writelm(struct nfp_cpp *cpp, u32 xpb_tgt, u32 mask, u32 value)

    Modify bits of a 32-bit value from the XPB bus

    :param struct nfp_cpp \*cpp:
        NFP CPP device handle

    :param u32 xpb_tgt:
        XPB target and address

    :param u32 mask:
        mask of bits to alter

    :param u32 value:
        value to modify

.. _`nfp_xpb_writelm.kernel`:

KERNEL
------

This operation is safe to call in interrupt or softirq context.

.. _`nfp_xpb_writelm.return`:

Return
------

0 on success, or -ERRNO

.. _`nfp_cpp_from_operations`:

nfp_cpp_from_operations
=======================

.. c:function:: struct nfp_cpp *nfp_cpp_from_operations(const struct nfp_cpp_operations *ops, struct device *parent, void *priv)

    Create a NFP CPP handle from an operations structure

    :param const struct nfp_cpp_operations \*ops:
        NFP CPP operations structure

    :param struct device \*parent:
        Parent device

    :param void \*priv:
        Private data of low-level implementation

.. _`nfp_cpp_from_operations.note`:

NOTE
----

On failure, cpp_ops->free will be called!

.. _`nfp_cpp_from_operations.return`:

Return
------

NFP CPP handle on success, ERR_PTR on failure

.. _`nfp_cpp_priv`:

nfp_cpp_priv
============

.. c:function:: void *nfp_cpp_priv(struct nfp_cpp *cpp)

    Get the operations private data of a CPP handle

    :param struct nfp_cpp \*cpp:
        CPP handle

.. _`nfp_cpp_priv.return`:

Return
------

Private data for the NFP CPP handle

.. _`nfp_cpp_device`:

nfp_cpp_device
==============

.. c:function:: struct device *nfp_cpp_device(struct nfp_cpp *cpp)

    Get the Linux device handle of a CPP handle

    :param struct nfp_cpp \*cpp:
        CPP handle

.. _`nfp_cpp_device.return`:

Return
------

Device for the NFP CPP bus

.. _`nfp_cpp_explicit_acquire`:

nfp_cpp_explicit_acquire
========================

.. c:function:: struct nfp_cpp_explicit *nfp_cpp_explicit_acquire(struct nfp_cpp *cpp)

    Acquire explicit access handle

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

.. _`nfp_cpp_explicit_acquire.description`:

Description
-----------

The 'data_ref' and 'signal_ref' values are useful when
constructing the NFP_EXPL_CSR1 and NFP_EXPL_POST values.

.. _`nfp_cpp_explicit_acquire.return`:

Return
------

NFP CPP explicit handle

.. _`nfp_cpp_explicit_set_target`:

nfp_cpp_explicit_set_target
===========================

.. c:function:: int nfp_cpp_explicit_set_target(struct nfp_cpp_explicit *expl, u32 cpp_id, u8 len, u8 mask)

    Set target fields for explicit

    :param struct nfp_cpp_explicit \*expl:
        Explicit handle

    :param u32 cpp_id:
        CPP ID field

    :param u8 len:
        CPP Length field

    :param u8 mask:
        CPP Mask field

.. _`nfp_cpp_explicit_set_target.return`:

Return
------

0, or -ERRNO

.. _`nfp_cpp_explicit_set_data`:

nfp_cpp_explicit_set_data
=========================

.. c:function:: int nfp_cpp_explicit_set_data(struct nfp_cpp_explicit *expl, u8 data_master, u16 data_ref)

    Set data fields for explicit

    :param struct nfp_cpp_explicit \*expl:
        Explicit handle

    :param u8 data_master:
        CPP Data Master field

    :param u16 data_ref:
        CPP Data Ref field

.. _`nfp_cpp_explicit_set_data.return`:

Return
------

0, or -ERRNO

.. _`nfp_cpp_explicit_set_signal`:

nfp_cpp_explicit_set_signal
===========================

.. c:function:: int nfp_cpp_explicit_set_signal(struct nfp_cpp_explicit *expl, u8 signal_master, u8 signal_ref)

    Set signal fields for explicit

    :param struct nfp_cpp_explicit \*expl:
        Explicit handle

    :param u8 signal_master:
        CPP Signal Master field

    :param u8 signal_ref:
        CPP Signal Ref field

.. _`nfp_cpp_explicit_set_signal.return`:

Return
------

0, or -ERRNO

.. _`nfp_cpp_explicit_set_posted`:

nfp_cpp_explicit_set_posted
===========================

.. c:function:: int nfp_cpp_explicit_set_posted(struct nfp_cpp_explicit *expl, int posted, u8 siga, enum nfp_cpp_explicit_signal_mode siga_mode, u8 sigb, enum nfp_cpp_explicit_signal_mode sigb_mode)

    Set completion fields for explicit

    :param struct nfp_cpp_explicit \*expl:
        Explicit handle

    :param int posted:
        True for signaled completion, false otherwise

    :param u8 siga:
        CPP Signal A field

    :param enum nfp_cpp_explicit_signal_mode siga_mode:
        CPP Signal A Mode field

    :param u8 sigb:
        CPP Signal B field

    :param enum nfp_cpp_explicit_signal_mode sigb_mode:
        CPP Signal B Mode field

.. _`nfp_cpp_explicit_set_posted.return`:

Return
------

0, or -ERRNO

.. _`nfp_cpp_explicit_put`:

nfp_cpp_explicit_put
====================

.. c:function:: int nfp_cpp_explicit_put(struct nfp_cpp_explicit *expl, const void *buff, size_t len)

    Set up the write (pull) data for a explicit access

    :param struct nfp_cpp_explicit \*expl:
        NFP CPP Explicit handle

    :param const void \*buff:
        Data to have the target pull in the transaction

    :param size_t len:
        Length of data, in bytes

.. _`nfp_cpp_explicit_put.description`:

Description
-----------

The 'len' parameter must be less than or equal to 128 bytes.

If this function is called before the configuration
registers are set, it will return -EINVAL.

.. _`nfp_cpp_explicit_put.return`:

Return
------

0, or -ERRNO

.. _`nfp_cpp_explicit_do`:

nfp_cpp_explicit_do
===================

.. c:function:: int nfp_cpp_explicit_do(struct nfp_cpp_explicit *expl, u64 address)

    Execute a transaction, and wait for it to complete

    :param struct nfp_cpp_explicit \*expl:
        NFP CPP Explicit handle

    :param u64 address:
        Address to send in the explicit transaction

.. _`nfp_cpp_explicit_do.description`:

Description
-----------

If this function is called before the configuration
registers are set, it will return -1, with an errno of EINVAL.

.. _`nfp_cpp_explicit_do.return`:

Return
------

0, or -ERRNO

.. _`nfp_cpp_explicit_get`:

nfp_cpp_explicit_get
====================

.. c:function:: int nfp_cpp_explicit_get(struct nfp_cpp_explicit *expl, void *buff, size_t len)

    Get the 'push' (read) data from a explicit access

    :param struct nfp_cpp_explicit \*expl:
        NFP CPP Explicit handle

    :param void \*buff:
        Data that the target pushed in the transaction

    :param size_t len:
        Length of data, in bytes

.. _`nfp_cpp_explicit_get.description`:

Description
-----------

The 'len' parameter must be less than or equal to 128 bytes.

If this function is called before all three configuration
registers are set, it will return -1, with an errno of EINVAL.

If this function is called before \ :c:func:`nfp_cpp_explicit_do`\ 
has completed, it will return -1, with an errno of EBUSY.

.. _`nfp_cpp_explicit_get.return`:

Return
------

0, or -ERRNO

.. _`nfp_cpp_explicit_release`:

nfp_cpp_explicit_release
========================

.. c:function:: void nfp_cpp_explicit_release(struct nfp_cpp_explicit *expl)

    Release explicit access handle

    :param struct nfp_cpp_explicit \*expl:
        NFP CPP Explicit handle

.. _`nfp_cpp_explicit_cpp`:

nfp_cpp_explicit_cpp
====================

.. c:function:: struct nfp_cpp *nfp_cpp_explicit_cpp(struct nfp_cpp_explicit *cpp_explicit)

    return CPP handle for CPP explicit

    :param struct nfp_cpp_explicit \*cpp_explicit:
        CPP explicit handle

.. _`nfp_cpp_explicit_cpp.return`:

Return
------

NFP CPP handle of the explicit

.. _`nfp_cpp_explicit_priv`:

nfp_cpp_explicit_priv
=====================

.. c:function:: void *nfp_cpp_explicit_priv(struct nfp_cpp_explicit *cpp_explicit)

    return private struct for CPP explicit

    :param struct nfp_cpp_explicit \*cpp_explicit:
        CPP explicit handle

.. _`nfp_cpp_explicit_priv.return`:

Return
------

private data of the explicit, or NULL

.. This file was automatic generated / don't edit.

