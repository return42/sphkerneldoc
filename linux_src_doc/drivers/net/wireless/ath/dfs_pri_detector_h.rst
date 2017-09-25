.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/dfs_pri_detector.h

.. _`pri_sequence`:

struct pri_sequence
===================

.. c:type:: struct pri_sequence

    sequence of pulses matching one PRI

.. _`pri_sequence.definition`:

Definition
----------

.. code-block:: c

    struct pri_sequence {
        struct list_head head;
        u32 pri;
        u32 dur;
        u32 count;
        u32 count_falses;
        u64 first_ts;
        u64 last_ts;
        u64 deadline_ts;
    }

.. _`pri_sequence.members`:

Members
-------

head
    list_head

pri
    pulse repetition interval (PRI) in usecs

dur
    duration of sequence in usecs

count
    number of pulses in this sequence

count_falses
    number of not matching pulses in this sequence

first_ts
    time stamp of first pulse in usecs

last_ts
    time stamp of last pulse in usecs

deadline_ts
    deadline when this sequence becomes invalid (first_ts + dur)

.. _`pri_detector`:

struct pri_detector
===================

.. c:type:: struct pri_detector

    PRI detector element for a dedicated radar type

.. _`pri_detector.definition`:

Definition
----------

.. code-block:: c

    struct pri_detector {
        void (*exit) (struct pri_detector *de);
        struct pri_sequence * (*add_pulse)(struct pri_detector *de, struct pulse_event *e);
        void (*reset) (struct pri_detector *de, u64 ts);
        const struct radar_detector_specs *rs;
        u64 last_ts;
        struct list_head sequences;
        struct list_head pulses;
        u32 count;
        u32 max_count;
        u32 window_size;
    }

.. _`pri_detector.members`:

Members
-------

exit
    destructor

add_pulse
    add pulse event, returns pri_sequence if pattern was detected

reset
    clear states and reset to given time stamp

rs
    detector specs for this detector element

last_ts
    last pulse time stamp considered for this element in usecs

sequences
    list_head holding potential pulse sequences

pulses
    list connecting pulse_elem objects

count
    number of pulses in queue

max_count
    maximum number of pulses to be queued

window_size
    window size back from newest pulse time stamp in usecs

.. This file was automatic generated / don't edit.

