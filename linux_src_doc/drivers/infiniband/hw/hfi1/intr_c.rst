.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/intr.c

.. _`format_hwmsg`:

format_hwmsg
============

.. c:function:: void format_hwmsg(char *msg, size_t msgl, const char *hwmsg)

    format a single hwerror message \ ``msg``\  message buffer \ ``msgl``\  length of message buffer \ ``hwmsg``\  message to add to message buffer

    :param char \*msg:
        *undescribed*

    :param size_t msgl:
        *undescribed*

    :param const char \*hwmsg:
        *undescribed*

.. _`hfi1_format_hwerrors`:

hfi1_format_hwerrors
====================

.. c:function:: void hfi1_format_hwerrors(u64 hwerrs, const struct hfi1_hwerror_msgs *hwerrmsgs, size_t nhwerrmsgs, char *msg, size_t msgl)

    format hardware error messages for display \ ``hwerrs``\  hardware errors bit vector \ ``hwerrmsgs``\  hardware error descriptions \ ``nhwerrmsgs``\  number of hwerrmsgs \ ``msg``\  message buffer \ ``msgl``\  message buffer length

    :param u64 hwerrs:
        *undescribed*

    :param const struct hfi1_hwerror_msgs \*hwerrmsgs:
        *undescribed*

    :param size_t nhwerrmsgs:
        *undescribed*

    :param char \*msg:
        *undescribed*

    :param size_t msgl:
        *undescribed*

.. This file was automatic generated / don't edit.

