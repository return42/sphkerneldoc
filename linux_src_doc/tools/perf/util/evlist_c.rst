.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/evlist.c

.. _`perf_evlist__set_id_pos`:

perf_evlist__set_id_pos
=======================

.. c:function:: void perf_evlist__set_id_pos(struct perf_evlist *evlist)

    set the positions of event ids.

    :param evlist:
        selected event list
    :type evlist: struct perf_evlist \*

.. _`perf_evlist__set_id_pos.description`:

Description
-----------

Events with compatible sample types all have the same id_pos
and is_pos.  For convenience, put a copy on evlist.

.. _`perf_evlist__mmap_ex`:

perf_evlist__mmap_ex
====================

.. c:function:: int perf_evlist__mmap_ex(struct perf_evlist *evlist, unsigned int pages, unsigned int auxtrace_pages, bool auxtrace_overwrite)

    Create mmaps to receive events.

    :param evlist:
        list of events
    :type evlist: struct perf_evlist \*

    :param pages:
        map length in pages
    :type pages: unsigned int

    :param auxtrace_pages:
        *undescribed*
    :type auxtrace_pages: unsigned int

    :param auxtrace_overwrite:
        *undescribed*
    :type auxtrace_overwrite: bool

.. _`perf_evlist__mmap_ex.description`:

Description
-----------

If \ ``overwrite``\  is \ ``false``\  the user needs to signal event consumption using
\ :c:func:`perf_mmap__write_tail`\ .  Using \ :c:func:`perf_evlist__mmap_read`\  does this
automatically.

Similarly, if \ ``auxtrace_overwrite``\  is \ ``false``\  the user needs to signal data
consumption using \ :c:func:`auxtrace_mmap__write_tail`\ .

.. _`perf_evlist__mmap_ex.return`:

Return
------

\ ``0``\  on success, negative error code otherwise.

.. This file was automatic generated / don't edit.

