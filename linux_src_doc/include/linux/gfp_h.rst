.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/gfp.h

.. _`page-mobility-and-placement-hints`:

Page mobility and placement hints
=================================

Page mobility and placement hints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These flags provide hints about how mobile the page is. Pages with similar
mobility are placed within the same pageblocks to minimise problems due
to external fragmentation.

\ ``__GFP_MOVABLE``\  (also a zone modifier) indicates that the page can be
moved by page migration during memory compaction or can be reclaimed.

\ ``__GFP_RECLAIMABLE``\  is used for slab allocations that specify
SLAB_RECLAIM_ACCOUNT and whose pages can be freed via shrinkers.

\ ``__GFP_WRITE``\  indicates the caller intends to dirty the page. Where possible,
these pages will be spread between local zones to avoid all the dirty
pages being in one zone (fair zone allocation policy).

\ ``__GFP_HARDWALL``\  enforces the cpuset memory allocation policy.

\ ``__GFP_THISNODE``\  forces the allocation to be satisified from the requested
node with no fallbacks or placement policy enforcements.

\ ``__GFP_ACCOUNT``\  causes the allocation to be accounted to kmemcg.

.. _`watermark-modifiers`:

Watermark modifiers
===================

Watermark modifiers -- controls access to emergency reserves
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\ ``__GFP_HIGH``\  indicates that the caller is high-priority and that granting
the request is necessary before the system can make forward progress.
For example, creating an IO context to clean pages.

\ ``__GFP_ATOMIC``\  indicates that the caller cannot reclaim or sleep and is
high priority. Users are typically interrupt handlers. This may be
used in conjunction with \ ``__GFP_HIGH``\ 

\ ``__GFP_MEMALLOC``\  allows access to all memory. This should only be used when
the caller guarantees the allocation will allow more memory to be freed
very shortly e.g. process exiting or swapping. Users either should
be the MM or co-ordinating closely with the VM (e.g. swap over NFS).

\ ``__GFP_NOMEMALLOC``\  is used to explicitly forbid access to emergency reserves.
This takes precedence over the \ ``__GFP_MEMALLOC``\  flag if both are set.

.. _`reclaim-modifiers`:

Reclaim modifiers
=================

Reclaim modifiers
~~~~~~~~~~~~~~~~~

\ ``__GFP_IO``\  can start physical IO.

\ ``__GFP_FS``\  can call down to the low-level FS. Clearing the flag avoids the
allocator recursing into the filesystem which might already be holding
locks.

\ ``__GFP_DIRECT_RECLAIM``\  indicates that the caller may enter direct reclaim.
This flag can be cleared to avoid unnecessary delays when a fallback
option is available.

\ ``__GFP_KSWAPD_RECLAIM``\  indicates that the caller wants to wake kswapd when
the low watermark is reached and have it reclaim pages until the high
watermark is reached. A caller may wish to clear this flag when fallback
options are available and the reclaim is likely to disrupt the system. The
canonical example is THP allocation where a fallback is cheap but
reclaim/compaction may cause indirect stalls.

\ ``__GFP_RECLAIM``\  is shorthand to allow/forbid both direct and kswapd reclaim.

The default allocator behavior depends on the request size. We have a concept
of so called costly allocations (with order > \ ``PAGE_ALLOC_COSTLY_ORDER``\ ).
!costly allocations are too essential to fail so they are implicitly
non-failing by default (with some exceptions like OOM victims might fail so
the caller still has to check for failures) while costly requests try to be
not disruptive and back off even without invoking the OOM killer.
The following three modifiers might be used to override some of these
implicit rules

\ ``__GFP_NORETRY``\ : The VM implementation will try only very lightweight
memory direct reclaim to get some memory under memory pressure (thus
it can sleep). It will avoid disruptive actions like OOM killer. The
caller must handle the failure which is quite likely to happen under
heavy memory pressure. The flag is suitable when failure can easily be
handled at small cost, such as reduced throughput

\ ``__GFP_RETRY_MAYFAIL``\ : The VM implementation will retry memory reclaim
procedures that have previously failed if there is some indication
that progress has been made else where.  It can wait for other
tasks to attempt high level approaches to freeing memory such as
compaction (which removes fragmentation) and page-out.
There is still a definite limit to the number of retries, but it is
a larger limit than with \ ``__GFP_NORETRY``\ .
Allocations with this flag may fail, but only when there is
genuinely little unused memory. While these allocations do not
directly trigger the OOM killer, their failure indicates that
the system is likely to need to use the OOM killer soon.  The
caller must handle failure, but can reasonably do so by failing
a higher-level request, or completing it only in a much less
efficient manner.
If the allocation does fail, and the caller is in a position to
free some non-essential memory, doing so could benefit the system
as a whole.

