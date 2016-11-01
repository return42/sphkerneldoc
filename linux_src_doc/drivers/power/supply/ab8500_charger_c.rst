.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/power/supply/ab8500_charger.c

.. _`ab8500_charger_interrupts`:

struct ab8500_charger_interrupts
================================

.. c:type:: struct ab8500_charger_interrupts

    ab8500 interupts

.. _`ab8500_charger_interrupts.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_charger_interrupts {
        char *name;
        irqreturn_t (*isr)(int irq, void *data);
    }

.. _`ab8500_charger_interrupts.members`:

Members
-------

name
    name of the interrupt
    \ ``isr``\          function pointer to the isr

isr
    *undescribed*

.. _`ab8500_charger`:

struct ab8500_charger
=====================

.. c:type:: struct ab8500_charger

    ab8500 Charger device information

.. _`ab8500_charger.definition`:

Definition
----------

.. code-block:: c

    struct ab8500_charger {
        struct device *dev;
        bool vbus_detected;
        bool vbus_detected_start;
        bool ac_conn;
        bool vddadc_en_ac;
        bool vddadc_en_usb;
        int vbat;
        int old_vbat;
        bool usb_device_is_unrecognised;
        bool autopower;
        bool autopower_cfg;
        int invalid_charger_detect_state;
        int is_aca_rid;
        atomic_t current_stepping_sessions;
        struct ab8500 *parent;
        struct ab8500_gpadc *gpadc;
        struct abx500_bm_data *bm;
        struct ab8500_charger_event_flags flags;
        struct ab8500_charger_usb_state usb_state;
        struct ab8500_charger_max_usb_in_curr max_usb_in_curr;
        struct ux500_charger ac_chg;
        struct ux500_charger usb_chg;
        struct ab8500_charger_info ac;
        struct ab8500_charger_info usb;
        struct regulator *regu;
        struct workqueue_struct *charger_wq;
        struct mutex usb_ipt_crnt_lock;
        struct delayed_work check_vbat_work;
        struct delayed_work check_hw_failure_work;
        struct delayed_work check_usbchgnotok_work;
        struct delayed_work kick_wd_work;
        struct delayed_work usb_state_changed_work;
        struct delayed_work attach_work;
        struct delayed_work ac_charger_attached_work;
        struct delayed_work usb_charger_attached_work;
        struct delayed_work vbus_drop_end_work;
        struct work_struct ac_work;
        struct work_struct detect_usb_type_work;
        struct work_struct usb_link_status_work;
        struct work_struct check_main_thermal_prot_work;
        struct work_struct check_usb_thermal_prot_work;
        struct usb_phy *usb_phy;
        struct notifier_block nb;
        struct mutex charger_attached_mutex;
    }

.. _`ab8500_charger.members`:

Members
-------

dev
    Pointer to the structure device

vbus_detected
    VBUS detected

vbus_detected_start
    VBUS detected during startup

ac_conn
    This will be true when the AC charger has been plugged

vddadc_en_ac
    Indicate if VDD ADC supply is enabled because AC
    charger is enabled

vddadc_en_usb
    Indicate if VDD ADC supply is enabled because USB
    charger is enabled
    \ ``vbat``\                 Battery voltage
    \ ``old_vbat``\             Previously measured battery voltage
    \ ``usb_device_is_unrecognised``\   USB device is unrecognised by the hardware
    \ ``autopower``\            Indicate if we should have automatic pwron after pwrloss
    \ ``autopower_cfg``\        platform specific power config support for "pwron after pwrloss"
    \ ``invalid_charger_detect_state``\  State when forcing AB to use invalid charger

vbat
    *undescribed*

old_vbat
    *undescribed*

usb_device_is_unrecognised
    *undescribed*

autopower
    *undescribed*

autopower_cfg
    *undescribed*

invalid_charger_detect_state
    *undescribed*

is_aca_rid
    Incicate if accessory is ACA type

current_stepping_sessions
    Counter for current stepping sessions

parent
    Pointer to the struct ab8500

gpadc
    Pointer to the struct gpadc

bm
    Platform specific battery management information

flags
    Structure for information about events triggered

usb_state
    Structure for usb stack information

max_usb_in_curr
    Max USB charger input current

ac_chg
    AC charger power supply

usb_chg
    USB charger power supply

ac
    Structure that holds the AC charger properties

usb
    Structure that holds the USB charger properties

regu
    Pointer to the struct regulator

charger_wq
    Work queue for the IRQs and checking HW state

usb_ipt_crnt_lock
    Lock to protect VBUS input current setting from mutuals

check_vbat_work
    *undescribed*

check_hw_failure_work
    Work for checking HW state

check_usbchgnotok_work
    Work for checking USB charger not ok status

kick_wd_work
    Work for kicking the charger watchdog in case
    of ABB rev 1.\* due to the watchog logic bug

usb_state_changed_work
    Work for checking USB state

attach_work
    Work for detecting USB type

ac_charger_attached_work
    Work for checking if AC charger is still
    connected

usb_charger_attached_work
    Work for checking if USB charger is still
    connected

vbus_drop_end_work
    Work for detecting VBUS drop end

ac_work
    Work for checking AC charger connection

detect_usb_type_work
    Work for detecting the USB type connected

usb_link_status_work
    Work for checking the new USB link status

check_main_thermal_prot_work
    Work for checking Main thermal status

check_usb_thermal_prot_work
    Work for checking USB thermal status

usb_phy
    *undescribed*

nb
    *undescribed*

charger_attached_mutex
    For controlling the wakelock

.. _`ab8500_power_supply_changed`:

ab8500_power_supply_changed
===========================

.. c:function:: void ab8500_power_supply_changed(struct ab8500_charger *di, struct power_supply *psy)

    a wrapper with local extentions for power_supply_changed

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

    :param struct power_supply \*psy:
        pointer to power_supply_that have changed.

.. _`ab8500_charger_get_ac_voltage`:

ab8500_charger_get_ac_voltage
=============================

.. c:function:: int ab8500_charger_get_ac_voltage(struct ab8500_charger *di)

    get ac charger voltage

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_get_ac_voltage.description`:

