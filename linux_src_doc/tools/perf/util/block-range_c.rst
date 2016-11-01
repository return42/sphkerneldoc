.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/block-range.c

.. _`block_range__create`:

block_range__create
===================

.. c:function:: struct block_range_iter block_range__create(u64 start, u64 end)

    :param u64 start:
        branch target starting this basic block

    :param u64 end:
        branch ending this basic block

.. _`block_range__create.description`:

Description
-----------

Create all the required block ranges to precisely span the given range.

.. This file was automatic generated / don't edit.

