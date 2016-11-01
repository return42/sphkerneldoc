.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/tests/parse-no-sample-id-all.c

.. _`test__parse_no_sample_id_all`:

test__parse_no_sample_id_all
============================

.. c:function:: int test__parse_no_sample_id_all(int subtest __maybe_unused)

    test parsing with no sample_id_all bit set.

    :param int subtest __maybe_unused:
        *undescribed*

.. _`test__parse_no_sample_id_all.description`:

Description
-----------

This function tests parsing data produced on kernel's that do not support the
sample_id_all bit.  Without the sample_id_all bit, non-sample events (such as
mmap events) do not have an id sample appended, and consequently logic
designed to determine the id will not work.  That case happens when there is
more than one selected event, so this test processes three events: 2
attributes representing the selected events and one mmap event.

.. _`test__parse_no_sample_id_all.return`:

Return
------

%0 on success, \ ``-1``\  if the test fails.

.. This file was automatic generated / don't edit.

