.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/compaction.c

.. _`isolate_freepages_range`:

isolate_freepages_range
=======================

.. c:function:: unsigned long isolate_freepages_range(struct compact_control *cc, unsigned long start_pfn, unsigned long end_pfn)

    isolate free pages.

    :param cc:
        Compaction control structure.
    :type cc: struct compact_control \*

    :param start_pfn:
        The first PFN to start isolating.
    :type start_pfn: unsigned long

    :param end_pfn:
        The one-past-last PFN.
    :type end_pfn: unsigned long

.. _`isolate_freepages_range.description`:

Description
-----------

Non-free pages, invalid PFNs, or zone boundaries within the
[start_pfn, end_pfn) range are considered errors, cause function to
undo its actions and return zero.

Otherwise, function returns one-past-the-last PFN of isolated page
(which may be greater then end_pfn if end fell in a middle of
a free page).

.. _`isolate_migratepages_block`:

isolate_migratepages_block
==========================

.. c:function:: unsigned long isolate_migratepages_block(struct compact_control *cc, unsigned long low_pfn, unsigned long end_pfn, isolate_mode_t isolate_mode)

    isolate all migrate-able pages within a single pageblock

    :param cc:
        Compaction control structure.
    :type cc: struct compact_control \*

    :param low_pfn:
        The first PFN to isolate
    :type low_pfn: unsigned long

    :param end_pfn:
        The one-past-the-last PFN to isolate, within same pageblock
    :type end_pfn: unsigned long

    :param isolate_mode:
        Isolation mode to be used.
    :type isolate_mode: isolate_mode_t

.. _`isolate_migratepages_block.description`:

Description
-----------

Isolate all pages that can be migrated from the range specified by
[low_pfn, end_pfn). The range is expected to be within same pageblock.
Returns zero if there is a fatal signal pending, otherwise PFN of the
first page that was not scanned (which may be both less, equal to or more
than end_pfn).

The pages are isolated on cc->migratepages list (not required to be empty),
and cc->nr_migratepages is updated accordingly. The cc->migrate_pfn field
is neither read nor updated.

.. _`isolate_migratepages_range`:

isolate_migratepages_range
==========================

.. c:function:: unsigned long isolate_migratepages_range(struct compact_control *cc, unsigned long start_pfn, unsigned long end_pfn)

    isolate migrate-able pages in a PFN range

    :param cc:
        Compaction control structure.
    :type cc: struct compact_control \*

    :param start_pfn:
        The first PFN to start isolating.
    :type start_pfn: unsigned long

    :param end_pfn:
        The one-past-last PFN.
    :type end_pfn: unsigned long

.. _`isolate_migratepages_range.description`:

Description
-----------

Returns zero if isolation fails fatally due to e.g. pending signal.
Otherwise, function returns one-past-the-last PFN of isolated page
(which may be greater than end_pfn if end fell in a middle of a THP page).

.. _`try_to_compact_pages`:

try_to_compact_pages
====================

.. c:function:: enum compact_result try_to_compact_pages(gfp_t gfp_mask, unsigned int order, unsigned int alloc_flags, const struct alloc_context *ac, enum compact_priority prio)

    Direct compact to satisfy a high-order allocation

    :param gfp_mask:
        The GFP mask of the current allocation
    :type gfp_mask: gfp_t

    :param order:
        The order of the current allocation
    :type order: unsigned int

    :param alloc_flags:
        The allocation flags of the current allocation
    :type alloc_flags: unsigned int

    :param ac:
        The context of current allocation
    :type ac: const struct alloc_context \*

    :param prio:
        Determines how hard direct compaction should try to succeed
    :type prio: enum compact_priority

.. _`try_to_compact_pages.description`:

Description
-----------

This is the main entry point for direct page compaction.

.. This file was automatic generated / don't edit.

