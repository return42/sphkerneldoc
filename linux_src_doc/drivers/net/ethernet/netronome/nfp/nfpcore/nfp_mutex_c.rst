.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_mutex.c

.. _`nfp_cpp_mutex_init`:

nfp_cpp_mutex_init
==================

.. c:function:: int nfp_cpp_mutex_init(struct nfp_cpp *cpp, int target, unsigned long long address, u32 key)

    Initialize a mutex location

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

    :param int target:
        NFP CPP target ID (ie NFP_CPP_TARGET_CLS or NFP_CPP_TARGET_MU)

    :param unsigned long long address:
        Offset into the address space of the NFP CPP target ID

    :param u32 key:
        Unique 32-bit value for this mutex

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

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

    :param int target:
        NFP CPP target ID (ie NFP_CPP_TARGET_CLS or NFP_CPP_TARGET_MU)

    :param unsigned long long address:
        Offset into the address space of the NFP CPP target ID

    :param u32 key:
        32-bit unique key (must match the key at this location)

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

    :param struct nfp_cpp_mutex \*mutex:
        NFP CPP Mutex handle

.. _`nfp_cpp_mutex_lock`:

nfp_cpp_mutex_lock
==================

.. c:function:: int nfp_cpp_mutex_lock(struct nfp_cpp_mutex *mutex)

    Lock a mutex handle, using the NFP MU Atomic Engine

    :param struct nfp_cpp_mutex \*mutex:
        NFP CPP Mutex handle

.. _`nfp_cpp_mutex_lock.return`:

Return
------

0 on success, or -errno on failure

.. _`nfp_cpp_mutex_unlock`:

nfp_cpp_mutex_unlock
====================

.. c:function:: int nfp_cpp_mutex_unlock(struct nfp_cpp_mutex *mutex)

    Unlock a mutex handle, using the MU Atomic Engine

    :param struct nfp_cpp_mutex \*mutex:
        NFP CPP Mutex handle

.. _`nfp_cpp_mutex_unlock.return`:

Return
------

0 on success, or -errno on failure

.. _`nfp_cpp_mutex_trylock`:

nfp_cpp_mutex_trylock
=====================

.. c:function:: int nfp_cpp_mutex_trylock(struct nfp_cpp_mutex *mutex)

    Attempt to lock a mutex handle

    :param struct nfp_cpp_mutex \*mutex:
        NFP CPP Mutex handle

.. _`nfp_cpp_mutex_trylock.return`:

Return
------

0 if the lock succeeded, -errno on failure

.. This file was automatic generated / don't edit.

