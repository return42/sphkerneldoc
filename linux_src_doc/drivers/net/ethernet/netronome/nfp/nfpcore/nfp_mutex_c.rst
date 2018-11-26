.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_mutex.c

.. _`nfp_cpp_mutex_init`:

nfp_cpp_mutex_init
==================

.. c:function:: int nfp_cpp_mutex_init(struct nfp_cpp *cpp, int target, unsigned long long address, u32 key)

    Initialize a mutex location

    :param cpp:
        NFP CPP handle
    :type cpp: struct nfp_cpp \*

    :param target:
        NFP CPP target ID (ie NFP_CPP_TARGET_CLS or NFP_CPP_TARGET_MU)
    :type target: int

    :param address:
        Offset into the address space of the NFP CPP target ID
    :type address: unsigned long long

    :param key:
        Unique 32-bit value for this mutex
    :type key: u32

.. _`nfp_cpp_mutex_init.description`:

Description
-----------

The CPP target:address must point to a 64-bit aligned location, and
will initialize 64 bits of data at the location.

This creates the initial mutex state, as locked by this
\ :c:func:`nfp_cpp_interface`\ .

This function should only be called when setting up
the initial lock state upon boot-up of the system.

.. _`nfp_cpp_mutex_init.return`:

Return
------

0 on success, or -errno on failure

.. _`nfp_cpp_mutex_alloc`:

nfp_cpp_mutex_alloc
===================

.. c:function:: struct nfp_cpp_mutex *nfp_cpp_mutex_alloc(struct nfp_cpp *cpp, int target, unsigned long long address, u32 key)

    Create a mutex handle

    :param cpp:
        NFP CPP handle
    :type cpp: struct nfp_cpp \*

    :param target:
        NFP CPP target ID (ie NFP_CPP_TARGET_CLS or NFP_CPP_TARGET_MU)
    :type target: int

    :param address:
        Offset into the address space of the NFP CPP target ID
    :type address: unsigned long long

    :param key:
        32-bit unique key (must match the key at this location)
    :type key: u32

.. _`nfp_cpp_mutex_alloc.description`:

Description
-----------

The CPP target:address must point to a 64-bit aligned location, and
reserve 64 bits of data at the location for use by the handle.

Only target/address pairs that point to entities that support the
MU Atomic Engine's CmpAndSwap32 command are supported.

.. _`nfp_cpp_mutex_alloc.return`:

Return
------

A non-NULL struct nfp_cpp_mutex \* on success, NULL on failure.

.. _`nfp_cpp_mutex_free`:

nfp_cpp_mutex_free
==================

.. c:function:: void nfp_cpp_mutex_free(struct nfp_cpp_mutex *mutex)

    Free a mutex handle - does not alter the lock state

    :param mutex:
        NFP CPP Mutex handle
    :type mutex: struct nfp_cpp_mutex \*

.. _`nfp_cpp_mutex_lock`:

nfp_cpp_mutex_lock
==================

.. c:function:: int nfp_cpp_mutex_lock(struct nfp_cpp_mutex *mutex)

    Lock a mutex handle, using the NFP MU Atomic Engine

    :param mutex:
        NFP CPP Mutex handle
    :type mutex: struct nfp_cpp_mutex \*

.. _`nfp_cpp_mutex_lock.return`:

Return
------

0 on success, or -errno on failure

.. _`nfp_cpp_mutex_unlock`:

nfp_cpp_mutex_unlock
====================

.. c:function:: int nfp_cpp_mutex_unlock(struct nfp_cpp_mutex *mutex)

    Unlock a mutex handle, using the MU Atomic Engine

    :param mutex:
        NFP CPP Mutex handle
    :type mutex: struct nfp_cpp_mutex \*

.. _`nfp_cpp_mutex_unlock.return`:

Return
------

0 on success, or -errno on failure

.. _`nfp_cpp_mutex_trylock`:

nfp_cpp_mutex_trylock
=====================

.. c:function:: int nfp_cpp_mutex_trylock(struct nfp_cpp_mutex *mutex)

    Attempt to lock a mutex handle

    :param mutex:
        NFP CPP Mutex handle
    :type mutex: struct nfp_cpp_mutex \*

.. _`nfp_cpp_mutex_trylock.return`:

Return
------

0 if the lock succeeded, -errno on failure

.. _`nfp_cpp_mutex_reclaim`:

nfp_cpp_mutex_reclaim
=====================

.. c:function:: int nfp_cpp_mutex_reclaim(struct nfp_cpp *cpp, int target, unsigned long long address)

    Unlock mutex if held by local endpoint

    :param cpp:
        NFP CPP handle
    :type cpp: struct nfp_cpp \*

    :param target:
        NFP CPP target ID (ie NFP_CPP_TARGET_CLS or NFP_CPP_TARGET_MU)
    :type target: int

    :param address:
        Offset into the address space of the NFP CPP target ID
    :type address: unsigned long long

.. _`nfp_cpp_mutex_reclaim.description`:

Description
-----------

Release lock if held by local system.  Extreme care is advised, call only
when no local lock users can exist.

.. _`nfp_cpp_mutex_reclaim.return`:

Return
------

0 if the lock was OK, 1 if locked by us, -errno on invalid mutex

.. This file was automatic generated / don't edit.

