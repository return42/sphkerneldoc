.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/supply/ab8500_fg.c

.. _`ab8500_fg_interrupts`:

struct ab8500_fg_interrupts
===========================

.. c:type:: struct ab8500_fg_interrupts

    ab8500 fg interupts

.. _`ab8500_fg_interrupts.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_fg_interrupts {
        char *name;
        irqreturn_t (*isr)(int irq, void *data);
    }

.. _`ab8500_fg_interrupts.members`:

Members
-------

name
    name of the interrupt
    \ ``isr``\          function pointer to the isr

isr
    *undescribed*

.. _`ab8500_fg`:

struct ab8500_fg
================

.. c:type:: struct ab8500_fg

    ab8500 FG device information

.. _`ab8500_fg.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_fg {
        struct device *dev;
        struct list_head node;
        int irq;
        int vbat;
        int vbat_nom;
        int inst_curr;
        int avg_curr;
        int bat_temp;
        int fg_samples;
        int accu_charge;
        int recovery_cnt;
        int high_curr_cnt;
        int init_cnt;
        int low_bat_cnt;
        int nbr_cceoc_irq_cnt;
        bool recovery_needed;
        bool high_curr_mode;
        bool init_capacity;
        bool turn_off_fg;
        enum ab8500_fg_calibration_state calib_state;
        enum ab8500_fg_discharge_state discharge_state;
        enum ab8500_fg_charge_state charge_state;
        struct completion ab8500_fg_started;
        struct completion ab8500_fg_complete;
        struct ab8500_fg_flags flags;
        struct ab8500_fg_battery_capacity bat_cap;
        struct ab8500_fg_avg_cap avg_cap;
        struct ab8500 *parent;
        struct ab8500_gpadc *gpadc;
        struct abx500_bm_data *bm;
        struct power_supply *fg_psy;
        struct workqueue_struct *fg_wq;
        struct delayed_work fg_periodic_work;
        struct delayed_work fg_low_bat_work;
        struct delayed_work fg_reinit_work;
        struct work_struct fg_work;
        struct work_struct fg_acc_cur_work;
        struct delayed_work fg_check_hw_failure_work;
        struct mutex cc_lock;
        struct kobject fg_kobject;
    }

.. _`ab8500_fg.members`:

Members
-------

dev
    Pointer to the structure device

node
    a list of AB8500 FGs, hence prepared for reentrance
    \ ``irq``\                  holds the CCEOC interrupt number

irq
    *undescribed*

vbat
    Battery voltage in mV

vbat_nom
    Nominal battery voltage in mV

inst_curr
    Instantenous battery current in mA

avg_curr
    Average battery current in mA
    \ ``bat_temp``\             battery temperature

bat_temp
    *undescribed*

fg_samples
    Number of samples used in the FG accumulation

accu_charge
    Accumulated charge from the last conversion

recovery_cnt
    Counter for recovery mode

high_curr_cnt
    Counter for high current mode

init_cnt
    Counter for init mode
    \ ``low_bat_cnt``\          Counter for number of consecutive low battery measures
    \ ``nbr_cceoc_irq_cnt``\    Counter for number of CCEOC irqs received since enabled

low_bat_cnt
    *undescribed*

nbr_cceoc_irq_cnt
    *undescribed*

recovery_needed
    Indicate if recovery is needed

high_curr_mode
    Indicate if we're in high current mode

init_capacity
    Indicate if initial capacity measuring should be done

turn_off_fg
    True if fg was off before current measurement
    \ ``calib_state``\          State during offset calibration

calib_state
    *undescribed*

discharge_state
    Current discharge state

charge_state
    Current charge state
    \ ``ab8500_fg_started``\    Completion struct used for the instant current start
    \ ``ab8500_fg_complete``\   Completion struct used for the instant current reading

ab8500_fg_started
    *undescribed*

ab8500_fg_complete
    *undescribed*

flags
    Structure for information about events triggered

bat_cap
    Structure for battery capacity specific parameters

avg_cap
    Average capacity filter

parent
    Pointer to the struct ab8500

gpadc
    Pointer to the struct gpadc

bm
    Platform specific battery management information

fg_psy
    Structure that holds the FG specific battery properties

fg_wq
    Work queue for running the FG algorithm

