.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/ti-soc-thermal/ti-bandgap.h

.. _`bandgap-driver-data-structure`:

bandgap driver data structure
=============================

==================================

+----------+----------------+
\| struct temp_sensor_regval \|
+---------------------------+
\* (Array of)
\|
\|
+-------------------+   +-----------------+
\| struct ti_bandgap \|-->\| struct device \* \|
+----------+--------+   +-----------------+
\|
\|
V
+------------------------+
\| struct ti_bandgap_data \|
+------------------------+
\|
\|
\* (Array of)
+------------+------------------------------------------------------+
\| +----------+------------+   +-------------------------+           \|
\| \| struct ti_temp_sensor \|-->\| struct temp_sensor_data \|           \|
\| +-----------------------+   +------------+------------+           \|
\|            \|                                                      \|
\|            +                                                      \|
\|            V                                                      \|
\| +----------+-------------------+                                  \|
\| \| struct temp_sensor_registers \|                                  \|
\| +------------------------------+                                  \|
\|                                                                   \|
+-------------------------------------------------------------------+

Above is a simple diagram describing how the data structure below
are organized. For each bandgap device there should be a ti_bandgap_data
containing the device instance configuration, as well as, an array of
sensors, representing every sensor instance present in this bandgap.

.. _`temp_sensor_registers`:

struct temp_sensor_registers
============================

.. c:type:: struct temp_sensor_registers

    descriptor to access registers and bitfields

.. _`temp_sensor_registers.definition`:

Definition
----------

.. code-block:: c

    struct temp_sensor_registers {
        u32 temp_sensor_ctrl;
        u32 bgap_tempsoff_mask;
        u32 bgap_soc_mask;
        u32 bgap_eocz_mask;
        u32 bgap_dtemp_mask;
        u32 bgap_mask_ctrl;
        u32 mask_hot_mask;
        u32 mask_cold_mask;
        u32 mask_sidlemode_mask;
        u32 mask_counter_delay_mask;
        u32 mask_freeze_mask;
        u32 mask_clear_mask;
        u32 mask_clear_accum_mask;
        u32 bgap_mode_ctrl;
        u32 mode_ctrl_mask;
        u32 bgap_counter;
        u32 counter_mask;
        u32 bgap_threshold;
        u32 threshold_thot_mask;
        u32 threshold_tcold_mask;
        u32 tshut_threshold;
        u32 tshut_efuse_mask;
        u32 tshut_efuse_shift;
        u32 tshut_hot_mask;
        u32 tshut_cold_mask;
        u32 bgap_status;
        u32 status_clean_stop_mask;
        u32 status_bgap_alert_mask;
        u32 status_hot_mask;
        u32 status_cold_mask;
        u32 bgap_cumul_dtemp;
        u32 ctrl_dtemp_0;
        u32 ctrl_dtemp_1;
        u32 ctrl_dtemp_2;
        u32 ctrl_dtemp_3;
        u32 ctrl_dtemp_4;
        u32 bgap_efuse;
    }

.. _`temp_sensor_registers.members`:

Members
-------

temp_sensor_ctrl
    TEMP_SENSOR_CTRL register offset

bgap_tempsoff_mask
    mask to temp_sensor_ctrl.tempsoff

bgap_soc_mask
    mask to temp_sensor_ctrl.soc

bgap_eocz_mask
    mask to temp_sensor_ctrl.eocz

bgap_dtemp_mask
    mask to temp_sensor_ctrl.dtemp

bgap_mask_ctrl
    BANDGAP_MASK_CTRL register offset

mask_hot_mask
    mask to bandgap_mask_ctrl.mask_hot

mask_cold_mask
    mask to bandgap_mask_ctrl.mask_cold

mask_sidlemode_mask
    mask to bandgap_mask_ctrl.mask_sidlemode

mask_counter_delay_mask
    mask to bandgap_mask_ctrl.mask_counter_delay

mask_freeze_mask
    mask to bandgap_mask_ctrl.mask_free

mask_clear_mask
    mask to bandgap_mask_ctrl.mask_clear

mask_clear_accum_mask
    mask to bandgap_mask_ctrl.mask_clear_accum

bgap_mode_ctrl
    BANDGAP_MODE_CTRL register offset

mode_ctrl_mask
    mask to bandgap_mode_ctrl.mode_ctrl

bgap_counter
    BANDGAP_COUNTER register offset

counter_mask
    mask to bandgap_counter.counter

bgap_threshold
    BANDGAP_THRESHOLD register offset (TALERT thresholds)

threshold_thot_mask
    mask to bandgap_threhold.thot

threshold_tcold_mask
    mask to bandgap_threhold.tcold

tshut_threshold
    TSHUT_THRESHOLD register offset (TSHUT thresholds)

tshut_efuse_mask
    mask to tshut_threshold.tshut_efuse

tshut_efuse_shift
    shift to tshut_threshold.tshut_efuse

tshut_hot_mask
    mask to tshut_threhold.thot

tshut_cold_mask
    mask to tshut_threhold.thot

