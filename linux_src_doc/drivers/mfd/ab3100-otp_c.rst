.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/ab3100-otp.c

.. _`ab3100_otp`:

struct ab3100_otp
=================

.. c:type:: struct ab3100_otp

    \ ``dev``\  containing device \ ``locked``\  whether the OTP is locked, after locking, no more bits can be changed but before locking it is still possible to change bits from 1->0. \ ``freq``\  clocking frequency for the OTP, this frequency is either 32768Hz or 1MHz/30 \ ``paf``\  product activation flag, indicates whether this is a real product (paf true) or a lab board etc (paf false) \ ``imeich``\  if this is set it is possible to override the IMEI number found in the tac, fac and svn fields with (secured) software \ ``cid``\  customer ID \ ``tac``\  type allocation code of the IMEI \ ``fac``\  final assembly code of the IMEI \ ``svn``\  software version number of the IMEI \ ``debugfs``\  a debugfs file used when dumping to file

.. _`ab3100_otp.definition`:

Definition
----------

.. code-block:: c

    struct ab3100_otp {
        struct device *dev;
        bool locked;
        u32 freq;
        bool paf;
        bool imeich;
        u16 cid:14;
        u32 tac:20;
        u8 fac;
        u32 svn:20;
        struct dentry *debugfs;
    }

.. _`ab3100_otp.members`:

Members
-------

dev
    *undescribed*

locked
    *undescribed*

freq
    *undescribed*

paf
    *undescribed*

imeich
    *undescribed*

cid
    *undescribed*

tac
    *undescribed*

fac
    *undescribed*

svn
    *undescribed*

debugfs
    *undescribed*

.. This file was automatic generated / don't edit.