fg_periodic_work
    Work to run the FG algorithm periodically

fg_low_bat_work
    Work to check low bat condition
    \ ``fg_reinit_work``\       Work used to reset and reinitialise the FG algorithm

fg_reinit_work
    *undescribed*

fg_work
    Work to run the FG algorithm instantly

fg_acc_cur_work
    Work to read the FG accumulator

fg_check_hw_failure_work
    Work for checking HW state

cc_lock
    Mutex for locking the CC

fg_kobject
    Structure of type kobject

.. _`ab8500_fg_get`:

ab8500_fg_get
=============

.. c:function:: struct ab8500_fg *ab8500_fg_get( void)

    returns a reference to the primary AB8500 fuel gauge (i.e. the first fuel gauge in the instance list)

    :param void:
        no arguments
    :type void: 

.. _`ab8500_fg_is_low_curr`:

ab8500_fg_is_low_curr
=====================

.. c:function:: int ab8500_fg_is_low_curr(struct ab8500_fg *di, int curr)

    Low or high current mode

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param curr:
        the current to base or our decision on
    :type curr: int

.. _`ab8500_fg_is_low_curr.description`:

Description
-----------

Low current mode if the current consumption is below a certain threshold

.. _`ab8500_fg_add_cap_sample`:

ab8500_fg_add_cap_sample
========================

.. c:function:: int ab8500_fg_add_cap_sample(struct ab8500_fg *di, int sample)

    Add capacity to average filter

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param sample:
        the capacity in mAh to add to the filter
    :type sample: int

.. _`ab8500_fg_add_cap_sample.description`:

Description
-----------

A capacity is added to the filter and a new mean capacity is calculated and
returned

.. _`ab8500_fg_clear_cap_samples`:

ab8500_fg_clear_cap_samples
===========================

.. c:function:: void ab8500_fg_clear_cap_samples(struct ab8500_fg *di)

    Clear average filter

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_clear_cap_samples.description`:

Description
-----------

The capacity filter is is reset to zero.

.. _`ab8500_fg_fill_cap_sample`:

ab8500_fg_fill_cap_sample
=========================

.. c:function:: void ab8500_fg_fill_cap_sample(struct ab8500_fg *di, int sample)

    Fill average filter

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param sample:
        the capacity in mAh to fill the filter with
    :type sample: int

.. _`ab8500_fg_fill_cap_sample.description`:

Description
-----------

The capacity filter is filled with a capacity in mAh

.. _`ab8500_fg_coulomb_counter`:

ab8500_fg_coulomb_counter
=========================

.. c:function:: int ab8500_fg_coulomb_counter(struct ab8500_fg *di, bool enable)

    enable coulomb counter

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param enable:
        enable/disable
    :type enable: bool

.. _`ab8500_fg_coulomb_counter.description`:

Description
-----------

Enable/Disable coulomb counter.
On failure returns negative value.

.. _`ab8500_fg_inst_curr_start`:

ab8500_fg_inst_curr_start
=========================

.. c:function:: int ab8500_fg_inst_curr_start(struct ab8500_fg *di)

    start battery instantaneous current

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_inst_curr_start.description`:

Description
-----------

Returns 0 or error code

.. _`ab8500_fg_inst_curr_start.note`:

Note
----

This is part "one" and has to be called before
\ :c:func:`ab8500_fg_inst_curr_finalize`\ 

.. _`ab8500_fg_inst_curr_started`:

ab8500_fg_inst_curr_started
===========================

.. c:function:: int ab8500_fg_inst_curr_started(struct ab8500_fg *di)

    check if fg conversion has started

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_inst_curr_started.description`:

Description
-----------

Returns 1 if conversion started, 0 if still waiting

.. _`ab8500_fg_inst_curr_done`:

ab8500_fg_inst_curr_done
========================

.. c:function:: int ab8500_fg_inst_curr_done(struct ab8500_fg *di)

    check if fg conversion is done

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_inst_curr_done.description`:

Description
-----------

Returns 1 if conversion done, 0 if still waiting

.. _`ab8500_fg_inst_curr_finalize`:

ab8500_fg_inst_curr_finalize
============================

.. c:function:: int ab8500_fg_inst_curr_finalize(struct ab8500_fg *di, int *res)

    battery instantaneous current

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param res:
        battery instantenous current(on success)
    :type res: int \*

