.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/include/asm/sn/sn_sal.h

.. _`sn_sal_rev`:

sn_sal_rev
==========

.. c:function:: u32 sn_sal_rev( void)

    get the SGI SAL revision number

    :param  void:
        no arguments

.. _`sn_sal_rev.description`:

Description
-----------

The SGI PROM stores its version in the sal_[ab]_rev_(major\|minor).
This routine simply extracts the major and minor values and
presents them in a u32 format.

For example, version 4.05 would be represented at 0x0405.

.. _`ia64_sn_pod_mode`:

ia64_sn_pod_mode
================

.. c:function:: u64 ia64_sn_pod_mode( void)

    call the SN_SAL_POD_MODE function

    :param  void:
        no arguments

.. _`ia64_sn_pod_mode.description`:

Description
-----------

SN_SAL_POD_MODE actually takes an argument, but it's always
0 when we call it from the kernel, so we don't have to expose
it to the caller.

.. _`ia64_sn_probe_mem`:

ia64_sn_probe_mem
=================

.. c:function:: u64 ia64_sn_probe_mem(long addr, long size, void *data_ptr)

    read from memory safely

    :param long addr:
        address to probe

    :param long size:
        number bytes to read (1,2,4,8)

    :param void \*data_ptr:
        address to store value read by probe (-1 returned if probe fails)

.. _`ia64_sn_probe_mem.description`:

Description
-----------

Call into the SAL to do a memory read.  If the read generates a machine
check, this routine will recover gracefully and return -1 to the caller.
\ ``addr``\  is usually a kernel virtual address in uncached space (i.e. the
address starts with 0xc), but if called in physical mode, \ ``addr``\  should
be a physical address.

.. _`ia64_sn_probe_mem.return-values`:

Return values
-------------

0 - probe successful
1 - probe failed (generated MCA)
2 - Bad arg
<0 - PAL error

.. _`ia64_sn_fru_capture`:

ia64_sn_fru_capture
===================

.. c:function:: u64 ia64_sn_fru_capture( void)

    tell the system controller to capture hw state

    :param  void:
        no arguments

.. _`ia64_sn_fru_capture.description`:

Description
-----------

This routine will call the SAL which will tell the system controller(s)
to capture hw mmr information from each SHub in the system.

.. _`ia64_sn_get_fit_compt`:

ia64_sn_get_fit_compt
=====================

.. c:function:: int ia64_sn_get_fit_compt(u64 nasid, u64 index, void *fitentry, void *banbuf, u64 banlen)

    read a FIT entry from the PROM header

    :param u64 nasid:
        NASID of node to read

    :param u64 index:
        FIT entry index to be retrieved (0..n)

    :param void \*fitentry:
        16 byte buffer where FIT entry will be stored.

    :param void \*banbuf:
        optional buffer for retrieving banner

    :param u64 banlen:
        length of banner buffer

.. _`ia64_sn_get_fit_compt.description`:

Description
-----------

Access to the physical PROM chips needs to be serialized since reads and
writes can't occur at the same time, so we need to call into the SAL when
we want to look at the FIT entries on the chips.

.. _`ia64_sn_get_fit_compt.return`:

Return
------

\ ``SALRET_OK``\  if ok
\ ``SALRET_INVALID_ARG``\  if index too big
\ ``SALRET_NOT_IMPLEMENTED``\  if running on older PROM
??? if nasid invalid OR banner buffer not large enough

.. This file was automatic generated / don't edit.

