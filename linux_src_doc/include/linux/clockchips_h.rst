.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/clockchips.h

.. _`clock_event_device`:

struct clock_event_device
=========================

.. c:type:: struct clock_event_device

    clock event device descriptor

.. _`clock_event_device.definition`:

Definition
----------

.. code-block:: c

    struct clock_event_device {
        void (*event_handler)(struct clock_event_device *);
        int (*set_next_event)(unsigned long evt, struct clock_event_device *);
        int (*set_next_ktime)(ktime_t expires, struct clock_event_device *);
        ktime_t next_event;
        u64 max_delta_ns;
        u64 min_delta_ns;
        u32 mult;
        u32 shift;
        enum clock_event_state state_use_accessors;
        unsigned int features;
        unsigned long retries;
        int (*set_state_periodic)(struct clock_event_device *);
        int (*set_state_oneshot)(struct clock_event_device *);
        int (*set_state_oneshot_stopped)(struct clock_event_device *);
        int (*set_state_shutdown)(struct clock_event_device *);
        int (*tick_resume)(struct clock_event_device *);
        void (*broadcast)(const struct cpumask *mask);
        void (*suspend)(struct clock_event_device *);
        void (*resume)(struct clock_event_device *);
        unsigned long min_delta_ticks;
        unsigned long max_delta_ticks;
        const char *name;
        int rating;
        int irq;
        int bound_on;
        const struct cpumask *cpumask;
        struct list_head list;
        struct module *owner;
    }

.. _`clock_event_device.members`:

Members
-------

event_handler
    Assigned by the framework to be called by the low
    level handler of the event source

set_next_event
    set next event function using a clocksource delta

set_next_ktime
    set next event function using a direct ktime value

next_event
    local storage for the next event in oneshot mode

max_delta_ns
    maximum delta value in ns

min_delta_ns
    minimum delta value in ns

mult
    nanosecond to cycles multiplier

shift
    nanoseconds to cycles divisor (power of two)

state_use_accessors
    current state of the device, assigned by the core code

features
    features

retries
    number of forced programming retries

set_state_periodic
    switch state to periodic

set_state_oneshot
    switch state to oneshot

set_state_oneshot_stopped
    switch state to oneshot_stopped

set_state_shutdown
    switch state to shutdown

tick_resume
    resume clkevt device

broadcast
    function to broadcast events

suspend
    *undescribed*

resume
    *undescribed*

min_delta_ticks
    minimum delta value in ticks stored for reconfiguration

max_delta_ticks
    maximum delta value in ticks stored for reconfiguration

name
    ptr to clock event name

rating
    variable to rate clock event devices

irq
    IRQ number (only for non CPU local devices)

bound_on
    Bound on CPU

cpumask
    cpumask to indicate for which CPUs this device works

list
    list head for the management code

owner
    module reference

.. This file was automatic generated / don't edit.