.. _`ab8500_fg_inst_curr_finalize.description`:

Description
-----------

Returns 0 or an error code

.. _`ab8500_fg_inst_curr_finalize.note`:

Note
----

This is part "two" and has to be called at earliest 250 ms
after \ :c:func:`ab8500_fg_inst_curr_start`\ 

.. _`ab8500_fg_inst_curr_blocking`:

ab8500_fg_inst_curr_blocking
============================

.. c:function:: int ab8500_fg_inst_curr_blocking(struct ab8500_fg *di)

    battery instantaneous current

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_inst_curr_blocking.description`:

Description
-----------

Returns 0 else error code

.. _`ab8500_fg_acc_cur_work`:

ab8500_fg_acc_cur_work
======================

.. c:function:: void ab8500_fg_acc_cur_work(struct work_struct *work)

    average battery current

    :param work:
        pointer to the work_struct structure
    :type work: struct work_struct \*

.. _`ab8500_fg_acc_cur_work.description`:

Description
-----------

Updated the average battery current obtained from the
coulomb counter.

.. _`ab8500_fg_bat_voltage`:

ab8500_fg_bat_voltage
=====================

.. c:function:: int ab8500_fg_bat_voltage(struct ab8500_fg *di)

    get battery voltage

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_bat_voltage.description`:

Description
-----------

Returns battery voltage(on success) else error code

.. _`ab8500_fg_volt_to_capacity`:

ab8500_fg_volt_to_capacity
==========================

.. c:function:: int ab8500_fg_volt_to_capacity(struct ab8500_fg *di, int voltage)

    Voltage based capacity

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param voltage:
        The voltage to convert to a capacity
    :type voltage: int

.. _`ab8500_fg_volt_to_capacity.description`:

Description
-----------

Returns battery capacity in per mille based on voltage

.. _`ab8500_fg_uncomp_volt_to_capacity`:

ab8500_fg_uncomp_volt_to_capacity
=================================

.. c:function:: int ab8500_fg_uncomp_volt_to_capacity(struct ab8500_fg *di)

    Uncompensated voltage based capacity

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_uncomp_volt_to_capacity.description`:

Description
-----------

Returns battery capacity based on battery voltage that is not compensated
for the voltage drop due to the load

.. _`ab8500_fg_battery_resistance`:

ab8500_fg_battery_resistance
============================

.. c:function:: int ab8500_fg_battery_resistance(struct ab8500_fg *di)

    Returns the battery inner resistance

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_battery_resistance.description`:

Description
-----------

Returns battery inner resistance added with the fuel gauge resistor value
to get the total resistance in the whole link from gnd to bat+ node.

.. _`ab8500_fg_load_comp_volt_to_capacity`:

ab8500_fg_load_comp_volt_to_capacity
====================================

.. c:function:: int ab8500_fg_load_comp_volt_to_capacity(struct ab8500_fg *di)

    Load compensated voltage based capacity

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_load_comp_volt_to_capacity.description`:

Description
-----------

Returns battery capacity based on battery voltage that is load compensated
for the voltage drop

.. _`ab8500_fg_convert_mah_to_permille`:

ab8500_fg_convert_mah_to_permille
=================================

.. c:function:: int ab8500_fg_convert_mah_to_permille(struct ab8500_fg *di, int cap_mah)

    Capacity in mAh to permille

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param cap_mah:
        capacity in mAh
    :type cap_mah: int

.. _`ab8500_fg_convert_mah_to_permille.description`:

Description
-----------

Converts capacity in mAh to capacity in permille

.. _`ab8500_fg_convert_permille_to_mah`:

ab8500_fg_convert_permille_to_mah
=================================

.. c:function:: int ab8500_fg_convert_permille_to_mah(struct ab8500_fg *di, int cap_pm)

    Capacity in permille to mAh

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param cap_pm:
        capacity in permille
    :type cap_pm: int

.. _`ab8500_fg_convert_permille_to_mah.description`:

Description
-----------

Converts capacity in permille to capacity in mAh

.. _`ab8500_fg_convert_mah_to_uwh`:

ab8500_fg_convert_mah_to_uwh
============================

.. c:function:: int ab8500_fg_convert_mah_to_uwh(struct ab8500_fg *di, int cap_mah)

    Capacity in mAh to uWh

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param cap_mah:
        capacity in mAh
    :type cap_mah: int

.. _`ab8500_fg_convert_mah_to_uwh.description`:

Description
-----------

Converts capacity in mAh to capacity in uWh

.. _`ab8500_fg_calc_cap_charging`:

ab8500_fg_calc_cap_charging
===========================

.. c:function:: int ab8500_fg_calc_cap_charging(struct ab8500_fg *di)

    Calculate remaining capacity while charging

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_calc_cap_charging.description`:

Description
-----------

Return the capacity in mAh based on previous calculated capcity and the FG
accumulator register value. The filter is filled with this capacity

.. _`ab8500_fg_calc_cap_discharge_voltage`:

ab8500_fg_calc_cap_discharge_voltage
====================================

.. c:function:: int ab8500_fg_calc_cap_discharge_voltage(struct ab8500_fg *di, bool comp)

    Capacity in discharge with voltage

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param comp:
        if voltage should be load compensated before capacity calc
    :type comp: bool

.. _`ab8500_fg_calc_cap_discharge_voltage.description`:

Description
-----------

Return the capacity in mAh based on the battery voltage. The voltage can
either be load compensated or not. This value is added to the filter and a
new mean value is calculated and returned.

.. _`ab8500_fg_calc_cap_discharge_fg`:

ab8500_fg_calc_cap_discharge_fg
===============================

.. c:function:: int ab8500_fg_calc_cap_discharge_fg(struct ab8500_fg *di)

    Capacity in discharge with FG

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_calc_cap_discharge_fg.description`:

Description
-----------

Return the capacity in mAh based on previous calculated capcity and the FG
accumulator register value. This value is added to the filter and a
new mean value is calculated and returned.

.. _`ab8500_fg_capacity_level`:

ab8500_fg_capacity_level
========================

.. c:function:: int ab8500_fg_capacity_level(struct ab8500_fg *di)

    Get the battery capacity level

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_capacity_level.description`:

Description
-----------

Get the battery capacity level based on the capacity in percent

.. _`ab8500_fg_calculate_scaled_capacity`:

ab8500_fg_calculate_scaled_capacity
===================================

.. c:function:: int ab8500_fg_calculate_scaled_capacity(struct ab8500_fg *di)

    Capacity scaling

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_calculate_scaled_capacity.description`:

Description
-----------

Calculates the capacity to be shown to upper layers. Scales the capacity
to have 100% as a reference from the actual capacity upon removal of charger
when charging is in maintenance mode.

.. _`ab8500_fg_update_cap_scalers`:

ab8500_fg_update_cap_scalers
============================

.. c:function:: void ab8500_fg_update_cap_scalers(struct ab8500_fg *di)

    Capacity scaling

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_update_cap_scalers.description`:

Description
-----------

To be called when state change from charge<->discharge to update
the capacity scalers.

.. _`ab8500_fg_check_capacity_limits`:

ab8500_fg_check_capacity_limits
===============================

.. c:function:: void ab8500_fg_check_capacity_limits(struct ab8500_fg *di, bool init)

    Check if capacity has changed

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param init:
        capacity is allowed to go up in init mode
    :type init: bool

.. _`ab8500_fg_check_capacity_limits.description`:

Description
-----------

Check if capacity or capacity limit has changed and notify the system
about it using the power_supply framework

.. _`ab8500_fg_algorithm_charging`:

ab8500_fg_algorithm_charging
============================

.. c:function:: void ab8500_fg_algorithm_charging(struct ab8500_fg *di)

    FG algorithm for when charging

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_algorithm_charging.description`:

Description
-----------

Battery capacity calculation state machine for when we're charging

.. _`ab8500_fg_algorithm_discharging`:

ab8500_fg_algorithm_discharging
===============================

.. c:function:: void ab8500_fg_algorithm_discharging(struct ab8500_fg *di)

    FG algorithm for when discharging

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_algorithm_discharging.description`:

Description
-----------

Battery capacity calculation state machine for when we're discharging

.. _`ab8500_fg_algorithm_calibrate`:

ab8500_fg_algorithm_calibrate
=============================

