.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/tcp_lp.c

.. _`tcp_lp_state`:

enum tcp_lp_state
=================

.. c:type:: enum tcp_lp_state


.. _`tcp_lp_state.definition`:

Definition
----------

.. code-block:: c

    enum tcp_lp_state {
        LP_VALID_RHZ,
        LP_VALID_OWD,
        LP_WITHIN_THR,
        LP_WITHIN_INF
    };

.. _`tcp_lp_state.constants`:

Constants
---------

LP_VALID_RHZ
    is remote HZ valid?

LP_VALID_OWD
    is OWD valid?

LP_WITHIN_THR
    are we within threshold?

LP_WITHIN_INF
    are we within inference?

.. _`tcp_lp_state.description`:

Description
-----------

TCP-LP's state flags.
We create this set of state flag mainly for debugging.

.. _`lp`:

struct lp
=========

.. c:type:: struct lp


.. _`lp.definition`:

Definition
----------

.. code-block:: c

    struct lp {
        u32 flag;
        u32 sowd;
        u32 owd_min;
        u32 owd_max;
        u32 owd_max_rsv;
        u32 remote_hz;
        u32 remote_ref_time;
        u32 local_ref_time;
        u32 last_drop;
        u32 inference;
    }

.. _`lp.members`:

Members
-------

flag
    TCP-LP state flag

sowd
    smoothed OWD << 3

owd_min
    min OWD

owd_max
    max OWD

owd_max_rsv
    resrved max owd

remote_hz
    estimated remote HZ

remote_ref_time
    remote reference time

local_ref_time
    local reference time

last_drop
    time for last active drop

inference
    current inference

.. _`lp.description`:

Description
-----------

TCP-LP's private struct.
We get the idea from original TCP-LP implementation where only left those we
found are really useful.

.. _`tcp_lp_init`:

tcp_lp_init
===========

.. c:function:: void tcp_lp_init(struct sock *sk)

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`tcp_lp_init.description`:

Description
-----------

Init all required variables.
Clone the handling from Vegas module implementation.

.. _`tcp_lp_cong_avoid`:

tcp_lp_cong_avoid
=================

.. c:function:: void tcp_lp_cong_avoid(struct sock *sk, u32 ack, u32 acked)

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param ack:
        *undescribed*
    :type ack: u32

    :param acked:
        *undescribed*
    :type acked: u32

.. _`tcp_lp_cong_avoid.description`:

Description
-----------

Implementation of cong_avoid.
Will only call newReno CA when away from inference.
From TCP-LP's paper, this will be handled in additive increasement.

.. _`tcp_lp_remote_hz_estimator`:

tcp_lp_remote_hz_estimator
==========================

.. c:function:: u32 tcp_lp_remote_hz_estimator(struct sock *sk)

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`tcp_lp_remote_hz_estimator.description`:

Description
-----------

Estimate remote HZ.
We keep on updating the estimated value, where original TCP-LP
implementation only guest it for once and use forever.

.. _`tcp_lp_owd_calculator`:

tcp_lp_owd_calculator
=====================

.. c:function:: u32 tcp_lp_owd_calculator(struct sock *sk)

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`tcp_lp_owd_calculator.description`:

Description
-----------

Calculate one way delay (in relative format).
Original implement OWD as minus of remote time difference to local time
difference directly. As this time difference just simply equal to RTT, when
the network status is stable, remote RTT will equal to local RTT, and result
OWD into zero.
It seems to be a bug and so we fixed it.

.. _`tcp_lp_rtt_sample`:

tcp_lp_rtt_sample
=================

.. c:function:: void tcp_lp_rtt_sample(struct sock *sk, u32 rtt)

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param rtt:
        *undescribed*
    :type rtt: u32

.. _`tcp_lp_rtt_sample.description`:

Description
-----------

Implementation or rtt_sample.
Will take the following action,
1. calc OWD,
2. record the min/max OWD,
3. calc smoothed OWD (SOWD).
Most ideas come from the original TCP-LP implementation.

.. _`tcp_lp_pkts_acked`:

tcp_lp_pkts_acked
=================

.. c:function:: void tcp_lp_pkts_acked(struct sock *sk, const struct ack_sample *sample)

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param sample:
        *undescribed*
    :type sample: const struct ack_sample \*

.. _`tcp_lp_pkts_acked.description`:

Description
-----------

Implementation of pkts_acked.
Deal with active drop under Early Congestion Indication.
Only drop to half and 1 will be handle, because we hope to use back
newReno in increase case.
We work it out by following the idea from TCP-LP's paper directly

.. This file was automatic generated / don't edit.

