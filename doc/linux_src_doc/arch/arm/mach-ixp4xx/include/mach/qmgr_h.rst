.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-ixp4xx/include/mach/qmgr.h

.. _`qmgr_stat_empty`:

qmgr_stat_empty
===============

.. c:function:: int qmgr_stat_empty(unsigned int queue)

    checks if a hardware queue is empty

    :param unsigned int queue:
        queue number

.. _`qmgr_stat_empty.description`:

Description
-----------

Returns non-zero value if the queue is empty.

.. _`qmgr_stat_below_low_watermark`:

qmgr_stat_below_low_watermark
=============================

.. c:function:: int qmgr_stat_below_low_watermark(unsigned int queue)

    checks if a queue is below low watermark

    :param unsigned int queue:
        queue number

.. _`qmgr_stat_below_low_watermark.description`:

Description
-----------

Returns non-zero value if the queue is below low watermark.

.. _`qmgr_stat_above_high_watermark`:

qmgr_stat_above_high_watermark
==============================

.. c:function:: int qmgr_stat_above_high_watermark(unsigned int queue)

    checks if a queue is above high watermark

    :param unsigned int queue:
        queue number

.. _`qmgr_stat_above_high_watermark.description`:

Description
-----------

Returns non-zero value if the queue is above high watermark

.. _`qmgr_stat_full`:

qmgr_stat_full
==============

.. c:function:: int qmgr_stat_full(unsigned int queue)

    checks if a hardware queue is full

    :param unsigned int queue:
        queue number

.. _`qmgr_stat_full.description`:

Description
-----------

Returns non-zero value if the queue is full.

.. _`qmgr_stat_underflow`:

qmgr_stat_underflow
===================

.. c:function:: int qmgr_stat_underflow(unsigned int queue)

    checks if a hardware queue experienced underflow

    :param unsigned int queue:
        queue number

.. _`qmgr_stat_underflow.description`:

Description
-----------

Returns non-zero value if the queue experienced underflow.

.. _`qmgr_stat_overflow`:

qmgr_stat_overflow
==================

.. c:function:: int qmgr_stat_overflow(unsigned int queue)

    checks if a hardware queue experienced overflow

    :param unsigned int queue:
        queue number

.. _`qmgr_stat_overflow.description`:

Description
-----------

Returns non-zero value if the queue experienced overflow.

.. This file was automatic generated / don't edit.