.. c:function:: void ab8500_fg_algorithm_calibrate(struct ab8500_fg *di)

    Internal columb counter offset calibration

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_algorithm`:

ab8500_fg_algorithm
===================

.. c:function:: void ab8500_fg_algorithm(struct ab8500_fg *di)

    Entry point for the FG algorithm

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_algorithm.description`:

Description
-----------

Entry point for the battery capacity calculation state machine

.. _`ab8500_fg_periodic_work`:

ab8500_fg_periodic_work
=======================

.. c:function:: void ab8500_fg_periodic_work(struct work_struct *work)

    Run the FG state machine periodically

    :param work:
        pointer to the work_struct structure
    :type work: struct work_struct \*

.. _`ab8500_fg_periodic_work.description`:

Description
-----------

Work queue function for periodic work

.. _`ab8500_fg_check_hw_failure_work`:

ab8500_fg_check_hw_failure_work
===============================

.. c:function:: void ab8500_fg_check_hw_failure_work(struct work_struct *work)

    Check OVV_BAT condition

    :param work:
        pointer to the work_struct structure
    :type work: struct work_struct \*

.. _`ab8500_fg_check_hw_failure_work.description`:

Description
-----------

Work queue function for checking the OVV_BAT condition

.. _`ab8500_fg_low_bat_work`:

ab8500_fg_low_bat_work
======================

.. c:function:: void ab8500_fg_low_bat_work(struct work_struct *work)

    Check LOW_BAT condition

    :param work:
        pointer to the work_struct structure
    :type work: struct work_struct \*

.. _`ab8500_fg_low_bat_work.description`:

Description
-----------

Work queue function for checking the LOW_BAT condition

.. _`ab8500_fg_battok_calc`:

ab8500_fg_battok_calc
=====================

.. c:function:: int ab8500_fg_battok_calc(struct ab8500_fg *di, int target)

    calculate the bit pattern corresponding to the target voltage.

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

    :param target:
        target voltage
    :type target: int

.. _`ab8500_fg_battok_calc.description`:

Description
-----------

Returns bit pattern closest to the target voltage
valid return values are 0-14. (0-BATT_OK_MAX_NR_INCREMENTS)

.. _`ab8500_fg_battok_init_hw_register`:

ab8500_fg_battok_init_hw_register
=================================