bgap_status
    BANDGAP_STATUS register offset

status_clean_stop_mask
    mask to bandgap_status.clean_stop

status_bgap_alert_mask
    mask to bandgap_status.bandgap_alert

status_hot_mask
    mask to bandgap_status.hot

status_cold_mask
    mask to bandgap_status.cold

bgap_cumul_dtemp
    BANDGAP_CUMUL_DTEMP register offset

ctrl_dtemp_0
    CTRL_DTEMP0 register offset

ctrl_dtemp_1
    CTRL_DTEMP1 register offset

ctrl_dtemp_2
    CTRL_DTEMP2 register offset

ctrl_dtemp_3
    CTRL_DTEMP3 register offset

ctrl_dtemp_4
    CTRL_DTEMP4 register offset

bgap_efuse
    BANDGAP_EFUSE register offset

.. _`temp_sensor_registers.description`:

Description
-----------

The register offsets and bitfields might change across
OMAP and variants versions. Hence this struct serves as a
descriptor map on how to access the registers and the bitfields.

This descriptor contains registers of all versions of bandgap chips.
Not all versions will use all registers, depending on the available
features. Please read TRMs for descriptive explanation on each bitfield.

.. _`temp_sensor_data`:

struct temp_sensor_data
=======================

.. c:type:: struct temp_sensor_data

    The thresholds and limits for temperature sensors.

.. _`temp_sensor_data.definition`:

Definition
----------

.. code-block:: c

    struct temp_sensor_data {
        u32 tshut_hot;
        u32 tshut_cold;
        u32 t_hot;
        u32 t_cold;
        u32 min_freq;
        u32 max_freq;
        int max_temp;
        int min_temp;
        int hyst_val;
        u32 update_int1;
        u32 update_int2;
    }

.. _`temp_sensor_data.members`:

Members
-------

tshut_hot
    temperature to trigger a thermal reset (initial value)

tshut_cold
    temp to get the plat out of reset due to thermal (init val)

t_hot
    temperature to trigger a thermal alert (high initial value)

t_cold
    temperature to trigger a thermal alert (low initial value)

min_freq
    sensor minimum clock rate

max_freq
    sensor maximum clock rate

max_temp
    sensor maximum temperature

min_temp
    sensor minimum temperature

hyst_val
    temperature hysteresis considered while converting ADC values

update_int1
    update interval

update_int2
    update interval

.. _`temp_sensor_data.description`:

Description
-----------

This data structure will hold the required thresholds and temperature limits
for a specific temperature sensor, like shutdown temperature, alert
temperature, clock / rate used, ADC conversion limits and update intervals

.. _`temp_sensor_regval`:

struct temp_sensor_regval
=========================

.. c:type:: struct temp_sensor_regval

    temperature sensor register values and priv data

.. _`temp_sensor_regval.definition`:

Definition
----------

.. code-block:: c

    struct temp_sensor_regval {
        u32 bg_mode_ctrl;
        u32 bg_ctrl;
        u32 bg_counter;
        u32 bg_threshold;
        u32 tshut_threshold;
        void *data;
    }

.. _`temp_sensor_regval.members`:

Members
-------

bg_mode_ctrl
    temp sensor control register value

bg_ctrl
    bandgap ctrl register value

bg_counter
    bandgap counter value

bg_threshold
    bandgap threshold register value

tshut_threshold
    bandgap tshut register value

data
    private data

.. _`temp_sensor_regval.description`:

Description
-----------

Data structure to save and restore bandgap register set context. Only
required registers are shadowed, when needed.

.. _`ti_bandgap`:

struct ti_bandgap
=================

.. c:type:: struct ti_bandgap

    bandgap device structure

.. _`ti_bandgap.definition`:

Definition
----------

.. code-block:: c

    struct ti_bandgap {
        struct device *dev;
        void __iomem *base;
        const struct ti_bandgap_data *conf;
        struct temp_sensor_regval *regval;
        struct clk *fclock;
        struct clk *div_clk;
        spinlock_t lock;
        int irq;
        int tshut_gpio;
        u32 clk_rate;
    }

.. _`ti_bandgap.members`:

Members
-------

dev
    struct device pointer

base
    io memory base address

