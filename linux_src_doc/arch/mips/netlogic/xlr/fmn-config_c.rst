.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/netlogic/xlr/fmn-config.c

.. _`setup_fmn_cc`:

setup_fmn_cc
============

.. c:function:: void setup_fmn_cc(struct xlr_fmn_info *dev_info, int start_stn_id, int end_stn_id, int num_buckets, int cpu_credits, int size)

    the buckets for the device. This size is distributed among all the CPUs so that all of them can send messages to the device.

    :param dev_info:
        FMN information structure for each devices
    :type dev_info: struct xlr_fmn_info \*

    :param start_stn_id:
        Starting station id of dev_info
    :type start_stn_id: int

    :param end_stn_id:
        End station id of dev_info
    :type end_stn_id: int

    :param num_buckets:
        Total number of buckets for den_info
    :type num_buckets: int

    :param cpu_credits:
        Allowed credits to cpu for each devices pointing by dev_info
    :type cpu_credits: int

    :param size:
        Size of the each buckets in the device station
    :type size: int

.. _`setup_fmn_cc.description`:

Description
-----------

The device is also given 'cpu_credits' to send messages to the CPUs

.. _`xlr_board_info_setup`:

xlr_board_info_setup
====================

.. c:function:: void xlr_board_info_setup( void)

    in each variant of XLR/XLS processor

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