Description
-----------

Returns ac charger voltage (on success)

.. _`ab8500_charger_ac_cv`:

ab8500_charger_ac_cv
====================

.. c:function:: int ab8500_charger_ac_cv(struct ab8500_charger *di)

    check if the main charger is in CV mode

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_ac_cv.description`:

Description
-----------

Returns ac charger CV mode (on success) else error code

.. _`ab8500_charger_get_vbus_voltage`:

ab8500_charger_get_vbus_voltage
===============================

.. c:function:: int ab8500_charger_get_vbus_voltage(struct ab8500_charger *di)

    get vbus voltage

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_get_vbus_voltage.description`:

Description
-----------

This function returns the vbus voltage.
Returns vbus voltage (on success)

.. _`ab8500_charger_get_usb_current`:

ab8500_charger_get_usb_current
==============================

.. c:function:: int ab8500_charger_get_usb_current(struct ab8500_charger *di)

    get usb charger current

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_get_usb_current.description`:

Description
-----------

This function returns the usb charger current.
Returns usb current (on success) and error code on failure

.. _`ab8500_charger_get_ac_current`:

ab8500_charger_get_ac_current
=============================

.. c:function:: int ab8500_charger_get_ac_current(struct ab8500_charger *di)

    get ac charger current

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_get_ac_current.description`:

Description
-----------

This function returns the ac charger current.
Returns ac current (on success) and error code on failure.

.. _`ab8500_charger_usb_cv`:

ab8500_charger_usb_cv
=====================