conf
    struct with bandgap configuration set (# sensors, conv_table, etc)

regval
    temperature sensor register values

fclock
    pointer to functional clock of temperature sensor

div_clk
    pointer to divider clock of temperature sensor fclk

lock
    spinlock for ti_bandgap structure

irq
    MPU IRQ number for thermal alert

tshut_gpio
    GPIO where Tshut signal is routed

clk_rate
    Holds current clock rate

.. _`ti_bandgap.description`:

Description
-----------

The bandgap device structure representing the bandgap device instance.
It holds most of the dynamic stuff. Configurations and sensor specific
entries are inside the \ ``conf``\  structure.

.. _`ti_temp_sensor`:

struct ti_temp_sensor
=====================

.. c:type:: struct ti_temp_sensor

    bandgap temperature sensor configuration data

.. _`ti_temp_sensor.definition`:

Definition
----------

.. code-block:: c

    struct ti_temp_sensor {
        struct temp_sensor_data *ts_data;
        struct temp_sensor_registers *registers;
        char *domain;
        const int slope_pcb;
        const int constant_pcb;
        int (*register_cooling)(struct ti_bandgap *bgp, int id);
        int (*unregister_cooling)(struct ti_bandgap *bgp, int id);
    }

.. _`ti_temp_sensor.members`:

Members
-------

ts_data
    pointer to struct with thresholds, limits of temperature sensor

registers
    pointer to the list of register offsets and bitfields

domain
    the name of the domain where the sensor is located

slope_pcb
    sensor gradient slope info for hotspot extrapolation equation
    with no external influence

constant_pcb
    sensor gradient const info for hotspot extrapolation equation
    with no external influence

register_cooling
    function to describe how this sensor is going to be cooled

unregister_cooling
    function to release cooling data

.. _`ti_temp_sensor.description`:

Description
-----------

Data structure to describe a temperature sensor handled by a bandgap device.
It should provide configuration details on this sensor, such as how to
access the registers affecting this sensor, shadow register buffer, how to
assess the gradient from hotspot, how to cooldown the domain when sensor
reports too hot temperature.

.. _`ti-bandgap-feature-types`:

ti bandgap feature types
========================

TI_BANDGAP_FEATURE_TSHUT - used when the thermal shutdown signal output
of a bandgap device instance is routed to the processor. This means
the system must react and perform the shutdown by itself (handle an
IRQ, for instance).

TI_BANDGAP_FEATURE_TSHUT_CONFIG - used when the bandgap device has control
over the thermal shutdown configuration. This means that the thermal
shutdown thresholds are programmable, for instance.

TI_BANDGAP_FEATURE_TALERT - used when the bandgap device instance outputs
a signal representing violation of programmable alert thresholds.

TI_BANDGAP_FEATURE_MODE_CONFIG - used when it is possible to choose which
mode, continuous or one shot, the bandgap device instance will operate.

TI_BANDGAP_FEATURE_COUNTER - used when the bandgap device instance allows
programming the update interval of its internal state machine.

TI_BANDGAP_FEATURE_POWER_SWITCH - used when the bandgap device allows
itself to be switched on/off.

TI_BANDGAP_FEATURE_CLK_CTRL - used when the clocks feeding the bandgap
device are gateable or not.

TI_BANDGAP_FEATURE_FREEZE_BIT - used when the bandgap device features
a history buffer that its update can be freezed/unfreezed.

TI_BANDGAP_FEATURE_COUNTER_DELAY - used when the bandgap device features
a delay programming based on distinct values.

TI_BANDGAP_FEATURE_HISTORY_BUFFER - used when the bandgap device features
a history buffer of temperatures.

TI_BANDGAP_FEATURE_ERRATA_814 - used to workaorund when the bandgap device
has Errata 814
TI_BANDGAP_FEATURE_ERRATA_813 - used to workaorund when the bandgap device
has Errata 813
TI_BANDGAP_FEATURE_UNRELIABLE - used when the sensor readings are too
inaccurate.
TI_BANDGAP_HAS(b, f) - macro to check if a bandgap device is capable of a
specific feature (above) or not. Return non-zero, if yes.

.. _`ti_bandgap_data`:

struct ti_bandgap_data
======================

.. c:type:: struct ti_bandgap_data

    ti bandgap data configuration structure

.. _`ti_bandgap_data.definition`:

Definition
----------

.. code-block:: c

    struct ti_bandgap_data {
        unsigned int features;
        const int *conv_table;
        u32 adc_start_val;
        u32 adc_end_val;
        char *fclock_name;
        char *div_ck_name;
        int sensor_count;
        int (*report_temperature)(struct ti_bandgap *bgp, int id);
        int (*expose_sensor)(struct ti_bandgap *bgp, int id, char *domain);
        int (*remove_sensor)(struct ti_bandgap *bgp, int id);
        struct ti_temp_sensor sensors[];
    }

.. _`ti_bandgap_data.members`:

Members
-------

features
    a bitwise flag set to describe the device features

conv_table
    Pointer to ADC to temperature conversion table

adc_start_val
    ADC conversion table starting value

adc_end_val
    ADC conversion table ending value

fclock_name
    clock name of the functional clock

div_ck_name
    clock name of the clock divisor

sensor_count
    count of temperature sensor within this bandgap device

report_temperature
    callback to report thermal alert to thermal API

expose_sensor
    callback to export sensor to thermal API

remove_sensor
    callback to destroy sensor from thermal API

sensors
    array of sensors present in this bandgap instance

.. _`ti_bandgap_data.description`:

Description
-----------

This is a data structure which should hold most of the static configuration
of a bandgap device instance. It should describe which features this instance
is capable of, the clock names to feed this device, the amount of sensors and
their configuration representation, and how to export and unexport them to
a thermal API.

.. This file was automatic generated / don't edit.

