.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/supply/ab8500_btemp.c

.. _`ab8500_btemp_interrupts`:

struct ab8500_btemp_interrupts
==============================

.. c:type:: struct ab8500_btemp_interrupts

    ab8500 interrupts

.. _`ab8500_btemp_interrupts.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_btemp_interrupts {
        char *name;
        irqreturn_t (*isr)(int irq, void *data);
    }

.. _`ab8500_btemp_interrupts.members`:

Members
-------

name
    name of the interrupt
    \ ``isr``\          function pointer to the isr

isr
    *undescribed*

.. _`ab8500_btemp`:

struct ab8500_btemp
===================

.. c:type:: struct ab8500_btemp

    ab8500 BTEMP device information

.. _`ab8500_btemp.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_btemp {
        struct device *dev;
        struct list_head node;
        int curr_source;
        int bat_temp;
        int prev_bat_temp;
        struct ab8500 *parent;
        struct ab8500_gpadc *gpadc;
        struct ab8500_fg *fg;
        struct abx500_bm_data *bm;
        struct power_supply *btemp_psy;
        struct ab8500_btemp_events events;
        struct ab8500_btemp_ranges btemp_ranges;
        struct workqueue_struct *btemp_wq;
        struct delayed_work btemp_periodic_work;
        bool initialized;
    }

.. _`ab8500_btemp.members`:

Members
-------

dev
    Pointer to the structure device

node
    List of AB8500 BTEMPs, hence prepared for reentrance

curr_source
    What current source we use, in uA

bat_temp
    Dispatched battery temperature in degree Celsius
    \ ``prev_bat_temp``\        Last measured battery temperature in degree Celsius

prev_bat_temp
    *undescribed*

parent
    Pointer to the struct ab8500

gpadc
    Pointer to the struct gpadc

fg
    Pointer to the struct fg

bm
    Platform specific battery management information

btemp_psy
    Structure for BTEMP specific battery properties

events
    Structure for information about events triggered

btemp_ranges
    Battery temperature range structure

btemp_wq
    Work queue for measuring the temperature periodically

btemp_periodic_work
    Work for measuring the temperature periodically

initialized
    True if battery id read.

.. _`ab8500_btemp_get`:

ab8500_btemp_get
================

.. c:function:: struct ab8500_btemp *ab8500_btemp_get( void)

    returns a reference to the primary AB8500 BTEMP (i.e. the first BTEMP in the instance list)

    :param void:
        no arguments
    :type void: 

.. _`ab8500_btemp_batctrl_volt_to_res`:

ab8500_btemp_batctrl_volt_to_res
================================

.. c:function:: int ab8500_btemp_batctrl_volt_to_res(struct ab8500_btemp *di, int v_batctrl, int inst_curr)

    convert batctrl voltage to resistance

    :param di:
        pointer to the ab8500_btemp structure
    :type di: struct ab8500_btemp \*

    :param v_batctrl:
        measured batctrl voltage
    :type v_batctrl: int

    :param inst_curr:
        measured instant current
    :type inst_curr: int

.. _`ab8500_btemp_batctrl_volt_to_res.description`:

Description
-----------

This function returns the battery resistance that is
derived from the BATCTRL voltage.
Returns value in Ohms.

.. _`ab8500_btemp_read_batctrl_voltage`:

ab8500_btemp_read_batctrl_voltage
=================================

.. c:function:: int ab8500_btemp_read_batctrl_voltage(struct ab8500_btemp *di)

    measure batctrl voltage

    :param di:
        pointer to the ab8500_btemp structure
    :type di: struct ab8500_btemp \*

.. _`ab8500_btemp_read_batctrl_voltage.description`:

Description
-----------

This function returns the voltage on BATCTRL. Returns value in mV.

.. _`ab8500_btemp_curr_source_enable`:

ab8500_btemp_curr_source_enable
===============================

.. c:function:: int ab8500_btemp_curr_source_enable(struct ab8500_btemp *di, bool enable)

    enable/disable batctrl current source

    :param di:
        pointer to the ab8500_btemp structure
    :type di: struct ab8500_btemp \*

    :param enable:
        enable or disable the current source
    :type enable: bool