\ ``__GFP_NOFAIL``\ : The VM implementation _must_ retry infinitely: the caller
cannot handle allocation failures. The allocation could block
indefinitely but will never return with failure. Testing for
failure is pointless.
New users should be evaluated carefully (and the flag should be
used only when there is no reasonable failure policy) but it is
definitely preferable to use the flag rather than opencode endless
loop around allocator.
Using this flag for costly allocations is _highly_ discouraged.

.. _`action-modifiers`:

Action modifiers
================

Action modifiers
~~~~~~~~~~~~~~~~

\ ``__GFP_NOWARN``\  suppresses allocation failure reports.

\ ``__GFP_COMP``\  address compound page metadata.

\ ``__GFP_ZERO``\  returns a zeroed page on success.

.. _`useful-gfp-flag-combinations`:

Useful GFP flag combinations
============================

Useful GFP flag combinations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Useful GFP flag combinations that are commonly used. It is recommended
that subsystems start with one of these combinations and then set/clear
\ ``__GFP_FOO``\  flags as necessary.

\ ``GFP_ATOMIC``\  users can not sleep and need the allocation to succeed. A lower
watermark is applied to allow access to "atomic reserves"

\ ``GFP_KERNEL``\  is typical for kernel-internal allocations. The caller requires
\ ``ZONE_NORMAL``\  or a lower zone for direct access but can direct reclaim.

\ ``GFP_KERNEL_ACCOUNT``\  is the same as GFP_KERNEL, except the allocation is
accounted to kmemcg.

\ ``GFP_NOWAIT``\  is for kernel allocations that should not stall for direct
reclaim, start physical IO or use any filesystem callback.

\ ``GFP_NOIO``\  will use direct reclaim to discard clean pages or slab pages
that do not require the starting of any physical IO.
Please try to avoid using this flag directly and instead use
memalloc_noio_{save,restore} to mark the whole scope which cannot
perform any IO with a short explanation why. All allocation requests
will inherit GFP_NOIO implicitly.

\ ``GFP_NOFS``\  will use direct reclaim but will not use any filesystem interfaces.
Please try to avoid using this flag directly and instead use
memalloc_nofs_{save,restore} to mark the whole scope which cannot/shouldn't
recurse into the FS layer with a short explanation why. All allocation
requests will inherit GFP_NOFS implicitly.

\ ``GFP_USER``\  is for userspace allocations that also need to be directly
accessibly by the kernel or hardware. It is typically used by hardware
for buffers that are mapped to userspace (e.g. graphics) that hardware
still must DMA to. cpuset limits are enforced for these allocations.

\ ``GFP_DMA``\  exists for historical reasons and should be avoided where possible.
The flags indicates that the caller requires that the lowest zone be
used (%ZONE_DMA or 16M on x86-64). Ideally, this would be removed but
it would require careful auditing as some users really require it and
others use the flag to avoid lowmem reserves in \ ``ZONE_DMA``\  and treat the
lowest zone as a type of emergency reserve.

\ ``GFP_DMA32``\  is similar to \ ``GFP_DMA``\  except that the caller requires a 32-bit
address.

\ ``GFP_HIGHUSER``\  is for userspace allocations that may be mapped to userspace,
do not need to be directly accessible by the kernel but that cannot
move once in use. An example may be a hardware allocation that maps
data directly into userspace but has no addressing limitations.

\ ``GFP_HIGHUSER_MOVABLE``\  is for userspace allocations that the kernel does not
need direct access to but can use \ :c:func:`kmap`\  when access is required. They
are expected to be movable via page reclaim or page migration. Typically,
pages on the LRU would also be allocated with \ ``GFP_HIGHUSER_MOVABLE``\ .

\ ``GFP_TRANSHUGE``\  and \ ``GFP_TRANSHUGE_LIGHT``\  are used for THP allocations. They
are compound allocations that will generally fail quickly if memory is not
available and will not wake kswapd/kcompactd on failure. The _LIGHT
version does not attempt reclaim/compaction at all and is by default used
in page fault path, while the non-light is used by khugepaged.

.. This file was automatic generated / don't edit.

