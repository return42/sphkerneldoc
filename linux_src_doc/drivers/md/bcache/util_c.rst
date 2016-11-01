.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/bcache/util.c

.. _`bch_next_delay`:

bch_next_delay
==============

.. c:function:: uint64_t bch_next_delay(struct bch_ratelimit *d, uint64_t done)

    increment \ ``d``\  by the amount of work done, and return how long to delay until the next time to do some work.

    :param struct bch_ratelimit \*d:
        *undescribed*

    :param uint64_t done:
        *undescribed*

.. _`bch_next_delay.description`:

Description
-----------

@d - the struct bch_ratelimit to update
\ ``done``\  - the amount of work done, in arbitrary units

Returns the amount of time to delay by, in jiffies

.. This file was automatic generated / don't edit.