.. c:function:: int ab8500_charger_usb_cv(struct ab8500_charger *di)

    check if the usb charger is in CV mode

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_usb_cv.description`:

Description
-----------

Returns ac charger CV mode (on success) else error code

.. _`ab8500_charger_detect_chargers`:

ab8500_charger_detect_chargers
==============================

.. c:function:: int ab8500_charger_detect_chargers(struct ab8500_charger *di, bool probe)

    Detect the connected chargers

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

    :param bool probe:
        if probe, don't delay and wait for HW

.. _`ab8500_charger_detect_chargers.description`:

Description
-----------

Returns the type of charger connected.
For USB it will not mean we can actually charge from it
but that there is a USB cable connected that we have to
identify. This is used during startup when we don't get
interrupts of the charger detection

Returns an integer value, that means,
NO_PW_CONN  no power supply is connected
AC_PW_CONN  if the AC power supply is connected
USB_PW_CONN  if the USB power supply is connected
AC_PW_CONN + USB_PW_CONN if USB and AC power supplies are both connected

.. _`ab8500_charger_max_usb_curr`:

ab8500_charger_max_usb_curr
===========================

.. c:function:: int ab8500_charger_max_usb_curr(struct ab8500_charger *di, enum ab8500_charger_link_status link_status)

    get the max curr for the USB type

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

    :param enum ab8500_charger_link_status link_status:
        the identified USB type

.. _`ab8500_charger_max_usb_curr.description`:

Description
-----------

Get the maximum current that is allowed to be drawn from the host
based on the USB type.
Returns error code in case of failure else 0 on success

.. _`ab8500_charger_read_usb_type`:

ab8500_charger_read_usb_type
============================

.. c:function:: int ab8500_charger_read_usb_type(struct ab8500_charger *di)

    read the type of usb connected

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_read_usb_type.description`:

Description
-----------

Detect the type of the plugged USB
Returns error code in case of failure else 0 on success

.. _`ab8500_charger_detect_usb_type`:

ab8500_charger_detect_usb_type
==============================