.. _`ab8500_btemp_curr_source_enable.description`:

Description
-----------

Enable or disable the current sources for the BatCtrl AD channel

.. _`ab8500_btemp_get_batctrl_res`:

ab8500_btemp_get_batctrl_res
============================

.. c:function:: int ab8500_btemp_get_batctrl_res(struct ab8500_btemp *di)

    get battery resistance

    :param di:
        pointer to the ab8500_btemp structure
    :type di: struct ab8500_btemp \*

.. _`ab8500_btemp_get_batctrl_res.description`:

Description
-----------

This function returns the battery pack identification resistance.
Returns value in Ohms.

.. _`ab8500_btemp_res_to_temp`:

ab8500_btemp_res_to_temp
========================

.. c:function:: int ab8500_btemp_res_to_temp(struct ab8500_btemp *di, const struct abx500_res_to_temp *tbl, int tbl_size, int res)

    resistance to temperature

    :param di:
        pointer to the ab8500_btemp structure
    :type di: struct ab8500_btemp \*

    :param tbl:
        pointer to the resiatance to temperature table
    :type tbl: const struct abx500_res_to_temp \*

    :param tbl_size:
        size of the resistance to temperature table
    :type tbl_size: int

    :param res:
        resistance to calculate the temperature from
    :type res: int

.. _`ab8500_btemp_res_to_temp.description`:

Description
-----------

This function returns the battery temperature in degrees Celsius
based on the NTC resistance.

.. _`ab8500_btemp_measure_temp`:

ab8500_btemp_measure_temp
=========================

.. c:function:: int ab8500_btemp_measure_temp(struct ab8500_btemp *di)

    measure battery temperature

    :param di:
        pointer to the ab8500_btemp structure
    :type di: struct ab8500_btemp \*

.. _`ab8500_btemp_measure_temp.description`:

Description
-----------

Returns battery temperature (on success) else the previous temperature

.. _`ab8500_btemp_id`:

ab8500_btemp_id
===============

.. c:function:: int ab8500_btemp_id(struct ab8500_btemp *di)

    Identify the connected battery

    :param di:
        pointer to the ab8500_btemp structure
    :type di: struct ab8500_btemp \*

.. _`ab8500_btemp_id.description`:

Description
-----------

This function will try to identify the battery by reading the ID
resistor. Some brands use a combined ID resistor with a NTC resistor to
both be able to identify and to read the temperature of it.

.. _`ab8500_btemp_periodic_work`:

ab8500_btemp_periodic_work
==========================

.. c:function:: void ab8500_btemp_periodic_work(struct work_struct *work)

    Measuring the temperature periodically

    :param work:
        pointer to the work_struct structure
    :type work: struct work_struct \*

.. _`ab8500_btemp_periodic_work.description`:

Description
-----------

Work function for measuring the temperature periodically

.. _`ab8500_btemp_batctrlindb_handler`:

ab8500_btemp_batctrlindb_handler
================================

.. c:function:: irqreturn_t ab8500_btemp_batctrlindb_handler(int irq, void *_di)

    battery removal detected

    :param irq:
        interrupt number
    :type irq: int

    :param _di:
        void pointer that has to address of ab8500_btemp
    :type _di: void \*

.. _`ab8500_btemp_batctrlindb_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_btemp_templow_handler`:

ab8500_btemp_templow_handler
============================

.. c:function:: irqreturn_t ab8500_btemp_templow_handler(int irq, void *_di)

    battery temp lower than 10 degrees

    :param irq:
        interrupt number
    :type irq: int

    :param _di:
        void pointer that has to address of ab8500_btemp
    :type _di: void \*

.. _`ab8500_btemp_templow_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_btemp_temphigh_handler`:

ab8500_btemp_temphigh_handler
=============================

.. c:function:: irqreturn_t ab8500_btemp_temphigh_handler(int irq, void *_di)

    battery temp higher than max temp

    :param irq:
        interrupt number
    :type irq: int

    :param _di:
        void pointer that has to address of ab8500_btemp
    :type _di: void \*

