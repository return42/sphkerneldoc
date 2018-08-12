.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/subscr.c

.. _`tipc_sub_check_overlap`:

tipc_sub_check_overlap
======================

.. c:function:: int tipc_sub_check_overlap(struct tipc_name_seq *seq, u32 found_lower, u32 found_upper)

    test for subscription overlap with the given values

    :param struct tipc_name_seq \*seq:
        *undescribed*

    :param u32 found_lower:
        *undescribed*

    :param u32 found_upper:
        *undescribed*

.. _`tipc_sub_check_overlap.description`:

Description
-----------

Returns 1 if there is overlap, otherwise 0.

.. This file was automatic generated / don't edit.

