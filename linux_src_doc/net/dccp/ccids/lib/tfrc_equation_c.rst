.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ccids/lib/tfrc_equation.c

.. _`tfrc_calc_x`:

tfrc_calc_x
===========

.. c:function:: u32 tfrc_calc_x(u16 s, u32 R, u32 p)

    Calculate the send rate as per section 3.1 of RFC3448

    :param u16 s:
        packet size          in bytes

    :param u32 R:
        RTT                  scaled by 1000000   (i.e., microseconds)

    :param u32 p:
        loss ratio estimate  scaled by 1000000

.. _`tfrc_calc_x.description`:

Description
-----------

Returns X_calc           in bytes per second (not scaled).

.. _`tfrc_calc_x_reverse_lookup`:

tfrc_calc_x_reverse_lookup
==========================

.. c:function:: u32 tfrc_calc_x_reverse_lookup(u32 fvalue)

    try to find p given f(p)

    :param u32 fvalue:
        function value to match, scaled by 1000000

.. _`tfrc_calc_x_reverse_lookup.description`:

Description
-----------

Returns closest match for p, also scaled by 1000000

.. _`tfrc_invert_loss_event_rate`:

tfrc_invert_loss_event_rate
===========================

.. c:function:: u32 tfrc_invert_loss_event_rate(u32 loss_event_rate)

    Compute p so that 10^6 corresponds to 100% When \ ``loss_event_rate``\  is large, there is a chance that p is truncated to 0. To avoid re-entering slow-start in that case, we set p = TFRC_SMALLEST_P > 0.

    :param u32 loss_event_rate:
        *undescribed*

.. This file was automatic generated / don't edit.