.. c:function:: int ab8500_charger_detect_usb_type(struct ab8500_charger *di)

    get the type of usb connected

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_detect_usb_type.description`:

Description
-----------

Detect the type of the plugged USB
Returns error code in case of failure else 0 on success

.. _`ab8500_charger_get_usb_cur`:

ab8500_charger_get_usb_cur
==========================

.. c:function:: int ab8500_charger_get_usb_cur(struct ab8500_charger *di)

    get usb current

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structre

.. _`ab8500_charger_get_usb_cur.description`:

Description
-----------

The usb stack provides the maximum current that can be drawn from
the standard usb host. This will be in mA.
This function converts current in mA to a value that can be written
to the register. Returns -1 if charging is not allowed

.. _`ab8500_charger_check_continue_stepping`:

ab8500_charger_check_continue_stepping
======================================

.. c:function:: bool ab8500_charger_check_continue_stepping(struct ab8500_charger *di, int reg)

    Check to allow stepping

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

    :param int reg:
        select what charger register to check

.. _`ab8500_charger_check_continue_stepping.description`:

Description
-----------

Check if current stepping should be allowed to continue.
Checks if charger source has not collapsed. If it has, further stepping
is not allowed.

.. _`ab8500_charger_set_current`:

ab8500_charger_set_current
==========================

.. c:function:: int ab8500_charger_set_current(struct ab8500_charger *di, int ich, int reg)

    set charger current

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

    :param int ich:
        charger current, in mA

    :param int reg:
        select what charger register to set

.. _`ab8500_charger_set_current.description`:

Description
-----------

Set charger current.
There is no state machine in the AB to step up/down the charger
current to avoid dips and spikes on MAIN, VBUS and VBAT when
charging is started. Instead we need to implement
this charger current step-up/down here.
Returns error code in case of failure else 0(on success)

.. _`ab8500_charger_set_vbus_in_curr`:

ab8500_charger_set_vbus_in_curr
===============================

.. c:function:: int ab8500_charger_set_vbus_in_curr(struct ab8500_charger *di, int ich_in)

    set VBUS input current limit

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

    :param int ich_in:
        charger input current limit

.. _`ab8500_charger_set_vbus_in_curr.description`:

Description
-----------

Sets the current that can be drawn from the USB host
Returns error code in case of failure else 0(on success)

.. _`ab8500_charger_set_main_in_curr`:

ab8500_charger_set_main_in_curr
===============================

.. c:function:: int ab8500_charger_set_main_in_curr(struct ab8500_charger *di, int ich_in)

    set main charger input current

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

    :param int ich_in:
        input charger current, in mA

.. _`ab8500_charger_set_main_in_curr.description`:

Description
-----------

Set main charger input current.
Returns error code in case of failure else 0(on success)

.. _`ab8500_charger_set_output_curr`:

ab8500_charger_set_output_curr
==============================

.. c:function:: int ab8500_charger_set_output_curr(struct ab8500_charger *di, int ich_out)

    set charger output current

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

    :param int ich_out:
        output charger current, in mA

.. _`ab8500_charger_set_output_curr.description`:

Description
-----------

Set charger output current.
Returns error code in case of failure else 0(on success)

.. _`ab8500_charger_led_en`:

ab8500_charger_led_en
=====================

.. c:function:: int ab8500_charger_led_en(struct ab8500_charger *di, int on)

    turn on/off chargign led

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

    :param int on:
        flag to turn on/off the chargign led

.. _`ab8500_charger_led_en.description`:

Description
-----------

Power ON/OFF charging LED indication
Returns error code in case of failure else 0(on success)

.. _`ab8500_charger_ac_en`:

ab8500_charger_ac_en
====================

.. c:function:: int ab8500_charger_ac_en(struct ux500_charger *charger, int enable, int vset, int iset)

    enable or disable ac charging

    :param struct ux500_charger \*charger:
        *undescribed*

    :param int enable:
        enable/disable flag

    :param int vset:
        charging voltage

    :param int iset:
        charging current

.. _`ab8500_charger_ac_en.description`:

Description
-----------

Enable/Disable AC/Mains charging and turns on/off the charging led
respectively.

.. _`ab8500_charger_usb_en`:

ab8500_charger_usb_en
=====================

.. c:function:: int ab8500_charger_usb_en(struct ux500_charger *charger, int enable, int vset, int ich_out)

    enable usb charging

    :param struct ux500_charger \*charger:
        *undescribed*

    :param int enable:
        enable/disable flag

    :param int vset:
        charging voltage

    :param int ich_out:
        charger output current

.. _`ab8500_charger_usb_en.description`:

Description
-----------

Enable/Disable USB charging and turns on/off the charging led respectively.
Returns error code in case of failure else 0(on success)

.. _`ab8500_charger_usb_check_enable`:

ab8500_charger_usb_check_enable
===============================

.. c:function:: int ab8500_charger_usb_check_enable(struct ux500_charger *charger, int vset, int iset)

    enable usb charging

    :param struct ux500_charger \*charger:
        pointer to the ux500_charger structure

    :param int vset:
        charging voltage

    :param int iset:
        charger output current

.. _`ab8500_charger_usb_check_enable.description`:

Description
-----------

Check if the VBUS charger has been disconnected and reconnected without
AB8500 rising an interrupt. Returns 0 on success.

.. _`ab8500_charger_ac_check_enable`:

ab8500_charger_ac_check_enable
==============================

.. c:function:: int ab8500_charger_ac_check_enable(struct ux500_charger *charger, int vset, int iset)

    enable usb charging

    :param struct ux500_charger \*charger:
        pointer to the ux500_charger structure

    :param int vset:
        charging voltage

    :param int iset:
        charger output current

.. _`ab8500_charger_ac_check_enable.description`:

Description
-----------

Check if the AC charger has been disconnected and reconnected without
AB8500 rising an interrupt. Returns 0 on success.

.. _`ab8500_charger_watchdog_kick`:

ab8500_charger_watchdog_kick
============================

.. c:function:: int ab8500_charger_watchdog_kick(struct ux500_charger *charger)

    kick charger watchdog

    :param struct ux500_charger \*charger:
        *undescribed*

.. _`ab8500_charger_watchdog_kick.description`:

Description
-----------

Kick charger watchdog
Returns error code in case of failure else 0(on success)

.. _`ab8500_charger_update_charger_current`:

ab8500_charger_update_charger_current
=====================================

.. c:function:: int ab8500_charger_update_charger_current(struct ux500_charger *charger, int ich_out)

    update charger current

    :param struct ux500_charger \*charger:
        *undescribed*

    :param int ich_out:
        *undescribed*

.. _`ab8500_charger_update_charger_current.description`:

Description
-----------

Update the charger output current for the specified charger
Returns error code in case of failure else 0(on success)

.. _`ab8540_charger_power_path_enable`:

ab8540_charger_power_path_enable
================================

.. c:function:: int ab8540_charger_power_path_enable(struct ux500_charger *charger, bool enable)

    enable usb power path mode

    :param struct ux500_charger \*charger:
        pointer to the ux500_charger structure

    :param bool enable:
        enable/disable flag

.. _`ab8540_charger_power_path_enable.description`:

Description
-----------

Enable or disable the power path for usb mode
Returns error code in case of failure else 0(on success)

.. _`ab8540_charger_usb_pre_chg_enable`:

ab8540_charger_usb_pre_chg_enable
=================================

.. c:function:: int ab8540_charger_usb_pre_chg_enable(struct ux500_charger *charger, bool enable)

    enable usb pre change

    :param struct ux500_charger \*charger:
        pointer to the ux500_charger structure

    :param bool enable:
        enable/disable flag

.. _`ab8540_charger_usb_pre_chg_enable.description`:

Description
-----------

Enable or disable the pre-chage for usb mode
Returns error code in case of failure else 0(on success)

.. _`ab8500_charger_check_vbat_work`:

ab8500_charger_check_vbat_work
==============================

.. c:function:: void ab8500_charger_check_vbat_work(struct work_struct *work)

    keep vbus current within spec \ ``work``\         pointer to the work_struct structure

    :param struct work_struct \*work:
        *undescribed*

.. _`ab8500_charger_check_vbat_work.description`:

Description
-----------

Due to a asic bug it is necessary to lower the input current to the vbus
charger when charging with at some specific levels. This issue is only valid
for below a certain battery voltage. This function makes sure that the
the allowed current limit isn't exceeded.

.. _`ab8500_charger_check_hw_failure_work`:

ab8500_charger_check_hw_failure_work
====================================

.. c:function:: void ab8500_charger_check_hw_failure_work(struct work_struct *work)

    check main charger failure

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. _`ab8500_charger_check_hw_failure_work.description`:

Description
-----------

Work queue function for checking the main charger status

.. _`ab8500_charger_kick_watchdog_work`:

ab8500_charger_kick_watchdog_work
=================================

.. c:function:: void ab8500_charger_kick_watchdog_work(struct work_struct *work)

    kick the watchdog

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. _`ab8500_charger_kick_watchdog_work.description`:

Description
-----------

Work queue function for kicking the charger watchdog.

For ABB revision 1.0 and 1.1 there is a bug in the watchdog
logic. That means we have to continously kick the charger
watchdog even when no charger is connected. This is only
valid once the AC charger has been enabled. This is
a bug that is not handled by the algorithm and the
watchdog have to be kicked by the charger driver
when the AC charger is disabled

.. _`ab8500_charger_ac_work`:

ab8500_charger_ac_work
======================

.. c:function:: void ab8500_charger_ac_work(struct work_struct *work)

    work to get and set main charger status

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. _`ab8500_charger_ac_work.description`:

Description
-----------

Work queue function for checking the main charger status

.. _`ab8500_charger_detect_usb_type_work`:

ab8500_charger_detect_usb_type_work
===================================

.. c:function:: void ab8500_charger_detect_usb_type_work(struct work_struct *work)

    work to detect USB type

    :param struct work_struct \*work:
        Pointer to the work_struct structure

.. _`ab8500_charger_detect_usb_type_work.description`:

Description
-----------

Detect the type of USB plugged

.. _`ab8500_charger_usb_link_attach_work`:

ab8500_charger_usb_link_attach_work
===================================

.. c:function:: void ab8500_charger_usb_link_attach_work(struct work_struct *work)

    work to detect USB type

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. _`ab8500_charger_usb_link_attach_work.description`:

Description
-----------

Detect the type of USB plugged

.. _`ab8500_charger_usb_link_status_work`:

ab8500_charger_usb_link_status_work
===================================

.. c:function:: void ab8500_charger_usb_link_status_work(struct work_struct *work)

    work to detect USB type

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. _`ab8500_charger_usb_link_status_work.description`:

Description
-----------

Detect the type of USB plugged

.. _`ab8500_charger_check_usbchargernotok_work`:

ab8500_charger_check_usbchargernotok_work
=========================================

.. c:function:: void ab8500_charger_check_usbchargernotok_work(struct work_struct *work)

    check USB chg not ok status

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. _`ab8500_charger_check_usbchargernotok_work.description`:

Description
-----------

Work queue function for checking the USB charger Not OK status

.. _`ab8500_charger_check_main_thermal_prot_work`:

ab8500_charger_check_main_thermal_prot_work
===========================================

.. c:function:: void ab8500_charger_check_main_thermal_prot_work(struct work_struct *work)

    check main thermal status

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. _`ab8500_charger_check_main_thermal_prot_work.description`:

Description
-----------

Work queue function for checking the Main thermal prot status

.. _`ab8500_charger_check_usb_thermal_prot_work`:

ab8500_charger_check_usb_thermal_prot_work
==========================================

.. c:function:: void ab8500_charger_check_usb_thermal_prot_work(struct work_struct *work)

    check usb thermal status

    :param struct work_struct \*work:
        pointer to the work_struct structure

.. _`ab8500_charger_check_usb_thermal_prot_work.description`:

Description
-----------

Work queue function for checking the USB thermal prot status

.. _`ab8500_charger_mainchunplugdet_handler`:

ab8500_charger_mainchunplugdet_handler
======================================

.. c:function:: irqreturn_t ab8500_charger_mainchunplugdet_handler(int irq, void *_di)

    main charger unplugged

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_mainchunplugdet_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_mainchplugdet_handler`:

ab8500_charger_mainchplugdet_handler
====================================

.. c:function:: irqreturn_t ab8500_charger_mainchplugdet_handler(int irq, void *_di)

    main charger plugged

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_mainchplugdet_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_mainextchnotok_handler`:

ab8500_charger_mainextchnotok_handler
=====================================

.. c:function:: irqreturn_t ab8500_charger_mainextchnotok_handler(int irq, void *_di)

    main charger not ok

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_mainextchnotok_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_mainchthprotr_handler`:

ab8500_charger_mainchthprotr_handler
====================================

.. c:function:: irqreturn_t ab8500_charger_mainchthprotr_handler(int irq, void *_di)

    Die temp is above main charger thermal protection threshold

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_mainchthprotr_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_mainchthprotf_handler`:

ab8500_charger_mainchthprotf_handler
====================================

.. c:function:: irqreturn_t ab8500_charger_mainchthprotf_handler(int irq, void *_di)

    Die temp is below main charger thermal protection threshold

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_mainchthprotf_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_vbusdetf_handler`:

ab8500_charger_vbusdetf_handler
===============================

.. c:function:: irqreturn_t ab8500_charger_vbusdetf_handler(int irq, void *_di)

    VBUS falling detected

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_vbusdetf_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_vbusdetr_handler`:

ab8500_charger_vbusdetr_handler
===============================

.. c:function:: irqreturn_t ab8500_charger_vbusdetr_handler(int irq, void *_di)

    VBUS rising detected

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_vbusdetr_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_usblinkstatus_handler`:

