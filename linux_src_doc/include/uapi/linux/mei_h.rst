.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/mei.h

.. _`set-and-unset-event-notification-for-a-connected-client`:

set and unset event notification for a connected client
=======================================================

The IOCTL argument is 1 for enabling event notification and 0 for
disabling the service
Return:  -EOPNOTSUPP if the devices doesn't support the feature

.. _`retrieve-notification`:

retrieve notification
=====================

The IOCTL output argument is 1 if an event was is pending and 0 otherwise
the ioctl has to be called in order to acknowledge pending event

Return:  -EOPNOTSUPP if the devices doesn't support the feature

.. This file was automatic generated / don't edit.

