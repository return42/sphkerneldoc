.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/tests/keep-tracking.c

.. _`test__keep_tracking`:

test__keep_tracking
===================

.. c:function:: int test__keep_tracking(int subtest __maybe_unused, int subtest __maybe_unused)

    test using a dummy software event to keep tracking.

    :param __maybe_unused:
        *undescribed*
    :type __maybe_unused: int subtest

    :param __maybe_unused:
        *undescribed*
    :type __maybe_unused: int subtest

.. _`test__keep_tracking.description`:

Description
-----------

This function implements a test that checks that tracking events continue
when an event is disabled but a dummy software event is not disabled.  If the
test passes \ ``0``\  is returned, otherwise \ ``-1``\  is returned.

.. This file was automatic generated / don't edit.

