.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/mm/mmap.c

.. _`mmap_address_hint_valid`:

mmap_address_hint_valid
=======================

.. c:function:: bool mmap_address_hint_valid(unsigned long addr, unsigned long len)

    Validate the address hint of mmap

    :param unsigned long addr:
        Address hint

    :param unsigned long len:
        Mapping length

.. _`mmap_address_hint_valid.description`:

Description
-----------

Check whether \ ``addr``\  and \ ``addr``\  + \ ``len``\  result in a valid mapping.

On 32bit this only checks whether \ ``addr``\  + \ ``len``\  is <= TASK_SIZE.

On 64bit with 5-level page tables another sanity check is required
because mappings requested by mmap(@addr, 0) which cross the 47-bit

.. _`mmap_address_hint_valid.virtual-address-boundary-can-cause-the-following-theoretical-issue`:

virtual address boundary can cause the following theoretical issue
------------------------------------------------------------------


An application calls mmap(addr, 0), i.e. without MAP_FIXED, where \ ``addr``\ 
is below the border of the 47-bit address space and \ ``addr``\  + \ ``len``\  is
above the border.

With 4-level paging this request succeeds, but the resulting mapping
address will always be within the 47-bit virtual address space, because
the hint address does not result in a valid mapping and is
ignored. Hence applications which are not prepared to handle virtual
addresses above 47-bit work correctly.

With 5-level paging this request would be granted and result in a
mapping which crosses the border of the 47-bit virtual address
space. If the application cannot handle addresses above 47-bit this
will lead to misbehaviour and hard to diagnose failures.

Therefore ignore address hints which would result in a mapping crossing
the 47-bit virtual address boundary.

Note, that in the same scenario with MAP_FIXED the behaviour is
different. The request with \ ``addr``\  < 47-bit and \ ``addr``\  + \ ``len``\  > 47-bit
fails on a 4-level paging machine but succeeds on a 5-level paging
machine. It is reasonable to expect that an application does not rely on
the failure of such a fixed mapping request, so the restriction is not
applied.

.. This file was automatic generated / don't edit.

