.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/dvb/frontend.h

.. _`fe_status`:

enum fe_status
==============

.. c:type:: enum fe_status

    enumerates the possible frontend status

.. _`fe_status.definition`:

Definition
----------

.. code-block:: c

    enum fe_status {
        FE_HAS_SIGNAL,
        FE_HAS_CARRIER,
        FE_HAS_VITERBI,
        FE_HAS_SYNC,
        FE_HAS_LOCK,
        FE_TIMEDOUT,
        FE_REINIT
    };

.. _`fe_status.constants`:

Constants
---------

FE_HAS_SIGNAL
    found something above the noise level

FE_HAS_CARRIER
    found a DVB signal

FE_HAS_VITERBI
    FEC is stable

FE_HAS_SYNC
    found sync bytes

FE_HAS_LOCK
    everything's working

FE_TIMEDOUT
    no lock within the last ~2 seconds

FE_REINIT
    frontend was reinitialized, application is recommended
    to reset DiSEqC, tone and parameters

.. _`dtv_stats`:

struct dtv_stats
================

.. c:type:: struct dtv_stats

    Used for reading a DTV status property

.. _`dtv_stats.definition`:

Definition
----------

.. code-block:: c

    struct dtv_stats {
        __u8 scale;
        union {unnamed_union};
    }

.. _`dtv_stats.members`:

Members
-------

scale
    Filled with enum fecap_scale_params - the scale
    in usage for that parameter

{unnamed_union}
    anonymous


.. _`dtv_stats.description`:

Description
-----------

For most delivery systems, this will return a single value for each
parameter.
It should be noticed, however, that new OFDM delivery systems like
ISDB can use different modulation types for each group of carriers.
On such standards, up to 8 groups of statistics can be provided, one
for each carrier group (called "layer" on ISDB).
In order to be consistent with other delivery systems, the first
value refers to the entire set of carriers ("global").
dtv_status:scale should use the value FE_SCALE_NOT_AVAILABLE when
the value for the entire group of carriers or from one specific layer
is not provided by the hardware.
st.len should be filled with the latest filled status + 1.

In other words, for ISDB, those values should be filled like:
u.st.stat.svalue[0] = global statistics;
u.st.stat.scale[0] = FE_SCALE_DECIBEL;
u.st.stat.value[1] = layer A statistics;
u.st.stat.scale[1] = FE_SCALE_NOT_AVAILABLE (if not available);
u.st.stat.svalue[2] = layer B statistics;
u.st.stat.scale[2] = FE_SCALE_DECIBEL;
u.st.stat.svalue[3] = layer C statistics;
u.st.stat.scale[3] = FE_SCALE_DECIBEL;
u.st.len = 4;

.. _`fe_tune_mode_oneshot`:

FE_TUNE_MODE_ONESHOT
====================

.. c:function::  FE_TUNE_MODE_ONESHOT()

    behaviour. Additionally, there will be no automatic monitoring of the lock status, and hence no frontend events will be generated. If a frontend device is closed, this flag will be automatically turned off when the device is reopened read-write.

.. This file was automatic generated / don't edit.

