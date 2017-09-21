.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ptp_clock_kernel.h

.. _`ptp_clock_info`:

struct ptp_clock_info
=====================

.. c:type:: struct ptp_clock_info

    decribes a PTP hardware clock

.. _`ptp_clock_info.definition`:

Definition
----------

.. code-block:: c

    struct ptp_clock_info {
        struct module *owner;
        char name;
        s32 max_adj;
        int n_alarm;
        int n_ext_ts;
        int n_per_out;
        int n_pins;
        int pps;
        struct ptp_pin_desc *pin_config;
        int (*adjfine)(struct ptp_clock_info *ptp, long scaled_ppm);
        int (*adjfreq)(struct ptp_clock_info *ptp, s32 delta);
        int (*adjtime)(struct ptp_clock_info *ptp, s64 delta);
        int (*gettime64)(struct ptp_clock_info *ptp, struct timespec64 *ts);
        int (*getcrosststamp)(struct ptp_clock_info *ptp, struct system_device_crosststamp *cts);
        int (*settime64)(struct ptp_clock_info *p, const struct timespec64 *ts);
        int (*enable)(struct ptp_clock_info *ptp, struct ptp_clock_request *request, int on);
        int (*verify)(struct ptp_clock_info *ptp, unsigned int pin, enum ptp_pin_function func, unsigned int chan);
        long (*do_aux_work)(struct ptp_clock_info *ptp);
    }

.. _`ptp_clock_info.members`:

Members
-------

owner
    The clock driver should set to THIS_MODULE.

name
    A short "friendly name" to identify the clock and to
    help distinguish PHY based devices from MAC based ones.
    The string is not meant to be a unique id.

max_adj
    The maximum possible frequency adjustment, in parts per billon.

n_alarm
    The number of programmable alarms.

n_ext_ts
    The number of external time stamp channels.

n_per_out
    The number of programmable periodic signals.

n_pins
    The number of programmable pins.

pps
    Indicates whether the clock supports a PPS callback.

pin_config
    Array of length 'n_pins'. If the number of
    programmable pins is nonzero, then drivers must
    allocate and initialize this array.

adjfine
    Adjusts the frequency of the hardware clock.
    parameter scaled_ppm: Desired frequency offset from
    nominal frequency in parts per million, but with a
    16 bit binary fractional field.

adjfreq
    Adjusts the frequency of the hardware clock.
    This method is deprecated.  New drivers should implement
    the \ ``adjfine``\  method instead.
    parameter delta: Desired frequency offset from nominal frequency
    in parts per billion

adjtime
    Shifts the time of the hardware clock.
    parameter delta: Desired change in nanoseconds.

gettime64
    Reads the current time from the hardware clock.
    parameter ts: Holds the result.

getcrosststamp
    Reads the current time from the hardware clock and
    system clock simultaneously.
    parameter cts: Contains timestamp (device,system) pair,
    where system time is realtime and monotonic.

settime64
    Set the current time on the hardware clock.
    parameter ts: Time value to set.

enable
    Request driver to enable or disable an ancillary feature.
    parameter request: Desired resource to enable or disable.
    parameter on: Caller passes one to enable or zero to disable.

verify
    Confirm that a pin can perform a given function. The PTP
    Hardware Clock subsystem maintains the 'pin_config'
    array on behalf of the drivers, but the PHC subsystem
    assumes that every pin can perform every function. This
    hook gives drivers a way of telling the core about
    limitations on specific pins. This function must return
    zero if the function can be assigned to this pin, and
    nonzero otherwise.
    parameter pin: index of the pin in question.
    parameter func: the desired function to use.
    parameter chan: the function channel index to use.

do_aux_work
    *undescribed*

.. _`ptp_clock_info.description`:

Description
-----------

clock operations

Drivers should embed their ptp_clock_info within a private
structure, obtaining a reference to it using \ :c:func:`container_of`\ .

The callbacks must all return zero on success, non-zero otherwise.

.. _`ptp_clock_event`:

struct ptp_clock_event
======================

.. c:type:: struct ptp_clock_event

    decribes a PTP hardware clock event

.. _`ptp_clock_event.definition`:

Definition
----------

.. code-block:: c

    struct ptp_clock_event {
        int type;
        int index;
        union {unnamed_union};
    }

.. _`ptp_clock_event.members`:

Members
-------

type
    One of the ptp_clock_events enumeration values.

index
    Identifies the source of the event.

{unnamed_union}
    anonymous


.. _`ptp_clock_register`:

ptp_clock_register
==================

.. c:function:: struct ptp_clock *ptp_clock_register(struct ptp_clock_info *info, struct device *parent)

    register a PTP hardware clock driver

    :param struct ptp_clock_info \*info:
        Structure describing the new clock.

    :param struct device \*parent:
        Pointer to the parent device of the new clock.

.. _`ptp_clock_register.description`:

Description
-----------

Returns a valid pointer on success or PTR_ERR on failure.  If PHC
support is missing at the configuration level, this function
returns NULL, and drivers are expected to gracefully handle that
case separately.

.. _`ptp_clock_unregister`:

ptp_clock_unregister
====================

.. c:function:: int ptp_clock_unregister(struct ptp_clock *ptp)

    unregister a PTP hardware clock driver

    :param struct ptp_clock \*ptp:
        The clock to remove from service.

.. _`ptp_clock_event`:

ptp_clock_event
===============

.. c:function:: void ptp_clock_event(struct ptp_clock *ptp, struct ptp_clock_event *event)

    notify the PTP layer about an event

    :param struct ptp_clock \*ptp:
        The clock obtained from \ :c:func:`ptp_clock_register`\ .

    :param struct ptp_clock_event \*event:
        Message structure describing the event.

.. _`ptp_clock_index`:

ptp_clock_index
===============

.. c:function:: int ptp_clock_index(struct ptp_clock *ptp)

    obtain the device index of a PTP clock

    :param struct ptp_clock \*ptp:
        The clock obtained from \ :c:func:`ptp_clock_register`\ .

.. _`ptp_find_pin`:

ptp_find_pin
============

.. c:function:: int ptp_find_pin(struct ptp_clock *ptp, enum ptp_pin_function func, unsigned int chan)

    obtain the pin index of a given auxiliary function

    :param struct ptp_clock \*ptp:
        The clock obtained from \ :c:func:`ptp_clock_register`\ .

    :param enum ptp_pin_function func:
        One of the ptp_pin_function enumerated values.

    :param unsigned int chan:
        The particular functional channel to find.

.. _`ptp_find_pin.return`:

Return
------

Pin index in the range of zero to ptp_clock_caps.n_pins - 1,
or -1 if the auxiliary function cannot be found.

.. _`ptp_schedule_worker`:

ptp_schedule_worker
===================

.. c:function:: int ptp_schedule_worker(struct ptp_clock *ptp, unsigned long delay)

    schedule ptp auxiliary work

    :param struct ptp_clock \*ptp:
        The clock obtained from \ :c:func:`ptp_clock_register`\ .

    :param unsigned long delay:
        number of jiffies to wait before queuing
        See \ :c:func:`kthread_queue_delayed_work`\  for more info.

.. This file was automatic generated / don't edit.

