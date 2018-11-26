.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/intel/atom/sst/sst_stream.c

.. _`sst_realloc_stream`:

sst_realloc_stream
==================

.. c:function:: int sst_realloc_stream(struct intel_sst_drv *sst_drv_ctx, int str_id)

    Send msg for (re-)allocating a stream using the \ ``sst_drv_ctx``\   intel_sst_drv context pointer

    :param sst_drv_ctx:
        *undescribed*
    :type sst_drv_ctx: struct intel_sst_drv \*

    :param str_id:
        stream ID
    :type str_id: int

.. _`sst_realloc_stream.description`:

Description
-----------

Send a msg for (re-)allocating a stream using the parameters previously
passed to \ :c:func:`sst_alloc_stream_mrfld`\  for the same stream ID.

.. _`sst_realloc_stream.return`:

Return
------

0 or negative errno value.

.. _`sst_start_stream`:

sst_start_stream
================

.. c:function:: int sst_start_stream(struct intel_sst_drv *sst_drv_ctx, int str_id)

    Send msg for a starting stream

    :param sst_drv_ctx:
        *undescribed*
    :type sst_drv_ctx: struct intel_sst_drv \*

    :param str_id:
        stream ID
    :type str_id: int

.. _`sst_start_stream.description`:

Description
-----------

This function is called by any function which wants to start
a stream.

.. _`sst_pause_stream`:

sst_pause_stream
================

.. c:function:: int sst_pause_stream(struct intel_sst_drv *sst_drv_ctx, int str_id)

    Send msg for a pausing stream

    :param sst_drv_ctx:
        *undescribed*
    :type sst_drv_ctx: struct intel_sst_drv \*

    :param str_id:
        stream ID
    :type str_id: int

.. _`sst_pause_stream.description`:

Description
-----------

This function is called by any function which wants to pause
an already running stream.

.. _`sst_resume_stream`:

sst_resume_stream
=================

.. c:function:: int sst_resume_stream(struct intel_sst_drv *sst_drv_ctx, int str_id)

    Send msg for resuming stream

    :param sst_drv_ctx:
        *undescribed*
    :type sst_drv_ctx: struct intel_sst_drv \*

    :param str_id:
        stream ID
    :type str_id: int

.. _`sst_resume_stream.description`:

Description
-----------

This function is called by any function which wants to resume
an already paused stream.

.. _`sst_drop_stream`:

sst_drop_stream
===============

.. c:function:: int sst_drop_stream(struct intel_sst_drv *sst_drv_ctx, int str_id)

    Send msg for stopping stream

    :param sst_drv_ctx:
        *undescribed*
    :type sst_drv_ctx: struct intel_sst_drv \*

    :param str_id:
        stream ID
    :type str_id: int

.. _`sst_drop_stream.description`:

Description
-----------

This function is called by any function which wants to stop
a stream.

.. _`sst_drain_stream`:

sst_drain_stream
================

.. c:function:: int sst_drain_stream(struct intel_sst_drv *sst_drv_ctx, int str_id, bool partial_drain)

    Send msg for draining stream

    :param sst_drv_ctx:
        *undescribed*
    :type sst_drv_ctx: struct intel_sst_drv \*

    :param str_id:
        stream ID
    :type str_id: int

    :param partial_drain:
        *undescribed*
    :type partial_drain: bool

.. _`sst_drain_stream.description`:

Description
-----------

This function is called by any function which wants to drain
a stream.

.. _`sst_free_stream`:

sst_free_stream
===============

.. c:function:: int sst_free_stream(struct intel_sst_drv *sst_drv_ctx, int str_id)

    Frees a stream

    :param sst_drv_ctx:
        *undescribed*
    :type sst_drv_ctx: struct intel_sst_drv \*

    :param str_id:
        stream ID
    :type str_id: int

.. _`sst_free_stream.description`:

Description
-----------

This function is called by any function which wants to free
a stream.

.. This file was automatic generated / don't edit.

