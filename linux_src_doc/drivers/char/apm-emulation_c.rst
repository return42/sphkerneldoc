.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/apm-emulation.c

.. _`apm_queue_event`:

apm_queue_event
===============

.. c:function:: void apm_queue_event(apm_event_t event)

    queue an APM event for kapmd

    :param apm_event_t event:
        APM event

.. _`apm_queue_event.description`:

Description
-----------

Queue an APM event for kapmd to process and ultimately take the
appropriate action.  Only a subset of events are handled:
\ ``APM_LOW_BATTERY``\ 
\ ``APM_POWER_STATUS_CHANGE``\ 
\ ``APM_USER_SUSPEND``\ 
\ ``APM_SYS_SUSPEND``\ 
\ ``APM_CRITICAL_SUSPEND``\ 

.. This file was automatic generated / don't edit.