.. c:function:: int ab8500_fg_battok_init_hw_register(struct ab8500_fg *di)

    init battok levels

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_instant_work`:

ab8500_fg_instant_work
======================

.. c:function:: void ab8500_fg_instant_work(struct work_struct *work)

    Run the FG state machine instantly

    :param work:
        pointer to the work_struct structure
    :type work: struct work_struct \*

.. _`ab8500_fg_instant_work.description`:

Description
-----------

Work queue function for instant work

.. _`ab8500_fg_cc_data_end_handler`:

ab8500_fg_cc_data_end_handler
=============================

.. c:function:: irqreturn_t ab8500_fg_cc_data_end_handler(int irq, void *_di)

    end of data conversion isr.

    :param irq:
        interrupt number
    :type irq: int

    :param _di:
        pointer to the ab8500_fg structure
    :type _di: void \*

.. _`ab8500_fg_cc_data_end_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_fg_cc_int_calib_handler`:

ab8500_fg_cc_int_calib_handler
==============================

.. c:function:: irqreturn_t ab8500_fg_cc_int_calib_handler(int irq, void *_di)

    end of calibration isr.

    :param irq:
        interrupt number
    :type irq: int

    :param _di:
        pointer to the ab8500_fg structure
    :type _di: void \*

.. _`ab8500_fg_cc_int_calib_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_fg_cc_convend_handler`:

ab8500_fg_cc_convend_handler
============================

.. c:function:: irqreturn_t ab8500_fg_cc_convend_handler(int irq, void *_di)

    isr to get battery avg current.

    :param irq:
        interrupt number
    :type irq: int

    :param _di:
        pointer to the ab8500_fg structure
    :type _di: void \*

.. _`ab8500_fg_cc_convend_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_fg_batt_ovv_handler`:

ab8500_fg_batt_ovv_handler
==========================

.. c:function:: irqreturn_t ab8500_fg_batt_ovv_handler(int irq, void *_di)

    Battery OVV occured

    :param irq:
        interrupt number
    :type irq: int

    :param _di:
        pointer to the ab8500_fg structure
    :type _di: void \*

.. _`ab8500_fg_batt_ovv_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_fg_lowbatf_handler`:

ab8500_fg_lowbatf_handler
=========================

.. c:function:: irqreturn_t ab8500_fg_lowbatf_handler(int irq, void *_di)

    Battery voltage is below LOW threshold

    :param irq:
        interrupt number
    :type irq: int

    :param _di:
        pointer to the ab8500_fg structure
    :type _di: void \*

.. _`ab8500_fg_lowbatf_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_fg_get_property`:

ab8500_fg_get_property
======================

.. c:function:: int ab8500_fg_get_property(struct power_supply *psy, enum power_supply_property psp, union power_supply_propval *val)

    get the fg properties

    :param psy:
        pointer to the power_supply structure
    :type psy: struct power_supply \*

    :param psp:
        pointer to the power_supply_property structure
    :type psp: enum power_supply_property

    :param val:
        pointer to the power_supply_propval union
    :type val: union power_supply_propval \*

.. _`ab8500_fg_get_property.description`:

Description
-----------

This function gets called when an application tries to get the
fg properties by reading the sysfs files.

.. _`ab8500_fg_get_property.voltage_now`:

voltage_now
-----------

battery voltage

.. _`ab8500_fg_get_property.current_now`:

current_now
-----------

battery instant current

.. _`ab8500_fg_get_property.current_avg`:

current_avg
-----------

battery average current

.. _`ab8500_fg_get_property.charge_full_design`:

charge_full_design
------------------

capacity where battery is considered full

.. _`ab8500_fg_get_property.charge_now`:

charge_now
----------

battery capacity in nAh

.. _`ab8500_fg_get_property.capacity`:

capacity
--------

capacity in percent

.. _`ab8500_fg_get_property.capacity_level`:

capacity_level
--------------

capacity level

Returns error code in case of failure else 0 on success

.. _`ab8500_fg_init_hw_registers`:

ab8500_fg_init_hw_registers
===========================

.. c:function:: int ab8500_fg_init_hw_registers(struct ab8500_fg *di)

    Set up FG related registers

    :param di:
        pointer to the ab8500_fg structure
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_init_hw_registers.description`:

Description
-----------

Set up battery OVV, low battery voltage registers

.. _`ab8500_fg_external_power_changed`:

ab8500_fg_external_power_changed
================================

.. c:function:: void ab8500_fg_external_power_changed(struct power_supply *psy)

    callback for power supply changes

    :param psy:
        pointer to the structure power_supply
    :type psy: struct power_supply \*

.. _`ab8500_fg_external_power_changed.description`:

Description
-----------

This function is the entry point of the pointer external_power_changed
of the structure power_supply.
This function gets executed when there is a change in any external power
supply that this driver needs to be notified of.

.. _`ab8500_fg_reinit_work`:

ab8500_fg_reinit_work
=====================

.. c:function:: void ab8500_fg_reinit_work(struct work_struct *work)

    work to reset the FG algorithm

    :param work:
        pointer to the work_struct structure
    :type work: struct work_struct \*

.. _`ab8500_fg_reinit_work.description`:

Description
-----------

Used to reset the current battery capacity to be able to
retrigger a new voltage base capacity calculation. For
test and verification purpose.

.. _`ab8500_fg_sysfs_exit`:

ab8500_fg_sysfs_exit
====================

.. c:function:: void ab8500_fg_sysfs_exit(struct ab8500_fg *di)

    de-init of sysfs entry

    :param di:
        pointer to the struct ab8500_chargalg
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_sysfs_exit.description`:

Description
-----------

This function removes the entry in sysfs.

.. _`ab8500_fg_sysfs_init`:

ab8500_fg_sysfs_init
====================

.. c:function:: int ab8500_fg_sysfs_init(struct ab8500_fg *di)

    init of sysfs entry

    :param di:
        pointer to the struct ab8500_chargalg
    :type di: struct ab8500_fg \*

.. _`ab8500_fg_sysfs_init.description`:

Description
-----------

This function adds an entry in sysfs.
Returns error code in case of failure else 0(on success)

.. This file was automatic generated / don't edit.

