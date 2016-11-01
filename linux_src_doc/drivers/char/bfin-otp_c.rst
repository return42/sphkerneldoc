.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/bfin-otp.c

.. _`bfin_otp_read`:

bfin_otp_read
=============

.. c:function:: ssize_t bfin_otp_read(struct file *file, char __user *buff, size_t count, loff_t *pos)

    Read OTP pages

    :param struct file \*file:
        *undescribed*

    :param char __user \*buff:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param loff_t \*pos:
        *undescribed*

.. _`bfin_otp_read.description`:

Description
-----------

All reads must be in half page chunks (half page == 64 bits).

.. _`bfin_otp_init_timing`:

bfin_otp_init_timing
====================

.. c:function:: u32 bfin_otp_init_timing( void)

    setup OTP timing parameters

    :param  void:
        no arguments

.. _`bfin_otp_init_timing.description`:

Description
-----------

Required before doing any write operation.  Algorithms from HRM.

.. _`bfin_otp_deinit_timing`:

bfin_otp_deinit_timing
======================

.. c:function:: void bfin_otp_deinit_timing(u32 timing)

    set timings to only allow reads

    :param u32 timing:
        *undescribed*

.. _`bfin_otp_deinit_timing.description`:

Description
-----------

Should be called after all writes are done.

.. _`bfin_otp_write`:

bfin_otp_write
==============

.. c:function:: ssize_t bfin_otp_write(struct file *filp, const char __user *buff, size_t count, loff_t *pos)

    write OTP pages

    :param struct file \*filp:
        *undescribed*

    :param const char __user \*buff:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param loff_t \*pos:
        *undescribed*

.. _`bfin_otp_write.description`:

Description
-----------

All writes must be in half page chunks (half page == 64 bits).

.. This file was automatic generated / don't edit.

