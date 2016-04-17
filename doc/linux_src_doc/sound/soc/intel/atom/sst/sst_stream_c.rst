.. -*- coding: utf-8; mode: rst -*-

============
sst_stream.c
============


.. _`sst_start_stream`:

sst_start_stream
================

.. c:function:: int sst_start_stream (struct intel_sst_drv *sst_drv_ctx, int str_id)

    Send msg for a starting stream

    :param struct intel_sst_drv \*sst_drv_ctx:

        *undescribed*

    :param int str_id:
        stream ID



.. _`sst_start_stream.description`:

Description
-----------

This function is called by any function which wants to start
a stream.



.. _`sst_resume_stream`:

sst_resume_stream
=================

.. c:function:: int sst_resume_stream (struct intel_sst_drv *sst_drv_ctx, int str_id)

    Send msg for resuming stream

    :param struct intel_sst_drv \*sst_drv_ctx:

        *undescribed*

    :param int str_id:
        stream ID



.. _`sst_resume_stream.description`:

Description
-----------

This function is called by any function which wants to resume
an already paused stream.



.. _`sst_drop_stream`:

sst_drop_stream
===============

.. c:function:: int sst_drop_stream (struct intel_sst_drv *sst_drv_ctx, int str_id)

    Send msg for stopping stream

    :param struct intel_sst_drv \*sst_drv_ctx:

        *undescribed*

    :param int str_id:
        stream ID



.. _`sst_drop_stream.description`:

Description
-----------

This function is called by any function which wants to stop
a stream.



.. _`sst_drain_stream`:

sst_drain_stream
================

.. c:function:: int sst_drain_stream (struct intel_sst_drv *sst_drv_ctx, int str_id, bool partial_drain)

    Send msg for draining stream

    :param struct intel_sst_drv \*sst_drv_ctx:

        *undescribed*

    :param int str_id:
        stream ID

    :param bool partial_drain:

        *undescribed*



.. _`sst_drain_stream.description`:

Description
-----------

This function is called by any function which wants to drain
a stream.



.. _`sst_free_stream`:

sst_free_stream
===============

.. c:function:: int sst_free_stream (struct intel_sst_drv *sst_drv_ctx, int str_id)

    Frees a stream

    :param struct intel_sst_drv \*sst_drv_ctx:

        *undescribed*

    :param int str_id:
        stream ID



.. _`sst_free_stream.description`:

Description
-----------

This function is called by any function which wants to free
a stream.

