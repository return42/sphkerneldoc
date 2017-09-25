.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/css.h

.. _`css_driver`:

struct css_driver
=================

.. c:type:: struct css_driver

    device driver for subchannels

.. _`css_driver.definition`:

Definition
----------

.. code-block:: c

    struct css_driver {
        struct css_device_id *subchannel_type;
        struct device_driver drv;
        void (*irq)(struct subchannel *);
        int (*chp_event)(struct subchannel *, struct chp_link *, int);
        int (*sch_event)(struct subchannel *, int);
        int (*probe)(struct subchannel *);
        int (*remove)(struct subchannel *);
        void (*shutdown)(struct subchannel *);
        int (*prepare) (struct subchannel *);
        void (*complete) (struct subchannel *);
        int (*freeze)(struct subchannel *);
        int (*thaw) (struct subchannel *);
        int (*restore)(struct subchannel *);
        int (*settle)(void);
    }

.. _`css_driver.members`:

Members
-------

subchannel_type
    subchannel type supported by this driver

drv
    embedded device driver structure

irq
    called on interrupts

chp_event
    called for events affecting a channel path

sch_event
    called for events affecting the subchannel

probe
    function called on probe

remove
    function called on remove

shutdown
    called at device shutdown

prepare
    prepare for pm state transition

complete
    undo work done in \ ``prepare``\ 

freeze
    callback for freezing during hibernation snapshotting

thaw
    undo work done in \ ``freeze``\ 

restore
    callback for restoring after hibernation

settle
    wait for asynchronous work to finish

.. This file was automatic generated / don't edit.

