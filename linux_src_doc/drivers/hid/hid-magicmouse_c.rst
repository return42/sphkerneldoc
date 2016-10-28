.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/hid-magicmouse.c

.. _`magicmouse_sc`:

struct magicmouse_sc
====================

.. c:type:: struct magicmouse_sc

    Tracks Magic Mouse-specific data.

.. _`magicmouse_sc.definition`:

Definition
----------

.. code-block:: c

    struct magicmouse_sc {
        struct input_dev *input;
        unsigned long quirks;
        int ntouches;
        int scroll_accel;
        unsigned long scroll_jiffies;
        struct touches[16];
        int tracking_ids[16];
    }

.. _`magicmouse_sc.members`:

Members
-------

input
    Input device through which we report events.

quirks
    Currently unused.

ntouches
    Number of touches in most recent touch report.

scroll_accel
    Number of consecutive scroll motions.

scroll_jiffies
    Time of last scroll motion.

touches
    Most recent data for a touch, indexed by tracking ID.

tracking_ids
    Mapping of current touch input data to \ ``touches``\ .

.. This file was automatic generated / don't edit.

