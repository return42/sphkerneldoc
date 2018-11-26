.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/arch/x86/util/intel-pt.c

.. _`intel_pt_compare_buffers`:

intel_pt_compare_buffers
========================

.. c:function:: bool intel_pt_compare_buffers(void *buf1, size_t compare_size, void *buf2, size_t offs2, size_t buf2_size)

    compare bytes in a buffer to a circular buffer.

    :param buf1:
        first buffer
    :type buf1: void \*

    :param compare_size:
        number of bytes to compare
    :type compare_size: size_t

    :param buf2:
        second buffer (a circular buffer)
    :type buf2: void \*

    :param offs2:
        offset in second buffer
    :type offs2: size_t

    :param buf2_size:
        size of second buffer
    :type buf2_size: size_t

.. _`intel_pt_compare_buffers.description`:

Description
-----------

The comparison allows for the possibility that the bytes to compare in the
circular buffer are not contiguous.  It is assumed that \ ``compare_size``\  <=
\ ``buf2_size``\ .  This function returns \ ``false``\  if the bytes are identical, \ ``true``\ 
otherwise.

.. This file was automatic generated / don't edit.

