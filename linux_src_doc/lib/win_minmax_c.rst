.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/win_minmax.c

.. _`minmax_subwin_update`:

minmax_subwin_update
====================

.. c:function:: u32 minmax_subwin_update(struct minmax *m, u32 win, const struct minmax_sample *val)

    windowed min/max tracker

    :param m:
        *undescribed*
    :type m: struct minmax \*

    :param win:
        *undescribed*
    :type win: u32

    :param val:
        *undescribed*
    :type val: const struct minmax_sample \*

.. _`minmax_subwin_update.description`:

Description
-----------

Kathleen Nichols' algorithm for tracking the minimum (or maximum)
value of a data stream over some fixed time interval.  (E.g.,
the minimum RTT over the past five minutes.) It uses constant
space and constant time per update yet almost always delivers
the same minimum as an implementation that has to keep all the
data in the window.

The algorithm keeps track of the best, 2nd best & 3rd best min
values, maintaining an invariant that the measurement time of
the n'th best >= n-1'th best. It also makes sure that the three
values are widely separated in the time window since that bounds
the worse case error when that data is monotonically increasing
over the window.

Upon getting a new min, we can forget everything earlier because
it has no value - the new min is <= everything else in the window
by definition and it's the most recent. So we restart fresh on
every new min and overwrites 2nd & 3rd choices. The same property
holds for 2nd & 3rd best.

.. This file was automatic generated / don't edit.

