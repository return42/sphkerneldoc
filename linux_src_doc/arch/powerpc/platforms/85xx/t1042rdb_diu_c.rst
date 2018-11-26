.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/85xx/t1042rdb_diu.c

.. _`t1042rdb_set_monitor_port`:

t1042rdb_set_monitor_port
=========================

.. c:function:: void t1042rdb_set_monitor_port(enum fsl_diu_monitor_port port)

    switch the output to a different monitor port

    :param port:
        *undescribed*
    :type port: enum fsl_diu_monitor_port

.. _`t1042rdb_set_pixel_clock`:

t1042rdb_set_pixel_clock
========================

.. c:function:: void t1042rdb_set_pixel_clock(unsigned int pixclock)

    program the DIU's clock

    :param pixclock:
        pixel clock in ps (pico seconds)
    :type pixclock: unsigned int

.. _`t1042rdb_valid_monitor_port`:

t1042rdb_valid_monitor_port
===========================

.. c:function:: enum fsl_diu_monitor_port t1042rdb_valid_monitor_port(enum fsl_diu_monitor_port port)

    set the monitor port for sysfs

    :param port:
        *undescribed*
    :type port: enum fsl_diu_monitor_port

.. This file was automatic generated / don't edit.