.. _`ab8500_btemp_temphigh_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_btemp_lowmed_handler`:

ab8500_btemp_lowmed_handler
===========================

.. c:function:: irqreturn_t ab8500_btemp_lowmed_handler(int irq, void *_di)

    battery temp between low and medium

    :param irq:
        interrupt number
    :type irq: int

    :param _di:
        void pointer that has to address of ab8500_btemp
    :type _di: void \*

.. _`ab8500_btemp_lowmed_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_btemp_medhigh_handler`:

ab8500_btemp_medhigh_handler
============================

.. c:function:: irqreturn_t ab8500_btemp_medhigh_handler(int irq, void *_di)

    battery temp between medium and high

    :param irq:
        interrupt number
    :type irq: int

    :param _di:
        void pointer that has to address of ab8500_btemp
    :type _di: void \*

.. _`ab8500_btemp_medhigh_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_btemp_periodic`:

ab8500_btemp_periodic
=====================

.. c:function:: void ab8500_btemp_periodic(struct ab8500_btemp *di, bool enable)

    Periodic temperature measurements

    :param di:
        pointer to the ab8500_btemp structure
    :type di: struct ab8500_btemp \*

    :param enable:
        enable or disable periodic temperature measurements
    :type enable: bool

.. _`ab8500_btemp_periodic.description`:

Description
-----------

Starts of stops periodic temperature measurements. Periodic measurements
should only be done when a charger is connected.

.. _`ab8500_btemp_get_temp`:

ab8500_btemp_get_temp
=====================

.. c:function:: int ab8500_btemp_get_temp(struct ab8500_btemp *di)

    get battery temperature

    :param di:
        pointer to the ab8500_btemp structure
    :type di: struct ab8500_btemp \*

.. _`ab8500_btemp_get_temp.description`:

Description
-----------

Returns battery temperature

.. _`ab8500_btemp_get_batctrl_temp`:

ab8500_btemp_get_batctrl_temp
=============================

.. c:function:: int ab8500_btemp_get_batctrl_temp(struct ab8500_btemp *btemp)

    get the temperature

    :param btemp:
        pointer to the btemp structure
    :type btemp: struct ab8500_btemp \*

.. _`ab8500_btemp_get_batctrl_temp.description`:

Description
-----------

Returns the batctrl temperature in millidegrees

.. _`ab8500_btemp_get_property`:

ab8500_btemp_get_property
=========================

.. c:function:: int ab8500_btemp_get_property(struct power_supply *psy, enum power_supply_property psp, union power_supply_propval *val)

    get the btemp properties

    :param psy:
        pointer to the power_supply structure
    :type psy: struct power_supply \*

    :param psp:
        pointer to the power_supply_property structure
    :type psp: enum power_supply_property

    :param val:
        pointer to the power_supply_propval union
    :type val: union power_supply_propval \*

.. _`ab8500_btemp_get_property.description`:

Description
-----------

This function gets called when an application tries to get the btemp
properties by reading the sysfs files.

.. _`ab8500_btemp_get_property.online`:

online
------

presence of the battery

.. _`ab8500_btemp_get_property.present`:

present
-------

presence of the battery

.. _`ab8500_btemp_get_property.technology`:

technology
----------

battery technology

.. _`ab8500_btemp_get_property.temp`:

temp
----

battery temperature
Returns error code in case of failure else 0(on success)

.. _`ab8500_btemp_external_power_changed`:

ab8500_btemp_external_power_changed
===================================

.. c:function:: void ab8500_btemp_external_power_changed(struct power_supply *psy)

    callback for power supply changes

    :param psy:
        pointer to the structure power_supply
    :type psy: struct power_supply \*

.. _`ab8500_btemp_external_power_changed.description`:

Description
-----------

This function is pointing to the function pointer external_power_changed
of the structure power_supply.
This function gets executed when there is a change in the external power
supply to the btemp.

.. This file was automatic generated / don't edit.