ab8500_charger_usblinkstatus_handler
====================================

.. c:function:: irqreturn_t ab8500_charger_usblinkstatus_handler(int irq, void *_di)

    USB link status has changed

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_usblinkstatus_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_usbchthprotr_handler`:

ab8500_charger_usbchthprotr_handler
===================================

.. c:function:: irqreturn_t ab8500_charger_usbchthprotr_handler(int irq, void *_di)

    Die temp is above usb charger thermal protection threshold

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_usbchthprotr_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_usbchthprotf_handler`:

ab8500_charger_usbchthprotf_handler
===================================

.. c:function:: irqreturn_t ab8500_charger_usbchthprotf_handler(int irq, void *_di)

    Die temp is below usb charger thermal protection threshold

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_usbchthprotf_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_usbchargernotokr_handler`:

ab8500_charger_usbchargernotokr_handler
=======================================

.. c:function:: irqreturn_t ab8500_charger_usbchargernotokr_handler(int irq, void *_di)

    USB charger not ok detected

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_usbchargernotokr_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_chwdexp_handler`:

ab8500_charger_chwdexp_handler
==============================

.. c:function:: irqreturn_t ab8500_charger_chwdexp_handler(int irq, void *_di)

    Charger watchdog expired

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_chwdexp_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_vbuschdropend_handler`:

ab8500_charger_vbuschdropend_handler
====================================

.. c:function:: irqreturn_t ab8500_charger_vbuschdropend_handler(int irq, void *_di)

    VBUS drop removed

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_vbuschdropend_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_vbusovv_handler`:

