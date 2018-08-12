.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/vfio_ccw_cp.c

.. _`ccwchain_calc_length`:

ccwchain_calc_length
====================

.. c:function:: int ccwchain_calc_length(u64 iova, struct channel_program *cp)

    calculate the length of the ccw chain.

    :param u64 iova:
        guest physical address of the target ccw chain

    :param struct channel_program \*cp:
        channel_program on which to perform the operation

.. _`ccwchain_calc_length.description`:

Description
-----------

This is the chain length not considering any TICs.
You need to do a new round for each TIC target.

The program is also validated for absence of not yet supported
indirect data addressing scenarios.

.. _`ccwchain_calc_length.return`:

Return
------

the length of the ccw chain or -errno.

.. _`cp_init`:

cp_init
=======

.. c:function:: int cp_init(struct channel_program *cp, struct device *mdev, union orb *orb)

    allocate ccwchains for a channel program.

    :param struct channel_program \*cp:
        channel_program on which to perform the operation

    :param struct device \*mdev:
        the mediated device to perform pin/unpin operations

    :param union orb \*orb:
        control block for the channel program from the guest

.. _`cp_init.description`:

Description
-----------

This creates one or more ccwchain(s), and copies the raw data of
the target channel program from \ ``orb``\ ->cmd.iova to the new ccwchain(s).

.. _`cp_init.limitations`:

Limitations
-----------

1. Supports only prefetch enabled mode.
2. Supports idal(c64) ccw chaining.
3. Supports 4k idaw.

.. _`cp_init.return`:

Return
------

\ ``0``\  on success and a negative error value on failure.

.. _`cp_free`:

cp_free
=======

.. c:function:: void cp_free(struct channel_program *cp)

    free resources for channel program.

    :param struct channel_program \*cp:
        channel_program on which to perform the operation

.. _`cp_free.description`:

Description
-----------

This unpins the memory pages and frees the memory space occupied by
\ ``cp``\ , which must have been returned by a previous call to \ :c:func:`cp_init`\ .
Otherwise, undefined behavior occurs.

.. _`cp_prefetch`:

cp_prefetch
===========

.. c:function:: int cp_prefetch(struct channel_program *cp)

    translate a guest physical address channel program to a real-device runnable channel program.

    :param struct channel_program \*cp:
        channel_program on which to perform the operation

.. _`cp_prefetch.description`:

Description
-----------

This function translates the guest-physical-address channel program
and stores the result to ccwchain list. \ ``cp``\  must have been
initialized by a previous call with \ :c:func:`cp_init`\ . Otherwise, undefined
behavior occurs.

.. _`cp_prefetch.for-each-chain-composing-the-channel-program`:

For each chain composing the channel program
--------------------------------------------

- On entry ch_len holds the count of CCWs to be translated.
- On exit ch_len is adjusted to the count of successfully translated CCWs.
This allows cp_free to find in ch_len the count of CCWs to free in a chain.

The S/390 CCW Translation APIS (prefixed by 'cp_') are introduced
as helpers to do ccw chain translation inside the kernel. Basically
they accept a channel program issued by a virtual machine, and
translate the channel program to a real-device runnable channel
program.

These APIs will copy the ccws into kernel-space buffers, and update
the guest phsical addresses with their corresponding host physical
addresses.  Then channel I/O device drivers could issue the
translated channel program to real devices to perform an I/O
operation.

These interfaces are designed to support translation only for
channel programs, which are generated and formatted by a
guest. Thus this will make it possible for things like VFIO to
leverage the interfaces to passthrough a channel I/O mediated
device in QEMU.

We support direct ccw chaining by translating them to idal ccws.

.. _`cp_prefetch.return`:

Return
------

\ ``0``\  on success and a negative error value on failure.

.. _`cp_get_orb`:

cp_get_orb
==========

.. c:function:: union orb *cp_get_orb(struct channel_program *cp, u32 intparm, u8 lpm)

    get the orb of the channel program

    :param struct channel_program \*cp:
        channel_program on which to perform the operation

    :param u32 intparm:
        new intparm for the returned orb

    :param u8 lpm:
        candidate value of the logical-path mask for the returned orb

.. _`cp_get_orb.description`:

Description
-----------

This function returns the address of the updated orb of the channel
program. Channel I/O device drivers could use this orb to issue a
ssch.

.. _`cp_update_scsw`:

cp_update_scsw
==============

.. c:function:: void cp_update_scsw(struct channel_program *cp, union scsw *scsw)

    update scsw for a channel program.

    :param struct channel_program \*cp:
        channel_program on which to perform the operation

    :param union scsw \*scsw:
        I/O results of the channel program and also the target to be
        updated

.. _`cp_update_scsw.description`:

Description
-----------

\ ``scsw``\  contains the I/O results of the channel program that pointed
to by \ ``cp``\ . However what \ ``scsw``\ ->cpa stores is a host physical
address, which is meaningless for the guest, which is waiting for
the I/O results.

This function updates \ ``scsw``\ ->cpa to its coressponding guest physical
address.

.. _`cp_iova_pinned`:

cp_iova_pinned
==============

.. c:function:: bool cp_iova_pinned(struct channel_program *cp, u64 iova)

    check if an iova is pinned for a ccw chain.

    :param struct channel_program \*cp:
        channel_program on which to perform the operation

    :param u64 iova:
        the iova to check

.. _`cp_iova_pinned.description`:

Description
-----------

If the \ ``iova``\  is currently pinned for the ccw chain, return true;
else return false.

.. This file was automatic generated / don't edit.

