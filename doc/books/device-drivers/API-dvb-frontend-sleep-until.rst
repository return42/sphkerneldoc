
.. _API-dvb-frontend-sleep-until:

========================
dvb_frontend_sleep_until
========================

*man dvb_frontend_sleep_until(9)*

*4.6.0-rc1*

Sleep for the amount of time given by add_usec parameter


Synopsis
========

.. c:function:: void dvb_frontend_sleep_until( ktime_t * waketime, u32 add_usec )

Arguments
=========

``waketime``
    pointer to a struct ktime_t

``add_usec``
    time to sleep, in microseconds


Description
===========

This function is used to measure the time required for the ``FE_DISHNETWORK_SEND_LEGACY_CMD`` ioctl to work. It needs to be as precise as possible, as it affects the detection of
the dish tone command at the satellite subsystem.

Its used internally by the DVB frontend core, in order to emulate ``FE_DISHNETWORK_SEND_LEGACY_CMD`` using the ``dvb_frontend_ops``.\ ``set_voltage`` callback.


NOTE
====

it should not be used at the drivers, as the emulation for the legacy callback is provided by the Kernel. The only situation where this should be at the drivers is when there are
some bugs at the hardware that would prevent the core emulation to work. On such cases, the driver would be writing a ``dvb_frontend_ops``.\ ``dishnetwork_send_legacy_command`` and
calling this function directly.
