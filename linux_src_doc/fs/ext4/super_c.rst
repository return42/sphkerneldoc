.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/super.c

.. _`ext4_get_stripe_size`:

ext4_get_stripe_size
====================

.. c:function:: unsigned long ext4_get_stripe_size(struct ext4_sb_info *sbi)

    Get the stripe size.

    :param sbi:
        In memory super block info
    :type sbi: struct ext4_sb_info \*

.. _`ext4_get_stripe_size.description`:

Description
-----------

If we have specified it via mount option, then
use the mount option value. If the value specified at mount time is
greater than the blocks per group use the super block value.
If the super block value is greater than blocks per group return 0.
Allocator needs it be less than blocks per group.

.. This file was automatic generated / don't edit.

