.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/mad.h

.. _`get_link_speed`:

get_link_speed
==============

.. c:function:: u16 get_link_speed(u16 link_speed)

    determine whether 12.5G or 25G speed

    :param u16 link_speed:
        the speed of active link

.. _`get_link_speed.description`:

Description
-----------

The function indirectly calculate required link speed
value for convert_xmit_counter function. If the link
speed is 25G, the function return as 1 as it is required
by xmit counter conversion formula :-( 25G / link_speed).
This conversion will provide value 1 if current
link speed is 25G or 2 if 12.5G.This is done to avoid
12.5 float number conversion.

.. _`convert_xmit_counter`:

convert_xmit_counter
====================

.. c:function:: u64 convert_xmit_counter(u64 xmit_wait_val, u16 link_width, u16 link_speed)

    calculate flit times for given xmit counter value

    :param u64 xmit_wait_val:
        current xmit counter value

    :param u16 link_width:
        width of active link

    :param u16 link_speed:
        speed of active link

.. This file was automatic generated / don't edit.