ab8500_charger_vbusovv_handler
==============================

.. c:function:: irqreturn_t ab8500_charger_vbusovv_handler(int irq, void *_di)

    VBUS overvoltage detected

    :param int irq:
        interrupt number

    :param void \*_di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_vbusovv_handler.description`:

Description
-----------

Returns IRQ status(IRQ_HANDLED)

.. _`ab8500_charger_ac_get_property`:

ab8500_charger_ac_get_property
==============================

.. c:function:: int ab8500_charger_ac_get_property(struct power_supply *psy, enum power_supply_property psp, union power_supply_propval *val)

    get the ac/mains properties

    :param struct power_supply \*psy:
        pointer to the power_supply structure

    :param enum power_supply_property psp:
        pointer to the power_supply_property structure

    :param union power_supply_propval \*val:
        pointer to the power_supply_propval union

.. _`ab8500_charger_ac_get_property.description`:

Description
-----------

This function gets called when an application tries to get the ac/mains
properties by reading the sysfs files.
AC/Mains properties are online, present and voltage.

.. _`ab8500_charger_ac_get_property.online`:

online
------

ac/mains charging is in progress or not

.. _`ab8500_charger_ac_get_property.present`:

present
-------

presence of the ac/mains

.. _`ab8500_charger_ac_get_property.voltage`:

voltage
-------

AC/Mains voltage
Returns error code in case of failure else 0(on success)

.. _`ab8500_charger_usb_get_property`:

ab8500_charger_usb_get_property
===============================

.. c:function:: int ab8500_charger_usb_get_property(struct power_supply *psy, enum power_supply_property psp, union power_supply_propval *val)

    get the usb properties

    :param struct power_supply \*psy:
        pointer to the power_supply structure

    :param enum power_supply_property psp:
        pointer to the power_supply_property structure

    :param union power_supply_propval \*val:
        pointer to the power_supply_propval union

.. _`ab8500_charger_usb_get_property.description`:

Description
-----------

This function gets called when an application tries to get the usb
properties by reading the sysfs files.
USB properties are online, present and voltage.

.. _`ab8500_charger_usb_get_property.online`:

online
------

usb charging is in progress or not

.. _`ab8500_charger_usb_get_property.present`:

present
-------

presence of the usb

.. _`ab8500_charger_usb_get_property.voltage`:

voltage
-------

vbus voltage
Returns error code in case of failure else 0(on success)

.. _`ab8500_charger_init_hw_registers`:

ab8500_charger_init_hw_registers
================================

.. c:function:: int ab8500_charger_init_hw_registers(struct ab8500_charger *di)

    Set up charger related registers

    :param struct ab8500_charger \*di:
        pointer to the ab8500_charger structure

.. _`ab8500_charger_init_hw_registers.description`:

Description
-----------

Set up charger OVV, watchdog and maximum voltage registers as well as
charging of the backup battery

.. This file was automatic generated / don't edit.

