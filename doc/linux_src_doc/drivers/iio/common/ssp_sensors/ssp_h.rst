.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/common/ssp_sensors/ssp.h

.. _`ssp_data`:

struct ssp_data
===============

.. c:type:: struct ssp_data

    ssp platformdata structure

.. _`ssp_data.definition`:

Definition
----------

.. code-block:: c

    struct ssp_data {
        struct spi_device *spi;
        struct ssp_sensorhub_info *sensorhub_info;
        struct timer_list wdt_timer;
        struct work_struct work_wdt;
        struct delayed_work work_refresh;
        bool shut_down;
        bool mcu_dump_mode;
        bool time_syncing;
        int64_t timestamp;
        int check_status[SSP_SENSOR_MAX];
        unsigned int com_fail_cnt;
        unsigned int reset_cnt;
        unsigned int timeout_cnt;
        unsigned int available_sensors;
        unsigned int cur_firm_rev;
        char last_resume_state;
        char last_ap_state;
        unsigned int sensor_enable;
        u32 delay_buf[SSP_SENSOR_MAX];
        s32 batch_latency_buf[SSP_SENSOR_MAX];
        s8 batch_opt_buf[SSP_SENSOR_MAX];
        int accel_position;
        int mag_position;
        int fw_dl_state;
        struct mutex comm_lock;
        struct mutex pending_lock;
        int mcu_reset_gpio;
        int ap_mcu_gpio;
        int mcu_ap_gpio;
        struct list_head pending_list;
        struct iio_dev  *sensor_devs[SSP_SENSOR_MAX];
        atomic_t enable_refcount;
        __le16 header_buffer[SSP_HEADER_BUFFER_SIZE / sizeof(__le16)]____cacheline_aligned;
    }

.. _`ssp_data.members`:

Members
-------

spi
    spi device

sensorhub_info
    info about sensorhub board specific features

wdt_timer
    watchdog timer

work_wdt
    watchdog work

work_refresh
    refresh work queue for reset request from MCU

shut_down
    shut down flag

mcu_dump_mode
    mcu dump mode for debug

time_syncing
    time syncing indication flag

timestamp
    previous time in ns calculated for time syncing

check_status
    status table for each sensor

com_fail_cnt
    communication fail count

reset_cnt
    reset count

timeout_cnt
    timeout count

available_sensors
    available sensors seen by sensorhub (bit array)

cur_firm_rev
    cached current firmware revision

last_resume_state
    last AP resume/suspend state used to handle the PM
    state of ssp

last_ap_state
    (obsolete) sleep notification for MCU

sensor_enable
    sensor enable mask

delay_buf
    data acquisition intervals table

batch_latency_buf
    yet unknown but existing in communication protocol

batch_opt_buf
    yet unknown but existing in communication protocol

accel_position
    yet unknown but existing in communication protocol

mag_position
    yet unknown but existing in communication protocol

fw_dl_state
    firmware download state

comm_lock
    lock protecting the handshake

pending_lock
    lock protecting pending list and completion

mcu_reset_gpio
    mcu reset line

ap_mcu_gpio
    ap to mcu gpio line

mcu_ap_gpio
    mcu to ap gpio line

pending_list
    pending list for messages queued to be sent/read

sensor_devs
    registered IIO devices table

enable_refcount
    enable reference count for wdt (watchdog timer)

header_buffer
    cache aligned buffer for packet header

.. This file was automatic generated / don't edit.

