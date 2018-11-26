.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_intr.c

.. _`qib_format_hwmsg`:

qib_format_hwmsg
================

.. c:function:: void qib_format_hwmsg(char *msg, size_t msgl, const char *hwmsg)

    format a single hwerror message \ ``msg``\  message buffer \ ``msgl``\  length of message buffer \ ``hwmsg``\  message to add to message buffer

    :param msg:
        *undescribed*
    :type msg: char \*

    :param msgl:
        *undescribed*
    :type msgl: size_t

    :param hwmsg:
        *undescribed*
    :type hwmsg: const char \*

.. _`qib_format_hwerrors`:

qib_format_hwerrors
===================

.. c:function:: void qib_format_hwerrors(u64 hwerrs, const struct qib_hwerror_msgs *hwerrmsgs, size_t nhwerrmsgs, char *msg, size_t msgl)

    format hardware error messages for display \ ``hwerrs``\  hardware errors bit vector \ ``hwerrmsgs``\  hardware error descriptions \ ``nhwerrmsgs``\  number of hwerrmsgs \ ``msg``\  message buffer \ ``msgl``\  message buffer length

    :param hwerrs:
        *undescribed*
    :type hwerrs: u64

    :param hwerrmsgs:
        *undescribed*
    :type hwerrmsgs: const struct qib_hwerror_msgs \*

    :param nhwerrmsgs:
        *undescribed*
    :type nhwerrmsgs: size_t

    :param msg:
        *undescribed*
    :type msg: char \*

    :param msgl:
        *undescribed*
    :type msgl: size_t

.. This file was automatic generated / don't edit.

