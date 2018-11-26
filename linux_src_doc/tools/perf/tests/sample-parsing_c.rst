.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/tests/sample-parsing.c

.. _`test__sample_parsing`:

test__sample_parsing
====================

.. c:function:: int test__sample_parsing(int subtest __maybe_unused, int subtest __maybe_unused)

    test sample parsing.

    :param __maybe_unused:
        *undescribed*
    :type __maybe_unused: int subtest

    :param __maybe_unused:
        *undescribed*
    :type __maybe_unused: int subtest

.. _`test__sample_parsing.description`:

Description
-----------

This function implements a test that synthesizes a sample event, parses it
and then checks that the parsed sample matches the original sample.  The test
checks sample format bits separately and together.  If the test passes \ ``0``\  is
returned, otherwise \ ``-1``\  is returned.

.. This file was automatic generated / don't edit.

