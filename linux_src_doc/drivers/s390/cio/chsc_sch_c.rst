.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/chsc_sch.c

.. _`chsc_async`:

chsc_async
==========

.. c:function:: int chsc_async(struct chsc_async_area *chsc_area, struct chsc_request *request)

    try to start a chsc request asynchronously

    :param struct chsc_async_area \*chsc_area:
        request to be started

    :param struct chsc_request \*request:
        request structure to associate

.. _`chsc_async.description`:

Description
-----------

Tries to start a chsc request on one of the existing chsc subchannels.

.. _`chsc_async.return`:

Return
------

\ ``0``\  if the request was performed synchronously
\ ``-EINPROGRESS``\  if the request was successfully started
\ ``-EBUSY``\  if all chsc subchannels are busy
\ ``-ENODEV``\  if no chsc subchannels are available

.. _`chsc_async.context`:

Context
-------

interrupts disabled, chsc_lock held

.. This file was automatic generated / don't edit.

